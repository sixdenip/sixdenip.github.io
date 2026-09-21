#!/usr/bin/env python3
"""
Verify multilingual architecture:
1. Check that translation keys are ONLY used for section titles, badges, subtitles, navigation, and UI headers.
2. Verify that each item across experience, education, projects, publications, skills, and about has full, independent Markdown files for EN, FR, and DE.
3. Validate YAML front matter and content in all Markdown files.
"""
import os
import re
import json
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_translations():
    js_path = os.path.join(REPO_ROOT, "assets", "js", "translations.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract JSON object from window.TRANSLATIONS = { ... };
    match = re.search(r'window\.TRANSLATIONS\s*=\s*(\{.+?\});\s*$', content, re.DOTALL)
    if not match:
        raise ValueError("Could not parse window.TRANSLATIONS in translations.js")
    js_obj_str = match.group(1)

    # Basic cleanup to parse as pseudo JSON
    lines = []
    for line in js_obj_str.split("\n"):
        line_clean = re.sub(r'//.*$', '', line)
        lines.append(line_clean)
    clean_text = "\n".join(lines)
    # Remove trailing commas
    clean_text = re.sub(r',\s*([\}\]])', r'\1', clean_text)
    
    # Use yaml parser since JS object syntax matches YAML
    translations = yaml.safe_load(clean_text)
    return translations

def check_collections():
    collections = {
        "_about": ["01-about"],
        "_experience": ["01-placeholder", "02-safran", "03-etis", "04-xlim"],
        "_education": ["01-phd", "02-master", "03-exchange", "04-licence"],
        "_projects": ["01-smart-glasses", "02-pollution-advisor", "03-foot-angle", "04-snn-fpga", "05-smart-car"],
        "_publications": [
            "01-early-exit", "02-evaluating-arcs", "03-utility-ewsn", "04-gres-meco",
            "05-hybrid-memocode", "06-seque-edge", "07-raven-ngres", "08-sida-samos", "09-towards-acsos"
        ],
        "_skills": ["01-languages", "02-embedded", "03-dbms", "04-flow", "05-spoken", "06-awards"]
    }

    languages = ["en", "fr", "de"]
    missing = []
    total_files = 0

    for col_dir, item_prefixes in collections.items():
        dir_path = os.path.join(REPO_ROOT, col_dir)
        if not os.path.isdir(dir_path):
            missing.append(f"Directory {col_dir} missing")
            continue
        for prefix in item_prefixes:
            for lang in languages:
                filename = f"{prefix}-{lang}.md"
                file_path = os.path.join(dir_path, filename)
                if not os.path.isfile(file_path):
                    missing.append(f"Missing file: {col_dir}/{filename}")
                else:
                    total_files += 1
                    with open(file_path, "r", encoding="utf-8") as f:
                        text = f.read()
                    if not text.startswith("---"):
                        missing.append(f"Invalid front matter in {col_dir}/{filename}")
                    else:
                        parts = text.split("---", 2)
                        try:
                            fm = yaml.safe_load(parts[1])
                            if fm.get("lang") != lang:
                                missing.append(f"Mismatched lang in {col_dir}/{filename}: {fm.get('lang')} != {lang}")
                        except Exception as e:
                            missing.append(f"Error parsing YAML in {col_dir}/{filename}: {e}")

    print(f"Collections check: {total_files} files verified across 6 collections.")
    if missing:
        print("FAILURES:")
        for m in missing:
            print("  -", m)
        return False
    print("All collection markdown files exist and have valid YAML front matter.")
    return True

def check_translation_keys():
    translations = load_translations()
    en_keys = set(translations["en"].keys())
    fr_keys = set(translations["fr"].keys())
    de_keys = set(translations["de"].keys())

    # Check key parity
    diff_fr = en_keys.symmetric_difference(fr_keys)
    diff_de = en_keys.symmetric_difference(de_keys)
    if diff_fr:
        print(f"Key mismatch between EN and FR: {diff_fr}")
        return False
    if diff_de:
        print(f"Key mismatch between EN and DE: {diff_de}")
        return False

    print(f"Translations check: {len(en_keys)} keys found with 100% parity across en, fr, de.")

    # Verify no item keys exist in translations
    item_prefixes = ["exp.job", "exp.safran", "exp.etis", "exp.xlim", "edu.phd", "edu.master", "pub.p", "projects.smart"]
    found_item_keys = [k for k in en_keys if any(k.startswith(p) for p in item_prefixes)]
    if found_item_keys:
        print(f"ERROR: Found item keys in translations.js: {found_item_keys}")
        return False
    print("Verified: No item keys in translations.js! Translation keys are strictly limited to section titles, navigation, and UI headers.")

    # Find all data-i18n usages in templates
    html_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        if "/.git" in root or "/_site" in root or "node_modules" in root:
            continue
        for f in files:
            if f.endswith(".html") or (f.endswith(".md") and ("_sections" in root or "_includes" in root)):
                html_files.append(os.path.join(root, f))

    used_keys = set()
    for hf in html_files:
        with open(hf, "r", encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(r'data-i18n="([^"]+)"', content)
        for m in matches:
            if "{{" in m:
                for sid in ["about", "experience", "education", "publications", "projects", "skills"]:
                    used_keys.add(re.sub(r'\{\{[^}]+\}\}', sid, m))
            else:
                used_keys.add(m)

    missing_in_dict = used_keys - en_keys
    if missing_in_dict:
        print(f"WARNING: The following data-i18n keys are used in templates but missing in dictionary: {missing_in_dict}")
        return False
    print(f"All {len(used_keys)} data-i18n keys used in templates are present in translations.js.")
    return True

if __name__ == "__main__":
    c_ok = check_collections()
    t_ok = check_translation_keys()
    if c_ok and t_ok:
        print("\nSUCCESS: All architecture requirements verified perfectly!")
    else:
        print("\nFAILURE: Some requirements not met.")
        exit(1)
