```python
import urllib.robotparser as urobot

class RobotsTxtHandler:
    def __init__(self):
        self.rp = urobot.RobotFileParser()

    def can_fetch(self, url, user_agent='*'):
        self.rp.set_url(url)
        self.rp.read()
        return self.rp.can_fetch(user_agent, url)
```