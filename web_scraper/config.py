```python
# MongoDB Configuration
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "alien_info_db"

# Web Scraping Configuration
BASE_URLS = {
    "news": "https://www.example-news.com",
    "blogs": "https://www.example-blogs.com",
    "forums": "https://www.example-forums.com",
    "social_media": "https://www.example-socialmedia.com"
}

# Rate Limiting Configuration
REQUESTS_PER_MINUTE = 10

# Sleep Interval Configuration
SLEEP_INTERVAL = 5

# Pagination Configuration
PAGINATION_LIMIT = 10

# Infinite Scroll Configuration
SCROLL_PAUSE_TIME = 2

# Error Handling Configuration
ERROR_LOG_PATH = "logs/error.log"

# Automation Configuration
SCHEDULE = {
    "hour": 0,
    "minute": 0,
    "second": 0
}

# Manual Trigger Configuration
MANUAL_TRIGGER_PATH = "trigger/manual_trigger.txt"

# Update and Maintenance Configuration
UPDATE_CHECK_INTERVAL = 7  # in days

# Testing and Deployment Configuration
TESTING_MODE = True
DEPLOYMENT_PATH = "/path/to/deployment/directory"
```
