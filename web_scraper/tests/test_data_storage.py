```python
import unittest
from pymongo import MongoClient
from web_scraper.data_storage import DataStorage
from web_scraper.config import Config

class TestDataStorage(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.client = MongoClient(self.config.MONGODB_CONNECTION_STRING)
        self.db = self.client[self.config.DATABASE_NAME]
        self.collection = self.db[self.config.COLLECTION_NAME]
        self.data_storage = DataStorage(self.config)

    def test_store_data(self):
        data = {
            "title": "Alien sighting",
            "content": "Alien sighting reported in New York",
            "date": "2021-12-01",
            "author": "John Doe",
            "tags": ["alien", "sighting", "New York"],
            "source": "https://example.com/alien-sighting",
            "type": "text"
        }
        self.data_storage.store_data(data)
        stored_data = self.collection.find_one({"source": "https://example.com/alien-sighting"})
        self.assertIsNotNone(stored_data)
        self.assertEqual(stored_data["title"], "Alien sighting")

    def test_remove_duplicates(self):
        data = {
            "title": "Alien sighting",
            "content": "Alien sighting reported in New York",
            "date": "2021-12-01",
            "author": "John Doe",
            "tags": ["alien", "sighting", "New York"],
            "source": "https://example.com/alien-sighting",
            "type": "text"
        }
        self.data_storage.store_data(data)
        self.data_storage.store_data(data)
        count = self.collection.count_documents({"source": "https://example.com/alien-sighting"})
        self.assertEqual(count, 1)

    def tearDown(self):
        self.collection.delete_many({})

if __name__ == "__main__":
    unittest.main()
```