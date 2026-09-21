---
order: 6
section_id: "skills"
title: "Skills, Languages & Recognitions"
nav_title: "Skills"
subtitle: "Technical competencies, embedded hardware tools, languages, and competitive hackathon achievements."
badge: "Expertise & Honors"
badge_icon: "⚡"
---

<div class="skills-grid">
{% assign sorted_skills = site.skills | sort: "order" %}
{% for item in sorted_skills %}
  <div class="skill-card lang-item" data-lang="{{ item.lang }}">
    <h3 class="skill-card-title">
      <span>{{ item.icon }}</span> <span>{{ item.title }}</span>
    </h3>
    <div class="skill-badges">
      {% for s in item.skills %}
        <span class="skill-pill">{{ s }}</span>
      {% endfor %}
    </div>
  </div>
{% endfor %}
</div>
