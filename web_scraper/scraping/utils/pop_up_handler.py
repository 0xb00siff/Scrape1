```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PopUpHandler:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait_time = wait_time

    def close_pop_up(self, pop_up_locator):
        try:
            WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, pop_up_locator))
            )
            pop_up_element = self.driver.find_element_by_css_selector(pop_up_locator)
            pop_up_element.click()
        except Exception as e:
            print(f"Failed to close pop-up: {e}")
```