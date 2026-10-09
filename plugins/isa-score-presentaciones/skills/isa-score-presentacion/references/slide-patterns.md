# Patrones de diapositiva

> **OBLIGATORIO, siempre y en todo momento:** antes de usar esta página, lee y cumple [`00-reglas-obligatorias.md`](00-reglas-obligatorias.md). Toda presentación es **muchísimo más visual** (≤ 30 palabras y una metáfora visual por diapositiva), **dinámica** (cada diapositiva se construye animada, Morph entre copias), **reutiliza la biblioteca y la portada reales**, dibuja las **arquitecturas con formas nativas**, no ahorra diapositivas y se entrega como **.pptx nativo con animaciones** (nunca el PPTX exportado de Claude Slides). Solo el autor puede relajar una regla, y de forma explícita.

Medidas en pulgadas sobre 13,333 × 7,5 in (EMU = in × 914 400). Cada patrón indica su llamada en `kit/isa_deck.py`, su animación y la captura de referencia en `assets/Examples/`.

Antes de componer un patrón, comprueba si existe ya como componente original en `component-library.md`.

## TitleSlide — portada (diapositiva real con placeholders)

- Es la diapositiva 1 de CAiSE’26 guardada en la plantilla con `{{TITLE}}`, `{{PRESENTER}}`, `{{COAUTHORS}}`, `{{AFFILIATION}}`, `{{VENUE}}`, `{{DAY}}{{DAY_SUFFIX}} {{MONTH_YEAR}}`. Toda presentación empieza por ella.
- Layout maestro **"Diapositiva de título"** con `showMasterSp="0"`.
- Fila de logos a 0,05–0,18 in del borde superior: `isa-logo` (x 0,32, ancho 2,12), `score-logo` (centrado, x 5,46, ancho 2,42), `us-logo` (pegado a la derecha, ancho 2,12).
- Banda `crimson-deep` a todo el ancho (y 1,63 in, alto 1,69 in) con el título en `band-title` blanco centrado (1–2 líneas).
- Autores en `authors` (presentador subrayado), línea vacía, afiliación en `affiliation`; congreso y fecha abajo en `venue` (`muted`), con ordinal en superíndice ("10th").
- Sin animaciones ni transición.
- Kit: `d.title_slide(title, authors=[("Nombre", True), …], affiliation, venue, date)` · Capturas: `template-title-placeholders.png`, `showcase-01-title.png`.

## AgendaArc — agenda / tabla de contenidos

- Un gran círculo `signal-red` de 6 pt que sangra por la izquierda (x −5,5 in, diámetro ≈ 9,3 in): sólo se ve un arco.
- Sobre el arco, círculos numerados de 1,18 in (borde 3 pt `signal-red`, número `signal-red` 36 pt bold) y, a su derecha, marcos blancos de 7,86 × 1,04 in con borde 3 pt `signal-red`, icono a la izquierda y etiqueta `agenda-item` en mayúsculas.
- La sección actual es un círculo **relleno** `signal-red` con número blanco, llamado `!!Agenda current`.
- Se repite al inicio de cada sección; entre una y otra la transición Morph desliza el círculo relleno.
- Primera aparición: marcos con Wipe desde la izquierda escalonados (*after* + *with* con 150 ms de retraso).
- Variante PhD Forum: "Table of Contents" como lista numerada con la sección actual en **negrita** (Roboto 20 pt) junto a un diagrama de la tesis.
- Kit: `d.agenda_slide(["Introduction", "Proposal", "Evaluation", "Conclusions"], current=1, number=2)` · Capturas: `showcase-02-agenda.png`, `showcase-11-agenda-current-3.png`.

## StatementSlide — gancho o separador

- Diapositiva vacía con una frase centrada en `statement` (`crimson`), a veces con una palabra en `crimson-deep` ("**Pricing**-driven Development and Operation") o una cita con autor debajo en `ink`.
- Variantes: pregunta retórica de una línea en negro bold ("How can we do this?"), sigla gigante en `alert-red` (C S O P) que en la siguiente copia Morph despliega su significado.
- Kit: `d.section_divider(text, number, accent_words=[…])` · Captura: `showcase-03-statement.png`.

## ContentSlide — marco estándar

- Layout **"Sólo el título"** (o "Título y objetos" sin cuerpo). Título `slide-title` centrado arriba, número lógico abajo a la derecha, cita opcional abajo a la izquierda.
- El cuerpo es un diagrama, una tabla de pricing con iconos, capturas o tarjetas — no viñetas. Cuando haya lista, numerada y corta.
- Kit: `d.content_slide(title, number=n)` + `d.citation(s, "Autor, A. (2024). …")`.

## LayerCards — arquitectura por capas

- Tarjetas redondeadas (`radius-card`) apiladas o lado a lado: `card-blue` (Accessibility), `card-green` (Orchestration), `card-orange` (Capability), cada una con su `-line` de 1,5 pt y etiqueta `card-label` en mayúsculas con su `-ink`.
- Dentro: cajas blancas con texto pequeño, flechas verdes (capa de orquestación) o naranjas, icono de usuario y robot.
- Entrada: cada capa con Wipe *from_top* encadenado *after*.
- Kit: `d.card(s, x, y, w, h, "ORCHESTRATION LAYER", style="green")` · Captura: `showcase-04-build-step1.png`.

## SpotlightBuild — secuencia con marco que viaja

- Misma diapositiva duplicada 3–8 veces (Morph). En cada copia un marco hueco `!!Spotlight` (2,25 pt `crimson-deep`, o 3 pt `alert-red`) rodea el siguiente componente; Morph lo desliza.
- El número lógico NO cambia.
- Kit: `s2 = d.build_step(s1); d.spotlight(s2, x, y, w, h)`; en la siguiente copia mueve `!!Spotlight` · Capturas: `showcase-05…`, `showcase-06…`.

## FocusOverlay — velo + tarjeta

- Sobre el diagrama, un rectángulo a sangre `veil` (gris al 55 %) y encima una tarjeta blanca con borde `signal-red` 2,25 pt con una definición en `quote` (término en negrita cursiva, comillas tipográficas grandes).
- Variante: el velo deja ver un recorte (captura de código, tabla) a pantalla casi completa.
- Entrada: Morph funde el velo; la tarjeta entra con Zoom *after*.
- Kit: `d.focus_overlay(s)`, `d.quote_card(s, x, y, w, h, [("Término", {"bold": True}), (" definición…", {})])` · Captura: `showcase-07-focus-overlay-quote.png`.

## StatBubbles — datos del estudio

- Círculos `stat-fill` con borde `amber` de distintos tamaños, cifra en negrita `crimson-deep` y unidad pequeña debajo; al lado una cifra titular `stat-number` (`signal-red`) y bullets con números grandes.
- Fondo opcional partido en dos mitades pastel (amarillo claro / rosa) para "dataset" vs "resultados", con logos de las SaaS analizadas debajo.
- Entrada: burbujas con Zoom encadenado *after*; titular con Float In al clic.
- Kit: `d.stat_bubble(s, x, y, d, "162", "pricings")` · Captura: `showcase-08-stat-bubbles.png`.

## ResearchQuestions — evaluación

- Filas de tarjeta blanca redondeada con borde `card-pink-line`: píldora `crimson-deep` "RQ1", etiqueta corta bold `crimson-deep`, pregunta en bold y nota en gris debajo.
- Variante AGF: título "RQ₁: How are …?" con subíndice y la pregunta como título de la diapositiva durante toda su sección.
- Respuestas: tarjetas `card-pink` con cifra grande y tablas con cabecera `crimson-deep`.
- Entrada: cada fila con Wipe desde la izquierda al clic (piezas de la fila *with*).
- Kit: `d.rq_row(s, x, y, w, "RQ1", "Tool coverage", "To what extent…?", "nota")` · Captura: `showcase-09-research-questions.png`.

## NumberedPoints — 01 · 02 · 03 · 04

- Rejilla 2 × 2 con numerales `point-number` (`crimson`) y, al lado, encabezado bold `crimson` + descripción en `ink`. Para *future work*, contribuciones o conclusiones.
- Alternativa: iconos en disco + texto corto en fila (Conclusions), o la "rueda" de segmentos de *future work* que gira con Morph.
- Entrada: Float In por punto (número al clic, texto *with* +150 ms).
- Kit: ver `build_showcase.py` (diapositiva 10) · Captura: `showcase-10-numbered-points.png`.

## ClosingSlide — gracias / contacto (diapositiva real con placeholders)

- Es la última diapositiva de CAiSE’26 guardada en la plantilla; añade `({{EMAIL}})`, la imagen "QR placeholder" y el grupo "Funding logos". Toda presentación termina con ella, siempre con correo, QR y financiación.
- La portada reutilizada: mismos logos, misma banda y título; autores con correo del presentador entre paréntesis; QR al artículo/repositorio a la izquierda (≈ 4,2 in); banda de financiación (`junta-andalucia` + `funding-ministerio-nextgen`) abajo a la derecha.
- Kit: `d.closing_slide(title, authors, email, venue=…, date=…, qr_image="qr.png")` · Capturas: `template-closing-placeholders.png`, `showcase-13-closing.png`.

## MotionCatalogue — referencia de efectos

- Rejilla de tarjetas, una por efecto de entrada del kit, animadas en cadena *after*. Sirve para probar efectos en el PowerPoint de destino.
- Captura: `showcase-12-animation-catalogue.png`.

## Recursos recurrentes del grupo (ahora en la biblioteca)

- **Tabla de pricing con iconos** (`pricing-table-build`, `pricing-build-user`, `character-cases`): columnas BASIC / PRO / BUSINESS con precio en cabecera rosada, iconos de colores por funcionalidad; leyenda "USAGE LIMITS" (Relaxed / Moderate / Strict con discos verde, amarillo, rojo) y tarjetas de *add-on* con marcador verde ("$10 / month").
- **Bucle DevOps** (`devops-to-pricing-driven`, `devops-numbered-overview`; infinito `navy` + `green`) con línea de eventos de proveedor debajo ("PROVIDER EVENTS (peᵢ)").
- **Monitores** (`pricing-table-build` paso 6–7, `curse-of-customization`) con configuraciones y el símbolo Ⓢ(BASIC, calls) — espacio de configuraciones; llave `crimson-ink` agrupando.
- **Personajes ilustrados** (`character-cases`, `thinking-character-story`) (presentador, *decision-maker*) que reaccionan; logos de SaaS reales en escenas tipo nube de pensamiento.
- Diagramas UML/metamodelos con un marco `alert-red` que destaca la clase de la que se habla.
