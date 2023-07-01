```python
from pymongo import MongoClient
from ..config import MONGODB_URI, DB_NAME, COLLECTION_NAME
from ..error_handling.logger import Logger

class DataStorer:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]
        self.logger = Logger().get_logger(__name__)

    def store_data(self, data):
        try:
            self.collection.insert_one(data)
            self.logger.info(f"Data stored successfully in MongoDB: {data['title']}")
        except Exception as e:
            self.logger.error(f"Error occurred while storing data in MongoDB: {str(e)}")

    def check_duplicate(self, data):
        if self.collection.find_one({"source": data["source"]}):
            self.logger.info(f"Duplicate data found, skipping: {data['title']}")
            return True
        return False

    def store(self, data):
        if not self.check_duplicate(data):
            self.store_data(data)
```
