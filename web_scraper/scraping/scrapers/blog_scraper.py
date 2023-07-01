```python
import requests
from bs4 import BeautifulSoup
from ..utils import pagination_handler, infinite_scroll_handler, pop_up_handler, robots_txt_handler
from ...data_extraction import data_extractor, metadata_extractor
from ...data_cleaning import data_cleaner, duplicate_handler
from ...error_handling import error_handler, logger

class BlogScraper:
    def __init__(self, base_url, db_connector):
        self.base_url = base_url
        self.db_connector = db_connector
        self.data_extractor = data_extractor.DataExtractor()
        self.metadata_extractor = metadata_extractor.MetadataExtractor()
        self.data_cleaner = data_cleaner.DataCleaner()
        self.duplicate_handler = duplicate_handler.DuplicateHandler(db_connector)

    def scrape(self):
        if not robots_txt_handler.is_allowed(self.base_url):
            logger.log(f"Scraping not allowed for {self.base_url}")
            return

        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            error_handler.handle(http_err)
            return
        except Exception as err:
            error_handler.handle(err)
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        blog_posts = soup.find_all('div', class_='blog-post')

        for post in blog_posts:
            try:
                data = self.data_extractor.extract(post)
                metadata = self.metadata_extractor.extract(post)
                cleaned_data = self.data_cleaner.clean(data)
                cleaned_metadata = self.data_cleaner.clean(metadata)

                if not self.duplicate_handler.is_duplicate(cleaned_data, cleaned_metadata):
                    self.db_connector.store(cleaned_data, cleaned_metadata)
            except Exception as err:
                error_handler.handle(err)

        pagination_handler.handle_pagination(self.base_url, soup, self.scrape)
        infinite_scroll_handler.handle_infinite_scroll(self.base_url, soup, self.scrape)
        pop_up_handler.handle_pop_ups(self.base_url, soup, self.scrape)
```