---
title: "प्रragya Lab - Publications"
layout: default
excerpt: "प्रragya Lab -- Publications."
sitemap: false
permalink: /publications/
---

<div class="search-container">
  <input type="text" class="search-box" id="searchInput" placeholder="Search publications by title, author, venue, or category...">
</div>

<!-- Publications by Year -->
<div id="publications-container">
  {% assign years = site.data.publist | group_by: 'year' | sort: 'name' | reverse %}
  
  {% for year_group in years %}
  <div class="year-section">
    <h2 class="year-title">{{ year_group.name }}</h2>
    
    {% for publi in year_group.items %}
    <div class="publication-item" data-category="{{ publi.categories | join: ' ' }}" data-year="{{ publi.year }}">
      <div class="category-tag category-{{ publi.venue_tag }}">{{ publi.venue_short }}</div>
      <div class="pub-title">{{ publi.title }}</div>
      <div class="pub-authors">{{ publi.authors }}</div>
      <div class="pub-venue">{{ publi.venue }}</div>
      <div class="pub-actions">
        {% if publi.paper_url %}
        <a href="{{ publi.paper_url }}" class="pub-btn" target="_blank">Paper</a>
        {% endif %}
        {% if publi.cite_url %}
        <a href="{{ publi.cite_url }}" class="pub-btn" target="_blank">Cite</a>
        {% endif %}
        {% if publi.website_url %}
        <a href="{{ publi.website_url }}" class="pub-btn" target="_blank">Website</a>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
  {% endfor %}
</div>

<div id="no-results" class="no-results hidden">
  No publications found matching your search criteria.
</div>

<style>
.search-container {
  margin-bottom: 30px;
}

.search-box {
  width: 100%;
  max-width: 500px;
  padding: 12px 20px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
}

.year-section {
  margin-bottom: 40px;
}

.year-title {
  font-size: 28px;
  color: #666;
  text-align: right;
  margin-bottom: 20px;
  font-weight: 300;
}

.publication-item {
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  border-left: 4px solid #007bff;
  transition: box-shadow 0.2s;
}

.publication-item:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.category-tag {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 10px;
  color: white;
}

.category-tallip { background-color: #28a745; }
.category-icml { background-color: #007bff; }
.category-neurips { background-color: #fd7e14; }
.category-acl { background-color: #6f42c1; }
.category-emnlp { background-color: #dc3545; }
.category-arxiv { background-color: #6c757d; }

.pub-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 10px;
  line-height: 1.4;
  color: #333;
}

.pub-authors {
  color: #666;
  margin-bottom: 8px;
  line-height: 1.5;
}

.pub-venue {
  color: #888;
  font-style: italic;
  margin-bottom: 15px;
}

.pub-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.pub-btn {
  padding: 6px 12px;
  border: 1px solid #007bff;
  border-radius: 4px;
  text-decoration: none;
  color: #007bff;
  font-size: 12px;
  text-transform: uppercase;
  font-weight: 500;
  transition: all 0.3s;
}

.pub-btn:hover {
  background-color: #007bff;
  color: white;
  text-decoration: none;
}

.hidden {
  display: none;
}

.no-results {
  text-align: center;
  color: #888;
  font-size: 18px;
  margin: 40px 0;
  padding: 40px;
  background-color: #f8f9fa;
  border-radius: 8px;
}

@media (max-width: 768px) {
  .year-title {
    font-size: 24px;
    text-align: left;
  }
  
  .pub-actions {
    gap: 8px;
  }
}
</style>

<script>
// Search functionality
function setupSearch() {
  const searchInput = document.getElementById('searchInput');
  const publicationItems = document.querySelectorAll('.publication-item');
  const noResults = document.getElementById('no-results');

  searchInput.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    let visibleCount = 0;

    publicationItems.forEach(item => {
      const title = item.querySelector('.pub-title').textContent.toLowerCase();
      const authors = item.querySelector('.pub-authors').textContent.toLowerCase();
      const venue = item.querySelector('.pub-venue').textContent.toLowerCase();
      const categories = item.dataset.category.toLowerCase();

      const isVisible = title.includes(searchTerm) || 
                      authors.includes(searchTerm) || 
                      venue.includes(searchTerm) ||
                      categories.includes(searchTerm);

      if (isVisible) {
        item.classList.remove('hidden');
        visibleCount++;
      } else {
        item.classList.add('hidden');
      }
    });

    // Show/hide year sections based on visible publications
    document.querySelectorAll('.year-section').forEach(section => {
      const visiblePubs = section.querySelectorAll('.publication-item:not(.hidden)');
      if (visiblePubs.length === 0) {
        section.classList.add('hidden');
      } else {
        section.classList.remove('hidden');
      }
    });

    // Show no results message
    if (visibleCount === 0 && searchTerm.length > 0) {
      noResults.classList.remove('hidden');
    } else {
      noResults.classList.add('hidden');
    }
  });
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
  setupSearch();
});
</script>