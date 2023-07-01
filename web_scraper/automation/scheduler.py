```python
import schedule
import time
from web_scraper.main import run_scraper

def job():
    print("Running the scraper...")
    run_scraper()

def schedule_scraper(interval, period):
    if period == 'daily':
        schedule.every(interval).days.do(job)
    elif period == 'hourly':
        schedule.every(interval).hours.do(job)
    elif period == 'weekly':
        schedule.every(interval).weeks.do(job)
    else:
        print("Invalid period. Please choose from 'daily', 'hourly', or 'weekly'.")

    while True:
        schedule.run_pending()
        time.sleep(1)
```