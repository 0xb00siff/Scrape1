```python
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from web_scraper.config import BASE_URLS
from web_scraper.error_handler import handle_error
from web_scraper.logger import log_action, log_error
import requests

def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        handle_error(e, "Failed to fetch URL: " + url)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    return extract_content(soup), extract_metadata(soup)

def extract_content(soup):
    try:
        content = {}
        content['text'] = extract_text(soup)
        content['images'] = extract_images(soup)
        content['videos'] = extract_videos(soup)
        log_action("Content extracted successfully.")
        return content
    except Exception as e:
        handle_error(e, "Failed to extract content.")
        return None

def extract_text(soup):
    paragraphs = soup.find_all('p')
    return [p.text for p in paragraphs]

def extract_images(soup):
    images = soup.find_all('img')
    return [urljoin(BASE_URLS, img['src']) for img in images]

def extract_videos(soup):
    videos = soup.find_all('video')
    return [urljoin(BASE_URLS, video['src']) for video in videos]

def extract_metadata(soup):
    try:
        metadata = {}
        metadata['date'] = extract_date(soup)
        metadata['author'] = extract_author(soup)
        metadata['source'] = extract_source(soup)
        metadata['tags'] = extract_tags(soup)
        log_action("Metadata extracted successfully.")
        return metadata
    except Exception as e:
        handle_error(e, "Failed to extract metadata.")
        return None

def extract_date(soup):
    date = soup.find('time')
    return date['datetime'] if date else None

def extract_author(soup):
    author = soup.find('span', {'class': 'author'})
    return author.text if author else None

def extract_source(soup):
    return soup.find('link', {'rel': 'canonical'})['href']

def extract_tags(soup):
    tags = soup.find_all('a', {'rel': 'tag'})
    return [tag.text for tag in tags]
```