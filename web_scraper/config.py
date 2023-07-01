```python
# web_scraper/config.py

# Importing required libraries
from pymongo import MongoClient

# Base URLs to scrape
BASE_URLS = [
    "https://www.example1.com",
    "https://www.example2.com",
    "https://www.example3.com"
]

# Pagination settings
PAGINATION = {
    "enabled": True,
    "pages_to_scrape": 10
}

# Sleep intervals to prevent getting blocked
SLEEP_INTERVAL = 5  # in seconds

# MongoDB connection details
MONGO_DETAILS = {
    "host": "localhost",
    "port": 27017,
    "db_name": "alien_info_db",
    "collection_name": "alien_info"
}

# MongoDB client
MONGO_CLIENT = MongoClient(MONGO_DETAILS["host"], MONGO_DETAILS["port"])

# Data schema for MongoDB
DATA_SCHEMA = {
    "title": "",
    "content": "",
    "date": "",
    "author": "",
    "tags": [],
    "source": "",
    "type": ""  # text, image, video
}

# Keywords to search for in the content
KEYWORDS = ["alien", "UFO", "UAP"]

# Log file path
LOG_FILE_PATH = "web_scraper/logs/log.txt"

# Scheduler settings
SCHEDULER_SETTINGS = {
    "enabled": True,
    "interval": 24  # in hours
}
```