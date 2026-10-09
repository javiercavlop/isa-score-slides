# Lecciones aprendidas y recetas

Conocimiento práctico que **no** está (o no está tan claro) en el sistema de diseño: lo que falló al hacer presentaciones reales y cómo se resolvió. Léelo junto a `00-reglas-obligatorias.md`; cuando haya conflicto, mandan las reglas.

## 1. Dónde inspirarse antes de diseñar

| Necesito… | Mira |
| --- | --- |
| Ver cómo cuenta el grupo un tipo de idea | `references/fuentes/INDICE.md` (cada diapositiva de las 7 charlas, con transición, animaciones y componente) + miniaturas `references/fuentes/<deck>-NN.jpg` (ábrelas con Read) |
| Una solución ya resuelta y adaptable en Claude Slides | `examples/spark/RECETARIO.md` (64 diapositivas: qué metáfora/técnica usa cada una, recetas HTML) + `examples/spark/miniaturas.png` |
| Reutilizar diapositivas originales con su animación | `kit/library/catalog.json` → `d.insert_component(id)`; cualquier otra diapositiva fuente → `import_slides(d.prs, "sources/<deck>.pptx", {n})` |
| Saber cómo se mueve algo | `references/motion.md` (técnicas Morph 1–9 con el componente que las muestra) |

Secuencias de las charlas que **no** están en la biblioteca y conviene importar o adaptar en vez de rehacer (números de diapositiva reales; detalle en el índice):

| Tema | Dónde |
| --- | --- |
| *User-oriented pricings* → complejidad → espacio de configuración (variante AGF, con Morph) | CAiSE'25 4–12 · ICWE'25 4–9 · JCIS 4–10 · PhD Forum 13 |
| iPricing, A-MINT y PRIME (herramientas del grupo) · ciclo de Pricing Intelligence | CAiSE'26 15–17 · 19 |
| Pricing4SaaS, Pricing2Yaml, iPricing (4:3, `x_offset=1524000`) · resultados y «extracción ideal» con Morph | ICSOC'24 13–17 · 34–42 |
| QACO *servitization* y sus limitaciones (pricing, mono/multi-configuración) · PACO | SCORE 2025 13–28 · 33–35 |
| Metamodelos iPricing / iSubscription · SPACE · PRIME y HARVEY | PhD Forum 26–28 · 39 · 44–51 |
| Una pregunta de investigación desarrollada en secuencia Morph | JCIS 22–27 (RQ1), 33–36 (RQ2–RQ3) |
| *Pricing-driven self-adaptation* | ICWE'25 14–15 · PhD Forum 38 |

## 2. Errores que ya ocurrieron (no repetir)

| Síntoma | Causa | Cómo se evita |
| --- | --- | --- |
| «Mucho texto, pocas metáforas visuales» | Se escribió el contenido antes de pensar la imagen | Metáfora primero (§1 de las reglas), ≤ 30 palabras, guion en `<aside>` |
| Las piezas de una cascada aparecen todas a la vez | En Slides, mismo `order` = mismo paso, aunque lleven `auto` | Un `order` por pieza; `kit/slides_cascade_fix.py` lo arregla en bloque |
| Flechas y agenda sin animar | Se animaron cajas pero no conectores | Todo `x-connector` lleva build-in en su sentido (`left/right/drop/rise`) |
| «Las animaciones no están» en el .pptx descargado | La exportación PPTX de Slides no escribe `p:transition` ni `p:timing` | Siempre Camino A o C; comprobar con `kit/verify_pptx.py` |
| El magic move «no se ve» en Slides | Solo se reproduce en modo Presentar y se desactiva con «reducir movimiento» del sistema | Comprobar el movimiento en el .pptx, no en el editor |
| Copias 2–4 de la agenda sin animación | El componente original solo anima la primera copia | `timing_from` en `map.json` (o copiar `<p:timing>` de la copia 1: mismos ids) |
| Etiqueta de agenda partida en dos líneas | El marco original es estrecho | ≤ 22 caracteres por sección («OPENBINDING & BIM», no «OPENBINDING AND BIM V1») |
| Hueco vacío del QR en el cierre | La semilla trae «QR placeholder» | Sin QR, el conversor lo elimina; con QR, `qr_image="qr.png"` |
| Copiar logos del sistema de diseño falla (*source artifact has no file*) | Son assets subidos, no ficheros | Copia por `asset_ids` (`references/logos.md`); en el .pptx ya van en la plantilla |
| Texto con `<span style="font-size…">` rechazado | Claude Slides no admite tamaños dentro de un texto | Un elemento por tamaño de letra |
| Piezas aparcadas fuera del lienzo desaparecen al convertir | Coordenadas negativas se omiten | No aparcar fuera; entrar con Wipe/Fly In |
| Primera diapositiva de un componente con Morph «sin pareja» | Conserva la transición que tenía en su charla original | Es inocuo (equivale a un fundido); `verify_pptx.py` lo marca para revisarlo |
| Vista previa del sistema de diseño con imágenes rotas | Un `namespace` en el índice sin `components/bundle.js` vuelve estáticas las vistas previas | No declarar `namespace` si no hay bundle |
| El kit/biblioteca no cabía en una lectura del sistema de diseño | Límite de 64 MB por lectura/publicación; .pptx en base64 | En el sistema, medios optimizados (`optimize_pptx.py`); en esta skill, originales sin pérdidas |

## 3. Claude Slides: lo que hay que saber para que convierta bien

- Deck = `project/deck.json` (orden) + `project/slides/<id>.html` (una `<section>` por diapositiva, lienzo 1920 × 1080, estilos en línea, `position:absolute`).
- `data-transition` va en la diapositiva que **sale** (`fade`, `push`, `magic`); el conversor la escribe en la que **entra**, como PowerPoint.
- Magic/Morph empareja por `id` idéntico en diapositivas consecutivas → en el .pptx, nombre `!!id`. Da `id` a todo lo que deba moverse o mantenerse (título `ttl`, marcos, tarjetas).
- `data-build-in="efecto order N [auto]"` solo en hijos directos del `<section>`. Efectos: `fade`, `rise`, `drop`, `left`, `right`, `scale`, `pop`.
- Un paso es automático solo si **todas** sus piezas llevan `auto` (se dispara 520 ms después del anterior). Si el primer paso es todo `auto`, se reproduce al entrar.
- Las copias de una secuencia Morph no repiten build-ins: el movimiento lo hace Morph.
- Iconos: `<x-icon name="…">` (Lucide en la conversión); formas `<x-shape kind="…">`; conectores `<x-connector x1 y1 x2 y2 [route]>`.
- Notas: `<aside>` → notas del orador. Ahí van explicaciones, matices y cautelas.

## 4. Conversión a .pptx nativo (Camino C) — detalles

- `slides_to_pptx.py` renderiza en Chromium (Playwright) con Roboto/Roboto Condensed de `npm @fontsource/*` (Google Fonts puede estar bloqueado por el proxy) e iconos de `lucide-static`.
- Primitivas por elemento: caja, texto (con los saltos de línea medidos), imagen (`object-fit: contain`), SVG/icono rasterizado a 2×, forma, conector. Un elemento con varias primitivas se agrupa.
- Unidades: 1 px = 6350 EMU; tamaño de letra pt = px × 0,5. La fuente de títulos pasa a Arial Narrow; peso 300 → «Roboto Light».
- `map.json` (`references/pptx-workflow.md`): `title_slide`, `closing_slide` (`funding`, `qr_image`), `components` con `slides`, `number` (número lógico), `replacements` (las etiquetas de `agenda-arc` llevan dos tabuladores delante: `"\t\tINTRODUCTION"`), `covers`, `notes`, `timing_from`. Ejemplo completo: `examples/spark/map.json`.
- Las imágenes `/_blob/<id>` del deck se descargan a una carpeta (`read` del artefacto por id) con `assets.json` `{id: fichero}`.

## 5. Verificar antes de entregar

```bash
python3 kit/verify_pptx.py talk.pptx --expect 64 --sheet talk-sheet.png
```

Revisa: nº de diapositivas, que ninguna de contenido quede estática, que cada Morph comparta nombres con la anterior, y la hoja de miniaturas (ábrela con Read). Para renderizar con LibreOffice instala las fuentes (Roboto, Roboto Condensed; las .woff2 de @fontsource convertidas a TTF en `~/.fonts`). LibreOffice muestra animaciones pero **no** Morph: Morph solo se ve en PowerPoint ≥ 2019 / Microsoft 365 (en versiones antiguas y Google Slides cae a Fade).

## 6. Contenido y tono

- No sobredimensionar: nada de «resuelve», «garantiza», «óptimo» si las fuentes no lo demuestran. Valores de ejemplo → nota gris pequeña «Illustrative values» en la diapositiva y explicación en notas. Lo no confirmado se dice como tal.
- Arquitecturas: copiar estructura y nombres exactos de la documentación oficial (p. ej. la de OpenBinding), no inventar componentes.
- Capturas reales: grandes, borde fino `ink`, marco carmesí sobre la zona, tarjeta carmesí con el dato; si los datos son de ejemplo, decirlo.
- Número lógico: se repite en todas las copias de una secuencia; los componentes lo reciben con `number=`.
- Títulos en Title Case sin punto; siglas propias en mayúsculas; todo el texto visible en inglés.

## 7. Mantener esta skill

- Charla nueva buena → añádela a `sources/`, regenera `references/fuentes/` (miniaturas e índice) y, si tiene secuencias reutilizables, añádelas a `kit/build_library.py` y reconstruye la biblioteca.
- Un deck nuevo que guste → cópialo como `examples/<nombre>/` con su `map.json` y un `RECETARIO.md`.
- Lección nueva (algo que el autor tuvo que corregir) → una fila en la tabla del §2 y, si es una regla, en `00-reglas-obligatorias.md` del sistema de diseño.
