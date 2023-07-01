```python
from bs4 import BeautifulSoup
from src.logger import Logger
from src.error_handler import ErrorHandler
import requests

class DataExtractor:
    def __init__(self):
        self.logger = Logger()
        self.error_handler = ErrorHandler()

    def extract_data(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            data = {
                'title': self.extract_title(soup),
                'content': self.extract_content(soup),
                'date': self.extract_date(soup),
                'author': self.extract_author(soup),
                'tags': self.extract_tags(soup),
                'source': url,
                'type': self.extract_type(soup)
            }

            self.logger.log_action(f"Data extracted from {url}")
            return data

        except Exception as e:
            self.error_handler.handle_error(f"Error extracting data from {url}: {str(e)}")
            return None

    def extract_title(self, soup):
        try:
            return soup.find('title').text
        except:
            return None

    def extract_content(self, soup):
        try:
            return soup.find('body').text
        except:
            return None

    def extract_date(self, soup):
        try:
            return soup.find('time').text
        except:
            return None

    def extract_author(self, soup):
        try:
            return soup.find('author').text
        except:
            return None

    def extract_tags(self, soup):
        try:
            return [tag.text for tag in soup.find_all('tag')]
        except:
            return None

    def extract_type(self, soup):
        if soup.find('video'):
            return 'video'
        elif soup.find('img'):
            return 'image'
        else:
            return 'text'
```