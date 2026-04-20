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

SFTP_REMOTE_GAME_RULES = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/minecraft/game_rules.dat"
SFTP_REMOTE_COMMAND_STORAGE = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/eden/command_storage.dat"
SFTP_REMOTE_GETOFFMYLAWN = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/config/getoffmylawn.json"

REMOTE_FILES = [
    (SFTP_REMOTE_GAME_RULES, os.path.join(INPUT_DIR, "game_rules.dat")),
    (SFTP_REMOTE_COMMAND_STORAGE, os.path.join(INPUT_DIR, "command_storage.dat")),
    (SFTP_REMOTE_GETOFFMYLAWN, os.path.join(INPUT_DIR, "getoffmylawn.json")),
]

if __name__ == "__main__":
    try:
        fetch_files_via_sftp(REMOTE_FILES, INPUT_DIR)
    except Exception as e:
        print("SFTP error:", e)

    convert_gamerules(INPUT_DIR, OUTPUT_DIR)
    convert_command_storage(INPUT_DIR, SETTINGS_DIR)
    convert_getoffmylawn(INPUT_DIR, SETTINGS_DIR)