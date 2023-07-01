```python
import unittest
from web_scraper import WebScraper
from data_extractor import DataExtractor
from data_cleaner import DataCleaner
from data_storage import DataStorage
from error_handler import ErrorHandler
from logger import Logger
from scheduler import Scheduler
from updater import Updater
from utils import Utils

class TestAlienInfoWebScraper(unittest.TestCase):

    def setUp(self):
        self.web_scraper = WebScraper()
        self.data_extractor = DataExtractor()
        self.data_cleaner = DataCleaner()
        self.data_storage = DataStorage()
        self.error_handler = ErrorHandler()
        self.logger = Logger()
        self.scheduler = Scheduler()
        self.updater = Updater()
        self.utils = Utils()

    def test_web_scraper(self):
        result = self.web_scraper.scrape_data()
        self.assertIsNotNone(result)

    def test_data_extractor(self):
        result = self.data_extractor.extract_data()
        self.assertIsNotNone(result)

    def test_data_cleaner(self):
        result = self.data_cleaner.clean_data()
        self.assertIsNotNone(result)

    def test_data_storage(self):
        result = self.data_storage.store_data()
        self.assertIsNotNone(result)

    def test_error_handler(self):
        result = self.error_handler.handle_error()
        self.assertIsNotNone(result)

    def test_logger(self):
        result = self.logger.log_action()
        self.assertIsNotNone(result)

    def test_scheduler(self):
        result = self.scheduler.schedule_task()
        self.assertIsNotNone(result)

    def test_updater(self):
        result = self.updater.update_bot()
        self.assertIsNotNone(result)

    def test_utils(self):
        result = self.utils.helper_function()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```