import os
import nbtlib
from modules.utils import clean, write_yaml, sanitize_filename, deep_format
from modules.mob_manager import handle_mob_manager


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

        cleaned = deep_format(cleaned)

        out = os.path.join(settings_dir, f"{sanitize_filename(key)}.yml")
        write_yaml(out, cleaned)

    print("✔ command_storage processed")