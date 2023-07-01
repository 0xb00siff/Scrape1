```python
import unittest
from src import error_handler

class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.error_handler = error_handler.ErrorHandler()

    def test_log_error(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            self.error_handler.log_error(e)
            with open("logs/error_logs.txt", "r") as file:
                last_line = file.readlines()[-1]
                self.assertIn("Test Exception", last_line)

    def test_handle_error(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            result = self.error_handler.handle_error(e)
            self.assertEqual(result, "Error: Test Exception")

if __name__ == '__main__':
    unittest.main()
```