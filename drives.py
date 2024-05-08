import os

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