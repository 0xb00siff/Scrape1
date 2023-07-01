```python
import unittest
from unittest.mock import patch
from web_scraper.scheduler import Scheduler

class TestScheduler(unittest.TestCase):

    @patch('web_scraper.scheduler.Scheduler.run')
    def test_scheduler_run(self, mock_run):
        scheduler = Scheduler()
        scheduler.run()
        mock_run.assert_called_once()

    @patch('web_scraper.scheduler.Scheduler.schedule')
    def test_scheduler_schedule(self, mock_schedule):
        scheduler = Scheduler()
        scheduler.schedule('daily')
        mock_schedule.assert_called_once_with('daily')

    @patch('web_scraper.scheduler.Scheduler.trigger')
    def test_scheduler_trigger(self, mock_trigger):
        scheduler = Scheduler()
        scheduler.trigger()
        mock_trigger.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```