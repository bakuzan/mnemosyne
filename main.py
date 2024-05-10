import os
import time
from concurrent.futures import ThreadPoolExecutor

import config
import printer
from db import fetch_locations, fetch_blacklist, fetch_whitelist, fetch_tracked_folders
from drives import get_destinations
from utils import init_copier, format_duration

# Load .env
config.setup()


def start():
    printer.green("Starting MNEMOSYNE...")
    before = time.perf_counter()

    # Gather required information
    drives = get_destinations()
    locations = fetch_locations()

    # Have user confirm this is Okay
    printer.yellow(drives)
    printer.yellow('')

    answer = input("Is it Okay to copy to these drives? (y/n)")
    if not answer.lower() in ["y", "Y"]:
        printer.red("Exiting MNEMOSYNE...")
        exit()

    # Iterate locations to copy from
    for location in locations:
        b = time.perf_counter()
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
            jobs = [e.submit(copytree, source_dir, dest_dir)
                    for dest_dir in dest_dirs]

        while any(job.running() for job in jobs):
            time.sleep(.25)

        printer.magenta(f"{name} Complete.",)
        a = time.perf_counter()
        printer.magenta(f"LOOP: {format_duration(a - b)}.\r\n")

    # Copying finished, write out folder contents that you want tracked
    place = drives[0]
    tracks = fetch_tracked_folders()

    for track in tracks:
        output_path = track["OutputPath"]
        target_path = os.path.join(place, track["FolderName"])
        items = os.listdir(target_path)

        printer.yellow(f"Writing {output_path}...")
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(items))

    # Wrap up the process
    printer.green("MNEMOSYNE finishing...")
    after = time.perf_counter()
    printer.green(f"  RUNTIME {format_duration(after - before)}.\r\n")


# Run the script contents
if __name__ == "__main__":
    start()
