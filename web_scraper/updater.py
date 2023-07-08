```python
import time
from scraper import Scraper
from data_extractor import DataExtractor
from data_cleaner import DataCleaner
from data_storage import DataStorage
from config import Config
from logger import Logger

class Updater:
    def __init__(self):
        self.scraper = Scraper()
        self.extractor = DataExtractor()
        self.cleaner = DataCleaner()
        self.storage = DataStorage()
        self.config = Config()
        self.logger = Logger()

    def update(self):
        try:
            self.logger.log("Update process started.")
            for url in self.config.urls:
                self.logger.log(f"Scraping started for {url}")
                raw_data = self.scraper.scrape(url)
                self.logger.log(f"Data extraction started for {url}")
                extracted_data = self.extractor.extract(raw_data)
                self.logger.log(f"Data cleaning started for {url}")
                cleaned_data = self.cleaner.clean(extracted_data)
                self.logger.log(f"Data storage started for {url}")
                self.storage.store(cleaned_data)
                self.logger.log(f"Update process completed for {url}")
                time.sleep(self.config.sleep_interval)
        except Exception as e:
            self.logger.log(f"Error occurred during update: {str(e)}", "ERROR")

if __name__ == "__main__":
    updater = Updater()
    updater.update()
```