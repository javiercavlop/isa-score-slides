# Producir el PowerPoint (con animaciones)

> **OBLIGATORIO, siempre y en todo momento:** antes de usar esta página, lee y cumple [`00-reglas-obligatorias.md`](00-reglas-obligatorias.md). Toda presentación es **muchísimo más visual** (≤ 30 palabras y una metáfora visual por diapositiva), **dinámica** (cada diapositiva se construye animada, Morph entre copias), **reutiliza la biblioteca y la portada reales**, dibuja las **arquitecturas con formas nativas**, no ahorra diapositivas y se entrega como **.pptx nativo con animaciones** (nunca el PPTX exportado de Claude Slides). Solo el autor puede relajar una regla, y de forma explícita.

El producto final de este sistema es un **.pptx 16:9** que se abre en PowerPoint con sus transiciones Morph y animaciones intactas. Hay tres caminos; todos usan los ficheros guardados aquí. **La exportación PPTX de Claude Slides no escribe transiciones ni animaciones**: si el deck se diseñó allí, usa el Camino C.

| Fichero | Qué es |
| --- | --- |
| `kit/isa_deck.py` | Biblioteca Python (python-pptx + lxml) que construye diapositivas con los patrones y escribe transiciones/animaciones en OOXML nativo. También es un CLI para animar cualquier .pptx y para restaurar las plantillas. |
| `kit/isa-score-template.pptx.b64.txt` | La plantilla .pptx en base64 (el almacén del sistema sólo sirve tipos web): tema *isa-v2* (paleta "Colores Cristina", Arial Narrow), maestro con sus 19 layouts, **la portada y el cierre reales con placeholders `{{…}}`** (diapositivas 1 y 2) y una diapositiva oculta con los logos. |
| `kit/library/<id>.pptx.b64.txt` | Los 46 componentes de la biblioteca (diapositivas originales con Morph y animaciones). Índice: `kit/library/catalog.json`; guía: `component-library.md`. |
| `kit/build_showcase.py` | Ejemplo completo que genera `ISA-SCORE_showcase.pptx`: portada y cierre reales, un caso de cada patrón y efecto y dos componentes de biblioteca. |
| `kit/ISA-SCORE_showcase.pptx.b64.txt` | El resultado del ejemplo (27 diapositivas), en base64. Capturas en `assets/Examples`. |
| `kit/build_library.py` | Cómo se extrajo la biblioteca de las presentaciones fuente (para añadir componentes nuevos de futuras charlas). |
| `kit/slides_to_pptx.py` | Camino C: convierte un deck de Claude Slides en .pptx nativo con Morph, animaciones, portada/cierre reales y componentes de biblioteca. |
| `kit/optimize_pptx.py` | Recomprime los medios de un .pptx (o de sus copias `.b64.txt`) a 2× su tamaño visible, sin tocar formas ni animaciones. Obligatorio antes de subir un .pptx al sistema. |

Descarga los ficheros de `kit/` al mismo directorio, con los de la biblioteca que vayas a usar en una subcarpeta `library/` junto a `catalog.json` (`read` con `paths`, en tandas de < 64 MB; ver "Almacenamiento"). `Deck()` decodifica la plantilla automáticamente si encuentra `isa-score-template.pptx.b64.txt` a su lado; para obtener los .pptx a mano: `python isa_deck.py --restore isa-score-template.pptx.b64.txt` (escribe `isa-score-template.pptx`, que también se puede abrir y usar directamente en PowerPoint como plantilla). Requisitos: `pip install python-pptx lxml`. Fuentes en el equipo que proyecta: Roboto (y Barlow si se usa `alt`); Arial Narrow y Calibri vienen con Office.

## Camino A — generar con el kit (recomendado)

```python
from isa_deck import Deck, find_shape
d = Deck("isa-score-template.pptx")

# 1. SIEMPRE la portada real (rellena sus placeholders)
d.title_slide("Paper title", authors=[("Presenter Name", True), "Co-author"],
              affiliation="SCORE Lab, I3US, Universidad de Sevilla, Seville, Spain",
              venue="CAiSE'26", date="10th June 2026")

# 2. Componentes originales de la biblioteca (Morph + animaciones incluidos)
d.insert_component("agenda-arc", slides=[1], number=2,
                   replacements={"PROPOSAL": "APPROACH"})
d.insert_component("pricing-table-build", number=3)

s = d.content_slide("H.A.R.V.E.Y. Architecture", number=12)
a = d.card(s, 0.8, 1.6, 3.6, 4.6, "ACCESSIBILITY LAYER", style="blue")
b = d.card(s, 4.8, 1.6, 3.6, 4.6, "ORCHESTRATION LAYER", style="green")
c = d.card(s, 8.8, 1.6, 3.6, 4.6, "CAPABILITY LAYER", style="orange")
d.animate_sequence(s, [a, b, c], effect="wipe", direction="from_left", first="after", then="after")

s2 = d.build_step(s)                 # copia + Morph (mismo número lógico)
from isa_deck import apply_animations; apply_animations(s2, [])   # la copia no repite la entrada
d.spotlight(s2, 0.7, 1.5, 3.8, 4.8)  # marco que viajará en las siguientes copias

# 3. SIEMPRE el cierre real: correo, QR y financiación
d.closing_slide("Paper title", authors=[("Presenter Name", True), "Co-author"], email="name@us.es",
                venue="CAiSE'26", date="10th June 2026", qr_image="qr.png")
d.save("talk.pptx")
```

API principal (coordenadas en pulgadas):

- Portada y cierre reales: `title_slide(title, authors | presenter+coauthors, affiliation, venue, date)`, `closing_slide(..., email, qr_image=None, funding=True)` — duplican las semillas de la plantilla y sustituyen `{{TITLE}}`, `{{PRESENTER}}`, `{{COAUTHORS}}`, `{{AFFILIATION}}`, `{{VENUE}}`, `{{DAY}}{{DAY_SUFFIX}} {{MONTH_YEAR}}`, `{{EMAIL}}`; sin `qr_image` queda el hueco "QR placeholder".
- Biblioteca: `list_components(category)`, `component_texts(id)`, `insert_component(id, replacements, number, slides)`; de bajo nivel, `import_slides(prs, path, numbers)` copia diapositivas de CUALQUIER .pptx sin pérdidas (medios byte a byte, Morph, animaciones, SmartArt y, si hace falta, su maestro/tema/layouts originales) y `replace_text(slides, mapping)`.
- Marcos: `content_slide(title, number)`, `section_divider(text, number, accent_words)`, `agenda_slide(items, current, number)`, `closing_slide(...)`, `new_slide(layout)` para cualquier layout del maestro (`"two"`, `"compare"`, `"big_image"`, `"full_image"`, …).
- Piezas: `card`, `spotlight`, `focus_overlay`, `quote_card`, `stat_bubble`, `rq_row`, `numbered_circle`, `arrow`, `text`, `citation`, `slide_number`, `logo(slide, "score-logo", x, y, w)`.
- Dinámica: `build_step(slide)` (duplicar + Morph), `morph(slide, option, dur_ms)`, `fade(slide)`, `set_transition(slide, "none")`, `animate(slide, shape, effect, direction, trigger, delay, dur, cls)`, `animate_sequence(...)`, `move_offslide(shape, side)`, `hide(slide, shape)`.
- Efectos: `ENTRANCE_EFFECTS` = appear, fade, dissolve, wipe, zoom, float_in, rise_up, fly_in, peek_in, blinds, split, checkerboard, circle; salidas (`cls="exit"`): disappear, dissolve, fade, wipe, zoom. Direcciones: from_left, from_right, from_top, from_bottom.

## Camino B — animar un .pptx ya hecho (p. ej. exportado desde Claude Design)

Las exportaciones a PowerPoint de otras herramientas no incluyen Morph ni animaciones. Añádelas por **nombre de forma**:

```json
{"slides": {
  "4": {"transition": {"kind": "morph", "option": "byObject"}},
  "5": {"transition": {"kind": "morph", "dur_ms": 2000},
        "animations": [
          {"shape": "Layer access", "effect": "wipe", "direction": "from_left", "trigger": "after"},
          {"shape": "Layer orch",   "effect": "wipe", "direction": "from_left", "trigger": "after"},
          {"shape": "Key message",  "effect": "rise_up", "trigger": "click"}]}}}
```

`python isa_deck.py talk.pptx spec.json talk-animated.pptx` — las claves de diapositiva son posiciones 1-based. Para que Morph funcione en el camino B, las copias de una secuencia deben compartir nombres de forma (en Claude Design: duplica la diapositiva y cambia sólo lo que se mueve).

## Camino C — de un deck de Claude Slides a .pptx nativo

Para decks diseñados en Claude Slides (artefacto de tipo Slides con `project/deck.json` + `project/slides/*.html`). El conversor renderiza cada diapositiva en Chromium, mide cada elemento y lo redibuja como forma, texto o imagen **editable** sobre la plantilla del grupo; traduce `magic` a Morph (nombres `!!id`), `fade` a Fade y cada `data-build-in` a su animación nativa (tabla en `00-reglas-obligatorias.md`, §6). Los iconos y SVG se rasterizan a 2×; las notas (`<aside>`) pasan a notas del orador.

```bash
pip install python-pptx lxml playwright pillow && python -m playwright install chromium
npm i @fontsource/roboto @fontsource/roboto-condensed lucide-static     # fuentes e iconos para medir
python kit/slides_to_pptx.py DECK_DIR talk.pptx --assets ASSETS_DIR --map map.json --node node_modules
```

- `DECK_DIR`: carpeta con `project/` tal como la deja un `read` del deck. `ASSETS_DIR`: las imágenes del deck; cada `/_blob/<id>` se busca como `<id>.*` o en `ASSETS_DIR/assets.json` (`{"<id>": "fichero.png"}`).
- `map.json` sustituye diapositivas concretas por las **reales** del kit:

```json
{"title_slide":   {"slide": "cover", "title": "…", "authors": [["Presenter", true], "Co-author"], "venue": "…", "date": "…"},
 "closing_slide": {"slide": "closing", "title": "…", "authors": [["Presenter", true]], "email": "…", "qr_image": null, "funding": true},
 "components": [
  {"slide": "agenda1", "id": "agenda-arc", "slides": [1], "number": 2, "replacements": {"\t\tINTRODUCTION": "\t\tMOTIVATION"}},
  {"slide": "agenda2", "id": "agenda-arc", "slides": [2], "number": 8, "replacements": {…}, "timing_from": "agenda1"},
  {"slide": "pr-icons", "id": "pricing-table-build", "number": 5, "covers": ["pr-table", "pr-limits"], "notes": ["pr-icons", "pr-table", "pr-limits"]}]}
```

  `covers`: diapositivas del deck que el componente ya incluye (se omiten). `notes`: de qué diapositivas tomar las notas de cada copia. `timing_from`: reutiliza la línea de tiempo de otra copia del mismo componente (las copias 2–4 de `agenda-arc` no traen animaciones propias).
- Reglas del deck para que convierta bien: un `id` en todo lo que deba hacer Morph; cascadas con `order` distintos; nada con coordenadas negativas; textos con estilos en el elemento (no `<span>` con tamaño).
- Comprobación: mismo número de diapositivas que el deck, pares `!!` en cada diapositiva Morph, recuento de animaciones por diapositiva y render con LibreOffice. Morph solo se aprecia en PowerPoint.

## Almacenamiento del sistema (por qué `.b64.txt` y cómo no llenarlo)

El almacén de ficheros del sistema solo sirve tipos web, así que cada .pptx se guarda en base64 (+33 %). Límites que afectan: **64 MB por publicación y por lectura**, 16 MB por fichero de texto, 256 MB por versión. Hasta oct. 2026 la biblioteca y el showcase se guardaban sin pérdidas y ocupaban **≈ 79 MB** (capturas y personajes de 2–3 k px que se muestran a ~600 px): no cabían en una sola lectura ni publicación, y por eso hubo que pasarlos en .zip. Tras `optimize_pptx.py` ocupan **≈ 24 MB** (todo `kit/` ≈ 26 MB) con el mismo aspecto en pantalla.

- Antes de subir cualquier .pptx (componente nuevo, showcase, plantilla): `python kit/optimize_pptx.py fichero.pptx` (o `--b64` sobre las copias). `build_library.py` ya lo hace.
- Objetivo: cada componente ≤ 3 MB en base64; todo `kit/` < 40 MB para que se lea y publique en una sola llamada.
- Para descargar el kit: `read` con `paths` en tandas de < 64 MB (p. ej. kit + componentes que vayas a usar, no toda la biblioteca).
- La plantilla no se optimiza: su diapositiva oculta de logos se reutiliza a otros tamaños con `d.logo(...)`.

## Reglas al diseñar en Claude Design para luego exportar

- Lienzo 1920 × 1080; tokens en px de `tokens.json` (1 pt = 2 px).
- Construye cada idea como varias diapositivas duplicadas con un cambio cada una; pon el mismo número lógico en todas.
- Da a cada objeto que se anima un nombre claro (lo usa el `spec.json`).
- Portada y cierre: parte de las imágenes `assets/Examples/template-*-placeholders.png` y respeta su composición; en la exportación final se sustituyen por las semillas reales con `title_slide` / `closing_slide`, o se rellenan a mano en `isa-score-template.pptx`.
- Si una secuencia existe en la biblioteca, no la rediseñes: deja una diapositiva marcadora con su `id` y sustitúyela con `insert_component` al exportar.

## Comprobación

- Abre el .pptx en PowerPoint ≥ 2019 / Microsoft 365 (Morph). En versiones antiguas o Google Slides, Morph cae a Fade automáticamente; las animaciones de entrada se conservan en PowerPoint y Keynote.
- LibreOffice muestra las animaciones pero no Morph.
- `python -c "from pptx import Presentation; Presentation('talk.pptx')"` para validar que abre.
