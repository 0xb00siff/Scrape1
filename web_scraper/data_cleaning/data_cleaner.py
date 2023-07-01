```python
import re
from bs4 import BeautifulSoup

class DataCleaner:
    def __init__(self):
        pass

    def clean_text(self, text):
        """
        Clean the extracted text data.
        """
        # Remove HTML tags
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text()

        # Remove any URLs
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)

        # Remove punctuations
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Convert to lowercase
        text = text.lower()

        return text

    def clean_metadata(self, metadata):
        """
        Clean the extracted metadata.
        """
        # Remove any URLs from the 'source' field
        if 'source' in metadata:
            metadata['source'] = re.sub(r"http\S+|www\S+|https\S+", '', metadata['source'], flags=re.MULTILINE)

        # Convert 'date' field to a standard format (if it exists)
        if 'date' in metadata:
            metadata['date'] = self.standardize_date(metadata['date'])

        return metadata

    def standardize_date(self, date_str):
        """
        Convert a date string to a standard format.
        """
        # This is a placeholder. The actual implementation will depend on the formats of the dates being scraped.
        return date_str

    def remove_duplicates(self, data_list):
        """
        Remove duplicate entries from a list of data.
        """
        seen = set()
        return [x for x in data_list if not (x in seen or seen.add(x))]
```