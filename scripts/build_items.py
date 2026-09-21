#!/usr/bin/env python3
"""
Generate all multilingual item Markdown files across:
  - _about/
  - _experience/
  - _education/
  - _projects/
  - _publications/
  - _skills/

Each item in each language is written in full independently in a separate Markdown file.
"""
import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_md(rel_path, front_matter, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    fm_str = yaml.dump(front_matter, sort_keys=False, allow_unicode=True).strip()
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"---\n{fm_str}\n---\n\n{content.strip()}\n")
    print(f"Created {rel_path}")

# ==============================================================================
# 1. ABOUT
# ==============================================================================
def create_about():
    en_content = """
I am a **Computer Science & Embedded Systems Engineer and PhD Student**, specializing in **Embedded Systems**, **FPGA Acceleration**, **Low-Power Platforms**, and **Smart Connected Systems**.

I completed my **Master in Computer Science** at **CY Cergy Paris University**, graduating top of my class in the research track for *Smart Electronic Systems*, following an exchange program at **Oregon State University** (USA) and a **Licence in Computer Science** with high honors from the **University of Poitiers**. My work spans hardware-software co-design, ranging from research on Spiking Neural Networks (SNN) on FPGA, failure detection systems for robotics (ETIS laboratory), to streaming IP debugging on low-power FPGAs at **Safran Electronics & Defense**.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
  <div class="stat-item" style="text-align: left; padding: 1.5rem;">
    <h4 style="margin: 0 0 0.5rem; color: var(--accent-primary);">🎯 Core Interests</h4>
    <ul style="margin: 0; padding-left: 1.2rem; color: var(--text-muted); font-size: 0.95rem;">
      <li>FPGA Architecture &amp; R&amp;D (VHDL, Vivado, Quartus)</li>
      <li>Embedded Systems &amp; Firmware (C/C++, STM32, Arduino)</li>
      <li>Neuromorphic Computing &amp; Spiking Neural Networks (SNN)</li>
      <li>Robotics, Sensor Fusion &amp; Driving Assistance Systems</li>
      <li>Low-Power Computing &amp; IoT Solutions</li>
    </ul>
  </div>

  <div class="stat-item" style="text-align: left; padding: 1.5rem;">
    <h4 style="margin: 0 0 0.5rem; color: var(--accent-secondary);">📬 Contact Details</h4>
    <p style="margin-bottom: 0.75rem; font-size: 0.95rem; color: var(--text-muted);">
      Feel free to reach out for research inquiries, technical discussions, or collaboration opportunities.
    </p>
    <p style="margin: 0; font-size: 0.95rem; line-height: 1.7;">
      <strong>Nationality:</strong> French<br>
      <strong>Email:</strong> <a href="mailto:pierre-louis.sixdenier@outlook.fr">pierre-louis.sixdenier@outlook.fr</a><br>
      <strong>Phone:</strong> <a href="tel:+33680489143">+33 6 80 48 91 43</a><br>
      <strong>GitHub:</strong> <a href="https://github.com/sixdenip" target="_blank" rel="noopener">github.com/sixdenip</a><br>
      <strong>LinkedIn:</strong> <a href="https://linkedin.com/in/pierre-louis-sixdenier" target="_blank" rel="noopener">linkedin.com/in/pierre-louis-sixdenier</a>
    </p>
  </div>
</div>
"""

    fr_content = """
Je suis **ingénieur en informatique & systèmes embarqués et doctorant**, spécialisé en **systèmes embarqués**, **accélération sur FPGA**, **plateformes basse consommation** et **systèmes intelligents communicants**.

J'ai obtenu mon **Master en Informatique** à **CY Cergy Paris Université**, major de promotion du parcours recherche en *Systèmes Électroniques Intelligents*, après un séjour d'échange à **Oregon State University** (États-Unis) et une **Licence d'Informatique** avec mention à l'**Université de Poitiers**. Mes travaux portent sur la co-conception matériel-logiciel, depuis la recherche sur les réseaux de neurones à impulsions (SNN) sur FPGA, la détection de défaillances pour la robotique (laboratoire ETIS), jusqu'au débogage d'IP de streaming sur FPGA basse consommation chez **Safran Electronics & Defense**.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
  <div class="stat-item" style="text-align: left; padding: 1.5rem;">
    <h4 style="margin: 0 0 0.5rem; color: var(--accent-primary);">🎯 Domaines d'Intérêt</h4>
    <ul style="margin: 0; padding-left: 1.2rem; color: var(--text-muted); font-size: 0.95rem;">
      <li>Architecture FPGA &amp; R&amp;D (VHDL, Vivado, Quartus)</li>
      <li>Systèmes Embarqués &amp; Firmware (C/C++, STM32, Arduino)</li>
      <li>Calcul Neuromorphique &amp; Réseaux de Neurones à Impulsions (SNN)</li>
      <li>Robotique, Fusion de Capteurs &amp; Systèmes d'Aide à la Conduite</li>
      <li>Calcul Basse Consommation &amp; Solutions IoT</li>
    </ul>
  </div>

  <div class="stat-item" style="text-align: left; padding: 1.5rem;">
    <h4 style="margin: 0 0 0.5rem; color: var(--accent-secondary);">📬 Contact</h4>
    <p style="margin-bottom: 0.75rem; font-size: 0.95rem; color: var(--text-muted);">
      N'hésitez pas à me contacter pour des échanges scientifiques, des opportunités de recherche ou des collaborations.
    </p>
    <p style="margin: 0; font-size: 0.95rem; line-height: 1.7;">
      <strong>Nationalité :</strong> Française<br>
      <strong>Email :</strong> <a href="mailto:pierre-louis.sixdenier@outlook.fr">pierre-louis.sixdenier@outlook.fr</a><br>
      <strong>Téléphone :</strong> <a href="tel:+33680489143">+33 6 80 48 91 43</a><br>
      <strong>GitHub :</strong> <a href="https://github.com/sixdenip" target="_blank" rel="noopener">github.com/sixdenip</a><br>
      <strong>LinkedIn :</strong> <a href="https://linkedin.com/in/pierre-louis-sixdenier" target="_blank" rel="noopener">linkedin.com/in/pierre-louis-sixdenier</a>
    </p>
  </div>
</div>
"""

    de_content = """
Ich bin **Ingenieur für Informatik & Eingebettete Systeme sowie Doktorand**, spezialisiert auf **Eingebettete Systeme**, **FPGA-Beschleunigung**, **Low-Power-Plattformen** und **intelligente vernetzte Systeme**.

Meinen **Master of Science in Informatik** habe ich an der **CY Cergy Paris Universität** als Jahrgangsbester im Forschungsschwerpunkt *Intelligente Elektronische Systeme* abgeschlossen, nach einem Austauschprogramm an der **Oregon State University** (USA) und einem **Bachelor in Informatik** mit Auszeichnung an der **Universität Poitiers**. Meine Forschung umfasst Hardware-Software-Co-Design, von Untersuchungen zu Spiking Neural Networks (SNN) auf FPGA über Fehlererkennungssysteme für die Robotik (ETIS-Labor) bis hin zur Entwicklung von Streaming-IPs für Low-Power-FPGAs bei **Safran Electronics & Defense**.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
  <div class="stat-item" style="text-align: left; padding: 1.5rem;">
    <h4 style="margin: 0 0 0.5rem; color: var(--accent-primary);">🎯 Forschungsschwerpunkte</h4>
    <ul style="margin: 0; padding-left: 1.2rem; color: var(--text-muted); font-size: 0.95rem;">
      <li>FPGA-Architektur &amp; R&amp;D (VHDL, Vivado, Quartus)</li>
      <li>Eingebettete Systeme &amp; Firmware (C/C++, STM32, Arduino)</li>
      <li>Neuromorphes Rechnen &amp; Spiking Neural Networks (SNN)</li>
      <li>Robotik, Sensorfusion &amp; Fahrerassistenzsysteme</li>
      <li>Low-Power Computing &amp; IoT-Lösungen</li>
    </ul>
  </div>

  <div class="stat-item" style="text-align: left; padding: 1.5rem;">
    <h4 style="margin: 0 0 0.5rem; color: var(--accent-secondary);">📬 Kontaktinformationen</h4>
    <p style="margin-bottom: 0.75rem; font-size: 0.95rem; color: var(--text-muted);">
      Gerne stehe ich für wissenschaftliche Anfragen, Fachgespräche und Kooperationsmöglichkeiten zur Verfügung.
    </p>
    <p style="margin: 0; font-size: 0.95rem; line-height: 1.7;">
      <strong>Nationalität:</strong> Französisch<br>
      <strong>E-Mail:</strong> <a href="mailto:pierre-louis.sixdenier@outlook.fr">pierre-louis.sixdenier@outlook.fr</a><br>
      <strong>Telefon:</strong> <a href="tel:+33680489143">+33 6 80 48 91 43</a><br>
      <strong>GitHub:</strong> <a href="https://github.com/sixdenip" target="_blank" rel="noopener">github.com/sixdenip</a><br>
      <strong>LinkedIn:</strong> <a href="https://linkedin.com/in/pierre-louis-sixdenier" target="_blank" rel="noopener">linkedin.com/in/pierre-louis-sixdenier</a>
    </p>
  </div>
</div>
"""

    write_md("_about/01-about-en.md", {"order": 1, "lang": "en"}, en_content)
    write_md("_about/01-about-fr.md", {"order": 1, "lang": "fr"}, fr_content)
    write_md("_about/01-about-de.md", {"order": 1, "lang": "de"}, de_content)

# ==============================================================================
# 2. EXPERIENCE
# ==============================================================================
def create_experience():
    # 01 - Placeholder Job
    write_md("_experience/01-placeholder-en.md", {
        "order": 1,
        "lang": "en",
        "role": "[Job Title Placeholder • e.g. PhD Researcher / R&D Engineer]",
        "organization": "[Company / Research Institution Placeholder]",
        "period": "Nov 2020 – May 2026",
        "location": "France / Germany",
        "is_placeholder": True,
        "tags": ["Nov 2020 – May 2026", "Embedded Systems", "R&D"]
    }, """
*[Placeholder: Describe your primary responsibilities, research topics, or engineering objectives during this period.]*

- **[Key Project / Thesis]:** Detailed description of research or industrial project deliverables.
- **[Methodology & Architecture]:** Hardware/software co-design, prototyping, and algorithm implementation.
- **[Outcomes]:** Publications, industrial patents, benchmarks, or deployed embedded platforms.
""")

    write_md("_experience/01-placeholder-fr.md", {
        "order": 1,
        "lang": "fr",
        "role": "[Poste Placeholder • ex. Doctorant Chercheur / Ingénieur R&D]",
        "organization": "[Entreprise / Institut de Recherche Placeholder]",
        "period": "Nov 2020 – Mai 2026",
        "location": "France / Allemagne",
        "is_placeholder": True,
        "tags": ["Nov 2020 – Mai 2026", "Systèmes Embarqués", "R&D"]
    }, """
*[Placeholder : Décrivez vos principales missions, thématiques de recherche ou objectifs d'ingénierie pour cette période.]*

- **[Projet Clé / Thèse] :** Description détaillée des livrables de recherche ou projets industriels.
- **[Méthodologie & Architecture] :** Co-conception matériel/logiciel, prototypage et implémentation d'algorithmes.
- **[Résultats] :** Publications, brevets industriels, bancs d'essai ou plateformes embarquées déployées.
""")

    write_md("_experience/01-placeholder-de.md", {
        "order": 1,
        "lang": "de",
        "role": "[Berufsbezeichnung Platzhalter • z. B. Doktorand / R&D-Ingenieur]",
        "organization": "[Unternehmen / Forschungsinstitut Platzhalter]",
        "period": "Nov 2020 – Mai 2026",
        "location": "Deutschland / Frankreich",
        "is_placeholder": True,
        "tags": ["Nov 2020 – Mai 2026", "Eingebettete Systeme", "R&D"]
    }, """
*[Platzhalter: Beschreiben Sie Ihre Hauptaufgaben, Forschungsthemen oder Entwicklungsziele in diesem Zeitraum.]*

- **[Schlüsselprojekt / Dissertation]:** Detaillierte Beschreibung der Forschungsergebnisse oder industriellen Projektziele.
- **[Methodik & Architektur]:** Hardware/Software-Co-Design, Prototyping und Algorithmenimplementierung.
- **[Ergebnisse]:** Publikationen, Patente, Benchmarks oder bereitgestellte eingebettete Plattformen.
""")

    # 02 - Safran
    write_md("_experience/02-safran-en.md", {
        "order": 2,
        "lang": "en",
        "role": "FPGA R&D Engineer Intern",
        "organization": "Safran Electronics & Defense",
        "period": "May 2020 – Nov 2020",
        "location": "France",
        "tags": ["FPGA", "VHDL", "Low-Power", "Streaming IP", "Vivado"]
    }, """
Conception of a debugging streaming IP for an embedded low-power FPGA platform.

- Architected and implemented a custom streaming IP dedicated to non-intrusive live debugging on resource-constrained FPGAs.
- Optimized resource utilization, timing closure, and power consumption for defense and aerospace embedded requirements.
- Performed RTL simulation, verification testbenches, and on-board hardware validation.
""")

    write_md("_experience/02-safran-fr.md", {
        "order": 2,
        "lang": "fr",
        "role": "Ingénieur R&D FPGA (Stagiaire)",
        "organization": "Safran Electronics & Defense",
        "period": "Mai 2020 – Nov 2020",
        "location": "France",
        "tags": ["FPGA", "VHDL", "Basse consommation", "IP Streaming", "Vivado"]
    }, """
Conception d'une IP de streaming pour le débogage en direct sur plateforme FPGA basse consommation.

- Architecture et implémentation d'une IP de streaming dédiée au débogage non intrusif sur FPGA à ressources contraintes.
- Optimisation de l'utilisation des ressources, du respect des contraintes temporelles et de la consommation énergétique pour les exigences aéronautiques et de défense.
- Simulation RTL, bancs de test de vérification et validation matérielle sur carte.
""")

    write_md("_experience/02-safran-de.md", {
        "order": 2,
        "lang": "de",
        "role": "FPGA R&D Entwicklungsingenieur (Praktikant)",
        "organization": "Safran Electronics & Defense",
        "period": "Mai 2020 – Nov 2020",
        "location": "Frankreich",
        "tags": ["FPGA", "VHDL", "Low-Power", "Streaming-IP", "Vivado"]
    }, """
Konzeption einer Streaming-IP zur Live-Fehlerbehebung auf einer eingebetteten Low-Power-FPGA-Plattform.

- Entwurf und Implementierung einer dedizierten Streaming-IP für nicht-intrusives Live-Debugging auf ressourcenbeschränkten FPGAs.
- Optimierung der Ressourcennutzung, des Timing-Closures und des Stromverbrauchs für Luftfahrt- und Verteidigungsanforderungen.
- RTL-Simulation, Verifikations-Testbenches und Hardware-Validierung auf der Zielplatine.
""")

    # 03 - ETIS
    write_md("_experience/03-etis-en.md", {
        "order": 3,
        "lang": "en",
        "role": "Research Intern",
        "organization": "ETIS Laboratory (Equipes Traitement de l'Information et Systèmes)",
        "period": "December 2018",
        "location": "Cergy, France",
        "tags": ["Robotics", "Failure Detection", "C++", "Sensor Telemetry"]
    }, """
Conception and implementation of a failure detection system for robots.

- Investigated autonomous robotics anomaly detection algorithms based on sensor telemetry and internal state monitoring.
- Developed a real-time detection prototype to prevent robotic failure and ensure operational reliability.
""")

    write_md("_experience/03-etis-fr.md", {
        "order": 3,
        "lang": "fr",
        "role": "Stagiaire de Recherche",
        "organization": "Laboratoire ETIS (Équipes Traitement de l'Information et Systèmes)",
        "period": "Décembre 2018",
        "location": "Cergy, France",
        "tags": ["Robotique", "Détection de pannes", "C++", "Télémétrie capteurs"]
    }, """
Conception et mise en œuvre d'un système de détection de défaillances pour robots.

- Étude d'algorithmes de détection d'anomalies pour la robotique autonome basés sur la télémétrie des capteurs et les états internes.
- Développement d'un prototype de détection temps réel pour anticiper les défaillances robotiques et assurer la fiabilité opérationnelle.
""")

    write_md("_experience/03-etis-de.md", {
        "order": 3,
        "lang": "de",
        "role": "Forschungspraktikant",
        "organization": "ETIS Labor (Equipes Traitement de l'Information et Systèmes)",
        "period": "Dezember 2018",
        "location": "Cergy, Frankreich",
        "tags": ["Robotik", "Fehlererkennung", "C++", "Sensortelemetrie"]
    }, """
Konzeption und Implementierung eines Fehlererkennungssystems für Roboter.

- Untersuchung von Anomalieerkennungsalgorithmen für autonome Roboter basierend auf Sensortelemetrie und interner Zustandsüberwachung.
- Entwicklung eines Echtzeit-Erkennungsprototyps zur Vermeidung von Systemausfällen und Sicherung der Betriebszuverlässigkeit.
""")

    # 04 - XLIM
    write_md("_experience/04-xlim-en.md", {
        "order": 4,
        "lang": "en",
        "role": "Research Intern",
        "organization": "XLIM-SIC Laboratory",
        "period": "June 2017",
        "location": "Poitiers, France",
        "tags": ["L-System", "C++", "Procedural Generation", "Algorithms"]
    }, """
Conception of a proof-of-concept (PoC) on an L-System (Lindenmayer system) generator.

- Explored algorithmic procedural generation, rewriting grammars, and geometric visualization of fractals.
- Implemented the generation engine and user interface for interactive rule testing.
""")

    write_md("_experience/04-xlim-fr.md", {
        "order": 4,
        "lang": "fr",
        "role": "Stagiaire de Recherche",
        "organization": "Laboratoire XLIM-SIC",
        "period": "Juin 2017",
        "location": "Poitiers, France",
        "tags": ["L-Système", "C++", "Génération Procédurale", "Algorithmes"]
    }, """
Conception d'une preuve de concept (PoC) sur un générateur de L-Systèmes (systèmes de Lindenmayer).

- Étude de la génération procédurale algorithmique, des grammaires de réécriture et de la visualisation géométrique de fractales.
- Implémentation du moteur de génération et d'une interface pour l'expérimentation interactive de règles.
""")

    write_md("_experience/04-xlim-de.md", {
        "order": 4,
        "lang": "de",
        "role": "Forschungspraktikant",
        "organization": "XLIM-SIC Labor",
        "period": "Juni 2017",
        "location": "Poitiers, Frankreich",
        "tags": ["L-System", "C++", "Prozedurale Generierung", "Algorithmen"]
    }, """
Konzeption eines Proof-of-Concept (PoC) für einen L-System-Generator (Lindenmayer-Systeme).

- Untersuchung algorithmischer prozeduraler Generierung, Ersetzungsgrammatiken und geometrischer Fraktal-Visualisierung.
- Implementierung der Generierungs-Engine und Benutzeroberfläche für interaktive Regeltests.
""")

# ==============================================================================
# 3. EDUCATION
# ==============================================================================
def create_education():
    # 01 - PhD
    write_md("_education/01-phd-en.md", {
        "order": 1,
        "lang": "en",
        "degree": "Doctor of Philosophy (Ph.D.) in Computer Science",
        "institution": "[Doctoral School / Research Laboratory Placeholder]",
        "period": "2020 – 2026 (Expected)",
        "location": "France / Germany",
        "is_placeholder": True,
        "tags": ["PhD Candidate", "Doctoral Research", "Embedded Systems"]
    }, """
**Thesis:** *"[PhD Dissertation Title Placeholder • Embedded Systems / Hardware Computing / AI]"*

- **Advisors:** [Advisor Names Placeholder]
- **Specialization:** Embedded Systems, Hardware Acceleration, Edge AI, Distributed Systems.
""")

    write_md("_education/01-phd-fr.md", {
        "order": 1,
        "lang": "fr",
        "degree": "Doctorat (Ph.D.) en Informatique",
        "institution": "[École Doctorale / Laboratoire de Recherche Placeholder]",
        "period": "2020 – 2026 (Prévu)",
        "location": "France / Allemagne",
        "is_placeholder": True,
        "tags": ["Doctorant", "Recherche Doctorale", "Systèmes Embarqués"]
    }, """
**Thèse :** *"[Titre de la thèse • Systèmes Embarqués / Calcul Matériel / IA]"*

- **Directeurs de thèse :** [Noms des encadrants]
- **Spécialisation :** Systèmes embarqués, accélération matérielle, Edge AI, systèmes distribués.
""")

    write_md("_education/01-phd-de.md", {
        "order": 1,
        "lang": "de",
        "degree": "Promotion (Dr.-Ing. / Ph.D.) in Informatik",
        "institution": "[Graduiertenschule / Forschungslabor Platzhalter]",
        "period": "2020 – 2026 (Voraussichtlich)",
        "location": "Deutschland / Frankreich",
        "is_placeholder": True,
        "tags": ["Doktorand", "Doktorarbeit", "Eingebettete Systeme"]
    }, """
**Dissertation:** *"[Titel der Dissertation • Eingebettete Systeme / Hardwarebeschleunigung / KI]"*

- **Betreuer:** [Namen der Betreuer]
- **Schwerpunkte:** Eingebettete Systeme, Hardware-Beschleunigung, Edge AI, Verteilte Systeme.
""")

    # 02 - Master
    write_md("_education/02-master-en.md", {
        "order": 2,
        "lang": "en",
        "degree": "Master in Computer Science",
        "institution": "CY Cergy Paris University",
        "period": "2018 – 2020",
        "location": "Cergy, France",
        "tags": ["Valedictorian / Top-Ranking", "Smart Electronic Systems", "FPGA", "VHDL"]
    }, """
**Distinction:** Top-ranking of the research program in *Smart Electronic Systems*.

- Advanced curriculum covering embedded computing architectures, hardware description languages (VHDL), real-time operating systems, and smart electronic systems.
- Conducted research projects on Spiking Neural Networks (SNN) on FPGA and intelligent sensor networks.
""")

    write_md("_education/02-master-fr.md", {
        "order": 2,
        "lang": "fr",
        "degree": "Master en Informatique",
        "institution": "CY Cergy Paris Université",
        "period": "2018 – 2020",
        "location": "Cergy, France",
        "tags": ["Major de Promotion", "Systèmes Électroniques Intelligents", "FPGA", "VHDL"]
    }, """
**Distinction :** Major de promotion du parcours recherche en *Systèmes Électroniques Intelligents*.

- Programme avancé en architectures de calcul embarquées, langages de description matérielle (VHDL), systèmes d'exploitation temps réel et systèmes électroniques communicants.
- Réalisation de projets de recherche sur les réseaux de neurones à impulsions (SNN) sur FPGA et réseaux de capteurs intelligents.
""")

    write_md("_education/02-master-de.md", {
        "order": 2,
        "lang": "de",
        "degree": "Master of Science in Informatik",
        "institution": "CY Cergy Paris Universität",
        "period": "2018 – 2020",
        "location": "Cergy, Frankreich",
        "tags": ["Jahrgangsbester", "Intelligente Elektronische Systeme", "FPGA", "VHDL"]
    }, """
**Auszeichnung:** Jahrgangsbester im Forschungsschwerpunkt *Intelligente Elektronische Systeme*.

- Fortgeschrittenes Curriculum zu eingebetteten Rechnerarchitekturen, Hardwarebeschreibungssprachen (VHDL), Echtzeitbetriebssystemen und intelligenten elektronischen Systemen.
- Forschungsprojekte zu Spiking Neural Networks (SNN) auf FPGA und intelligenten Sensornetzwerken.
""")

    # 03 - Exchange
    write_md("_education/03-exchange-en.md", {
        "order": 3,
        "lang": "en",
        "degree": "Exchange Program in Computer Science",
        "institution": "Oregon State University",
        "period": "2017 – 2018",
        "location": "Corvallis, OR, USA",
        "tags": ["USA Exchange", "Computer Science", "Language Tutoring"]
    }, """
International academic exchange program in the School of Electrical Engineering and Computer Science.

- Followed advanced Computer Science coursework in algorithms, operating systems, and computer engineering.
- Gave French lessons as a tutor to undergraduate students.
""")

    write_md("_education/03-exchange-fr.md", {
        "order": 3,
        "lang": "fr",
        "degree": "Programme d'Échange Universitaire en Informatique",
        "institution": "Oregon State University",
        "period": "2017 – 2018",
        "location": "Corvallis, OR, États-Unis",
        "tags": ["Échange USA", "Informatique", "Tutorat linguistique"]
    }, """
Séjour académique international à la School of Electrical Engineering and Computer Science.

- Suivi de cours approfondis en algorithmique, systèmes d'exploitation et ingénierie informatique.
- Enseignement du français en tant que tuteur auprès d'étudiants de premier cycle.
""")

    write_md("_education/03-exchange-de.md", {
        "order": 3,
        "lang": "de",
        "degree": "Auslandsstudium in Informatik",
        "institution": "Oregon State University",
        "period": "2017 – 2018",
        "location": "Corvallis, OR, USA",
        "tags": ["USA-Austausch", "Informatik", "Sprachtutorium"]
    }, """
Internationales akademisches Austauschprogramm an der School of Electrical Engineering and Computer Science.

- Fortgeschrittene Informatikkurse in Algorithmen, Betriebssystemen und Computertechnik.
- Französischunterricht als Tutor für Bachelorstudierende.
""")

    # 04 - Licence
    write_md("_education/04-licence-en.md", {
        "order": 4,
        "lang": "en",
        "degree": "Licence in Computer Science",
        "institution": "University of Poitiers",
        "period": "2015 – 2018",
        "location": "Poitiers, France",
        "tags": ["High Honors", "Computer Science", "Algorithms", "C / C++"]
    }, """
**Graduation:** Graduated with high honors (Mention Bien / Très Bien).

- Comprehensive training in computer science fundamentals: algorithms, data structures, object-oriented programming (C++, C, Java), mathematics, and database management.
""")

    write_md("_education/04-licence-fr.md", {
        "order": 4,
        "lang": "fr",
        "degree": "Licence d'Informatique",
        "institution": "Université de Poitiers",
        "period": "2015 – 2018",
        "location": "Poitiers, France",
        "tags": ["Mention Bien", "Informatique", "Algorithmique", "C / C++"]
    }, """
**Diplôme :** Obtenu avec mention bien / très bien.

- Formation fondamentale complète en informatique : algorithmique, structures de données, programmation orientée objet (C++, C, Java), mathématiques et bases de données.
""")

    write_md("_education/04-licence-de.md", {
        "order": 4,
        "lang": "de",
        "degree": "Bachelor in Informatik (Licence)",
        "institution": "Universität Poitiers",
        "period": "2015 – 2018",
        "location": "Poitiers, Frankreich",
        "tags": ["Mit Auszeichnung", "Informatik", "Algorithmen", "C / C++"]
    }, """
**Abschluss:** Mit Auszeichnung abgeschlossen (Mention Bien / Très Bien).

- Fundierte Grundausbildung in Informatik: Algorithmen, Datenstrukturen, objektorientierte Programmierung (C++, C, Java), Mathematik und Datenbankmanagement.
""")

# ==============================================================================
# 4. PROJECTS
# ==============================================================================
def create_projects():
    # 01 - Smart Glasses
    write_md("_projects/01-smart-glasses-en.md", {
        "order": 1,
        "lang": "en",
        "category": "personal",
        "title": "Smart Glasses",
        "icon": "👓",
        "github": "https://github.com/sixdenip",
        "tags": ["BLE", "OLED HUD", "Android", "Wearables", "Embedded C"]
    }, """
A wearable Heads-Up Display (HUD) built on an OLED screen mounted directly onto glasses. Communicates with an Android device via Bluetooth Low Energy (BLE) to deliver turn-by-turn navigation assistance in real time.
""")

    write_md("_projects/01-smart-glasses-fr.md", {
        "order": 1,
        "lang": "fr",
        "category": "personal",
        "title": "Lunettes Connectées",
        "icon": "👓",
        "github": "https://github.com/sixdenip",
        "tags": ["BLE", "Affichage tête haute", "Android", "Wearables", "C Embarqué"]
    }, """
Affichage tête haute (HUD) sur écran OLED monté sur lunettes. Communique avec un appareil Android en BLE pour fournir une assistance à la navigation virage par virage en temps réel.
""")

    write_md("_projects/01-smart-glasses-de.md", {
        "order": 1,
        "lang": "de",
        "category": "personal",
        "title": "Intelligente Datenbrille",
        "icon": "👓",
        "github": "https://github.com/sixdenip",
        "tags": ["BLE", "OLED HUD", "Android", "Wearables", "Eingebettetes C"]
    }, """
Head-up-Display (HUD) auf einem an einer Brille montierten OLED-Display, das über BLE mit einem Android-Gerät kommuniziert, um Echtzeit-Navigationsanweisungen bereitzustellen.
""")

    # 02 - Pollution Advisor
    write_md("_projects/02-pollution-advisor-en.md", {
        "order": 2,
        "lang": "en",
        "category": "personal",
        "title": "Pollution Advisor",
        "icon": "🌱",
        "github": "https://github.com/sixdenip",
        "tags": ["Arduino", "Air Quality Sensors", "Android", "Open Data", "IoT"]
    }, """
A crowdsourced environmental monitoring solution consisting of a compact sensor-equipped Arduino device paired with an Android mobile app to collect, map, and open-source real-time urban air pollution data.
""")

    write_md("_projects/02-pollution-advisor-fr.md", {
        "order": 2,
        "lang": "fr",
        "category": "personal",
        "title": "Conseiller en Pollution",
        "icon": "🌱",
        "github": "https://github.com/sixdenip",
        "tags": ["Arduino", "Capteurs qualité de l'air", "Android", "Open Data", "IoT"]
    }, """
Solution de mesure environnementale participative comprenant un boîtier Arduino équipé de capteurs et une application mobile Android pour cartographier la pollution urbaine en open-data.
""")

    write_md("_projects/02-pollution-advisor-de.md", {
        "order": 2,
        "lang": "de",
        "category": "personal",
        "title": "Umwelt- & Schadstoffberater",
        "icon": "🌱",
        "github": "https://github.com/sixdenip",
        "tags": ["Arduino", "Luftqualitätssensoren", "Android", "Open Data", "IoT"]
    }, """
Crowdsourced Umweltüberwachungslösung bestehend aus einem Arduino-Gerät mit Sensoren und einer Android-App zur Erfassung und Bereitstellung offener Daten über städtische Luftverschmutzung.
""")

    # 03 - Foot Angle Detector
    write_md("_projects/03-foot-angle-en.md", {
        "order": 3,
        "lang": "en",
        "category": "personal",
        "title": "Foot Angle Detector",
        "icon": "📐",
        "github": "https://github.com/sixdenip",
        "tags": ["Android", "Computer Vision", "ArUco Markers", "HealthTech"]
    }, """
A therapeutic computer-vision Android application that calculates the biomechanical angle of a patient's foot placed on an ArUco calibration board, providing non-invasive diagnostic angles for medical and physical rehabilitation tracking.
""")

    write_md("_projects/03-foot-angle-fr.md", {
        "order": 3,
        "lang": "fr",
        "category": "personal",
        "title": "Détecteur d'Angle du Pied",
        "icon": "📐",
        "github": "https://github.com/sixdenip",
        "tags": ["Android", "Vision par ordinateur", "Marqueurs ArUco", "Santé"]
    }, """
Application Android de vision par ordinateur à visée thérapeutique calculant l'angle d'un pied sur mire ArUco pour le suivi médical et la rééducation biomécanique.
""")

    write_md("_projects/03-foot-angle-de.md", {
        "order": 3,
        "lang": "de",
        "category": "personal",
        "title": "Fußwinkel-Detektor",
        "icon": "📐",
        "github": "https://github.com/sixdenip",
        "tags": ["Android", "Computer Vision", "ArUco-Marker", "HealthTech"]
    }, """
Therapeutische Computer-Vision-Android-App zur Berechnung des Fußwinkels auf einem ArUco-Kalibrierungsbrett für die medizinische Reha-Überwachung.
""")

    # 04 - SNN FPGA
    write_md("_projects/04-snn-fpga-en.md", {
        "order": 4,
        "lang": "en",
        "category": "academic",
        "title": "Spiking Neural Network on FPGA",
        "icon": "⚡",
        "github": "https://github.com/sixdenip",
        "tags": ["FPGA", "VHDL", "Spiking Neural Networks", "Neuromorphic", "Vivado"]
    }, """
Research, RTL modeling, and hardware simulation of a biologically inspired Spiking Neural Network (SNN) architecture implemented on FPGA for low-power, neuromorphic spike-based computation.
""")

    write_md("_projects/04-snn-fpga-fr.md", {
        "order": 4,
        "lang": "fr",
        "category": "academic",
        "title": "Réseau de Neurones à Impulsions sur FPGA",
        "icon": "⚡",
        "github": "https://github.com/sixdenip",
        "tags": ["FPGA", "VHDL", "Réseaux de neurones pulsés", "Neuromorphique", "Vivado"]
    }, """
Recherche, modélisation RTL et simulation matérielle d'un réseau de neurones à impulsions (SNN) sur architecture FPGA pour le calcul neuromorphique basse consommation.
""")

    write_md("_projects/04-snn-fpga-de.md", {
        "order": 4,
        "lang": "de",
        "category": "academic",
        "title": "Spiking Neural Network auf FPGA",
        "icon": "⚡",
        "github": "https://github.com/sixdenip",
        "tags": ["FPGA", "VHDL", "Spiking Neural Networks", "Neuromorph", "Vivado"]
    }, """
Forschung, RTL-Modellierung und Hardwaresimulation eines biologisch inspirierten Spiking Neural Networks (SNN) auf FPGA für energieeffizientes neuromorphes Rechnen.
""")

    # 05 - Smart Car
    write_md("_projects/05-smart-car-en.md", {
        "order": 5,
        "lang": "en",
        "category": "academic",
        "title": "“La futée” : Smart Car",
        "icon": "🚗",
        "github": "https://github.com/sixdenip",
        "tags": ["Embedded Systems", "ADAS", "Sensor Fusion", "Smart Mobility", "C++"]
    }, """
An intelligent advanced driver-assistance system (ADAS) that anticipates forward hazards, obstacles, and collision risks using multi-sensor inputs to issue proactive real-time driver warnings.
""")

    write_md("_projects/05-smart-car-fr.md", {
        "order": 5,
        "lang": "fr",
        "category": "academic",
        "title": "« La futée » : Véhicule Intelligent",
        "icon": "🚗",
        "github": "https://github.com/sixdenip",
        "tags": ["Systèmes embarqués", "ADAS", "Fusion de capteurs", "Mobilité intelligente", "C++"]
    }, """
Système intelligent d'aide à la conduite (ADAS) anticipant les dangers de la route grâce à une fusion de capteurs embarqués pour alerter le conducteur proactivement en temps réel.
""")

    write_md("_projects/05-smart-car-de.md", {
        "order": 5,
        "lang": "de",
        "category": "academic",
        "title": "„La futée“ : Intelligentes Fahrzeug",
        "icon": "🚗",
        "github": "https://github.com/sixdenip",
        "tags": ["Eingebettete Systeme", "ADAS", "Sensorfusion", "Smart Mobility", "C++"]
    }, """
Fahrerassistenzsystem (ADAS), das Gefahren und Hindernisse auf der Straße durch Sensorfusion vorausschauend erkennt und den Fahrer in Echtzeit warnt.
""")

# ==============================================================================
# 5. PUBLICATIONS
# ==============================================================================
def create_publications():
    pubs = [
        {
            "id": "01-early-exit",
            "order": 1,
            "year": 2025,
            "title": "Early-Exit Neural Architecture Search for Energy-Harvesting Edge Computing",
            "authors": "Pierre-Louis Sixdenier, Mark Deutel, Jürgen Teich",
            "venue_short": "IEEE MCSoC 2025",
            "venue": "2025 IEEE 18th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)",
            "pages": "372--379",
            "doi": "10.1109/MCSoC67473.2025.00066",
            "doi_url": "https://doi.org/10.1109/MCSoC67473.2025.00066",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-sixdenier2025early",
            "badge": "🏆 Best Paper Award • IEEE MCSoC 2025",
            "badge_highlight": True,
            "abstract_en": "Investigates early-exit deep neural network (EE-NN) architecture search tailored for edge computing platforms powered by intermittent energy harvesting, dynamically selecting confidence-based early exits to preserve accuracy under fluctuating ambient power.",
            "abstract_fr": "Étude de la recherche d'architectures de réseaux de neurones profonds à sorties précoces (EE-NN) pour les plateformes edge alimentées par récupération intermittente d'énergie, sélectionnant dynamiquement les sorties de confiance pour préserver la précision sous puissance fluctuante.",
            "abstract_de": "Untersuchung der Suche nach Architekturen neuronaler Netze mit vorzeitigen Ausgängen (Early-Exit-NNs) für Edge-Computing-Systeme mit intermittierender Energieernte (Energy Harvesting) zur dynamischen Genauigkeitsanpassung bei schwankender Umgebungsenergie.",
            "bibtex": """@inproceedings{sixdenier2025early,
  author    = {Sixdenier, Pierre-Louis and Deutel, Mark and Teich, J{\\"u}rgen},
  title     = {Early-Exit Neural Architecture Search for Energy-Harvesting Edge Computing},
  booktitle = {2025 IEEE 18th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)},
  year      = {2025},
  pages     = {372--379},
  doi       = {10.1109/MCSoC67473.2025.00066}
}"""
        },
        {
            "id": "02-evaluating-arcs",
            "order": 2,
            "year": 2025,
            "title": "Evaluating the Potential of Intermittent Early-Exit Neural Networks",
            "authors": "Pierre-Louis Sixdenier, Stefan Wildermann, Jürgen Teich",
            "venue_short": "ARCS 2025",
            "venue": "Architecture of Computing Systems - 38th International Conference, ARCS 2025, Proceedings",
            "pages": "1--15",
            "doi": "10.1007/978-3-031-90576-6_1",
            "doi_url": "https://doi.org/10.1007/978-3-031-90576-6_1",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-sixdenier2025evaluating",
            "badge": "Springer LNCS • ARCS 2025",
            "badge_highlight": False,
            "abstract_en": "Evaluates the computational trade-offs, inference accuracy, and energy footprint of intermittent early-exit neural networks running on battery-free microcontrollers, showing significant speedups under severe energy constraints.",
            "abstract_fr": "Évalue les compromis computationnels, la précision d'inférence et l'empreinte énergétique des réseaux de neurones intermittents à sorties anticipées sur microcontrôleurs sans batterie, démontrant des gains de vitesse significatifs sous fortes contraintes énergétiques.",
            "abstract_de": "Evaluiert die Rechenkompromisse, Inferenzgenauigkeit und den Energie-Footprint intermittierender Early-Exit-Neuronaler Netze auf batterielosen Mikrocontrollern mit deutlichen Beschleunigungen unter strengen Energielimits.",
            "bibtex": """@inproceedings{sixdenier2025evaluating,
  author    = {Sixdenier, Pierre-Louis and Wildermann, Stefan and Teich, J{\\"u}rgen},
  title     = {Evaluating the Potential of Intermittent Early-Exit Neural Networks},
  booktitle = {Architecture of Computing Systems - 38th International Conference, ARCS 2025},
  year      = {2025},
  pages     = {1--15},
  doi       = {10.1007/978-3-031-90576-6_1}
}"""
        },
        {
            "id": "03-utility-ewsn",
            "order": 3,
            "year": 2025,
            "title": "WiP Paper: Utility-Aware Transmission of Sensor Data on Energy-Harvesting IoT Gateways",
            "authors": "Pierre-Louis Sixdenier, Jebacyril Arockiaraj, Stefan Wildermann, Jürgen Teich",
            "venue_short": "EWSN 2025",
            "venue": "Proceedings of the 2025 International Conference on Embedded Wireless Systems and Networks (EWSN 2025)",
            "pages": "1--4",
            "doi": "10.5555/ewsn2025.wip",
            "doi_url": "https://dblp.org/pid/344/6869.html",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-sixdenier2025utility",
            "badge": "ACM / EWSN 2025",
            "badge_highlight": False,
            "abstract_en": "Presents a utility-driven transmission scheduling policy for self-powered IoT edge gateways that prioritizes highly informative sensory data bursts according to energy availability forecasts.",
            "abstract_fr": "Présente une politique d'ordonnancement de transmission orientée utilité pour passerelles IoT autonomes, priorisant les paquets hautement informatifs selon les prévisions de récolte d'énergie.",
            "abstract_de": "Präsentiert eine nutzenbasierte Übertragungsplanungsstrategie für energieautarke IoT-Edge-Gateways, die hochinformative Sensordatenpakete entsprechend der Energieverfügbarkeitsprognose priorisiert.",
            "bibtex": """@inproceedings{sixdenier2025utility,
  author    = {Sixdenier, Pierre-Louis and Arockiaraj, Jebacyril and Wildermann, Stefan and Teich, J{\\"u}rgen},
  title     = {WiP Paper: Utility-Aware Transmission of Sensor Data on Energy-Harvesting IoT Gateways},
  booktitle = {2025 International Conference on Embedded Wireless Systems and Networks (EWSN)},
  year      = {2025},
  pages     = {1--4}
}"""
        },
        {
            "id": "04-gres-meco",
            "order": 4,
            "year": 2024,
            "title": "GRES: Guaranteed Remaining Energy Scheduling of Energy-harvesting Sensors by Quality Adaptation",
            "authors": "Pierre-Louis Sixdenier, Stefan Wildermann, Jürgen Teich",
            "venue_short": "IEEE MECO 2024",
            "venue": "13th Mediterranean Conference on Embedded Computing (MECO 2024)",
            "pages": "1--8",
            "doi": "10.1109/MECO62516.2024.10577901",
            "doi_url": "https://doi.org/10.1109/MECO62516.2024.10577901",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-sixdenier2024gres",
            "badge": "IEEE MECO 2024",
            "badge_highlight": False,
            "abstract_en": "Introduces GRES, a runtime scheduling methodology that mathematically guarantees non-zero residual energy across harvesting cycles by dynamically modulating sensor acquisition quality.",
            "abstract_fr": "Introduit GRES, une méthodologie d'ordonnancement à l'exécution garantissant formellement une énergie résiduelle non nulle en adaptant dynamiquement la qualité d'acquisition des capteurs.",
            "abstract_de": "Führt GRES ein, eine Laufzeit-Scheduling-Methodik, die mathematisch eine verbleibende Restenergie über Erntezyklen hinweg durch dynamische Anpassung der Sensor-Erfassungsqualität garantiert.",
            "bibtex": """@inproceedings{sixdenier2024gres,
  author    = {Sixdenier, Pierre-Louis and Wildermann, Stefan and Teich, J{\\"u}rgen},
  title     = {GRES: Guaranteed Remaining Energy Scheduling of Energy-harvesting Sensors by Quality Adaptation},
  booktitle = {13th Mediterranean Conference on Embedded Computing (MECO)},
  year      = {2024},
  pages     = {1--8},
  doi       = {10.1109/MECO62516.2024.10577901}
}"""
        },
        {
            "id": "05-hybrid-memocode",
            "order": 5,
            "year": 2023,
            "title": "Hybrid Genetic Reinforcement Learning for Generating Run-Time Requirement Enforcers",
            "authors": "Jan Spieck, Pierre-Louis Sixdenier, Khalil Esper, Stefan Wildermann, Jürgen Teich",
            "venue_short": "ACM/IEEE MEMOCODE 2023",
            "venue": "Proceedings of the 21st ACM-IEEE International Conference on Formal Methods and Models for System Design",
            "pages": "68--78",
            "doi": "10.1145/3610582.3614138",
            "doi_url": "https://doi.org/10.1145/3610582.3614138",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-spieck2023hybrid",
            "badge": "ACM / IEEE MEMOCODE 2023",
            "badge_highlight": False,
            "abstract_en": "Proposes a hybrid genetic algorithm and reinforcement learning pipeline to automatically synthesize verified runtime requirement enforcers for multicore embedded platforms.",
            "abstract_fr": "Propose une approche hybride combinant algorithmes génétiques et apprentissage par renforcement pour synthétiser automatiquement des contrôleurs d'exécution vérifiés sur systèmes multicœurs.",
            "abstract_de": "Schlägt eine hybride Pipeline aus genetischen Algorithmen und Reinforcement Learning vor, um automatisch verifizierte Laufzeit-Anforderungsdurchsetzer für Multicore-Systeme zu synthetisieren.",
            "bibtex": """@inproceedings{spieck2023hybrid,
  author    = {Spieck, Jan and Sixdenier, Pierre-Louis and Esper, Khalil and Wildermann, Stefan and Teich, J{\\"u}rgen},
  title     = {Hybrid Genetic Reinforcement Learning for Generating Run-Time Requirement Enforcers},
  booktitle = {21st ACM-IEEE International Conference on Formal Methods and Models for System Design (MEMOCODE)},
  year      = {2023},
  pages     = {68--78},
  doi       = {10.1145/3610582.3614138}
}"""
        },
        {
            "id": "06-seque-edge",
            "order": 6,
            "year": 2023,
            "title": "Seque: Lean and Energy-aware Data Management for IoT Gateways",
            "authors": "Pierre-Louis Sixdenier, Stefan Wildermann, Martin Ottens, Jürgen Teich",
            "venue_short": "IEEE EDGE 2023",
            "venue": "2023 IEEE International Conference on Edge Computing (EDGE 2023)",
            "pages": "180--189",
            "doi": "10.1109/EDGE60047.2023.00032",
            "doi_url": "https://doi.org/10.1109/EDGE60047.2023.00032",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-sixdenier2023seque",
            "badge": "IEEE EDGE 2023",
            "badge_highlight": False,
            "abstract_en": "Develops Seque, a lightweight and energy-aware time-series data management engine customized for flash memory endurance and battery-assisted IoT edge micro-gateways.",
            "abstract_fr": "Développe Seque, un moteur léger et économe en énergie de gestion de séries temporelles optimisé pour la longévité de la mémoire flash sur micro-passerelles IoT.",
            "abstract_de": "Entwickelt Seque, eine schlanke und energiebewusste Zeitreihendaten-Engine, optimiert für Flash-Speicher-Lebensdauer und batteriegestützte IoT-Edge-Mikrogateways.",
            "bibtex": """@inproceedings{sixdenier2023seque,
  author    = {Sixdenier, Pierre-Louis and Wildermann, Stefan and Ottens, Martin and Teich, J{\\"u}rgen},
  title     = {Seque: Lean and Energy-aware Data Management for IoT Gateways},
  booktitle = {2023 IEEE International Conference on Edge Computing (EDGE)},
  year      = {2023},
  pages     = {180--189},
  doi       = {10.1109/EDGE60047.2023.00032}
}"""
        },
        {
            "id": "07-raven-ngres",
            "order": 7,
            "year": 2023,
            "title": "RAVEN: Reinforcement Learning for Generating Verifiable Run-Time Requirement Enforcers for MPSoCs",
            "authors": "Khalil Esper, Jan Spieck, Pierre-Louis Sixdenier, Stefan Wildermann, Jürgen Teich",
            "venue_short": "OASIcs NG-RES 2023",
            "venue": "4th Workshop on Next Generation Real-Time Embedded Systems (NG-RES 2023)",
            "pages": "4:1--4:14",
            "doi": "10.4230/OASIcs.NG-RES.2023.4",
            "doi_url": "https://doi.org/10.4230/OASIcs.NG-RES.2023.4",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-esper2023raven",
            "badge": "OASIcs OpenAccess • NG-RES 2023",
            "badge_highlight": False,
            "abstract_en": "Introduces RAVEN to generate formally verifiable runtime requirement enforcers on multiprocessor systems-on-chip (MPSoCs) using deep reinforcement learning actors with formal shields.",
            "abstract_fr": "Présente RAVEN pour générer des contrôleurs d'exécution formellement vérifiables sur multiprocesseurs sur puce (MPSoC) via l'apprentissage par renforcement sécurisé.",
            "abstract_de": "Führt RAVEN ein, um formal verifizierbare Laufzeit-Durchsetzer auf Multiprozessor-System-on-Chips (MPSoCs) mittels Deep Reinforcement Learning und formalen Sicherheits-Shields zu generieren.",
            "bibtex": """@inproceedings{esper2023raven,
  author    = {Esper, Khalil and Spieck, Jan and Sixdenier, Pierre-Louis and Wildermann, Stefan and Teich, J{\\"u}rgen},
  title     = {RAVEN: Reinforcement Learning for Generating Verifiable Run-Time Requirement Enforcers for MPSoCs},
  booktitle = {4th Workshop on Next Generation Real-Time Embedded Systems (NG-RES)},
  year      = {2023},
  pages     = {4:1--4:14},
  doi       = {10.4230/OASIcs.NG-RES.2023.4}
}"""
        },
        {
            "id": "08-sida-samos",
            "order": 8,
            "year": 2022,
            "title": "SIDAM: A Design Space Exploration Framework for Multi-sensor Embedded Systems Powered by Energy Harvesting",
            "authors": "Pierre-Louis Sixdenier, Stefan Wildermann, Daniel Ziegler, Jürgen Teich",
            "venue_short": "SAMOS XXII 2022",
            "venue": "Embedded Computer Systems: Architectures, Modeling, and Simulation - 22nd International Conference",
            "pages": "377--392",
            "doi": "10.1007/978-3-031-15074-6_26",
            "doi_url": "https://doi.org/10.1007/978-3-031-15074-6_26",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-sixdenier2022sidam",
            "badge": "Springer LNCS • SAMOS XXII",
            "badge_highlight": False,
            "abstract_en": "Formulates SIDAM, an automated multi-objective design space exploration tool for sizing solar panels, supercapacitors, and sensor sampling policies in autonomous ambient systems.",
            "abstract_fr": "Formule SIDAM, un outil d'exploration automatique d'espace de conception multi-objectifs pour le dimensionnement de panneaux solaires, supercondensateurs et politiques d'acquisition de capteurs.",
            "abstract_de": "Formuliert SIDAM, ein automatisiertes Multi-Objective-Design-Space-Exploration-Framework zur Dimensionierung von Solarzellen, Superkondensatoren und Sensor-Abtaststrategien in autonomen Systemen.",
            "bibtex": """@inproceedings{sixdenier2022sidam,
  author    = {Sixdenier, Pierre-Louis and Wildermann, Stefan and Ziegler, Daniel and Teich, J{\\"u}rgen},
  title     = {SIDAM: A Design Space Exploration Framework for Multi-sensor Embedded Systems Powered by Energy Harvesting},
  booktitle = {Embedded Computer Systems: Architectures, Modeling, and Simulation (SAMOS XXII)},
  year      = {2022},
  pages     = {377--392},
  doi       = {10.1007/978-3-031-15074-6_26}
}"""
        },
        {
            "id": "09-towards-acsos",
            "order": 9,
            "year": 2021,
            "title": "Towards an Autonomous, Power-Efficient Base Station for Sensor Data Collection",
            "authors": "Pierre-Louis Sixdenier",
            "venue_short": "IEEE ACSOS-C 2021",
            "venue": "2021 IEEE International Conference on Autonomic Computing and Self-Organizing Systems Companion (ACSOS-C)",
            "pages": "174--176",
            "doi": "10.1109/ACSOS-C52956.2021.00052",
            "doi_url": "https://doi.org/10.1109/ACSOS-C52956.2021.00052",
            "dblp_url": "https://dblp.org/pid/344/6869.html",
            "bibtex_id": "bib-sixdenier2021towards",
            "badge": "IEEE ACSOS-C 2021",
            "badge_highlight": False,
            "abstract_en": "Early doctoral vision paper establishing foundational design challenges for self-sustainable, energy-neutral base stations collecting remote sensor telemetry in remote environments.",
            "abstract_fr": "Article prospectif doctoral posant les défis fondamentaux d'architecture pour stations de base autonomes et énergétiquement neutres collectant des données environnementales.",
            "abstract_de": "Frühes Doktoranden-Forschungspapier über die grundlegenden Architekturausforderungen für autarke, energieneutrale Basisstationen zur Sensordatenerfassung in abgelegenen Umgebungen.",
            "bibtex": """@inproceedings{sixdenier2021towards,
  author    = {Sixdenier, Pierre-Louis},
  title     = {Towards an Autonomous, Power-Efficient Base Station for Sensor Data Collection},
  booktitle = {2021 IEEE International Conference on Autonomic Computing and Self-Organizing Systems Companion (ACSOS-C)},
  year      = {2021},
  pages     = {174--176},
  doi       = {10.1109/ACSOS-C52956.2021.00052}
}"""
        }
    ]

    for p in pubs:
        fm_common = {
            "order": p["order"],
            "year": p["year"],
            "title": p["title"],
            "authors": p["authors"],
            "self_author": "Pierre-Louis Sixdenier",
            "venue_short": p["venue_short"],
            "venue": p["venue"],
            "pages": p["pages"],
            "doi": p["doi"],
            "doi_url": p["doi_url"],
            "dblp_url": p["dblp_url"],
            "bibtex_id": p["bibtex_id"],
            "badge": p["badge"],
            "badge_highlight": p["badge_highlight"],
            "bibtex": p["bibtex"]
        }

        # EN
        fm_en = dict(fm_common, lang="en")
        write_md(f"_publications/{p['id']}-en.md", fm_en, p["abstract_en"])

        # FR
        fm_fr = dict(fm_common, lang="fr")
        write_md(f"_publications/{p['id']}-fr.md", fm_fr, p["abstract_fr"])

        # DE
        fm_de = dict(fm_common, lang="de")
        write_md(f"_publications/{p['id']}-de.md", fm_de, p["abstract_de"])

# ==============================================================================
# 6. SKILLS
# ==============================================================================
def create_skills():
    skills_data = [
        {
            "id": "01-languages",
            "order": 1,
            "icon": "💻",
            "en": {
                "title": "Programming Languages",
                "skills": ["C++", "C", "VHDL", "Python", "Node.js", "HTML / CSS"]
            },
            "fr": {
                "title": "Langages de Programmation",
                "skills": ["C++", "C", "VHDL", "Python", "Node.js", "HTML / CSS"]
            },
            "de": {
                "title": "Programmiersprachen",
                "skills": ["C++", "C", "VHDL", "Python", "Node.js", "HTML / CSS"]
            }
        },
        {
            "id": "02-embedded",
            "order": 2,
            "icon": "🔌",
            "en": {
                "title": "Embedded & FPGA",
                "skills": ["FPGA", "Vivado (Xilinx)", "Quartus (Intel/Altera)", "STM32 (Keil µVision)", "Arduino", "BLE / Bluetooth", "Sensors & Actuators"]
            },
            "fr": {
                "title": "Systèmes Embarqués & FPGA",
                "skills": ["FPGA", "Vivado (Xilinx)", "Quartus (Intel/Altera)", "STM32 (Keil µVision)", "Arduino", "BLE / Bluetooth", "Capteurs & Actionneurs"]
            },
            "de": {
                "title": "Eingebettete Systeme & FPGA",
                "skills": ["FPGA", "Vivado (Xilinx)", "Quartus (Intel/Altera)", "STM32 (Keil µVision)", "Arduino", "BLE / Bluetooth", "Sensoren & Aktoren"]
            }
        },
        {
            "id": "03-dbms",
            "order": 3,
            "icon": "🗄️",
            "en": {
                "title": "Databases & DBMS",
                "skills": ["MongoDB", "Neo4J", "PostgreSQL", "MySQL"]
            },
            "fr": {
                "title": "Bases de Données & SGBD",
                "skills": ["MongoDB", "Neo4J", "PostgreSQL", "MySQL"]
            },
            "de": {
                "title": "Datenbanken & DBMS",
                "skills": ["MongoDB", "Neo4J", "PostgreSQL", "MySQL"]
            }
        },
        {
            "id": "04-flow",
            "order": 4,
            "icon": "⚙️",
            "en": {
                "title": "Programming Flow & Tools",
                "skills": ["Git & GitHub", "Docker", "UML Design", "Linux / Shell"]
            },
            "fr": {
                "title": "Outils & Méthodologies",
                "skills": ["Git & GitHub", "Docker", "Conception UML", "Linux / Shell"]
            },
            "de": {
                "title": "Entwicklungstools & Methodik",
                "skills": ["Git & GitHub", "Docker", "UML-Design", "Linux / Shell"]
            }
        },
        {
            "id": "05-spoken",
            "order": 5,
            "icon": "🌐",
            "en": {
                "title": "Spoken Languages",
                "skills": ["<strong>French:</strong> Native", "<strong>English:</strong> C1 (IELTS: 7, TOEIC: 975)", "<strong>Spanish:</strong> B1"]
            },
            "fr": {
                "title": "Langues Vivantes",
                "skills": ["<strong>Français :</strong> Langue maternelle", "<strong>Anglais :</strong> C1 (IELTS : 7, TOEIC : 975)", "<strong>Espagnol :</strong> B1"]
            },
            "de": {
                "title": "Sprachkenntnisse",
                "skills": ["<strong>Französisch:</strong> Muttersprache", "<strong>Englisch:</strong> C1 (IELTS: 7, TOEIC: 975)", "<strong>Spanisch:</strong> B1"]
            }
        },
        {
            "id": "06-awards",
            "order": 6,
            "icon": "🏆",
            "en": {
                "title": "Proud Of & Awards",
                "skills": ["🥈 <strong>2nd Place:</strong> Renault Digital Hackathon 2019", "🥈 <strong>2nd Place:</strong> ENSEack 2020"]
            },
            "fr": {
                "title": "Distinctions & Hackathons",
                "skills": ["🥈 <strong>2e Place :</strong> Hackathon Renault Digital 2019", "🥈 <strong>2e Place :</strong> ENSEack 2020"]
            },
            "de": {
                "title": "Erfolge & Auszeichnungen",
                "skills": ["🥈 <strong>2. Platz:</strong> Renault Digital Hackathon 2019", "🥈 <strong>2. Platz:</strong> ENSEack 2020"]
            }
        }
    ]

    for s in skills_data:
        for lang in ["en", "fr", "de"]:
            data = s[lang]
            fm = {
                "order": s["order"],
                "lang": lang,
                "title": data["title"],
                "icon": s["icon"],
                "skills": data["skills"]
            }
            write_md(f"_skills/{s['id']}-{lang}.md", fm, "")

def main():
    print("Building multilingual item Markdown files...")
    create_about()
    create_experience()
    create_education()
    create_projects()
    create_publications()
    create_skills()
    print("All multilingual items generated successfully!")

if __name__ == "__main__":
    main()
