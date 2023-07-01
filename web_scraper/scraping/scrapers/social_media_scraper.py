```python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from ..utils.pagination_handler import handle_pagination
from ..utils.infinite_scroll_handler import handle_infinite_scroll
from ..utils.pop_up_handler import handle_pop_ups
from ..utils.robots_txt_handler import is_allowed
from ...data_extraction.data_extractor import extract_data
from ...error_handling.error_handler import handle_error
from ...performance.rate_limiter import rate_limited

class SocialMediaScraper:
    def __init__(self, base_url, driver_path):
        self.base_url = base_url
        self.driver = webdriver.Chrome(driver_path)

    @rate_limited(1)
    def scrape(self):
        if not is_allowed(self.base_url):
            return

        try:
            self.driver.get(self.base_url)
            handle_pop_ups(self.driver)

            while True:
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                posts = soup.find_all('div', class_='post')

                for post in posts:
                    data = extract_data(post)
                    yield data

                if not handle_pagination(self.driver) and not handle_infinite_scroll(self.driver):
                    break

        except Exception as e:
            handle_error(e)

        finally:
            self.driver.quit()
```