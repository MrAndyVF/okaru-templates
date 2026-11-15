#!/usr/bin/env python3
"""Empaqueta el esquema de color OKARU como extensión (.oxt) y la instala (apply) o la quita (undo)."""
import hashlib, os, re, shutil, subprocess, sys, tempfile, zipfile

IDENTIFIER = "dev.okaru.libreoffice.theme"  # el mismo de antes: unopkg reemplaza la versión vieja en el sitio
WORK = os.path.join(os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache"), "okaru", "libreoffice-theme")
RENDERED = os.path.join(WORK, "okaru.xcu")
STAMP = os.path.join(WORK, "installed.sha256")

MANIFEST = """<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="http://openoffice.org/2001/manifest">
  <manifest:file-entry manifest:full-path="okaru.xcu" manifest:media-type="application/vnd.sun.star.configuration-data"/>
</manifest:manifest>
"""
DESCRIPTION = f"""<?xml version="1.0" encoding="UTF-8"?>
<description xmlns="http://openoffice.org/extensions/description/2006"
             xmlns:xlink="http://www.w3.org/1999/xlink">
  <identifier value="{IDENTIFIER}"/>
  <version value="2.0.0"/>
  <display-name><name lang="en">OKARU color scheme</name></display-name>
  <publisher><name xlink:href="https://github.com/MrAndyVF/okaru-templates" lang="en">OKARU</name></publisher>
</description>
"""


def unopkg(*args):
    tool = shutil.which("unopkg")
    if tool is None:
        return None  # sin LibreOffice no hay nada que hacer
    return subprocess.run([tool, *args], capture_output=True, text=True, timeout=120)


def apply():
    with open(RENDERED, encoding="utf-8") as f:
        xcu = f.read()
    # El registro guarda los colores como entero RRGGBB.
    xcu = re.sub(r"<value>([0-9a-fA-F]{6})</value>", lambda m: f"<value>{int(m.group(1), 16)}</value>", xcu)
    digest = hashlib.sha256(xcu.encode()).hexdigest()
    try:
        if open(STAMP).read().strip() == digest:
            return 0  # ya instalada con estos colores
    except OSError:
        pass
    with tempfile.TemporaryDirectory() as tmp:
        oxt = os.path.join(tmp, "okaru-theme.oxt")
        with zipfile.ZipFile(oxt, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("META-INF/manifest.xml", MANIFEST)
            z.writestr("description.xml", DESCRIPTION)
            z.writestr("okaru.xcu", xcu)
        result = unopkg("add", "--force", "--suppress-license", oxt)
    if result is None:
        return 0
    if result.returncode != 0:
        print(f"Warning: unopkg could not install the OKARU color scheme: {result.stderr.strip()}", file=sys.stderr)
        return 1
    with open(STAMP, "w") as f:
        f.write(digest + "\n")
    return 0


def undo():
    result = unopkg("list", IDENTIFIER)
    if result is not None and result.returncode == 0:
        unopkg("remove", IDENTIFIER)
    for path in (STAMP, RENDERED):
        if os.path.exists(path):
            os.remove(path)
    return 0


if __name__ == "__main__":
    sys.exit(apply() if sys.argv[1:] == ["apply"] else undo())
