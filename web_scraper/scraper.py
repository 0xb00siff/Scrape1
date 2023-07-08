```python
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.robotparser import RobotFileParser

from config import BASE_URLS, SELENIUM_OPTIONS, SLEEP_INTERVAL
from error_handler import handle_error
from logger import log_action, log_error

def is_crawl_allowed(url):
    rp = RobotFileParser()
    rp.set_url(url + "/robots.txt")
    rp.read()
    return rp.can_fetch("*", url)

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        handle_error(e)
        log_error(f"Failed to get content from {url}")
        return None

def get_dynamic_page_content(url):
    try:
        driver = webdriver.Chrome(options=SELENIUM_OPTIONS)
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        return driver.page_source
    finally:
        driver.quit()

def scrape_page(url, dynamic=False):
    if not is_crawl_allowed(url):
        log_action(f"Crawling disallowed by robots.txt: {url}")
        return None

    log_action(f"Scraping page: {url}")
    page_content = get_dynamic_page_content(url) if dynamic else get_page_content(url)
    if page_content is None:
        return None

    soup = BeautifulSoup(page_content, 'html.parser')
    return soup

def scrape_website(base_url, dynamic=False):
    page_number = 1
    while True:
        url = f"{base_url}?page={page_number}"
        soup = scrape_page(url, dynamic)
        if soup is None:
            break

        yield soup

        page_number += 1
        time.sleep(SLEEP_INTERVAL)

def scrape_all_websites():
    for base_url in BASE_URLS:
        yield from scrape_website(base_url)

def scrape():
    for soup in scrape_all_websites():
        # Extract data from soup here
        pass
```