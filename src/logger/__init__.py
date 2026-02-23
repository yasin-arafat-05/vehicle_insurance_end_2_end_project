import os 
import logging 
from datetime import datetime
from from_root import from_root
from logging.handlers import RotatingFileHandler


# constant for loggin configuration:
LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024 #5MB
BACKUP_COUNT = 3 


# make the constant files:
log_dir_path = os.path.join(from_root(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_path_file = os.path.join(log_dir_path,LOG_FILE)


# make a function for logger:
def configure_logger():
    """
    Description: 
        Configure login with a *1. rotating file handler* and a *2. console file handler*.
    Args:
        None 
    Return: 
        None
    """
    # logger configuration:
    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG)
    formater = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")
    
    # 1. Rotating file handler:
    file_handler = RotatingFileHandler(filename=log_path_file,
                                       maxBytes=MAX_LOG_SIZE,
                                       backupCount=BACKUP_COUNT)
    file_handler.setFormatter(fmt=formater)
    file_handler.setLevel(logging.DEBUG)
    
    
    # 2. Console file handler:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(fmt=formater)
    console_handler.setLevel(logging.INFO)
    
    
    # add handelers to looger:
    logger.addHandler(hdlr=file_handler)
    logger.addHandler(hdlr=console_handler)
    

# configure the logger:
configure_logger()
