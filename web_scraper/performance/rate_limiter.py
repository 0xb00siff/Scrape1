```python
import time
from random import randint
from web_scraper.config import RATE_LIMIT_MIN_DELAY, RATE_LIMIT_MAX_DELAY

class RateLimiter:
    def __init__(self):
        self.last_request_time = time.time()

    def wait(self):
        """Wait between requests to respect rate limit"""
        time_since_last_request = time.time() - self.last_request_time
        delay = self.get_delay()

        if time_since_last_request < delay:
            time.sleep(delay - time_since_last_request)

        self.last_request_time = time.time()

    @staticmethod
    def get_delay():
        """Get a random delay within the rate limit range"""
        return randint(RATE_LIMIT_MIN_DELAY, RATE_LIMIT_MAX_DELAY)
```