---
order: 3
section_id: "education"
title: "Academic Background"
nav_title: "Education"
subtitle: "Formal higher education degrees, academic distinctions, and international exchange programs."
badge: "Curriculum Vitae"
badge_icon: "🎓"
---

<div class="timeline">
{% assign sorted_edu = site.education | sort: "order" %}
{% for item in sorted_edu %}
<div class="timeline-item lang-item" data-lang="{{ item.lang }}">
  <div class="timeline-dot"></div>
  <div class="timeline-card"{% if item.is_placeholder %} style="border-style: dashed; border-color: var(--card-hover-border);"{% endif %}>
    <div class="timeline-header">
      <h3 class="timeline-role">{{ item.degree }}</h3>
      <span class="timeline-period">{{ item.period }}</span>
    </div>
    <div class="timeline-org">
      <span>{{ item.institution }}</span>
      {% if item.location %}<span class="timeline-location">&bull; {{ item.location }}</span>{% endif %}
    </div>
    <div class="timeline-desc markdown-body">
{{ item.content | markdownify }}
    </div>
    {% if item.tags %}
    <div class="timeline-tags">
      {% for tag in item.tags %}
      <span class="tag-pill">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>
