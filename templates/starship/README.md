# Starship

**EN** — Adds `palette = "okaru"` and a `[palettes.okaru]` table to `~/.config/starship.toml` (or
`$STARSHIP_CONFIG`), so the named colors of your prompt (`green`, `blue`, `purple`…) follow the palette. The
table lives between two marker comments and is rewritten on every palette change; nothing else in the file is
touched, and an invalid file is never written. Disabling the template removes the table and restores the
previous `palette` value. New prompts pick up the change immediately.

**ES** — Añade `palette = "okaru"` y una tabla `[palettes.okaru]` a `~/.config/starship.toml` (o a
`$STARSHIP_CONFIG`), así los colores con nombre del prompt (`green`, `blue`, `purple`…) siguen la paleta. La
tabla va entre dos comentarios de marca y se reescribe con cada cambio de paleta; el resto del archivo no se
toca y nunca se escribe un archivo inválido. Al desactivar la plantilla se quita la tabla y `palette` vuelve a su
valor anterior. Los prompts nuevos ya salen con el cambio.
