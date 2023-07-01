```python
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    """
    Setup selenium driver
    """
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    return driver

def make_request(url):
    """
    Make a GET request to a url
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong",err)

def parse_html(response):
    """
    Parse HTML using BeautifulSoup
    """
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def scroll_page(driver, scroll_pause_time=0.5):
    """
    Scroll to the end of a dynamic page
    """
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def wait_for_element(driver, element_id, timeout=10):
    """
    Wait for an element to load
    """
    try:
        element_present = EC.presence_of_element_located((By.ID, element_id))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

def extract_element_data(soup, element):
    """
    Extract data from a specific element
    """
    return soup.find_all(element)

def clean_text(text):
    """
    Clean text data
    """
    return text.strip().replace('\n', ' ').replace('\r', '')
```