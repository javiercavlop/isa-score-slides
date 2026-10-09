---
name: isa-score-presentacion
description: Prepara presentaciones académicas con el estilo del ISA Research Group / SCORE Lab (Universidad de Sevilla) a partir de un contexto y una descripción breve, y las entrega como PowerPoint nativo con Morph y animaciones, más un deck de Claude Slides para revisar. Úsala cuando pidan una charla, presentación, slides o diapositivas del grupo ISA, SCORE, I3US o de la Universidad de Sevilla (congreso, PhD Forum, seminario, reunión de proyecto), o "con el sistema de diseño ISA · SCORE", y cuando pidan convertir un deck de Claude Slides o Claude Design a PowerPoint con animaciones.
---

# Presentaciones ISA · SCORE

Convierte un encargo (contexto + descripción breve + fuentes) en una presentación del grupo que ya cumple, sin que nadie lo pida, todo lo que el autor exige: muchísimo más visual, animada, con la portada, el cierre y la biblioteca reales, arquitecturas con formas nativas, sin límite de diapositivas y entregada como .pptx nativo con animaciones.

Rutas: `${CLAUDE_SKILL_DIR}` es la carpeta de esta skill (en chat, rutas relativas a este fichero).

| Carpeta | Contenido |
| --- | --- |
| `references/00-reglas-obligatorias.md` | **Las reglas que mandan sobre todo.** Léelas enteras antes de diseñar. |
| `references/lecciones-y-recetas.md` | **Lo aprendido en charlas reales**: errores que ya ocurrieron, dónde inspirarse, detalles de Slides y de la conversión, verificación, tono. |
| `references/encargo-plantilla.md` | Qué datos hacen falta y cómo se piden. |
| `references/fuentes/INDICE.md` + `references/fuentes/<deck>-NN.jpg` | Índice diapositiva a diapositiva de las 7 charlas (transición, animaciones, componente) y sus miniaturas numeradas. |
| `references/sistema-de-diseno-README.md`, `slide-patterns.md`, `component-library.md`, `motion.md`, `pptx-workflow.md`, `tokens.json`, `logos.md` | Copia del sistema de diseño (marca, patrones, biblioteca, movimiento, producción). En esas páginas, `kit/…pptx.b64.txt` corresponde aquí a `kit/…pptx` (ficheros reales). |
| `kit/` | `isa_deck.py` (kit), `slides_to_pptx.py` (Slides → .pptx), `slides_cascade_fix.py` (un paso por pieza en las cascadas de Slides), `verify_pptx.py` (comprobación + hoja de miniaturas), `optimize_pptx.py`, `build_library.py`, `build_showcase.py`, `isa-score-template.pptx` (portada y cierre reales), `ISA-SCORE_showcase.pptx` (ejemplo), `library/` (46 componentes originales sin pérdidas + `catalog.json`). |
| `sources/` | Las 7 presentaciones originales del grupo (CAiSE'26, CAiSE'25, ICWE'25, JCIS, PhD Forum 2026, SCORE 2025, ICSOC'24) y capturas de Delivera. Solo lectura: material de referencia y origen de la biblioteca. |
| `examples/spark/` | Ejemplo completo y bueno: deck de Slides de 64 diapositivas, sus imágenes, `map.json`, `miniaturas.png` y `RECETARIO.md` (qué técnica usa cada diapositiva y recetas HTML para adaptarlas). |

Sistema de diseño publicado (vista previa, tokens, assets): https://claude.ai/artifact/GQ3oB24oKr1Kz7X31QoR63 («Presentaciones SCORE Lab - ISA Group»).

## Paso 0 — Revisar el encargo antes de nada

Lee `references/encargo-plantilla.md` y contrasta el encargo con él.

- **Imprescindible**: (1) tema y contexto (2–10 líneas: qué se presenta y por qué), (2) público/evento y duración, (3) ponente y coautores, (4) congreso o reunión y fecha. Si falta alguno, **pregunta** con AskUserQuestion (opciones concretas, una sola ronda, máx. 4 preguntas) antes de investigar o diseñar. Si nadie puede contestar (ejecución programada), usa el valor por defecto de la plantilla y dilo arriba en la respuesta.
- **Recomendado** (fuentes, mensajes clave, cautelas, secciones, capturas, enlaces): si falta, sigue con lo que haya y dilo en una línea.
- **Encargo mal planteado** — pregunta en vez de adivinar cuando: no hay contenido sustantivo («hazme una presentación de mi trabajo» sin más); piden otro estilo o marca distinta del grupo; piden afirmar resultados, cifras o validaciones que las fuentes no respaldan; el contenido es contradictorio; o piden relajar una regla obligatoria sin decirlo explícitamente (confirma). Explica en una frase por qué preguntas.
- No preguntes lo que las reglas ya fijan (si debe ser visual, si animar, si usar la biblioteca, cuántas diapositivas): la respuesta es siempre sí / las que hagan falta.

**Atajo — ya hay un deck** (enlace a un deck de Claude Slides/Design hecho con el sistema): lee el artefacto, descarga sus imágenes, revísalo contra la lista de comprobación de las reglas (propón las mejoras visuales o de animación que falten) y salta al Paso 5.

## Paso 1 — Cargar el sistema

1. Lee `references/00-reglas-obligatorias.md` entera, después `references/lecciones-y-recetas.md` y `references/sistema-de-diseno-README.md`. Consulta `component-library.md`, `slide-patterns.md` y `motion.md` cuando los necesites.
2. Prepara el kit en un directorio de trabajo: copia `kit/` (o trabaja desde `${CLAUDE_SKILL_DIR}/kit`; no escribas dentro de la skill). Dependencias: `pip install python-pptx lxml pillow` (y para el Camino C, `playwright` + Chromium y `npm i @fontsource/roboto @fontsource/roboto-condensed lucide-static`).

## Paso 2 — Contenido

Investiga y lee las fuentes dadas (papers, repos, documentación, URLs; usa la web si hace falta). Extrae hechos exactos. **Nunca inventes resultados, cifras ni capacidades**; respeta las cautelas del encargo (valores ilustrativos, cosas no confirmadas…) y llévalas a las notas o a una etiqueta pequeña en la diapositiva.

## Paso 3 — Guion visual

1. Divide la charla en 3–5 secciones (agenda `agenda-arc`, una copia por sección) y cada sección en ideas.
2. Para cada idea elige **primero** la metáfora visual (catálogo en `00-reglas-obligatorias.md` §1) y después el texto (≤ 30 palabras). El guion hablado va a las notas.
3. Busca cada tema en `kit/library/catalog.json` y en `references/fuentes/INDICE.md`: si el grupo ya lo contó (pricing SaaS, espacio de configuración, curse of customization, DevOps, feature toggles, arquitectura por capas, QACO→PACO, iPricing, trabajo futuro…), usa el componente o importa esas diapositivas (`import_slides`). Para lo nuevo, inspírate en las miniaturas de las charlas (ábrelas con Read) y en `examples/spark/RECETARIO.md`.
4. Convierte cada idea en una **secuencia** de diapositivas físicas con Morph (mismo número lógico). Sin límite de diapositivas.
5. Si la charla dura más de 15 min, enseña el esquema (secciones → ideas → metáfora/componente, una línea cada una) y pide visto bueno antes de construir; si el usuario no está, sigue.

## Paso 4 — Construir

**Opción por defecto (con revisión visual):** deck de Claude Slides + conversión a .pptx (Camino C).
- Crea el deck desde el tipo Slides con el sistema de diseño «Presentaciones SCORE Lab - ISA Group» y sigue las instrucciones del tipo. Parte de las recetas de `examples/spark/RECETARIO.md` (copia la estructura HTML de la diapositiva equivalente y adáptala) y de `references/lecciones-y-recetas.md` §3.
- Portada y cierre con la composición de `00-reglas-obligatorias.md` §4. Los logos se copian como assets (`references/logos.md`), nunca como ficheros.
- Cascadas con un `order` por pieza (pasa `kit/slides_cascade_fix.py` sobre las diapositivas antes de convertir); todas las flechas con build-in en su sentido; `id` estable en todo lo que haga Morph; nada con coordenadas negativas; un elemento por tamaño de letra.
- Las diapositivas que cubrirá un componente de biblioteca se maquetan parecidas (para revisar) y se sustituyen en la conversión.

**Sin tipo Slides disponible:** Camino A directamente con `isa_deck.py` (`references/pptx-workflow.md`).

## Paso 5 — PowerPoint nativo

Escribe `map.json` (formato en `references/pptx-workflow.md`, Camino C; ejemplo en `examples/spark/map.json`): portada y cierre reales (`title_slide`, `closing_slide`), y cada componente de biblioteca con `covers`, `notes`, `replacements` y `timing_from` para las copias de la agenda. Descarga las imágenes del deck a una carpeta de assets y ejecuta:

```bash
python3 ${CLAUDE_SKILL_DIR}/kit/slides_to_pptx.py DECK_DIR salida.pptx --assets ASSETS_DIR --map map.json --node node_modules --work work/
```

Nunca entregues el PPTX exportado desde Claude Slides: no lleva transiciones ni animaciones.

## Paso 6 — Verificar y entregar

1. `python3 ${CLAUDE_SKILL_DIR}/kit/verify_pptx.py salida.pptx --expect N --sheet hoja.png`: sin diapositivas de contenido estáticas, cada Morph con nombres en común con la anterior, nº de diapositivas = deck. Abre la hoja de miniaturas con Read y revisa composición y textos.
2. Pasa la lista de comprobación final de `00-reglas-obligatorias.md`.
3. Entrega el .pptx (y el enlace al deck). En la respuesta: 2–4 frases, qué se cumple de la lista, qué falta o se asumió, y que Morph solo se ve en PowerPoint ≥ 2019 / 365.

## Mantenimiento de la biblioteca

Para añadir componentes de una charla nueva: copia su .pptx a `sources/` (o una carpeta de trabajo), añade la entrada a `CATALOG` en `kit/build_library.py` y ejecuta `python3 build_library.py SOURCES_DIR library/` (sin pérdidas; `--optimize` recomprime medios para el almacén del sistema de diseño). Las imágenes de `sources/` y `kit/library/` son originales: no las optimices dentro de la skill.
