# Pierre-Louis Sixdenier &ndash; Academic Resume &amp; Portfolio Website

[![Deploy Jekyll site to Pages](https://github.com/sixdenier/sixdenier.github.io/actions/workflows/pages.yml/badge.svg)](https://github.com/sixdenier/sixdenier.github.io/actions/workflows/pages.yml)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-blue?logo=github)](https://sixdenier.github.io)
[![Jekyll](https://img.shields.io/badge/Static%20Site%20Generator-Jekyll-red?logo=jekyll)](https://jekyllrb.com)

A modern, responsive, and animated academic portfolio and resume website built specifically for **Pierre-Louis Sixdenier**, PhD candidate in Computer Science / Artificial Intelligence.

Designed to be hosted directly on **GitHub Pages** using the **Jekyll** template engine.

---

## ✨ Features

- **Markdown-Driven Sections**: Every section is an independent Markdown file located in `_sections/`. You can add, edit, re-order, or disable sections without touching HTML!
- **Modern & Smooth Design**:
  - Dark / Light mode toggle with persistent state in `localStorage` and system theme detection.
  - Glassmorphism UI components with refined gradient borders and ambient floating background glows.
  - Interactive scroll-reveal animations via `IntersectionObserver`.
  - Sticky header navigation with auto-updating **ScrollSpy**.
  - Accessible and respects `prefers-reduced-motion`.
- **Academic Highlights**:
  - **Professional Experience** & **Academic Background**: Interactive chronological timeline layout with tags, role details, and honors.
  - **Scientific Papers**: Rich publication cards with conference badges, author highlighting, abstracts, PDF/arXiv/code links, and an expandable 1-click **Copy BibTeX** snippet.
  - **Side Projects**: Open-source repositories and software tooling showcase cards.
  - **Skills & Service**: Research frameworks, languages, HPC tools, and peer-review appointments.
- **Print-Friendly**: Built-in `@media print` CSS cleanly strips navigation and buttons to generate a printer-ready academic CV when pressing `Ctrl+P` / `Cmd+P`.

---

## 📁 Repository Structure

```
sixdenier.github.io/
├── .github/
│   └── workflows/
│       └── pages.yml        # GitHub Actions workflow for automated deployment
├── _config.yml              # Jekyll site metadata, author details, social links
├── Gemfile                  # Ruby dependencies (github-pages)
├── index.html               # Main homepage layout iterating through _sections/
├── _layouts/
│   └── default.html         # HTML5 base template (header, content, footer, scripts)
├── _includes/
│   ├── head.html            # Meta tags, SEO, Google Fonts, stylesheets
│   ├── nav.html             # Navigation bar dynamically built from sections
│   ├── hero.html            # Animated hero banner with stats and quick links
│   └── footer.html          # Clean footer with back-to-top button
├── _sections/               # Markdown-powered sections
│   ├── 01-about.md          # Biography & research overview
│   ├── 02-experience.md     # Professional experience (timeline)
│   ├── 03-education.md      # Academic background (degrees & honors)
│   ├── 04-publications.md   # Scientific papers with BibTeX copy
│   ├── 05-projects.md       # Side projects & software
│   └── 06-skills.md         # Skills & academic service
└── assets/
    ├── css/
    │   └── style.css        # Modern responsive design & animations
    ├── js/
    │   └── main.js          # Theme toggle, scrollspy, BibTeX copy toast
    └── images/
        └── avatar.svg       # Sleek vector avatar placeholder
```

---

## 🚀 How to Customize

### 1. Update Personal & Lab Info
Open `_config.yml` and adjust your information:
```yaml
title: "Pierre-Louis Sixdenier"
author: "Pierre-Louis Sixdenier"
email: "pierre-louis.sixdenier@example.edu"
affiliation: "Doctoral School of Computer Science"
lab: "Vision & Learning Laboratory"
location: "Paris, France"

social:
  github: "sixdenier"
  linkedin: "pierre-louis-sixdenier"
  scholar: "https://scholar.google.com/citations?user=YOUR_ID"
```

### 2. Editing or Adding Sections
To edit any section, open the corresponding file in `_sections/`:
- **Add a Paper**: Open `_sections/04-publications.md` and duplicate a `<article class="pub-card">` block.
- **Add Experience**: Open `_sections/02-experience.md` and add a new `<div class="timeline-item">`.
- **Add a Project**: Open `_sections/05-projects.md` and add a new `<div class="project-card">`.
- **Reorder Sections**: Simply change the `order: 1..N` value in the YAML front matter of the Markdown file. The navigation menu and homepage automatically reorder themselves!

### 3. Replace the Avatar
Drop your portrait photo at `assets/images/avatar.jpg` (or `.png`), and update the path in `_includes/hero.html` and `_includes/head.html`.

---

## 🌐 Deploying to GitHub Pages

### Option A: Automatic via GitHub Actions (Recommended)
1. Push your repository to GitHub:
   ```bash
   git add .
   git commit -m "Initialize modern Jekyll academic resume"
   git push origin main
   ```
2. In your repository on GitHub, navigate to **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, select **GitHub Actions**.
4. The `.github/workflows/pages.yml` workflow will automatically build and publish your site to `https://sixdenier.github.io/`.

### Option B: Deploy from Branch
1. Under **Settings** > **Pages**, keep **Deploy from a branch**.
2. Select branch `main` and root `/`.
3. GitHub Pages will build the Jekyll site automatically.

---

## 💻 Local Development (Optional)

If you have Ruby installed locally:
```bash
bundle install
bundle exec jekyll serve --livereload
```
Then visit `http://localhost:4000`.