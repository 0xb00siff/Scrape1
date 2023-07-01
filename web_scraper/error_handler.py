```python
import logging
from web_scraper.logger import Logger

class ErrorHandler:
    def __init__(self):
        self.logger = Logger().get_logger()

    def handle_error(self, error, message):
        self.logger.error(f"{message}: {str(error)}")

    def handle_exception(self, e, message):
        self.logger.exception(f"{message}: {str(e)}")

    def handle_warning(self, warning, message):
        self.logger.warning(f"{message}: {str(warning)}")

    def handle_info(self, info, message):
        self.logger.info(f"{message}: {str(info)}")
```