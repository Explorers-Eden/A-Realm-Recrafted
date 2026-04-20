import os
import re
import yaml
import json
import nbtlib
import paramiko

# ---- SFTP CONFIG (from environment / GitHub Secrets) ----
SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_PORT = int(os.getenv("SFTP_PORT", "22"))
SFTP_USER = os.getenv("SFTP_USER")
SFTP_PASS = os.getenv("SFTP_PASS")

# exact remote file paths
SFTP_REMOTE_GAME_RULES = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/minecraft/game_rules.dat"
SFTP_REMOTE_COMMAND_STORAGE = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/eden/command_storage.dat"
SFTP_REMOTE_GETOFFMYLAWN = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/config/getoffmylawn.json"

# ---- PATHS ----
INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SETTINGS_DIR, exist_ok=True)


# -------------------------
# SFTP DOWNLOAD
# -------------------------
def fetch_files_via_sftp():
    if not SFTP_HOST or not SFTP_USER or not SFTP_PASS:
        print("SFTP credentials missing.")
        return

    transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
    try:
        transport.connect(username=SFTP_USER, password=SFTP_PASS)
        sftp = paramiko.SFTPClient.from_transport(transport)

        remote_files = [
            (SFTP_REMOTE_GAME_RULES, os.path.join(INPUT_DIR, "game_rules.dat")),
            (SFTP_REMOTE_COMMAND_STORAGE, os.path.join(INPUT_DIR, "command_storage.dat")),
            (SFTP_REMOTE_GETOFFMYLAWN, os.path.join(INPUT_DIR, "getoffmylawn.json")),
        ]

        for remote_path, local_path in remote_files:
            try:
                sftp.get(remote_path, local_path)
                print(f"Downloaded: {remote_path}")
            except IOError as e:
                print(f"Failed to download {remote_path}: {e}")

        sftp.close()
    finally:
        transport.close()


# -------------------------
# UTIL
# -------------------------
def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(name))


def write_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)


# -------------------------
# CLEANER
# -------------------------
def clean(obj):
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            k_str = str(k)
            if k_str.endswith("_initial"):
                continue
            if k_str in ("command_template", "icon", "bodyicon"):
                continue
            if "command_template" in k_str:
                continue

            cleaned_v = clean(v)
            if isinstance(cleaned_v, str) and "command_template" in cleaned_v:
                continue

            cleaned[k_str] = cleaned_v
        return cleaned

    elif isinstance(obj, list):
        return [clean(v) for v in obj if "command_template" not in str(v)]

    else:
        if isinstance(obj, str) and "command_template" in obj:
            return None
        return obj


# -------------------------
# GAMERULES
# -------------------------
def convert_gamerules():
    file_path = os.path.join(INPUT_DIR, "game_rules.dat")
    if not os.path.exists(file_path):
        print("game_rules.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.unpack()

    raw = data.get("data", {})
    gamerules_clean = {}

    for rule, value in (raw.items() if isinstance(raw, dict) else []):
        if str(value).lower() in ("1", "true"):
            gamerules_clean[str(rule)] = "Enabled"
        elif str(value).lower() in ("0", "false"):
            gamerules_clean[str(rule)] = "Disabled"
        else:
            gamerules_clean[str(rule)] = value

    write_yaml(os.path.join(OUTPUT_DIR, "gamerules.yml"), gamerules_clean)
    print("✔ gamerules.yml written")


# -------------------------
# COMMAND STORAGE
# -------------------------
def convert_command_storage():
    file_path = os.path.join(INPUT_DIR, "command_storage.dat")
    if not os.path.exists(file_path):
        print("command_storage.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.unpack()

    contents = data.get("data", {}).get("contents", {})
    settings = contents.get("settings", {})

    if not isinstance(settings, dict):
        print("settings invalid")
        return

    for key, value in settings.items():
        key_str = str(key)

        if key_str.endswith("_initial") or key_str == "command_template":
            continue

        cleaned = clean(value)
        if not cleaned:
            continue

        safe_key = sanitize_filename(key_str)
        write_yaml(os.path.join(SETTINGS_DIR, f"{safe_key}.yml"), cleaned)

    print("✔ settings/*.yml written")


# -------------------------
# GETOFFMYLAWN (NEW)
# -------------------------
def convert_getoffmylawn():
    file_path = os.path.join(INPUT_DIR, "getoffmylawn.json")
    if not os.path.exists(file_path):
        print("getoffmylawn.json not found")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading getoffmylawn.json: {e}")
        return

    cleaned = clean(data)

    output_path = os.path.join(OUTPUT_DIR, "getoffmylawn.yml")
    write_yaml(output_path, cleaned)

    print("✔ getoffmylawn.yml written")


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    try:
        fetch_files_via_sftp()
    except Exception as e:
        print(f"SFTP failed: {e}")

    convert_gamerules()
    convert_command_storage()
    convert_getoffmylawn()