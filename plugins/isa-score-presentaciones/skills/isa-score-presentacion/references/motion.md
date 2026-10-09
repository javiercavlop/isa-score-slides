# Movimiento: transiciones y animaciones

> **OBLIGATORIO, siempre y en todo momento:** antes de usar esta página, lee y cumple [`00-reglas-obligatorias.md`](00-reglas-obligatorias.md). Toda presentación es **muchísimo más visual** (≤ 30 palabras y una metáfora visual por diapositiva), **dinámica** (cada diapositiva se construye animada, Morph entre copias), **reutiliza la biblioteca y la portada reales**, dibuja las **arquitecturas con formas nativas**, no ahorra diapositivas y se entrega como **.pptx nativo con animaciones** (nunca el PPTX exportado de Claude Slides). Solo el autor puede relajar una regla, y de forma explícita.

Medido sobre 356 diapositivas de las 7 presentaciones fuente. El dinamismo del estilo **no** viene de efectos llamativos sino de dos mecanismos combinados: secuencias de diapositivas duplicadas unidas con **Morph**, y revelados **en la propia diapositiva** encadenados con *After/With Previous*. Todo lo de esta página está implementado en `kit/isa_deck.py` y genera XML idéntico al que escribe PowerPoint.

## 1. Transiciones

| Transición | Uso en las fuentes | Cuándo | Kit |
| --- | --- | --- | --- |
| **Morph, by object** (fallback Fade) | 180 de 356 diapositivas (≈ 50 %) | Cada paso de una secuencia construida; entre diapositivas que comparten objetos | `d.morph(s)` · `d.build_step(s)` |
| Morph, by word | 4 | Títulos o frases que cambian una palabra (QACO → PACO) | `d.morph(s, option="byWord")` |
| **Sin transición (corte)** | ≈ 170 (≈ 48 %) | Portada, cambio de sección, diapositiva sin objetos comunes con la anterior | `set_transition(s, "none")` (por defecto) |
| Fade / Split / Wipe | 2 / 1 / 1 | Excepcional | `d.fade(s)` · `set_transition(s, "split")` |

Duraciones: `spd="slow"` es el valor por defecto en todas. Variantes: `p14:dur="2000"` para un morph amplio (zoom o rotación de un diagrama completo); `p14:dur="50"` para un **corte morph** (CAiSE'26) — el cambio es instantáneo pero los objetos comunes no parpadean; `advTm="1500"` para avance automático en mini-secuencias cronometradas (otros `advTm` de las fuentes son restos de ensayos: ignóralos).

XML de referencia (el kit lo escribe tal cual):

```xml
<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main">
  <mc:Choice Requires="p159">
    <p:transition spd="slow" xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" p14:dur="2000">
      <p159:morph option="byObject"/></p:transition></mc:Choice>
  <mc:Fallback><p:transition spd="slow"><p:fade/></p:transition></mc:Fallback>
</mc:AlternateContent>
```

## 2. Técnicas Morph del grupo

Cada técnica = duplicar la diapositiva (`d.build_step(s)` conserva nombres e ids, así Morph empareja todo) y cambiar **una** cosa en la copia. El número lógico (`slide-number`) se repite en todas las copias.

1. **Construcción progresiva** — la copia añade la siguiente pieza (tabla de pricing → límites de uso → add-on → espacio de configuraciones). La pieza nueva puede llevar además una animación de entrada.
2. **Marco que viaja (spotlight)** — un rectángulo hueco `!!Spotlight` (2,25 pt `crimson-deep` o 3 pt `alert-red`) cambia de posición/tamaño en cada copia y Morph lo desliza de un componente al siguiente de una arquitectura.
3. **Entrada desde fuera del lienzo** — la pieza está aparcada fuera (y negativa) en la diapositiva anterior; Morph la hace volar a su sitio (`d.move_offslide(shape, "top")` en la copia previa).
4. **Zoom a una zona** — la copia escala y desplaza la imagen o el grupo del diagrama para acercarse a una parte (arquitectura → *Information Extractor*).
5. **Rueda que gira** — un diagrama circular de segmentos (*future work*) rota en cada copia para traer al frente el siguiente segmento; usa `p14:dur="2000"`.
6. **Agenda que avanza** — en cada vuelta a la agenda, el círculo relleno `!!Agenda current` cambia de número; Morph lo desplaza por el arco.
7. **Sustitución de palabras** — se tacha y recolorea parte de un término (QACO → PACO, *QoS-aware* → *Pricing-aware*) con Morph *by word* o *by char*.
8. **Velo de foco** — la copia añade `!!Overlay` (velo `veil`) y una tarjeta encima; Morph funde el velo.
9. **Explosión** — una tabla pequeña se separa en abanico de configuraciones (líneas `crimson-ink` hacia una lista) y vuelve a juntarse.

Componentes de biblioteca que muestran cada técnica con las diapositivas originales: 1 → `pricing-table-build`, `pricing-build-user`, `feature-toggles-codebase`; 2 → `architecture-spotlight`, `conclusions-recap`; 3 → `layers-zoom`; 4 → `diagram-zoom-pan`, `feature-toggle-anatomy`, `pipeline-flow`; 5 → `rotating-wheel`, `segment-wheel-build`; 6 → `agenda-arc`; 7 → `strike-replace`, `acronym-expansion`; 8 → `devops-to-pricing-driven`; 9 → `curse-of-customization`. Para reutilizar el movimiento exacto, insértalos (`d.insert_component`) en lugar de reconstruirlos.

Nombres: usa el prefijo `!!` (convención de PowerPoint) para forzar el emparejamiento de objetos que cambian de tipo o de texto entre copias.

## 3. Animaciones en la diapositiva

Efectos de entrada encontrados (clase, `presetID`/`presetSubtype`, frecuencia) y su nombre en el kit:

| PowerPoint | ID / subtipo | Usos | Kit `effect=` | Duración | Para qué |
| --- | --- | --- | --- | --- | --- |
| Wipe (desde izq. ≫ abajo, der., arriba) | 22 / 8, 4, 2, 1 | 281 | `wipe` + `direction` | 500 ms | Flechas, conectores, cajas de un flujo, filas de tabla, subrayados |
| Zoom | 53 / 16 | 209 | `zoom` | 500 ms | Iconos, burbujas de datos, logos de herramientas |
| Appear | 1 / 0 | 97 | `appear` | — | Etiquetas y piezas que deben estar ya |
| Dissolve In | 9 / 0 | 61 | `dissolve` | 500 ms | Imágenes y capturas |
| Float In | 42 / 0 | 40 | `float_in` | 1000 ms | Textos de conclusión, números 01–04 |
| Rise Up | 37 / 0 | 25 | `rise_up` | 1000 ms | Mensajes clave al final de la diapositiva |
| Fly In | 2 / 1, 2, 4, 8 | 23 | `fly_in` | 500 ms | Personajes / ilustraciones que entran |
| Blinds | 3 / 10 | 23 | `blinds` | 500 ms | Tablas y gráficos completos |
| Peek In | 12 / 8, 4 | 16 | `peek_in` | 500 ms | Paneles laterales |
| Checkerboard | 5 / 10 | 5 | `checkerboard` | 500 ms | Excepcional |
| Fade | 10 / 0 | 4 | `fade` | 500 ms | Superposiciones |
| Split | 16 / 21 | 3 | `split` | 500 ms | Separadores verticales |
| Circle | 6 / 32 | 1 | `circle` | 2000 ms | Revelar un diagrama circular |

Salidas (35 en total): Dissolve Out (9, 23 usos), Disappear (1, 8), Zoom (53/32, 3), Wipe (22, 1) → `cls="exit"` con `dissolve`, `disappear`, `wipe`, `zoom`. No hay efectos de énfasis ni trayectorias en las fuentes.

### Disparadores y ritmo

- Distribución en las fuentes: *With Previous* 39 %, *On Click* 32 %, *After Previous* 29 %.
- Una diapositiva típica: el primer elemento entra **After Previous** al llegar (sin clic), luego cada paso del discurso es un **clic** que dispara un grupo encadenado (`click` → `with`/`after`).
- Las cadenas *After Previous* de Zoom (iconos uno tras otro, 500 ms cada uno) son la firma visual del grupo: `d.animate_sequence(s, shapes, "zoom", first="after", then="after")`.
- Flujos de izquierda a derecha: caja (Zoom) → flecha (Wipe desde la izquierda, *after*) → siguiente caja (Zoom, *after*).
- Máximo ≈ 8 clics por diapositiva; si hay más, parte la idea en otra copia con Morph.

### Uso en el kit

```python
d.animate(slide, shape, "wipe", direction="from_left", trigger="click")     # nuevo paso
d.animate(slide, arrow, "wipe", direction="from_left", trigger="after")     # encadenado
d.animate(slide, label, "appear", trigger="with", delay=200)                 # simultáneo
d.animate(slide, old, "dissolve", cls="exit", trigger="click")              # salida
```

`apply_animations(slide, steps)` reescribe toda la línea de tiempo; `d.animate` la reconstruye acumulando. Los efectos se dirigen a formas, imágenes o grupos por su id (`shape.shape_id`).

## 4. Desde Claude Slides

En un deck de Claude Slides el movimiento se declara con `data-transition` y `data-build-in`; `kit/slides_to_pptx.py` lo traduce a lo anterior (tabla completa en `00-reglas-obligatorias.md`, §6). Semántica que hay que respetar al escribir el deck:

- `data-transition` va en la diapositiva que **sale**; en PowerPoint la transición se escribe en la que **entra**. Magic move ↔ Morph empareja por el mismo `id` (→ nombre `!!id`).
- `data-build-in="efecto order N [auto]"`: cada `order` distinto es **un paso**. Piezas con el mismo `order` aparecen juntas: para una cascada, un `order` por pieza.
- Un paso es automático solo si **todas** sus entradas llevan `auto` (→ *After Previous*); si no, es un clic. El resto de piezas del mismo paso → *With Previous*.
- Conectores: el efecto es Wipe en el sentido de la flecha (`left` para →, `drop` para ↓…).
- Magic move solo se ve en modo Presentar de Slides y se desactiva con “reducir movimiento” del sistema; para comprobar el resultado real, genera el .pptx.

## 5. Diapositivas ocultas

Los decks conservan entre 2 y 15 diapositivas ocultas (`show="0"`): variantes descartadas y respaldo para preguntas. Mantén ese hábito: oculta en lugar de borrar.
