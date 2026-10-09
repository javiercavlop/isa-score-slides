> **OBLIGATORIO, siempre y en todo momento:** antes de usar esta página, lee y cumple [`00-reglas-obligatorias.md`](00-reglas-obligatorias.md). Toda presentación es **muchísimo más visual** (≤ 30 palabras y una metáfora visual por diapositiva), **dinámica** (cada diapositiva se construye animada, Morph entre copias), **reutiliza la biblioteca y la portada reales**, dibuja las **arquitecturas con formas nativas**, no ahorra diapositivas y se entrega como **.pptx nativo con animaciones** (nunca el PPTX exportado de Claude Slides). Solo el autor puede relajar una regla, y de forma explícita.

Sistema de diseño para las charlas académicas del grupo **ISA / SCORE Lab (I3US, Universidad de Sevilla)**: congresos (CAiSE, ICWE, ICSOC, JCIS…), PhD Forum y seminarios. Se extrajo de siete presentaciones reales del grupo. El entregable final es siempre un **PowerPoint (.pptx) 16:9 con transiciones Morph y animaciones nativas**; el kit de este sistema (`kit/isa_deck.py` + `kit/isa-score-template.pptx.b64.txt`) lo genera. Lee primero `00-reglas-obligatorias.md` y después `slide-patterns.md`, `component-library.md`, `motion.md` y `pptx-workflow.md` antes de construir una presentación.

## Reglas fijas de toda presentación nueva (no negociables)

Detalle, recetas y comprobaciones en `00-reglas-obligatorias.md`, que manda sobre todo lo demás. Se aplican sin que el encargo las pida; solo el autor puede relajarlas, y de forma explícita.

1. **Muchísimo más visual.** Cada diapositiva es una metáfora visual (personaje, flujo, rejilla de candidatos, capas, hub, línea temporal, captura con marco…): ≤ 30 palabras visibles, ≥ 3 objetos visuales, un icono por concepto, cifras como objetos. El guion va en las notas, no en la diapositiva.
2. **Dinamismo en cada diapositiva.** Todo se construye delante del público: cascadas pieza a pieza (un paso por pieza), todas las flechas y conectores animados en su sentido, mensaje clave al final, Morph entre copias y agenda animada en cada sección. Solo efectos de entrada.
3. **Biblioteca antes que diseño nuevo.** Si el tema ya lo contó el grupo (pricing SaaS, espacio de configuración, curse of customization, DevOps, agenda, arquitectura por capas, trabajo futuro…), se insertan las diapositivas originales (`d.insert_component`) con sus animaciones, no una imitación.
4. **Portada y cierre reales del grupo** (TitleSlide y ClosingSlide): las semillas de la plantilla con placeholders `{{TITLE}}`, `{{PRESENTER}}`, `{{COAUTHORS}}`, `{{AFFILIATION}}`, `{{VENUE}}`, `{{DAY}}{{DAY_SUFFIX}} {{MONTH_YEAR}}` y, en el cierre, `{{EMAIL}}`, QR y financiación. No se redibujan: se rellenan (`d.title_slide(...)`, `d.closing_slide(...)`). En Claude Slides se reproduce su composición exacta (`00-reglas-obligatorias.md` §4).
5. **Arquitecturas con elementos nativos de PowerPoint**: capas pastel, cajas con icono y conectores editables, construidos con animación y recorridos con un spotlight que Morph desplaza. Nunca una imagen pegada ni una lista.
6. **El entregable es un .pptx nativo con Morph y animaciones** (Camino A o C de `pptx-workflow.md`), comprobado antes de entregar. La exportación PPTX de Claude Slides pierde transiciones y animaciones: nunca es el entregable final.
7. **No ahorres diapositivas.** Cada idea es una secuencia de copias con Morph y el mismo número lógico; 60–80 físicas para una charla de 30–40 min es lo normal.
8. Lo que no exista en la biblioteca se compone con los patrones de `slide-patterns.md` y las técnicas de `motion.md`, siempre dentro de las reglas 1–7.

## Principios

- **Blanco, carmesí y diagramas.** Todas las diapositivas son blancas (`surface`); el color de marca es el carmesí de la Universidad de Sevilla (`crimson`, `crimson-deep`). El contenido son diagramas, iconos, capturas y tablas de pricing, no viñetas.
- **Una idea por diapositiva lógica, construida en varias físicas.** Una idea se cuenta duplicando la diapositiva y cambiando un detalle en cada copia (aparece una pieza, se mueve un marco, se tacha una palabra) unidas con **Morph**. El número de diapositiva es *lógico*: se repite en todas las copias de la secuencia.
- **El movimiento explica.** Las animaciones revelan en el orden del razonamiento (Wipe desde la izquierda en flujos, Zoom para iconos y burbujas). Nada se anima por decorar.
- **Texto mínimo, grande y en inglés.** Las charlas son en inglés: títulos en *Title Case* sin punto final, frases cortas, siglas propias en mayúsculas (H.A.R.V.E.Y., PACO, QACO, iPricing). Preguntas retóricas como gancho ("What is the best subscription option…?").

## Fundamentos visuales

### Color

- Fondo siempre `surface`. Nunca diapositivas oscuras; para “oscurecer” se usa el velo `veil` sobre la diapositiva (patrón *Focus overlay*).
- Títulos en `crimson`. La banda del título de portada, los números de diapositiva, las flechas y las píldoras RQ en `crimson-deep` con texto `on-crimson`.
- Agenda y marcos de cita en `signal-red`. Marcos de foco (*spotlight*) en `crimson-deep` 2,25 pt (decks FJCL) o `alert-red` 3 pt (decks AGF).
- Diagramas de arquitectura por capas con la paleta pastel de draw.io: `card-blue` / `card-green` / `card-orange` (+ `-line`, `-ink`). Paneles de énfasis en `card-pink` y `card-rose`. Burbujas de datos en `stat-fill` con borde `amber`.
- Bucle DevOps y gráficos: `navy` + `green`; series secundarias `teal`, `sky`, `teal-deep`, `bronze`.
- Texto en `ink`; citas y pies en `ink-soft`; `muted` sólo para la línea de congreso/fecha de portada (≥24 px).

### Tipografía

- Títulos de diapositiva: `slide-title` — fuente de títulos del tema (**Arial Narrow** bold 28 pt, centrado, `crimson`). Los decks de AGF usan Roboto bold 32 pt para el mismo rol: ambas son válidas, pero no mezcles dentro de un deck.
- Cuerpo: **Roboto** (`body`, `body-lg`, `caption`). Alternativa de los decks FJCL: Barlow Semi Condensed (`alt`). Roboto y Barlow son Google Fonts: instálalas en el equipo que proyecta.
- Portada y cierre: **Calibri** (`band-title`, `authors`, `affiliation`, `venue`).
- Números: `stat-number` para cifras titulares, `point-number` (Roboto Light) para 01–04, `slide-number` abajo a la derecha.
- Tamaños: tokens en px sobre lienzo 1920×1080 (1 pt = 2 px). No bajes de 14 pt salvo en `citation` (9 pt).

### Composición

- Lienzo 16:9 (13,333 × 7,5 in). Título centrado arriba (`space-title-top`), márgenes laterales `space-edge`, contenido desde `space-content-top`.
- Número lógico abajo a la derecha (caja en x = 11 725 206 EMU, y = 6 396 335 EMU); referencia bibliográfica en `citation` abajo a la izquierda cuando la diapositiva usa trabajo publicado.
- Geometría mayoritariamente recta (`radius-none`); tarjetas de capa con `radius-card`; círculos con `radius-round`. Sin degradados, sin sombras decorativas, sin barras de acento.
- Imágenes: iconos planos de colores, ilustraciones de personajes (presentador, *decision-maker*) y capturas reales de páginas de pricing enmarcadas en negro o carmesí.

## Logos y afiliaciones (`assets/Logos`)

- Fila de portada y cierre, siempre en este orden: `isa-logo.jpeg` (izquierda), `score-logo.png` (centro), `us-logo.png` (derecha). Variantes: `us-seal.png` (sello circular del layout maestro), `i3us-logo.png` (PhD Forum), `score-us-lockup.jpeg` (lockup SCORE + US en una pieza).
- Financiación en la diapositiva de cierre, abajo a la derecha: `junta-andalucia.png` + `funding-ministerio-nextgen.png` (Ministerio de Ciencia, NextGenerationEU, PRTR, AEI).
- Nunca redibujes, recolorees ni recortes los logos; sobre blanco solamente.
- **Los logos, las capturas de `assets/Examples` y los fotogramas de `assets/Library` NO son ficheros del sistema**: son subidas de su almacén de assets (`/_blob/<id>`). Una copia por fichero (`files: {"…": {"artifact": <este sistema>, "path": "project/assets/Logos/isa-logo.jpeg"}}`) falla con *source artifact has no file*. Para llevarlos a un deck u otro artefacto, cópialos como assets: publish al artefacto destino con `asset: true`, `from_url` = este sistema y `asset_ids` = los ids de `assets/Logos/README.md` (o de `assetGroups` en `design-system.json`), y referencia la URL `/_blob/<id>` que devuelve. Para usarlos en local: `read` con el id como `path`. En el .pptx no hace falta: van dentro de la plantilla (`d.logo(...)`).

## Biblioteca de componentes

46 secuencias originales del grupo, agrupadas en *Library · Apertura / Agenda / Pricing / Procesos / Arquitectura / Evaluación / Cierre*, con vista previa animada paso a paso y fotogramas en `assets/Library`. Las más reutilizables: `pricing-table-build` (iconos → tabla BASIC/PRO/BUSINESS → límites → add-on → espacio de configuración), `curse-of-customization`, `devops-to-pricing-driven`, `agenda-arc`, `architecture-spotlight`, `rotating-wheel` (rueda de *future work* que gira), `segment-wheel-build`, `pyramid-levels`, `stat-split-panels`, `chevron-steps`. Índice completo en `component-library.md` y `kit/library/catalog.json`.

## Patrones de diapositiva

Para contenido nuevo, catálogo con geometría y animación en `slide-patterns.md`; cada uno tiene su componente con vista previa: **TitleSlide**, **AgendaArc**, **StatementSlide**, **ContentSlide**, **LayerCards**, **SpotlightBuild**, **FocusOverlay**, **StatBubbles**, **ResearchQuestions**, **NumberedPoints**, **ClosingSlide** y **MotionCatalogue**. Estructura típica de una charla (≈ 45–57 diapositivas físicas para 15–20 lógicas):

1. TitleSlide → 2. gancho (`hook-pricing-question`, `quote-hook`, StatementSlide) → 3. agenda (`agenda-arc`, actual = 1) → motivación (`pricing-table-build`, `curse-of-customization`, `devops-to-pricing-driven`) → agenda (actual = 2) → propuesta (`layers-zoom`, `architecture-spotlight`, SpotlightBuild + FocusOverlay) → agenda (actual = 3) → evaluación (`rq-cards`, `methodology-funnel`, `stat-split-panels`, `results-table`) → conclusiones y trabajo futuro (`rotating-wheel`, `chevron-steps`, `numbered-points-0104`) → ClosingSlide (correo + QR + financiación).

## Movimiento

Resumen; detalle, XML y reglas en `motion.md`:

- **Transición principal: Morph *by object*** (≈ 50 % de las diapositivas), con *Fade* como alternativa automática para quien no tenga Morph. Duraciones: `spd="slow"`; 2000 ms para morphs amplios; 50 ms para un “corte morph” que conserva los objetos.
- **Corte seco (sin transición)** en el resto: portada, cambios de sección y diapositivas sin objetos comunes. Fade, Split o Wipe sólo de forma excepcional.
- **Animaciones en diapositiva** más usadas: Wipe (sobre todo desde la izquierda), Zoom, Appear, Dissolve, Float In, Rise Up. Los disparadores *After Previous* y *With Previous* encadenan revelados; el clic marca los pasos del discurso.

## Producción en PowerPoint

Sigue `pptx-workflow.md`. En corto: genera con `kit/isa_deck.py` sobre la plantilla `kit/isa-score-template.pptx.b64.txt` (un .pptx en base64 que el kit decodifica solo; maestro *isa-v2* con sus 19 layouts y los logos incrustados), o añade Morph y animaciones a un .pptx exportado con `python kit/isa_deck.py deck.pptx spec.json`. Los componentes de biblioteca se insertan con `d.insert_component(...)` desde `kit/library/`. `kit/ISA-SCORE_showcase.pptx.b64.txt` es un ejemplo completo (portada y cierre reales, patrones, dos componentes de biblioteca); sus capturas están en `assets/Examples`.

## Autoría y licencia

Autores: **Francisco Javier Cavero López** y **Alejandro García Fernández**, de SCORE Lab (I3US, Universidad de Sevilla) y del Grupo ISA. El diseño original busca evocar la estética y el estilo visual de las presentaciones del ISA Research Group (Universidad de Sevilla), que se toman como referencia e inspiración visual. El texto completo está en `LICENSE`.

| Qué | Condiciones |
| --- | --- |
| **El sistema de diseño**: documentación, tokens, componentes y vistas previas, kit, plantilla, showcase, biblioteca de componentes y capturas | **CC BY 4.0**. Reproducirlo, modificarlo, adaptarlo o redistribuirlo, también en versiones derivadas (otro sistema, plantilla, kit o biblioteca basados en este), exige reconocer la autoría original, incluir una referencia a la licencia y señalar los cambios realizados. |
| **Las presentaciones generadas** con el sistema (diapositivas, .pptx, .pdf y presentaciones finales) | **Autorización adicional de los autores**: pueden usarse, modificarse, publicarse y distribuirse libremente, incluso con fines comerciales, **sin atribución**. No hace falta poner créditos, referencias a SCORE Lab ni menciones a CC BY 4.0 en las diapositivas ni en los documentos exportados. |
| **El contenido propio** que cada usuario añade a sus presentaciones | No le afecta ninguna de las dos: pertenece a quien lo crea. |
| **Logos, marcas y materiales de terceros** (ISA, SCORE, I3US, Universidad de Sevilla, Junta de Andalucía, Ministerio/NextGenerationEU/PRTR/AEI, logos de productos en los componentes, tipografías) | Fuera de la licencia. Se rigen por las condiciones de sus titulares. |

Al generar una presentación no añadas avisos de licencia ni créditos del sistema a las diapositivas. Cuando se redistribuya o modifique el propio sistema de diseño, conserva `LICENSE` y la atribución.
