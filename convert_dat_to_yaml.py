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


# Gamerules → single file
def convert_gamerules():
    file_path = os.path.join(INPUT_DIR, "game_rules.dat")
    if not os.path.exists(file_path):
        print("game_rules.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.root

    gamerules_raw = data["Data"]["GameRules"]
    gamerules_clean = {}

    for rule, value in gamerules_raw.items():
        if value in ["true", "false"]:
            gamerules_clean[rule] = value == "true"
        elif value in ["0", "1"]:
            gamerules_clean[rule] = value == "1"
        else:
            gamerules_clean[rule] = value

    output_path = os.path.join(OUTPUT_DIR, "gamerules.yml")
    write_yaml(output_path, gamerules_clean)

    print("✔ gamerules.yml written")


# Command storage → split into files
def convert_command_storage():
    file_path = os.path.join(INPUT_DIR, "command_storage.dat")
    if not os.path.exists(file_path):
        print("command_storage.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.unpack()

    settings = data.get("Data", {}).get("settings", {})

    for key, value in settings.items():
        safe_key = sanitize_filename(key)

        output_path = os.path.join(SETTINGS_DIR, f"{safe_key}.yml")

        if isinstance(value, dict):
            flattened = flatten_dict(value)
            write_yaml(output_path, flattened)
        else:
            write_yaml(output_path, {"value": value})

    print("✔ settings/*.yml written")


if __name__ == "__main__":
    convert_gamerules()
    convert_command_storage()