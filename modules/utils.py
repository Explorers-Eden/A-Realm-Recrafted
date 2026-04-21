import re
import yaml

GLOBAL_VALUE_MAP = {
    "enabled": "Enabled",
    "disabled": "Disabled",
}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(name))


def write_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)


def format_percent(value):
    try:
        if isinstance(value, (int, float)):
            v = float(value)
            if not v.is_integer():
                return f"{int(round(v * 100))}%"
            return str(int(v))

        if isinstance(value, str):
            s = value.strip()
            if not s:
                return value

            low = s.lower()
            if low in GLOBAL_VALUE_MAP:
                return GLOBAL_VALUE_MAP[low]

            if re.match(r"^-?\d+(\.\d+)?$", s):
                v = float(s)
                if not v.is_integer():
                    return f"{int(round(v * 100))}%"
                return s
    except Exception:
        pass
    return value


def deep_format(obj):
    if isinstance(obj, dict):
        return {k: deep_format(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [deep_format(v) for v in obj]
    return format_percent(obj)


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
        cleaned = {}
        for k, v in obj.items():
            k = str(k)
            if k.endswith("_initial"):
                continue
            if k in ("command_template", "icon", "bodyicon"):
                continue
            if "command_template" in k:
                continue

            val = clean(v)
            if isinstance(val, str) and "command_template" in val:
                continue

            cleaned[k] = val
        return cleaned

    if isinstance(obj, list):
        return [clean(v) for v in obj if "command_template" not in str(v)]

    return obj