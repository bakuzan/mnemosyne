import os
import shutil

import printer

# Helpers


def copy_if_newer(src, dst):
    if not os.path.isfile(dst) or os.path.getmtime(src) > os.path.getmtime(dst):
        printer.yellow(f"Copying {src} > {dst}...")
        shutil.copy2(src, dst)

# Copier creator


def init_copier(location, blacklist, whitelist):
    def copytree(src, dst):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)

            # Don't copy if blacklisted
            if item in blacklist:
                continue

            # If whitelist required, skip if not in whitelist
            if location["IsWhitelistRequired"] == 1 and (not item in whitelist):
                continue

            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True,
                                copy_function=copy_if_newer)
            else:
                copy_if_newer(s, d)
    return copytree


# Duration formatting
def format_duration(duration_seconds):
    # Convert to hours, minutes, and seconds
    hours, rem = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    return "{:0>2}h {:0>2}m {:05.2f}s".format(int(hours), int(minutes), seconds)
