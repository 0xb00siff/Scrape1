```python
from bs4 import BeautifulSoup

class MetadataExtractor:
    def __init__(self):
        pass

    def extract_metadata(self, soup):
        metadata = {}

        # Extract date of posting
        date = self._extract_date(soup)
        if date:
            metadata['date'] = date

        # Extract author
        author = self._extract_author(soup)
        if author:
            metadata['author'] = author

        # Extract source URL
        source_url = self._extract_source_url(soup)
        if source_url:
            metadata['source_url'] = source_url

        # Extract tags or keywords
        tags = self._extract_tags(soup)
        if tags:
            metadata['tags'] = tags

        return metadata

    def _extract_date(self, soup):
        # This method should be overridden by subclasses to extract the date from the specific website
        raise NotImplementedError

    def _extract_author(self, soup):
        # This method should be overridden by subclasses to extract the author from the specific website
        raise NotImplementedError

    def _extract_source_url(self, soup):
        # This method should be overridden by subclasses to extract the source URL from the specific website
        raise NotImplementedError

    def _extract_tags(self, soup):
        # This method should be overridden by subclasses to extract the tags or keywords from the specific website
        raise NotImplementedError
```