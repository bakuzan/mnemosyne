import os, re

def get_destinations():
    env = os.getenv("ENV")
    if env == 'Development':
        return [
            "C:\\projects\\D",
            "C:\\projects\\E",
            "C:\\projects\\F",
        ]
    else:
        return [alpha for alpha in os.listdrives() if 'C' not in alpha]


def filter_drives(drives):
    filter_str = input("Enter a space separated list of Drives you want to use:")
    choices = [re.sub('[^a-zA-Z]', '', s, flags=re.UNICODE).strip().upper() for s in filter_str.split(' ')]
    return [d for d in drives for c in choices if c in d]

