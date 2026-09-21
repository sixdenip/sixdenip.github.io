---
order: 1
section_id: "about"
title: "About Me"
nav_title: "About"
subtitle: "Embedded Systems Engineer & Computer Science Doctoral Student passionate about FPGA, neuromorphic hardware, and smart connected devices."
badge: "Biography"
badge_icon: "👋"
---

{% assign sorted_about = site.about | sort: "order" %}
{% for item in sorted_about %}
<div class="lang-item" data-lang="{{ item.lang }}">
{{ item.content | markdownify }}
</div>
{% endfor %}
