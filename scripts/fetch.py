import os
import sys

from scripts.sftp import fetch_files_via_sftp

INPUT_DIR = "raw_dat"

if __name__ == "__main__":
    os.makedirs(INPUT_DIR, exist_ok=True)
    if not fetch_files_via_sftp(INPUT_DIR):
        sys.exit(1)
