import logging, time

logger = logging.getLogger(__name__)

# File Handler setup
file_handler = logging.FileHandler(f'./logs/{time.time()}.log')
formatter = logging.Formatter(u"%(message)s")
file_handler.setFormatter(formatter)

# Set logger values
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

def get_logger():
    return logger
