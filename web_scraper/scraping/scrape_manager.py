```python
from .scrapers import news_scraper, blog_scraper, forum_scraper, social_media_scraper
from ..error_handling import error_handler, logger
from ..performance import efficiency_manager, rate_limiter

class ScrapeManager:
    def __init__(self):
        self.scrapers = [
            news_scraper.NewsScraper(),
            blog_scraper.BlogScraper(),
            forum_scraper.ForumScraper(),
            social_media_scraper.SocialMediaScraper()
        ]

    def scrape(self):
        for scraper in self.scrapers:
            try:
                efficiency_manager.manage_resources()
                rate_limiter.limit_rate()
                scraper.scrape()
            except Exception as e:
                error_handler.handle_error(e)
                logger.log_error(e)

    def scrape_specific(self, scraper_type):
        for scraper in self.scrapers:
            if isinstance(scraper, scraper_type):
                try:
                    efficiency_manager.manage_resources()
                    rate_limiter.limit_rate()
                    scraper.scrape()
                except Exception as e:
                    error_handler.handle_error(e)
                    logger.log_error(e)
```