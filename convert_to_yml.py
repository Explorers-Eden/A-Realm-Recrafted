import os

from modules.sftp import fetch_files_via_sftp
from modules.gamerules import convert_gamerules
from modules.command_storage import convert_command_storage
from modules.getoffmylawn import convert_getoffmylawn
from modules.diff_checker import compare_directories

INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")

BASELINE_DIR = "config_baseline"
DIFF_REPORT = "config_diff.txt"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SETTINGS_DIR, exist_ok=True)

if __name__ == "__main__":
    fetch_files_via_sftp(INPUT_DIR)

    convert_gamerules(INPUT_DIR, OUTPUT_DIR)
    convert_command_storage(INPUT_DIR, SETTINGS_DIR)
    convert_getoffmylawn(INPUT_DIR, SETTINGS_DIR)

    if os.path.exists(BASELINE_DIR):
        compare_directories(BASELINE_DIR, OUTPUT_DIR, DIFF_REPORT)
    else:
        print(f"Baseline directory not found, skipping diff: {BASELINE_DIR}")