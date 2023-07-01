```python
import os
from src.main import AlienInfoScraper

class Deployer:
    def __init__(self):
        self.scraper = AlienInfoScraper()

    def deploy(self):
        try:
            self.scraper.run()
            print("Deployment successful.")
        except Exception as e:
            print(f"Deployment failed. Error: {str(e)}")

if __name__ == "__main__":
    deployer = Deployer()
    deployer.deploy()
```