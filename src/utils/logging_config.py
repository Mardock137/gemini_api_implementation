import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'app.log')

# Ensure that the logs/ directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging(level=logging.INFO):
    """
    Configures logging to output to both console and a log file.
    """
    log_format = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    handlers = [
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, encoding='utf-8')
    ]

    logging.basicConfig(
        level=level,
        format=log_format,
        datefmt=date_format,
        handlers=handlers,
        force=True  # Override any previous logging configuration
    ) 