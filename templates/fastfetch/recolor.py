#!/usr/bin/env python3
"""Cambia los colores con nombre de ~/.config/fastfetch/config.jsonc por los de la paleta.

apply: "keyColor": "green" -> "keyColor": "#rrggbb" /*okaru:green*/ (y lo mismo en logo.color).
undo: vuelve a "green". El comentario guarda el nombre original, así que reaplicar y deshacer son exactos.
Mezclas (degradado del logo): "#rrggbb" /*okaru:blue..magenta@3*/ = 3/8 del camino de blue a magenta.
"""
import json, os, re, sys, tempfile

home = os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config")
path = os.path.join(home, "fastfetch", "config.jsonc")
# La salida de la plantilla (output_path en template.toml).
colors_path = os.path.join(os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache"), "okaru", "fastfetch-colors.json")
# "keyColor" de cada módulo y las claves "1".."9" de logo.color; valor con nombre o ya recoloreado.
PATTERN = re.compile(
    r'("(?:keyColor|[1-9])"\s*:\s*)"(?:([a-z_]+)|#[0-9a-fA-F]{6})"(?:\s*/\*okaru:([a-z_]+(?:\.\.[a-z_]+@[0-8])?)\*/)?'
)


def main():
    if not os.path.isfile(path):
        return 0
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if sys.argv[1] == "apply":
        with open(colors_path, encoding="utf-8") as f:
            palette = json.load(f)

        def mix(name):
            a, b = name[:-2].split("..")
            if a not in palette or b not in palette:
                return None
            t = int(name[-1]) / 8
            return "#" + "".join(
                f"{round(int(palette[a][i:i + 2], 16) * (1 - t) + int(palette[b][i:i + 2], 16) * t):02x}"
                for i in (1, 3, 5)
            )

        def sub(m):
            name = m.group(3) or m.group(2)
            if ".." in name:
                hx = mix(name)
                return f'{m.group(1)}"{hx}" /*okaru:{name}*/' if hx else m.group(0)
            if name not in palette:
                return m.group(0)  # color que no es de la paleta (p. ej. ANSI crudo): se respeta
            return f'{m.group(1)}"{palette[name]}" /*okaru:{name}*/'
    else:
        def sub(m):
            # las mezclas no tienen nombre de fastfetch: se dejan con su hex (válido) y su marca
            if not m.group(3) or ".." in m.group(3):
                return m.group(0)
            return f'{m.group(1)}"{m.group(3)}"'

    new = PATTERN.sub(sub, text)
    if new == text:
        return 0
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".config.")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(new)
    os.chmod(tmp, os.stat(path).st_mode & 0o777)
    os.replace(tmp, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
