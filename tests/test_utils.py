```python
import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.url = "https://example.com"
        self.invalid_url = "https://invalidurl.com"

    def test_make_request(self):
        response = utils.make_request(self.url)
        self.assertEqual(response.status_code, 200)

    def test_make_request_invalid_url(self):
        with self.assertRaises(Exception):
            utils.make_request(self.invalid_url)

    def test_parse_html(self):
        html_content = "<html><body><h1>Hello World</h1></body></html>"
        soup = utils.parse_html(html_content)
        self.assertEqual(soup.h1.text, "Hello World")

    def test_handle_string(self):
        string = "  Hello World  "
        cleaned_string = utils.handle_string(string)
        self.assertEqual(cleaned_string, "Hello World")

    def test_extract_metadata(self):
        html_content = """
        <html>
            <body>
                <div class="metadata">
                    <span class="date">2022-01-01</span>
                    <span class="author">John Doe</span>
                </div>
            </body>
        </html>
        """
        soup = utils.parse_html(html_content)
        metadata = utils.extract_metadata(soup)
        self.assertEqual(metadata['date'], '2022-01-01')
        self.assertEqual(metadata['author'], 'John Doe')

if __name__ == "__main__":
    unittest.main()
```