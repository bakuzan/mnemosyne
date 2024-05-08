import os, time
from concurrent.futures import ThreadPoolExecutor

import config
import printer
from db import fetch_locations, fetch_blacklist, fetch_whitelist
from drives import get_destinations
from utils import init_copier

# Load .env
config.setup()

def start():
    printer.green("Starting MNEMOSYNE...")

    # Gather required information
    drives = get_destinations()
    locations = fetch_locations()

    # Have user confirm this is Okay
    printer.yellow(drives)
    answer = input("Is it Okay to copy to these drives? (y/n)")
    if not answer.lower() in ["y","Y"]:
        printer.red("Exiting MNEMOSYNE...")
        exit()

    # Iterate locations to copy from
    for location in locations:
        name = location["Name"]
        source_dir = location["SrcPath"]
        destination_dir = location["DestName"]

        # Create real target paths on backup drives
        dest_dirs = [os.path.join(drive, destination_dir) for drive in drives]
        # Create function that will do the copying
        blacklist = [item["Name"] for item in fetch_blacklist(location["Id"])]
        whitelist = [item["Name"] for item in fetch_whitelist(location["Id"])]
        copytree = init_copier(location, blacklist, whitelist)

        printer.blue(f"Processing {name}...")
        printer.cyan(f"From: {source_dir}")
        printer.cyan(f"  To: {'; '.join(dest_dirs)}")

        with ThreadPoolExecutor(max_workers=3) as e:
            jobs = [e.submit(copytree, source_dir, dest_dir) for dest_dir in dest_dirs]

        while any(job.running() for job in jobs):
            time.sleep(.25)

        printer.magenta(f"{name} Complete.")
    
    printer.green("MNEMOSYNE finishing...")

# Run the script contents
if __name__ == "__main__":
    start()
    