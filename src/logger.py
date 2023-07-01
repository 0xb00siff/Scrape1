```python
import logging
import os

# Define the path for the log files
ERROR_LOG_PATH = os.path.join(os.getcwd(), 'logs/error_logs.txt')
ACTION_LOG_PATH = os.path.join(os.getcwd(), 'logs/action_logs.txt')

# Create logger for error logging
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)

# Create logger for action logging
action_logger = logging.getLogger('action_logger')
action_logger.setLevel(logging.INFO)

# Create file handler which logs error messages
error_handler = logging.FileHandler(ERROR_LOG_PATH)
error_handler.setLevel(logging.ERROR)

# Create file handler which logs all actions
action_handler = logging.FileHandler(ACTION_LOG_PATH)
action_handler.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
error_handler.setFormatter(formatter)
action_handler.setFormatter(formatter)

# Add the handlers to the logger
error_logger.addHandler(error_handler)
action_logger.addHandler(action_handler)

def log_error(message):
    """
    Function to log error messages
    """
    error_logger.error(message)

def log_action(message):
    """
    Function to log all actions
    """
    action_logger.info(message)
```