```python
import unittest
from src.logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def test_log_message(self):
        message = "Test log message"
        self.logger.log_message(message)
        with open("logs/action_logs.txt", "r") as file:
            last_line = file.readlines()[-1]
        self.assertIn(message, last_line)

    def test_log_error(self):
        error_message = "Test error message"
        self.logger.log_error(error_message)
        with open("logs/error_logs.txt", "r") as file:
            last_line = file.readlines()[-1]
        self.assertIn(error_message, last_line)

if __name__ == '__main__':
    unittest.main()
```