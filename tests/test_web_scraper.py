```python
import unittest
from src import web_scraper
from config import urls

class TestWebScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = web_scraper.WebScraper()
        self.test_url = urls.TEST_URL

    def test_scrape_data(self):
        result = self.scraper.scrape_data(self.test_url)
        self.assertIsNotNone(result)

    def test_handle_pagination(self):
        result = self.scraper.handle_pagination(self.test_url)
        self.assertIsNotNone(result)

    def test_handle_infinite_scrolling(self):
        result = self.scraper.handle_infinite_scrolling(self.test_url)
        self.assertIsNotNone(result)

    def test_handle_popups(self):
        result = self.scraper.handle_popups(self.test_url)
        self.assertIsNotNone(result)

    def test_follow_robots_txt(self):
        result = self.scraper.follow_robots_txt(self.test_url)
        self.assertTrue(result)

    def test_extract_textual_data(self):
        result = self.scraper.extract_textual_data(self.test_url)
        self.assertIsNotNone(result)

    def test_extract_images(self):
        result = self.scraper.extract_images(self.test_url)
        self.assertIsNotNone(result)

    def test_extract_videos(self):
        result = self.scraper.extract_videos(self.test_url)
        self.assertIsNotNone(result)

    def test_extract_metadata(self):
        result = self.scraper.extract_metadata(self.test_url)
        self.assertIsNotNone(result)

    def test_clean_data(self):
        raw_data = self.scraper.scrape_data(self.test_url)
        result = self.scraper.clean_data(raw_data)
        self.assertIsNotNone(result)

    def test_handle_duplicates(self):
        raw_data = self.scraper.scrape_data(self.test_url)
        result = self.scraper.handle_duplicates(raw_data)
        self.assertIsNotNone(result)

    def test_store_data(self):
        raw_data = self.scraper.scrape_data(self.test_url)
        cleaned_data = self.scraper.clean_data(raw_data)
        result = self.scraper.store_data(cleaned_data)
        self.assertTrue(result)

    def test_rate_limiting(self):
        result = self.scraper.rate_limiting()
        self.assertTrue(result)

    def test_sleep_intervals(self):
        result = self.scraper.sleep_intervals()
        self.assertTrue(result)

    def test_error_handling(self):
        result = self.scraper.error_handling()
        self.assertTrue(result)

    def test_logging(self):
        result = self.scraper.logging()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```