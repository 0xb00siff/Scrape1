```python
import schedule
import time
from scraper import Scraper
from data_extractor import DataExtractor
from data_cleaner import DataCleaner
from data_storage import DataStorage
from config import Config
from logger import Logger

class Scheduler:
    def __init__(self):
        self.scraper = Scraper()
        self.extractor = DataExtractor()
        self.cleaner = DataCleaner()
        self.storage = DataStorage()
        self.logger = Logger()

    def job(self):
        try:
            # Scrape data
            raw_data = self.scraper.scrape_data()

            # Extract data
            extracted_data = self.extractor.extract_data(raw_data)

            # Clean data
            cleaned_data = self.cleaner.clean_data(extracted_data)

            # Store data
            self.storage.store_data(cleaned_data)

            self.logger.log("Scraping job completed successfully.")
        except Exception as e:
            self.logger.log(f"Error occurred during scraping job: {str(e)}", error=True)

    def run_daily(self):
        schedule.every().day.at(Config.SCRAPING_TIME).do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def run_now(self):
        self.job()

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run_daily()
```