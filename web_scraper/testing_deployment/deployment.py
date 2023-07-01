```python
import os
from subprocess import call

from web_scraper.config import DEPLOYMENT_PATH, DEPLOYMENT_SERVER, DEPLOYMENT_USER

def deploy():
    try:
        # Archive the project
        call(['tar', '-czf', 'web_scraper.tar.gz', 'web_scraper'])

        # Copy the archive to the deployment server
        call(['scp', 'web_scraper.tar.gz', f'{DEPLOYMENT_USER}@{DEPLOYMENT_SERVER}:{DEPLOYMENT_PATH}'])

        # SSH into the server and extract the archive
        call(['ssh', f'{DEPLOYMENT_USER}@{DEPLOYMENT_SERVER}', 'tar', '-xzf', f'{DEPLOYMENT_PATH}/web_scraper.tar.gz'])

        # Start the bot on the server
        call(['ssh', f'{DEPLOYMENT_USER}@{DEPLOYMENT_SERVER}', 'python3', f'{DEPLOYMENT_PATH}/web_scraper/main.py'])

        print("Deployment successful.")
    except Exception as e:
        print(f"Deployment failed: {str(e)}")

if __name__ == "__main__":
    deploy()
```
