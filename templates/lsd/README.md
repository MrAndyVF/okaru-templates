# lsd

**EN** — Writes `~/.config/lsd/colors.yaml` from the palette (permissions, sizes, dates, git status…). lsd only
reads it with `color: theme: custom`: when you have no `config.yaml`, one with just that setting is created;
when you have your own, it is never edited and Settings shows a warning until you add the setting. Disabling the
template removes `colors.yaml` and the `config.yaml` it created (only if you did not change it).

**ES** — Escribe `~/.config/lsd/colors.yaml` desde la paleta (permisos, tamaños, fechas, estado de git…). lsd
solo lo lee con `color: theme: custom`: si no tienes `config.yaml` se crea uno con solo ese ajuste; si tienes el
tuyo no se edita nunca y Ajustes muestra un aviso hasta que lo añadas. Al desactivar la plantilla se borran
`colors.yaml` y el `config.yaml` que creó (solo si no lo cambiaste).
