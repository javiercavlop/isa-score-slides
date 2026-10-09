# Ejemplo: SPARK (oct. 2026)

Presentación de referencia hecha con este sistema tras las correcciones del autor (más visual, más animada, portada del grupo, biblioteca reutilizada, arquitecturas con formas, animaciones en el .pptx).

- `deck/project/deck.json` + `deck/project/slides/*.html`: el deck de Claude Slides (64 diapositivas). Úsalo como modelo de densidad visual, `data-build-in` (un `order` por pieza, flechas animadas en su sentido) y `data-transition="magic"` con `id` estables.
- `assets/`: sus imágenes; `assets.json` relaciona cada `/_blob/<id>` con su fichero.
- `map.json`: portada y cierre reales, `agenda-arc` ×4 (con `timing_from`), `pricing-table-build` y `curse-of-customization`.

Reproducirlo:

```bash
python3 ../../kit/slides_to_pptx.py deck SPARK.pptx --assets assets --map map.json --node node_modules --work work
```

El encargo original está resumido en `../../references/encargo-plantilla.md`.
