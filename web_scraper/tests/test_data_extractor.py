```python
import unittest
from web_scraper.data_extractor import DataExtractor

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

    def test_extract_data(self):
        sample_html = """
        <div>
            <h1>Alien sighting</h1>
            <p>This is a sample text about aliens.</p>
            <img src="alien.jpg">
            <video src="ufo.mp4"></video>
            <meta name="keywords" content="Aliens, UFO">
        </div>
        """
        result = self.data_extractor.extract_data(sample_html)
        expected_result = {
            "title": "Alien sighting",
            "content": "This is a sample text about aliens.",
            "images": ["alien.jpg"],
            "videos": ["ufo.mp4"],
            "metadata": {"keywords": "Aliens, UFO"}
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
```