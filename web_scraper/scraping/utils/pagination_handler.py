```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginationHandler:
    def __init__(self, driver):
        self.driver = driver

    def go_to_next_page(self, next_button_xpath):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, next_button_xpath))
            )
            next_button.click()
            return True
        except Exception as e:
            print(f"Failed to go to the next page: {e}")
            return False
```