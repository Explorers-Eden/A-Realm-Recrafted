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
# UTIL
# -------------------------
def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(name))


def write_yaml(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f, sort_keys=False)


# -------------------------
# CLEANER
# -------------------------
def clean(obj):
    """
    Recursively removes:
    - *_initial keys
    - command_template anywhere
    - icon/bodyicon fields anywhere
    """

    if isinstance(obj, dict):
        cleaned = {}

        for k, v in obj.items():
            k_str = str(k)

            # -------------------------
            # DROP KEYS
            # -------------------------
            if k_str.endswith("_initial"):
                continue

            if k_str in ("command_template", "icon", "bodyicon"):
                continue

            if "command_template" in k_str:
                continue

            cleaned_v = clean(v)

            # remove junk string values
            if isinstance(cleaned_v, str):
                if "command_template" in cleaned_v:
                    continue

            cleaned[k_str] = cleaned_v

        return cleaned

    elif isinstance(obj, list):
        return [
            clean(v)
            for v in obj
            if "command_template" not in str(v)
        ]

    else:
        if isinstance(obj, str):
            if "command_template" in obj:
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
        rule = str(rule)
    
        # normalize values
        if str(value) in ("1", "true", "True"):
            gamerules_clean[rule] = "Enabled"
        elif str(value) in ("0", "false", "False"):
            gamerules_clean[rule] = "Disabled"
        else:
            gamerules_clean[rule] = value

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

    # mapping for specific replacements in fabled_roots settings
    FR_VALUE_MAP = {
        "enabled": "Enabled",
        "disabled": "Disabled",
        "starter_equip": "Starter Equipment After Race Selection",
        "prefix": "Race Prefix In Front Of Player Name",
        "pvp": "PVP Among Own Race",
        "seeinvis": "See Invisible Players Of Own Race",
        "npc_spawning": "Descendant Spawning",
    }

    def apply_map(obj):
        """
        Recursively replace dict keys and string values according to FR_VALUE_MAP.
        """
        if isinstance(obj, dict):
            new = {}
            for k, v in obj.items():
                k_str = str(k)
                mapped_key = FR_VALUE_MAP.get(k_str, k_str)
                new[mapped_key] = apply_map(v)
            return new
        if isinstance(obj, list):
            return [apply_map(v) for v in obj]
        if isinstance(obj, str):
            return FR_VALUE_MAP.get(obj, obj)
        return obj

    for key, value in settings.items():

        key_str = str(key)

        # DROP WHOLE FILE
        if key_str == "nice_admin_tools":
            continue

        if key_str == "command_template" or key_str.endswith("_initial"):
            continue

        cleaned = clean(value)

        # remove empty results
        if cleaned is None or cleaned == {}:
            continue

        # If this is fabled_roots (or starts with it), apply replacements
        if key_str == "fabled_roots" or key_str.startswith("fabled_roots"):
            cleaned = apply_map(cleaned)

        safe_key = sanitize_filename(key_str)
        output_path = os.path.join(SETTINGS_DIR, f"{safe_key}.yml")

        write_yaml(output_path, cleaned)
        written += 1

    print(f"✔ settings/*.yml written ({written} files)")


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    convert_gamerules()
    convert_command_storage()
