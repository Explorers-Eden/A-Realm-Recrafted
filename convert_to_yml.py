import os

from modules.sftp import fetch_files_via_sftp
from modules.gamerules import convert_gamerules
from modules.command_storage import convert_command_storage
from modules.getoffmylawn import convert_getoffmylawn

INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(SETTINGS_DIR, exist_ok=True)

if __name__ == "__main__":
    fetch_files_via_sftp(INPUT_DIR)
    convert_gamerules(INPUT_DIR, OUTPUT_DIR)
    convert_command_storage(INPUT_DIR, SETTINGS_DIR)
    convert_getoffmylawn(INPUT_DIR, SETTINGS_DIR)