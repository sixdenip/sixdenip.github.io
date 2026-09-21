---
order: 5
section_id: "projects"
title: "Projects & Hardware Prototypes"
nav_title: "Projects"
subtitle: "Personal inventions, embedded IoT systems, and academic hardware/software research projects."
badge: "Portfolio & Engineering"
badge_icon: "💡"
---

<h3 style="margin: 1rem 0 1rem; color: var(--text-main); font-size: 1.25rem;" data-i18n="section.projects.personal_title">🔧 Personal Projects</h3>

<div class="projects-grid">
{% assign sorted_projects = site.projects | sort: "order" %}
{% for item in sorted_projects %}
  {% if item.category == "personal" %}
  <div class="project-card lang-item" data-lang="{{ item.lang }}">
    <div>
      <div class="project-top">
        <div class="project-icon">{{ item.icon }}</div>
        <div class="project-links">
          {% if item.github %}
          <a href="{{ item.github }}" target="_blank" rel="noopener" class="project-link-btn" title="GitHub Profile">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          </a>
          {% endif %}
        </div>
      </div>
      <h4 class="project-name" style="margin-bottom: 0.5rem; font-size: 1.15rem; color: var(--text-main);">{{ item.title }}</h4>
      <div class="project-desc markdown-body">
{{ item.content | markdownify }}
      </div>
    </div>
    {% if item.tags %}
    <div class="project-tags">
      {% for tag in item.tags %}
      <span class="tag-pill">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}
</div>

<h3 style="margin: 2.5rem 0 1rem; color: var(--text-main); font-size: 1.25rem;" data-i18n="section.projects.academic_title">🎓 Academic &amp; Research Projects</h3>

<div class="projects-grid">
{% for item in sorted_projects %}
  {% if item.category == "academic" %}
  <div class="project-card lang-item" data-lang="{{ item.lang }}">
    <div>
      <div class="project-top">
        <div class="project-icon">{{ item.icon }}</div>
        <div class="project-links">
          {% if item.github %}
          <a href="{{ item.github }}" target="_blank" rel="noopener" class="project-link-btn" title="GitHub Profile">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          </a>
          {% endif %}
        </div>
      </div>
      <h4 class="project-name" style="margin-bottom: 0.5rem; font-size: 1.15rem; color: var(--text-main);">{{ item.title }}</h4>
      <div class="project-desc markdown-body">
{{ item.content | markdownify }}
      </div>
    </div>
    {% if item.tags %}
    <div class="project-tags">
      {% for tag in item.tags %}
      <span class="tag-pill">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}
</div>
