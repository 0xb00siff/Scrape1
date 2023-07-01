```python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from time import sleep
from config import urls, config
from utils import check_robots_txt
from logger import log_action, log_error
from error_handler import handle_error

class WebScraper:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=config['webdriver_path'])
        self.wait = WebDriverWait(self.driver, config['wait_time'])

    def get_page_content(self, url):
        try:
            response = requests.get(url, headers=config['headers'])
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            handle_error(e, "Failed to get page content")
            return None

    def get_dynamic_page_content(self, url):
        try:
            self.driver.get(url)
            return BeautifulSoup(self.driver.page_source, 'html.parser')
        except Exception as e:
            handle_error(e, "Failed to get dynamic page content")
            return None

    def handle_pagination(self, soup, base_url):
        try:
            next_page = soup.find('a', {'rel': 'next'})
            if next_page:
                next_page_url = urljoin(base_url, next_page.get('href'))
                return self.get_page_content(next_page_url)
            else:
                return None
        except Exception as e:
            handle_error(e, "Failed to handle pagination")
            return None

    def scrape(self, url, dynamic=False):
        if check_robots_txt(url):
            if dynamic:
                soup = self.get_dynamic_page_content(url)
            else:
                soup = self.get_page_content(url)
            if soup:
                log_action(f"Scraped {url}")
                return soup
            else:
                log_error(f"Failed to scrape {url}")
                return None
        else:
            log_error(f"Scraping not allowed by robots.txt for {url}")
            return None

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = WebScraper()
    for url in urls:
        soup = scraper.scrape(url)
        if soup:
            # Pass the soup to data extractor
            pass
    scraper.close()
```