---
order: 2
section_id: "experience"
title: "Professional Experience"
nav_title: "Experience"
subtitle: "Industrial engineering positions, research lab internships, and professional appointments."
badge: "Career History"
badge_icon: "💼"
---

<div class="timeline">
{% assign sorted_exp = site.experience | sort: "order" %}
{% for item in sorted_exp %}
<div class="timeline-item lang-item" data-lang="{{ item.lang }}">
  <div class="timeline-dot"></div>
  <div class="timeline-card"{% if item.is_placeholder %} style="border-style: dashed; border-color: var(--card-hover-border);"{% endif %}>
    <div class="timeline-header">
      <h3 class="timeline-role">{{ item.role }}</h3>
      <span class="timeline-period">{{ item.period }}</span>
    </div>
    <div class="timeline-org">
      <span>{{ item.organization }}</span>
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
