---
title: "प्रragya Lab - Team"
layout: gridlay
excerpt: "प्रragya Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

**We are looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**

Jump to [Faculty](#faculty), [Fellows, Mentors, Collaborators](#fellows-mentors-collaborators), [Students](#students).

## Faculty
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 0 %}
<div class="row">
{% endif %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left; margin-right: 15px; margin-bottom: 5px;" alt="{{ member.name }}" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} </i>
  <ul style="overflow: hidden;">
  {% if member.number_educ == 1 %}
    <li>{{ member.education1 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 2 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 3 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
    <li>{{ member.education3 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 4 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
    <li>{{ member.education3 | markdownify }}</li>
    <li>{{ member.education4 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 5 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
    <li>{{ member.education3 | markdownify }}</li>
    <li>{{ member.education4 | markdownify }}</li>
    <li>{{ member.education5 | markdownify }}</li>
  {% endif %}
  </ul>
</div>
{% assign number_printed = number_printed | plus: 1 %}
{% if even_odd == 1 %}
</div>
{% endif %}
{% endfor %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Fellows, Mentors, Collaborators
{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 0 %}
<div class="row">
{% endif %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left; margin-right: 15px; margin-bottom: 5px;" alt="{{ member.name }}" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden;">
    </ul>
</div>
{% assign number_printed = number_printed | plus: 1 %}
{% if even_odd == 1 %}
</div>
{% endif %}
{% endfor %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Students
{% assign number_printed = 0 %}
{% for member in site.data.students %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 0 %}
<div class="row">
{% endif %}
<div class="col-sm-6 clearfix">
  {% if member.photo %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left; margin-right: 15px; margin-bottom: 5px;" alt="{{ member.name }}" />
  {% endif %}
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} </i>
  <ul style="overflow: hidden;">
  {% if member.number_educ == 1 %}
    <li>{{ member.education1 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 2 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 3 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
    <li>{{ member.education3 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 4 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
    <li>{{ member.education3 | markdownify }}</li>
    <li>{{ member.education4 | markdownify }}</li>
  {% endif %}
  {% if member.number_educ == 5 %}
    <li>{{ member.education1 | markdownify }}</li>
    <li>{{ member.education2 | markdownify }}</li>
    <li>{{ member.education3 | markdownify }}</li>
    <li>{{ member.education4 | markdownify }}</li>
    <li>{{ member.education5 | markdownify }}</li>
  {% endif %}
  </ul>
</div>
{% assign number_printed = number_printed | plus: 1 %}
{% if even_odd == 1 %}
</div>
{% endif %}
{% endfor %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}