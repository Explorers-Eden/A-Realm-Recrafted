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
        gamerules_clean[rule] = value

    output_path = os.path.join(OUTPUT_DIR, "gamerules.yml")
    write_yaml(output_path, gamerules_clean)

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

    # Navigate structure safely
    contents = data.get("data", {}).get("contents", {})
    settings = contents.get("settings", {})

    if not isinstance(settings, dict):
        print("settings not found or invalid")
        return

    written = 0

    for key, value in settings.items():

        key_str = str(key)

        # -------------------------
        # FILTER UNWANTED KEYS
        # -------------------------
        if "*command_template*" in key_str or "*initial*" in key_str:
            continue

        safe_key = sanitize_filename(key_str)
        output_path = os.path.join(SETTINGS_DIR, f"{safe_key}.yml")

        # -------------------------
        # HANDLE VALUE TYPES
        # -------------------------
        if isinstance(value, dict):
            cleaned = {}

            for k, v in value.items():
                if "*command_template*" in str(k) or "*initial*" in str(k):
                    continue
                cleaned[k] = v

            write_yaml(output_path, cleaned)

        elif isinstance(value, list):
            filtered = [
                v for v in value
                if "*command_template*" not in str(v)
                and "*initial*" not in str(v)
            ]
            write_yaml(output_path, {"items": filtered})

        else:
            write_yaml(output_path, {"value": value})

        written += 1

    print(f"✔ settings/*.yml written ({written} files)")


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    convert_gamerules()
    convert_command_storage()