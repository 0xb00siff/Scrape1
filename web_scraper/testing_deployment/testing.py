```python
import unittest
from web_scraper.scraping.scrape_manager import ScrapeManager
from web_scraper.data_extraction.data_extractor import DataExtractor
from web_scraper.data_cleaning.data_cleaner import DataCleaner
from web_scraper.data_storage.data_storer import DataStorer

class TestAlienInfoWebScraper(unittest.TestCase):

    def setUp(self):
        self.scrape_manager = ScrapeManager()
        self.data_extractor = DataExtractor()
        self.data_cleaner = DataCleaner()
        self.data_storer = DataStorer()

    def test_scrape_manager(self):
        result = self.scrape_manager.scrape_website("https://example.com")
        self.assertIsNotNone(result)

    def test_data_extractor(self):
        raw_data = self.scrape_manager.scrape_website("https://example.com")
        extracted_data = self.data_extractor.extract_data(raw_data)
        self.assertIsNotNone(extracted_data)

    def test_data_cleaner(self):
        raw_data = self.scrape_manager.scrape_website("https://example.com")
        extracted_data = self.data_extractor.extract_data(raw_data)
        cleaned_data = self.data_cleaner.clean_data(extracted_data)
        self.assertIsNotNone(cleaned_data)

    def test_data_storer(self):
        raw_data = self.scrape_manager.scrape_website("https://example.com")
        extracted_data = self.data_extractor.extract_data(raw_data)
        cleaned_data = self.data_cleaner.clean_data(extracted_data)
        result = self.data_storer.store_data(cleaned_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```