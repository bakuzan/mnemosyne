import logging
import datetime

logger = logging.getLogger(__name__)

# File Handler setup
now_datetime = datetime.datetime.now()
now_datetime_in_iso = datetime.datetime.strptime(
    now_datetime.isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%dT%H_%M_%S')

file_handler = logging.FileHandler(
    f'./logs/{now_datetime_in_iso}.log', 'w', 'utf-8')

# Set logger values
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)


def get_logger():
    return logger
