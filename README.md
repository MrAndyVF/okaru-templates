# OKARU (郁) · plantillas de la comunidad

Plantillas de color para [OKARU](https://github.com/MrAndyVF): cada una lleva la paleta activa de la shell a
otra aplicación (editores, navegadores, terminales, juegos…). OKARU lee `catalog.json` de este repo y
descarga solo las plantillas que actives en **Ajustes → Apariencia → Plantillas**.

## Aportar una plantilla

1. Crea `templates/<id>/` (id en minúsculas: letras, números, `.`, `_`, `-`).
2. Añade `template.toml`:

   ```toml
   [catalog.<id>]
   name = "Nombre visible"
   category = "editor" # ai, audio, browser, chat, compositor, editor, gaming, launcher, misc, system, terminal

   [templates.<id>]
   input_path = "<id>.json"            # archivo de entrada con los tokens de color
   output_path = "~/.config/app/theme.json"
   # post_hook = "./apply.sh"          # opcional
   ```

3. Añade los archivos que use y un `README.md` (qué hace, cómo activarla en la app, captura opcional).
4. Ejecuta `python3 tools/build_catalog.py` y sube `catalog.json` en el mismo pull request.

La GitHub Action comprueba que `catalog.json` esté al día y que cada plantilla tenga su `template.toml`.

## Licencia

MIT. Al enviar un pull request aceptas publicar tu plantilla bajo esta licencia; no subas trabajo de
terceros sin su permiso.
