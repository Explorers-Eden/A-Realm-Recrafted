import os
import json
from .utils import write_yaml, map_booleans
from .cleaner import clean

def convert_getoffmylawn(input_dir, settings_dir):
    path = os.path.join(input_dir, "getoffmylawn.json")
    if not os.path.exists(path):
        return

    data = clean(json.load(open(path, encoding="utf-8")))

    # (keep your exact mappings here unchanged)

    write_yaml(os.path.join(settings_dir, "getoffmylawn.yml"), data)
    print("✔ getoffmylawn.yml")