import requests
import unittest
from bs4 import BeautifulSoup

class JekyllWebsiteTest(unittest.TestCase):
    """Test suite for the Jekyll-based academic website."""
    
    BASE_URL = "http://localhost:4000"
    
    def test_homepage_accessibility(self):
        """Test that the homepage is accessible."""
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200, "Homepage should be accessible")
        self.assertIn("प्रragya Lab", response.text, "Homepage should contain lab name")
    
    def test_navigation_links(self):
        """Test that all navigation links are present."""
        response = requests.get(f"{self.BASE_URL}/")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check navigation links
        nav_links = soup.select('.navbar-nav li a')
        expected_links = ['Home', 'Team', 'Vacancies', 'Publications', 'Research']
        
        nav_texts = [link.text.strip() for link in nav_links]
        for expected in expected_links:
            self.assertIn(expected, nav_texts, f"Navigation should include {expected}")
    
    def test_publications_page_accessibility(self):
        """Test that the publications page is accessible."""
        response = requests.get(f"{self.BASE_URL}/publications/")
        self.assertEqual(response.status_code, 200, "Publications page should be accessible")
    
    def test_publications_content(self):
        """Test that publications are properly displayed."""
        response = requests.get(f"{self.BASE_URL}/publications/")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for search box
        search_box = soup.select_one('#searchInput')
        self.assertIsNotNone(search_box, "Search box should be present")
        
        # Check for publication items
        publications = soup.select('.publication-item')
        self.assertGreater(len(publications), 0, "Publications should be displayed")
        
        # Check for year sections
        year_sections = soup.select('.year-section')
        self.assertGreater(len(year_sections), 0, "Year sections should be present")
        
        # Check for proper HTML formatting (not escaped)
        for pub in publications:
            # Check that HTML is properly rendered
            title = pub.select_one('.pub-title')
            self.assertIsNotNone(title, "Publication title should be present")
            self.assertNotIn("&lt;", title.text, "HTML should not be escaped in title")
            
            # Check for action buttons
            actions = pub.select('.pub-btn')
            self.assertTrue(len(actions) > 0, "Publication should have action buttons")
    
    def test_publication_data_integrity(self):
        """Test that publication data is correctly displayed."""
        response = requests.get(f"{self.BASE_URL}/publications/")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check specific publications from publist.yml
        publications = soup.select('.publication-item')
        
        # Find a specific publication by title
        test_title = "YINYANG-ALIGN: Benchmarking Contradictory Objectives"
        found = False
        for pub in publications:
            title_elem = pub.select_one('.pub-title')
            if title_elem and test_title in title_elem.text:
                found = True
                
                # Check authors
                authors = pub.select_one('.pub-authors')
                self.assertIsNotNone(authors, "Authors should be present")
                self.assertIn("Amitava Das", authors.text, "Authors should match publist.yml")
                
                # Check venue
                venue = pub.select_one('.pub-venue')
                self.assertIsNotNone(venue, "Venue should be present")
                self.assertIn("ACL, 2025", venue.text, "Venue should match publist.yml")
                
                # Check category tag
                category = pub.select_one('.category-tag')
                self.assertIsNotNone(category, "Category tag should be present")
                self.assertIn("ACL", category.text, "Category should match publist.yml")
                
                break
        
        self.assertTrue(found, f"Publication '{test_title}' should be found")

if __name__ == "__main__":
    unittest.main()