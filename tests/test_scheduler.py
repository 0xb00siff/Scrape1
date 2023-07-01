```python
import unittest
from src.scheduler import Scheduler

class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_schedule_daily(self):
        result = self.scheduler.schedule_daily()
        self.assertTrue(result)

    def test_schedule_weekly(self):
        result = self.scheduler.schedule_weekly()
        self.assertTrue(result)

    def test_manual_trigger(self):
        result = self.scheduler.manual_trigger()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```