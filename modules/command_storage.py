import os
import nbtlib

from modules.utils import clean, write_yaml, sanitize_filename, deep_format
from modules.mappings import apply_mapping, FR_VALUE_MAP, KI_VALUE_MAP, WW_VALUE_MAP
from modules.mob_manager import handle_mob_manager
from modules.nice_actions import remap_nice_actions


def convert_command_storage(input_dir, settings_dir):
    path = os.path.join(input_dir, "command_storage.dat")

    if not os.path.exists(path):
        print("command_storage.dat not found")
        return

    try:
        data = nbtlib.load(path).unpack()
    except Exception as e:
        print("NBT error:", e)
        return

    settings = data.get("data", {}).get("contents", {}).get("settings", {})

    for key, value in settings.items():
        key = str(key)

        if key == "mob_manager":
            handle_mob_manager(value, settings_dir)
            continue

        cleaned = clean(value)
        if not cleaned:
            continue

        if key.startswith("fabled_roots"):
            cleaned = apply_mapping(cleaned, FR_VALUE_MAP)

        elif key.startswith("keepinv"):
            cleaned = apply_mapping(cleaned, KI_VALUE_MAP)

        elif key.startswith("warping_wonders"):
            cleaned = apply_mapping(cleaned, WW_VALUE_MAP)

        elif key.startswith("nice_actions"):
            cleaned = remap_nice_actions(cleaned)

        cleaned = deep_format(cleaned)

        out = os.path.join(settings_dir, f"{sanitize_filename(key)}.yml")
        write_yaml(out, cleaned)

    print("✔ command_storage processed")