import os, shutil

def init_copier(blacklist):
    def copytree(src, dst):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)

            # Don't copy if blacklisted
            if item in blacklist:
                continue

            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                copy_if_newer(s, d)
    return copytree

def copy_if_newer(src, dst):
    if not os.path.isfile(dst) or os.path.getmtime(src) > os.path.getmtime(dst):
        shutil.copy2(src, dst)