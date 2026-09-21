---
order: 4
section_id: "publications"
title: "Scientific Papers & Publications"
nav_title: "Publications"
subtitle: "Peer-reviewed conference proceedings and workshop publications in embedded systems, energy-harvesting IoT, and hardware-software co-design."
badge: "Research Output"
badge_icon: "📚"
---

<div style="margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem;">
  <p style="margin: 0; color: var(--text-muted); font-size: 0.95rem;" data-i18n="section.publications.indexed_in">
    Publications indexed in <strong>IEEE Xplore</strong>, <strong>ACM Digital Library</strong>, and <strong>DBLP</strong>.
  </p>
  <a href="{{ '/assets/papers.bib' | relative_url }}" download class="btn btn-secondary btn-sm" title="Download Complete BibTeX File">
    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
    <span data-i18n="section.publications.download_bib">Download papers.bib</span>
  </a>
</div>

{% assign sorted_pubs = site.publications | sort: "order" %}
{% for item in sorted_pubs %}
<article class="pub-card lang-item" data-lang="{{ item.lang }}">
  <div class="pub-top">
    {% if item.badge %}
    <span class="pub-venue-badge"{% if item.badge_highlight %} style="border-color: #eab308; color: #facc15;"{% endif %}>
      {{ item.badge }}
    </span>
    {% endif %}
    <span class="pub-year">{{ item.year }}</span>
  </div>

  <h3 class="pub-title">
    {{ item.title }}
  </h3>

  <div class="pub-authors">
    {{ item.authors }}
  </div>

  <div class="pub-abstract">
    <strong>Abstract:</strong> {{ item.content }}
  </div>

  <div class="pub-actions">
    {% if item.doi_url %}
    <a href="{{ item.doi_url }}" class="pub-btn" target="_blank" rel="noopener">
      DOI: {{ item.doi }}
    </a>
    {% endif %}
    {% if item.dblp_url %}
    <a href="{{ item.dblp_url }}" class="pub-btn" target="_blank" rel="noopener">DBLP</a>
    {% endif %}
    {% if item.bibtex %}
    <button class="pub-btn" data-toggle-bibtex="{{ item.bibtex_id }}-{{ item.lang }}">BibTeX</button>
    {% endif %}
  </div>

  {% if item.bibtex %}
  <div id="{{ item.bibtex_id }}-{{ item.lang }}" class="bibtex-block">
    <button class="btn btn-secondary btn-sm copy-bibtex-btn" data-copy-target="{{ item.bibtex_id }}-{{ item.lang }}">Copy</button>
<code>{{ item.bibtex }}</code>
  </div>
  {% endif %}
</article>
{% endfor %}
