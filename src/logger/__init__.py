## logging setup 

import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root  ## # Custom utility to get project root directory
from datetime import datetime
from logging.handlers import SMTPHandler

# Constants for log configuration
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ## Unique log filename based on timestamp
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

# Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR) # Ensure logs are saved at root/logs
os.makedirs(log_dir_path, exist_ok=True)

# === Complete path to log file ===
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    """
    # Create a custom logger
    logger = logging.getLogger()  #Get the root logger
    logger.setLevel(logging.DEBUG) # Capture all logs from DEBUG and above
    
    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation

     # === Rotating File Handler ===
    # Automatically creates new log files after size limit is reached
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)

    # Email alert handler (for ERROR and above)
    email_handler = SMTPHandler(
        mailhost=("smtp.gmail.com", 587),
        fromaddr="kanhavaidl@gmail.com",
        toaddrs=["alert_recipient@example.com"],
        subject="🚨 Application Error Logged",
        credentials=("your_email@gmail.com", "your_app_password"),
        secure=()
    )
    email_handler.setLevel(logging.ERROR)
    email_handler.setFormatter(formatter)
    logger.addHandler(email_handler)


    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()


## Logs are saved in a logs/ folder at the project root.

## Logs rotate after reaching 5 MB, keeping 3 backups.

## Logs print to both file (DEBUG+) and console (INFO+).

## Each log file is timestamped for easy traceability.