# Alien Information Web Scraper

This is the documentation for the Alien Information Web Scraper. This bot is designed to scrape the internet for the latest information related to aliens, UFOs, UAPs, and similar content from a variety of online platforms.

## Getting Started

To get started with the bot, you need to run the `main.py` file located in the `src` directory.

```python
python src/main.py
```

## Modules

The bot is divided into several modules, each responsible for a specific task.

### Web Scraper

The `web_scraper.py` module is responsible for scraping data from the internet. It uses Python's Beautiful Soup and Selenium libraries to extract data from static and dynamic websites.

### Data Extractor

The `data_extractor.py` module is responsible for extracting specific data from the scraped web pages. It extracts textual data, images, videos, and metadata such as the date of posting, author, source URL, and any associated tags or keywords.

### Data Cleaner

The `data_cleaner.py` module is responsible for cleaning the extracted data. It removes any irrelevant information, advertisements, or other non-essential elements. It also handles duplicates and avoids storing redundant data.

### Data Storage

The `data_storage.py` module is responsible for storing the cleaned and structured data in MongoDB. The data is stored in a structured format like JSON with fields such as title, content, date, author, tags, source, and type (text, image, video).

### Error Handler

The `error_handler.py` module is responsible for handling any errors that occur during the scraping process. It logs all errors for debugging and improvement purposes.

### Logger

The `logger.py` module is responsible for logging all actions of the bot. It creates two log files, `error_logs.txt` and `action_logs.txt`, in the `logs` directory.

### Scheduler

The `scheduler.py` module is responsible for automating the execution of the bot. It can be set to run the bot on a scheduled basis, for instance, daily, weekly, etc.

### Updater

The `updater.py` module is responsible for handling updates and maintenance of the bot as websites change their structures and scraping policies over time.

### Tester

The `tester.py` module is responsible for testing the bot before deployment to ensure it is functioning as expected.

### Deployer

The `deployer.py` module is responsible for deploying the bot in a production environment.

## Configuration

The bot uses three configuration files located in the `config` directory:

- `config.py`: Contains global settings for the bot.
- `urls.py`: Contains the base URLs and API endpoints for the bot to scrape.
- `credentials.py`: Contains the database credentials for MongoDB.

## Testing

To run the tests for the bot, you need to run the test files located in the `tests` directory.

```python
python tests/test_main.py
```

## Troubleshooting

If you encounter any issues while running the bot, you can refer to the `error_logs.txt` and `action_logs.txt` files in the `logs` directory for more information.

## Updates and Maintenance

To update the bot, you need to run the `updater.py` module. It will handle any necessary updates and maintenance tasks.

```python
python src/updater.py
```

## Deployment

To deploy the bot in a production environment, you need to run the `deployer.py` module.

```python
python src/deployer.py
```

## Contributing

If you wish to contribute to the development of the bot, please refer to the `CONTRIBUTING.md` file for guidelines.

## License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.