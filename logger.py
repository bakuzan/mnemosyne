import logging, time

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f'./logs/{time.time()}.log')

logger.addHandler(file_handler)

def get_logger():
    return logger
