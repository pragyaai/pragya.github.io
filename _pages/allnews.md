---
title: "News"
layout: textlay
excerpt: "प्रragya Lab at BITS Goa, India."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br> {{ article.headline | markdownify}}</p>
{% endfor %}
