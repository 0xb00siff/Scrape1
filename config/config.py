```python
# config/config.py

# MongoDB Configuration
MONGO_DB_NAME = "alien_info_db"
MONGO_COLLECTION_NAME = "alien_info_collection"
MONGO_HOST = "localhost"
MONGO_PORT = 27017

# Web Scraping Configuration
USER_AGENT = "AlienInfoBot/1.0"
REQUEST_TIMEOUT = 30
REQUEST_DELAY = 1  # delay between requests in seconds

# Pagination Configuration
MAX_PAGES = 100  # maximum number of pages to scrape per website

# Error Handling Configuration
MAX_RETRIES = 3  # maximum number of retries in case of request failure

# Scheduler Configuration
SCHEDULE_INTERVAL = 24  # interval between each run of the bot in hours

# Logger Configuration
LOG_LEVEL = "INFO"  # log level can be "INFO", "DEBUG", "ERROR"
ACTION_LOG_FILE = "logs/action_logs.txt"
ERROR_LOG_FILE = "logs/error_logs.txt"

# Test Configuration
TEST_MODE = False  # set to True for testing, False for production

# Updater Configuration
CHECK_FOR_UPDATES_INTERVAL = 7  # interval between each check for updates in days

# Deployer Configuration
DEPLOYMENT_MODE = "production"  # can be "development" or "production"
```