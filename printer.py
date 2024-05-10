from threading import Lock

from logger import get_logger

logger = get_logger()

#######################################################
# Printing with Threading
#######################################################
print_lock = Lock()
_print = print  # save original


def print(*args, **kwargs):
    """Prevents concurrent printing."""
    with print_lock:
        _print(*args, **kwargs)

#######################################################


def custom_pretty_print(d):
    for key, value in d.items():
        text = f"{key}: {value}"
        print(text)
        logger.info(text)
    print()


def coloured(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def coloured_print(r, g, b, text):
    print(coloured(r, g, b, text))
    logger.info(text)


def red(text):
    coloured_print(255, 0, 0, text)


def green(text):
    coloured_print(0, 255, 0, text)


def blue(text):
    coloured_print(0, 0, 255, text)


def yellow(text):
    coloured_print(255, 255, 0, text)


def magenta(text):
    coloured_print(255, 0, 255, text)


def cyan(text):
    coloured_print(0, 255, 255, text)
