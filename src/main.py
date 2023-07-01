```python
import schedule
import time
from src.web_scraper import WebScraper
from src.data_extractor import DataExtractor
from src.data_cleaner import DataCleaner
from src.data_storage import DataStorage
from src.error_handler import ErrorHandler
from src.logger import Logger
from src.updater import Updater
from config.config import SCHEDULE_INTERVAL

def main():
    try:
        logger = Logger()
        logger.log_action("Starting Alien Information Web Scraper")

        web_scraper = WebScraper()
        data_extractor = DataExtractor()
        data_cleaner = DataCleaner()
        data_storage = DataStorage()

        logger.log_action("Scraping data from web")
        raw_data = web_scraper.scrape_data()

        logger.log_action("Extracting relevant data")
        extracted_data = data_extractor.extract_data(raw_data)

        logger.log_action("Cleaning extracted data")
        cleaned_data = data_cleaner.clean_data(extracted_data)

        logger.log_action("Storing cleaned data in MongoDB")
        data_storage.store_data(cleaned_data)

        logger.log_action("Alien Information Web Scraper completed successfully")

    except Exception as e:
        error_handler = ErrorHandler()
        error_handler.handle_error(e)

def schedule_job():
    schedule.every(SCHEDULE_INTERVAL).hours.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    schedule_job()
    updater = Updater()
    updater.check_for_updates()
```