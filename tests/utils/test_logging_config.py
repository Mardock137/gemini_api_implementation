import os
import logging
from src.utils import logging_config

def test_setup_logging_creates_log_file(tmp_path):
    # Use a temporary directory for logs
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    log_file = log_dir / "app.log"

    # Patch LOG_DIR and LOG_FILE
    logging_config.LOG_DIR = str(log_dir)
    logging_config.LOG_FILE = str(log_file)

    # Setup logging
    logging_config.setup_logging(level=logging.INFO)

    # Log a test message
    logger = logging.getLogger("test_logger")
    logger.info("Test log message")

    # Check that the log file was created and contains the message
    assert log_file.exists()
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Test log message" in content 