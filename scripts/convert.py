import os

from scripts.gamerules import convert_gamerules
from scripts.command_storage import convert_command_storage
from scripts.getoffmylawn import convert_getoffmylawn
from scripts.diff_checker import compare_directories

INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")
BASELINE_DIR = "config_baseline"
DIFF_REPORT = "config_diff.txt"

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(SETTINGS_DIR, exist_ok=True)

    convert_gamerules(INPUT_DIR, OUTPUT_DIR)
    convert_command_storage(INPUT_DIR, SETTINGS_DIR)
    convert_getoffmylawn(INPUT_DIR, SETTINGS_DIR)

    if os.path.exists(BASELINE_DIR):
        compare_directories(BASELINE_DIR, OUTPUT_DIR, DIFF_REPORT)
    else:
        print(f"Baseline directory not found, skipping diff: {BASELINE_DIR}")
