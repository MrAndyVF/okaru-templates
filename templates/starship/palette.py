#!/usr/bin/env python3
"""Mantiene la paleta okaru en starship.toml.

apply: pone `palette = "okaru"` y la tabla [palettes.okaru] (entre marcas) desde la salida de la plantilla.
undo: quita la tabla y devuelve `palette` a como estaba. Nunca escribe un TOML que no se pueda leer.
"""
import os, re, sys, tempfile, tomllib

config = os.environ.get("STARSHIP_CONFIG") or os.path.join(
    os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config"), "starship.toml")
rendered = os.path.join(os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache"),
                        "okaru", "starship-palette.toml")
BEGIN, END = "# >>> okaru: paleta (generada, no editar)", "# <<< okaru: paleta"
PALETTE_LINE = re.compile(r'^palette\s*=\s*"([^"]*)"[^\n]*\n?', re.M)
PREVIOUS = re.compile(r'#\s*okaru, antes: "([^"]*)"')


def strip_palette(text):
    """Quita el bloque marcado y cualquier [palettes.okaru] suelto (de versiones anteriores)."""
    text = re.sub(rf"\n*{re.escape(BEGIN)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S)
    return re.sub(r"(?ms)^\[palettes\.okaru\]\n.*?(?=^\[|\Z)", "", text)


def main():
    if not os.path.isfile(config):
        return 0  # sin starship.toml no hay prompt que tematizar
    with open(config, encoding="utf-8") as f:
        original = f.read()
    try:
        tomllib.loads(original)
    except tomllib.TOMLDecodeError as e:
        print(f"Warning: {config} is not valid TOML, not changed: {e}", file=sys.stderr)
        return 1
    text = strip_palette(original).rstrip("\n") + "\n"
    current = PALETTE_LINE.search(text)

    if sys.argv[1:] == ["apply"]:
        with open(rendered, encoding="utf-8") as f:
            block = f.read().strip("\n")
        if current is None or current.group(1) != "okaru":
            previous = f'  # okaru, antes: "{current.group(1)}"' if current else "  # okaru"
            line = f'palette = "okaru"{previous}\n'
            # Clave de primer nivel: tiene que ir antes de la primera tabla.
            text = PALETTE_LINE.sub(line, text, count=1) if current else line + text
        text += f"\n{BEGIN}\n{block}\n{END}\n"
    elif current is not None and current.group(1) == "okaru":
        before = PREVIOUS.search(current.group(0))
        text = text.replace(current.group(0), f'palette = "{before.group(1)}"\n' if before else "", 1)

    if text == original:
        return 0
    tomllib.loads(text)  # nunca dejar un starship.toml roto
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(config), prefix=".starship.")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(tmp, os.stat(config).st_mode & 0o777)
    os.replace(tmp, config)
    return 0


if __name__ == "__main__":
    sys.exit(main())
