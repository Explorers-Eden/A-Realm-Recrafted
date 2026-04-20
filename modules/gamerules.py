import os
import nbtlib
from modules.utils import write_yaml

def convert_gamerules(input_dir, output_dir):
    path = os.path.join(input_dir, "game_rules.dat")
    if not os.path.exists(path):
        return

    data = nbtlib.load(path).unpack().get("data", {})

    out = {}
    for k, v in data.items():
        if str(v).lower() in ("true", "1"):
            out[k] = "Enabled"
        elif str(v).lower() in ("false", "0"):
            out[k] = "Disabled"
        else:
            out[k] = v

    write_yaml(os.path.join(output_dir, "gamerules.yml"), out)
    print("✔ gamerules.yml")