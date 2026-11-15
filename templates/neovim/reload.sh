#!/bin/sh
# Recarga el tema en cada Neovim abierto que use okaru (sockets nvim.<pid>.<n> de Neovim 0.9+).
command -v nvim >/dev/null 2>&1 || exit 0
for sock in "${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"/nvim.*; do
    [ -S "$sock" ] || continue
    timeout 2 nvim --server "$sock" --remote-expr \
        "execute('if get(g:, \"colors_name\", \"\") ==# \"okaru\" | colorscheme okaru | endif')" >/dev/null 2>&1 || true
done
