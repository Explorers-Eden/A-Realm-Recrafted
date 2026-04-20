import os
import yaml
import nbtlib
import re

INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SETTINGS_DIR, exist_ok=True)


def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', name)


def flatten_dict(d, parent_key="", sep="."):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


def write_yaml(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f, sort_keys=False)


# -------------------------
# GAMERULES CONVERSION (FIXED)
# -------------------------
def convert_gamerules():
    file_path = os.path.join(INPUT_DIR, "game_rules.dat")

    if not os.path.exists(file_path):
        print("game_rules.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.unpack()

    raw = data.get("data", {})  # <-- FIX: lowercase "data"

    gamerules_clean = {}

    # Case 1: dict format
    if isinstance(raw, dict):
        iterable = raw.items()

    # Case 2: list format (your case)
    elif isinstance(raw, list):
        iterable = []
        for item in raw:
            if isinstance(item, dict):
                iterable.extend(item.items())
            elif isinstance(item, (list, tuple)) and len(item) == 2:
                iterable.append(item)
    else:
        iterable = []

    for rule, value in iterable:
        gamerules_clean[rule] = value

    output_path = os.path.join(OUTPUT_DIR, "gamerules.yml")
    write_yaml(output_path, gamerules_clean)

    print(f"✔ gamerules.yml written ({len(gamerules_clean)} entries)")


# -------------------------
# COMMAND STORAGE (FIXED SAFETY)
# -------------------------
def convert_command_storage():
    file_path = os.path.join(INPUT_DIR, "command_storage.dat")

    if not os.path.exists(file_path):
        print("command_storage.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.unpack()

    raw = data.get("data", {})  # <-- FIXED same issue

    settings = {}

    if isinstance(raw, dict):
        settings = raw
    elif isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                settings.update(item)
            elif isinstance(item, (list, tuple)) and len(item) == 2:
                k, v = item
                settings[k] = v

    for key, value in settings.items():
        safe_key = sanitize_filename(str(key))
        output_path = os.path.join(SETTINGS_DIR, f"{safe_key}.yml")

        if isinstance(value, dict):
            flattened = flatten_dict(value)
            write_yaml(output_path, flattened)
        else:
            write_yaml(output_path, {"value": value})

    print(f"✔ settings/*.yml written ({len(settings)} files)")


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    convert_gamerules()
    convert_command_storage()