#!/usr/bin/env python3
"""Activa (set) o quita (unset) el esquema okaru en ~/.config/micro/settings.json sin tocar lo demás."""
import json, os, sys, tempfile

path = os.path.join(os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config"), "micro", "settings.json")
try:
    with open(path, encoding="utf-8") as f:
        settings = json.load(f)
except FileNotFoundError:
    settings = {}
except (OSError, ValueError) as e:
    # Un settings.json que no se puede leer no se pisa: el usuario perdería su config.
    sys.exit(f"Warning: micro settings.json is not valid JSON, not changed: {e}")

if sys.argv[1:] == ["set"]:
    if settings.get("colorscheme") == "okaru":
        sys.exit(0)
    settings["colorscheme"] = "okaru"
elif settings.get("colorscheme") == "okaru":
    del settings["colorscheme"]  # vuelve al de fábrica de micro
else:
    sys.exit(0)

os.makedirs(os.path.dirname(path), exist_ok=True)
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".settings.")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=4)
    f.write("\n")
os.replace(tmp, path)
