import re
import yaml

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(name))


def write_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)


def map_booleans(obj):
    if isinstance(obj, dict):
        return {k: map_booleans(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [map_booleans(v) for v in obj]
    if isinstance(obj, bool):
        return "Enabled" if obj else "Disabled"
    return obj


def clean(obj):
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            k = str(k)
            if k.endswith("_initial") or k in ("command_template", "icon", "bodyicon") or "command_template" in k:
                continue
            val = clean(v)
            if isinstance(val, str) and "command_template" in val:
                continue
            out[k] = val
        return out

    if isinstance(obj, list):
        return [clean(v) for v in obj if "command_template" not in str(v)]

    if isinstance(obj, str) and "command_template" in obj:
        return None

    return obj