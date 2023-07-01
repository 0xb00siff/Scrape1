```python
from pymongo import MongoClient
from web_scraper.config import MONGODB_CONNECTION_STRING

class DuplicateHandler:
    def __init__(self):
        self.client = MongoClient(MONGODB_CONNECTION_STRING)
        self.db = self.client['alien_info_db']
        self.collection = self.db['alien_info']

    def check_duplicate(self, data):
        """
        Check if the data already exists in the database
        """
        if self.collection.find_one(data):
            return True
        return False

    def handle_duplicates(self, data_list):
        """
        Remove duplicates from the data list
        """
        unique_data = [data for data in data_list if not self.check_duplicate(data)]
        return unique_data
```