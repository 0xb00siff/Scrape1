```python
import re
from src.logger import Logger
from src.error_handler import ErrorHandler

class DataCleaner:
    def __init__(self):
        self.logger = Logger()
        self.error_handler = ErrorHandler()

    def remove_irrelevant_info(self, data):
        try:
            cleaned_data = re.sub(r'\n|\r', '', data)
            cleaned_data = re.sub(r'\s\s+', ' ', cleaned_data)
            return cleaned_data
        except Exception as e:
            self.error_handler.handle_error(f"Error in removing irrelevant info: {e}")
            self.logger.log_error(f"Error in removing irrelevant info: {e}")

    def remove_ads(self, data):
        try:
            cleaned_data = re.sub(r'ADVERTISEMENT', '', data)
            return cleaned_data
        except Exception as e:
            self.error_handler.handle_error(f"Error in removing ads: {e}")
            self.logger.log_error(f"Error in removing ads: {e}")

    def handle_duplicates(self, data_list):
        try:
            cleaned_data_list = list(set(data_list))
            return cleaned_data_list
        except Exception as e:
            self.error_handler.handle_error(f"Error in handling duplicates: {e}")
            self.logger.log_error(f"Error in handling duplicates: {e}")

    def clean_data(self, data):
        try:
            cleaned_data = self.remove_irrelevant_info(data)
            cleaned_data = self.remove_ads(cleaned_data)
            return cleaned_data
        except Exception as e:
            self.error_handler.handle_error(f"Error in cleaning data: {e}")
            self.logger.log_error(f"Error in cleaning data: {e}")
```