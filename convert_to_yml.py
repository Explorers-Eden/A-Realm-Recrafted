import os

from modules.sftp import fetch_files_via_sftp
from modules.gamerules import convert_gamerules
from modules.command_storage import convert_command_storage
from modules.getoffmylawn import convert_getoffmylawn

INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SETTINGS_DIR, exist_ok=True)

REMOTE_FILES = [
    ("/srv/docker/crafty-4/.../game_rules.dat", f"{INPUT_DIR}/game_rules.dat"),
    ("/srv/docker/crafty-4/.../command_storage.dat", f"{INPUT_DIR}/command_storage.dat"),
    ("/srv/docker/crafty-4/.../getoffmylawn.json", f"{INPUT_DIR}/getoffmylawn.json"),
]

if __name__ == "__main__":
    try:
        fetch_files_via_sftp(REMOTE_FILES, INPUT_DIR)
    except Exception as e:
        print("SFTP error:", e)

    convert_gamerules(INPUT_DIR, OUTPUT_DIR)
    convert_command_storage(INPUT_DIR, SETTINGS_DIR)
    convert_getoffmylawn(INPUT_DIR, SETTINGS_DIR)