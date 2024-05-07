import os, time
from concurrent.futures import ThreadPoolExecutor

import config
import printer
from utils import init_copier

# Load .env
config.setup()

#
# TEMPORARY HARD CODED VALUES
#       TODO - MOVE THESE INTO DATABASE
drives = {
    "C:\\projects\\D",
    "C:\\projects\\E",
    "C:\\projects\\F",
}

locations = [
    { "name": "Books", "from": "C:\\projects\\C\\Books", "to": 'Books' },
    { "name": "Comics", "from": "C:\\projects\\C\\Comics", "to": 'Comics' },
    { "name": "Comics (New)", "from": "C:\\projects\\C\\Comics\\#temp", "to": 'Comics' },
    { "name": "Videos - Misc", "from": "C:\\projects\\C\\Videos", "to": 'Videos - Misc' },
    { "name": "Videos - Misc (New)", "from": "C:\\projects\\C\\Videos\\#temp\\Videos - Misc", "to": 'Videos - Misc' },
    { "name": "Videos", "from": "C:\\projects\\C\\Videos\\#temp", "to": 'Videos' },
]

blacklist = {
    '#temp',
    '# already copied',
    '# no copy',
    'Videos - Misc'
}

#
# TEMPORARY HARD CODED VALUES
# 

def start():
    printer.green("Starting MNEMOSYNE...")

    for location in locations:
        name = location["name"]
        source_dir = location["from"]
        destination_dir = location["to"]
        
        # Create real target paths on backup drives
        dest_dirs = [os.path.join(drive, destination_dir) for drive in drives]
        # Create function that will do the copying
        copytree = init_copier(blacklist)

        printer.blue(f"Processing {name}...")
        printer.cyan(f"From: {source_dir}")
        printer.cyan(f"  To: {'; '.join(dest_dirs)}")

        with ThreadPoolExecutor(max_workers=3) as e:
            jobs = [e.submit(copytree, source_dir, dest_dir) for dest_dir in dest_dirs]

        while any(job.running() for job in jobs):
            time.sleep(.25)

        printer.magenta(f"{name} Complete.")
    
    printer.green("MNEMOSYNE finishing...")

if __name__ == "__main__":
    start()