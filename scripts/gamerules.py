import os
import nbtlib
from scripts.utils import write_yaml


def convert_gamerules(input_dir, output_dir):
    path = os.path.join(input_dir, "game_rules.dat")

    if not os.path.exists(path):
        return

    try:
        data = nbtlib.load(path).unpack().get("data", {})
    except Exception as e:
        print("NBT error:", e)
        return

    result = {}

    for k, v in data.items():
        v = str(v)
        if v in ("1", "true", "True"):
            result[k] = "Enabled"
        elif v in ("0", "false", "False"):
            result[k] = "Disabled"
        else:
            result[k] = v

    write_yaml(os.path.join(output_dir, "gamerules.yml"), result)