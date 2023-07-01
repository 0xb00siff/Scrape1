```python
from pymongo import MongoClient
import config

class DataStorage:
    def __init__(self):
        self.client = MongoClient(config.MONGODB_CONNECTION_STRING)
        self.db = self.client[config.DATABASE_NAME]
        self.collection = self.db[config.COLLECTION_NAME]

    def store_data(self, data):
        try:
            self.collection.insert_one(data)
            print(f"Data stored successfully in MongoDB: {data['title']}")
        except Exception as e:
            print(f"An error occurred while storing data in MongoDB: {str(e)}")

    def check_duplicate(self, data):
        try:
            if self.collection.find_one({"source": data["source"]}):
                return True
            return False
        except Exception as e:
            print(f"An error occurred while checking for duplicates in MongoDB: {str(e)}")
            return False

    def store_cleaned_data(self, cleaned_data):
        for data in cleaned_data:
            if not self.check_duplicate(data):
                self.store_data(data)
            else:
                print(f"Duplicate data found, skipping: {data['title']}")
```