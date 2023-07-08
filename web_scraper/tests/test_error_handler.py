```python
import unittest
from web_scraper.error_handler import ErrorHandler

class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.error_handler = ErrorHandler()

    def test_handle_error(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            result = self.error_handler.handle_error(e)
            self.assertEqual(result, "Error occurred: Test Exception")

    def test_log_error(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            result = self.error_handler.log_error(e)
            self.assertEqual(result, "Error logged: Test Exception")

if __name__ == '__main__':
    unittest.main()
```