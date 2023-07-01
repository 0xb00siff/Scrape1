```python
from bs4 import BeautifulSoup

class DataExtractor:
    def __init__(self):
        pass

    def extract_text(self, soup):
        """
        Extracts textual data from the BeautifulSoup object
        """
        text_data = soup.get_text()
        return text_data

    def extract_images(self, soup):
        """
        Extracts image data from the BeautifulSoup object
        """
        images = soup.find_all('img')
        image_links = [img['src'] for img in images if 'src' in img.attrs]
        return image_links

    def extract_videos(self, soup):
        """
        Extracts video data from the BeautifulSoup object
        """
        videos = soup.find_all('video')
        video_links = [video['src'] for video in videos if 'src' in video.attrs]
        return video_links

    def extract_data(self, html_content):
        """
        Extracts all relevant data from the HTML content
        """
        soup = BeautifulSoup(html_content, 'html.parser')

        text_data = self.extract_text(soup)
        image_links = self.extract_images(soup)
        video_links = self.extract_videos(soup)

        return {
            'text': text_data,
            'images': image_links,
            'videos': video_links
        }
```