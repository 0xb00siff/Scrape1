```python
from bs4 import BeautifulSoup
import requests

class VideoExtractor:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def extract_videos(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        video_data = []

        # Extract video links
        video_tags = soup.find_all('video')
        for tag in video_tags:
            video_url = tag.get('src')
            if video_url:
                video_data.append({'type': 'video', 'url': video_url})

        # Extract embedded YouTube videos
        iframe_tags = soup.find_all('iframe')
        for tag in iframe_tags:
            iframe_src = tag.get('src')
            if 'youtube.com' in iframe_src:
                video_data.append({'type': 'video', 'url': iframe_src})

        return video_data
```