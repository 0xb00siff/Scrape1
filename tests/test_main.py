```python
import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.main = main.Main()

    def test_run(self):
        result = self.main.run()
        self.assertIsNotNone(result)

    def test_schedule(self):
        result = self.main.schedule()
        self.assertIsNotNone(result)

    def test_update(self):
        result = self.main.update()
        self.assertIsNotNone(result)

    def test_manual_trigger(self):
        result = self.main.manual_trigger()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```