import os
import yaml
import nbtlib
import re

INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SETTINGS_DIR, exist_ok=True)


# -------------------------
# UTILITIES
# -------------------------
def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(name))


def write_yaml(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f, sort_keys=False)


# -------------------------
# RECURSIVE CLEANER
# -------------------------
def clean_data(obj):
    """
    Recursively removes:
    - command_template
    - *_initial
    """
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            k_str = str(k)

            if k_str == "command_template":
                continue
            if k_str.endswith("_initial"):
                continue

            cleaned[k_str] = clean_data(v)
        return cleaned

    elif isinstance(obj, list):
        return [clean_data(v) for v in obj]

    else:
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

    if isinstance(raw, dict):
        items = raw.items()
    elif isinstance(raw, list):
        items = []
        for item in raw:
            if isinstance(item, dict):
                items.extend(item.items())
            elif isinstance(item, (list, tuple)) and len(item) == 2:
                items.append(item)
    else:
        items = []

    for rule, value in items:
        gamerules_clean[str(rule)] = value

    write_yaml(os.path.join(OUTPUT_DIR, "gamerules.yml"), gamerules_clean)

    print(f"✔ gamerules.yml written ({len(gamerules_clean)} entries)")


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
        print("settings not found or invalid")
        return

    written = 0

    for key, value in settings.items():

        key_str = str(key)

        # skip bad root keys
        if key_str == "command_template" or key_str.endswith("_initial"):
            continue

        safe_key = sanitize_filename(key_str)
        output_path = os.path.join(SETTINGS_DIR, f"{safe_key}.yml")

        # FULL recursive cleaning
        cleaned_value = clean_data(value)

        write_yaml(output_path, cleaned_value)
        written += 1

    print(f"✔ settings/*.yml written ({written} files)")


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    convert_gamerules()
    convert_command_storage()