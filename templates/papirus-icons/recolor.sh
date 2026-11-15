#!/bin/sh
# Recolorea las carpetas de los temas Papirus del usuario con papirus-folders. Nunca usa sudo: los temas del
# sistema (/usr/share/icons) no se tocan.
icons="${XDG_DATA_HOME:-$HOME/.local/share}/icons"
state="${XDG_CACHE_HOME:-$HOME/.cache}/okaru/papirus-folder-applied"
action="$1"
color="$2"
mode="$3"

# Con un tema Papirus elegido, la variante sigue al modo claro/oscuro; otro tema de iconos no se toca.
if [ "$action" = apply ] && command -v gsettings >/dev/null 2>&1; then
    current="$(gsettings get org.gnome.desktop.interface icon-theme 2>/dev/null | tr -d "'")"
    case "$current" in
    Papirus | Papirus-Dark | Papirus-Light) base=Papirus ;;
    ePapirus | ePapirus-Dark) base=ePapirus ;;
    *) base="" ;;
    esac
    if [ -n "$base" ]; then
        if [ "$mode" = dark ]; then wanted="$base-Dark"; elif [ "$base" = Papirus ]; then wanted=Papirus-Light; else wanted=ePapirus; fi
        [ "$current" = "$wanted" ] || gsettings set org.gnome.desktop.interface icon-theme "$wanted"
    fi
fi

if ! command -v papirus-folders >/dev/null 2>&1; then
    [ "$action" = apply ] && echo "Warning: install papirus-folders to recolor the Papirus folders" >&2
    exit 0
fi

mkdir -p "$(dirname "$state")"
found=0
for theme in Papirus Papirus-Dark Papirus-Light ePapirus ePapirus-Dark; do
    [ -d "$icons/$theme" ] && [ -w "$icons/$theme" ] || continue
    found=1
    if [ "$action" = apply ]; then
        # papirus-folders reescribe miles de enlaces: solo si el color cambió. --once: no escribe su config
        # del sistema (/var/lib/papirus-folders); el estado propio va en la caché del usuario.
        [ "$(cat "$state.$theme" 2>/dev/null)" = "$color" ] && continue
        papirus-folders --once -C "$color" -t "$theme" >/dev/null && printf '%s\n' "$color" > "$state.$theme"
    else
        papirus-folders --once -D -t "$theme" >/dev/null
        rm -f -- "$state.$theme"
    fi
done

if [ "$found" = 0 ] && [ "$action" = apply ]; then
    echo "Warning: no Papirus theme in $icons; copy it there to recolor the folders without root" >&2
fi
exit 0
