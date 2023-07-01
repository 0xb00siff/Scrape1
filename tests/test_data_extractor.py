```python
import unittest
from src.data_extractor import DataExtractor

class TestDataExtractor(unittest.TestCase):

    def setUp(self):
        self.data_extractor = DataExtractor()

    def test_extract_text(self):
        sample_html = "<p>This is a sample text about aliens.</p>"
        result = self.data_extractor.extract_text(sample_html)
        self.assertEqual(result, "This is a sample text about aliens.")

    def test_extract_images(self):
        sample_html = '<img src="alien.jpg">'
        result = self.data_extractor.extract_images(sample_html)
        self.assertEqual(result, ["alien.jpg"])

    def test_extract_videos(self):
        sample_html = '<video src="ufo.mp4"></video>'
        result = self.data_extractor.extract_videos(sample_html)
        self.assertEqual(result, ["ufo.mp4"])

    def test_extract_metadata(self):
        sample_html = '<meta name="keywords" content="Aliens, UFO">'
        result = self.data_extractor.extract_metadata(sample_html)
        self.assertEqual(result, {"keywords": "Aliens, UFO"})

    def test_handle_pagination(self):
        sample_html = '<a href="page2.html">Next</a>'
        result = self.data_extractor.handle_pagination(sample_html)
        self.assertEqual(result, "page2.html")

    def test_handle_infinite_scrolling(self):
        sample_html = '<div id="loadMore">Load More</div>'
        result = self.data_extractor.handle_infinite_scrolling(sample_html)
        self.assertEqual(result, "loadMore")

    def test_handle_popups(self):
        sample_html = '<div id="popup">Close</div>'
        result = self.data_extractor.handle_popups(sample_html)
        self.assertEqual(result, "popup")

    def test_follow_robots_txt(self):
        robots_txt = "User-agent: *\nDisallow: /private"
        result = self.data_extractor.follow_robots_txt(robots_txt)
        self.assertEqual(result, ["/private"])

if __name__ == '__main__':
    unittest.main()
```