```python
import sys
sys.path.append("..")

from scraping.scrape_manager import ScrapeManager

def manual_trigger():
    print("Manual trigger for Alien Information Web Scraper initiated.")
    scrape_manager = ScrapeManager()
    scrape_manager.start_scraping()

if __name__ == "__main__":
    manual_trigger()
```