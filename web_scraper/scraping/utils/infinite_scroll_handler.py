```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InfiniteScrollHandler:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_page_load(self, timeout=20):
        old_height = self.driver.execute_script("return document.body.scrollHeight")
        self.scroll_to_end()

        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.driver.execute_script("return document.body.scrollHeight") > old_height
            )
        except TimeoutException:
            pass  # End of page reached

    def handle_infinite_scroll(self):
        while True:
            self.wait_for_page_load()
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == old_height:
                break

            old_height = new_height
```
