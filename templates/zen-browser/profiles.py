#!/usr/bin/env python3
"""Instala (apply) o quita (undo) los estilos de OKARU en cada perfil de Zen Browser.

Por perfil: chrome/okaru-chrome.css y chrome/okaru-content.css, una línea @import marcada al principio de
userChrome.css / userContent.css y una línea marcada en user.js para que Zen lea esos archivos.
"""
import configparser, os, shutil, sys, tempfile

HOME = os.path.expanduser("~")
CACHE = os.path.join(os.environ.get("XDG_CACHE_HOME") or os.path.join(HOME, ".cache"), "okaru", "zen-browser")
ROOTS = [os.path.join(os.environ.get("XDG_CONFIG_HOME") or os.path.join(HOME, ".config"), "zen"),
         os.path.join(HOME, ".zen"),
         os.path.join(HOME, ".var/app/app.zen_browser.zen/.zen"),
         os.path.join(HOME, ".var/app/app.zen_browser.zen/config/zen")]
MARK = "/* okaru */"
PREF = 'user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true); // okaru'
FILES = {"userChrome.css": "okaru-chrome.css", "userContent.css": "okaru-content.css"}


def profiles():
    for root in ROOTS:
        ini = configparser.ConfigParser(interpolation=None)
        if not ini.read(os.path.join(root, "profiles.ini")):
            continue
        for section in ini.sections():
            path = ini.get(section, "Path", fallback=None)
            if not path:
                continue
            full = os.path.join(root, path) if ini.get(section, "IsRelative", fallback="1") == "1" else path
            if os.path.isfile(os.path.join(full, "prefs.js")):  # solo perfiles que Zen ya usó
                yield full


def write(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".okaru.")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    os.replace(tmp, path)


def edit(path, line, add, first):
    """Añade o quita `line` (marcada como nuestra) sin tocar el resto del archivo."""
    lines = open(path, encoding="utf-8").readlines() if os.path.isfile(path) else []
    kept = [l for l in lines if l.rstrip("\n") != line]
    if add:
        kept = ([line + "\n"] + kept) if first else (kept + [line + "\n"])
    if kept == lines:
        return
    if kept or os.path.isfile(path):
        if not kept:
            os.remove(path)  # solo tenía nuestra línea
        else:
            write(path, kept)


def main():
    add = sys.argv[1:] == ["apply"]
    for profile in profiles():
        chrome = os.path.join(profile, "chrome")
        for host, ours in FILES.items():
            target = os.path.join(chrome, ours)
            if add:
                os.makedirs(chrome, exist_ok=True)
                shutil.copyfile(os.path.join(CACHE, ours), target + ".tmp")
                os.replace(target + ".tmp", target)
            elif os.path.exists(target):
                os.remove(target)
            # @import tiene que ir antes que cualquier otra regla.
            edit(os.path.join(chrome, host), f'@import url("{ours}"); {MARK}', add, first=True)
        edit(os.path.join(profile, "user.js"), PREF, add, first=False)
        if not add and os.path.isdir(chrome) and not os.listdir(chrome):
            os.rmdir(chrome)
    return 0


if __name__ == "__main__":
    sys.exit(main())
