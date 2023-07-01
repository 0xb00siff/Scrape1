```python
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

class ImageExtractor:
    def __init__(self):
        self.session = requests.Session()

    def extract_images(self, url):
        """
        Extracts all images from a webpage
        """
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        images = []
        for img in soup.find_all('img'):
            img_url = img.attrs.get("src")
            if not img_url:
                continue
            img_url = urljoin(url, img_url)
            try:
                pos = img_url.index("?")
                img_url = img_url[:pos]
            except ValueError:
                pass
            if self.is_valid(img_url):
                images.append(img_url)
        return images

    def is_valid(self, url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)
```