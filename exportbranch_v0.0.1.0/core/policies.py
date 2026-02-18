import re

INVALID_WINDOWS = r'[<>:"/\\|?*]'

RESERVED_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}

def normalize_filename(name: str, lower=False):
    name = re.sub(INVALID_WINDOWS, "", name)

    base = name.split(".")[0].upper()
    if base in RESERVED_NAMES:
        name = f"_{name}"

    return name.lower() if lower else name
