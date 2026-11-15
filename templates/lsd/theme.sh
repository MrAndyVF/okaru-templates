#!/bin/sh
# lsd solo lee colors.yaml con `color: theme: custom` en config.yaml.
dir="${XDG_CONFIG_HOME:-$HOME/.config}/lsd"
config="$dir/config.yaml"
ours='# OKARU: creado por la plantilla lsd para usar colors.yaml.'
case "$1" in
apply)
    if [ ! -e "$config" ]; then
        printf '%s\ncolor:\n  theme: custom\n' "$ours" > "$config.tmp.$$" && mv -f "$config.tmp.$$" "$config"
    elif ! grep -Eq '^[[:space:]]+theme:[[:space:]]*custom' "$config"; then
        echo "Warning: set 'color: theme: custom' in $config so lsd uses the OKARU colors" >&2
        exit 1
    fi
    ;;
undo)
    # Solo se borra el config.yaml que creó esta plantilla y que nadie editó.
    if [ -f "$config" ] && [ "$(cat "$config")" = "$(printf '%s\ncolor:\n  theme: custom' "$ours")" ]; then
        rm -f -- "$config"
    fi
    rm -f -- "$dir/colors.yaml"
    ;;
esac
