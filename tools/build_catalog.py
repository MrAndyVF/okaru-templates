#!/usr/bin/env python3
"""Genera catalog.json a partir de templates/<id>/ (formato que lee OKARU).

Cada plantilla necesita template.toml con [catalog.<id>] name / category. Uso:
    python3 tools/build_catalog.py           # escribe catalog.json
    python3 tools/build_catalog.py --check   # falla si catalog.json no está al día
"""
import hashlib
import json
import os
import re
import sys
import tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "templates")
CATALOG = os.path.join(ROOT, "catalog.json")
SAFE_ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build():
    entries = []
    errors = []
    for tid in sorted(os.listdir(TEMPLATES)) if os.path.isdir(TEMPLATES) else []:
        base = os.path.join(TEMPLATES, tid)
        if not os.path.isdir(base):
            continue
        if not SAFE_ID.match(tid):
            errors.append(f"{tid}: id inválido (minúsculas, números, . _ -)")
            continue
        manifest = os.path.join(base, "template.toml")
        if not os.path.isfile(manifest):
            errors.append(f"{tid}: falta template.toml")
            continue
        with open(manifest, "rb") as f:
            meta = tomllib.load(f).get("catalog", {}).get(tid, {})
        if not meta.get("category"):
            errors.append(f"{tid}: falta [catalog.{tid}] category")
        files = []
        for dirpath, _, names in os.walk(base):
            for name in sorted(names):
                path = os.path.join(dirpath, name)
                rel = os.path.relpath(path, base).replace(os.sep, "/")
                # Ejecutable = empieza con #! (no depende del sistema de archivos, p. ej. NTFS).
                with open(path, "rb") as f:
                    mode = "0755" if f.read(2) == b"#!" else "0644"
                files.append({"name": rel, "md5": md5(path), "mode": mode})
        files.sort(key=lambda f: f["name"])
        entries.append({"name": tid, "category": meta.get("category", "misc"), "files": files})
    return entries, errors


def main():
    entries, errors = build()
    for e in errors:
        print("error:", e, file=sys.stderr)
    text = json.dumps(entries, indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        current = open(CATALOG, encoding="utf-8").read() if os.path.exists(CATALOG) else ""
        if current != text:
            print("catalog.json no está al día: ejecuta python3 tools/build_catalog.py", file=sys.stderr)
            return 1
        return 1 if errors else 0
    with open(CATALOG, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{len(entries)} plantillas en catalog.json")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
