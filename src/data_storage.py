```python
from pymongo import MongoClient
from config.config import MONGO_DB_URI, DB_NAME, COLLECTION_NAME
from logger import log_error, log_action

class DataStorage:
    def __init__(self):
        self.client = MongoClient(MONGO_DB_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def store_data(self, data):
        try:
            self.collection.insert_one(data)
            log_action(f"Data stored successfully in MongoDB: {data['title']}")
        except Exception as e:
            log_error(f"Error while storing data in MongoDB: {str(e)}")

    def check_duplicate(self, data):
        if self.collection.find_one({"source": data["source"]}):
            log_action(f"Duplicate data found, skipping: {data['title']}")
            return True
        return False

    def close_connection(self):
        self.client.close()
        log_action("MongoDB connection closed.")
```