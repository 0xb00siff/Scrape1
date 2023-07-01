```python
import unittest
from pymongo import MongoClient
from src.data_storage import DataStorage
from config.config import DATABASE_CONFIG

class TestDataStorage(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient(DATABASE_CONFIG['host'], DATABASE_CONFIG['port'])
        self.db = self.client[DATABASE_CONFIG['database']]
        self.collection = self.db[DATABASE_CONFIG['collection']]
        self.data_storage = DataStorage(self.collection)

    def tearDown(self):
        self.client.close()

    def test_store_data(self):
        data = {
            'title': 'Alien sighting',
            'content': 'Alien spotted in New York',
            'date': '2022-01-01',
            'author': 'John Doe',
            'tags': ['alien', 'sighting', 'New York'],
            'source': 'https://aliensite.com',
            'type': 'text'
        }
        self.data_storage.store_data(data)
        stored_data = self.collection.find_one({'title': 'Alien sighting'})
        self.assertIsNotNone(stored_data)
        self.assertEqual(stored_data['content'], 'Alien spotted in New York')

    def test_remove_duplicates(self):
        data = {
            'title': 'UFO sighting',
            'content': 'UFO spotted in London',
            'date': '2022-01-01',
            'author': 'Jane Doe',
            'tags': ['UFO', 'sighting', 'London'],
            'source': 'https://ufosite.com',
            'type': 'text'
        }
        self.data_storage.store_data(data)
        self.data_storage.store_data(data)
        count = self.collection.count_documents({'title': 'UFO sighting'})
        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()
```