```python
import unittest
from web_scraper.data_cleaner import DataCleaner

class TestDataCleaner(unittest.TestCase):

    def setUp(self):
        self.data_cleaner = DataCleaner()
        self.sample_data = {
            "title": "Alien sighting in New York",
            "content": "Alien sighting in New York. Advertisement. Buy now!",
            "date": "2022-01-01",
            "author": "John Doe",
            "tags": ["alien", "sighting", "New York"],
            "source": "https://example.com",
            "type": "text"
        }

    def test_remove_advertisements(self):
        cleaned_data = self.data_cleaner.remove_advertisements(self.sample_data)
        self.assertNotIn("Advertisement. Buy now!", cleaned_data["content"])

    def test_remove_duplicates(self):
        duplicate_data = [self.sample_data, self.sample_data]
        cleaned_data = self.data_cleaner.remove_duplicates(duplicate_data)
        self.assertEqual(len(cleaned_data), 1)

    def test_clean_data(self):
        cleaned_data = self.data_cleaner.clean_data(self.sample_data)
        self.assertNotIn("Advertisement. Buy now!", cleaned_data["content"])
        self.assertEqual(cleaned_data["title"], self.sample_data["title"])
        self.assertEqual(cleaned_data["date"], self.sample_data["date"])
        self.assertEqual(cleaned_data["author"], self.sample_data["author"])
        self.assertEqual(cleaned_data["tags"], self.sample_data["tags"])
        self.assertEqual(cleaned_data["source"], self.sample_data["source"])
        self.assertEqual(cleaned_data["type"], self.sample_data["type"])

if __name__ == '__main__':
    unittest.main()
```