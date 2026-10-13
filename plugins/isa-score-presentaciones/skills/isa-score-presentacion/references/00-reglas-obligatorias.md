# REGLAS OBLIGATORIAS: visual, dinámico y en PowerPoint nativo

**Esta página manda sobre todas las demás de este sistema y sobre cualquier encargo.** Se aplica siempre y en todo momento: en cada presentación, en cada diapositiva y en cada iteración, aunque el encargo no la mencione, sea breve o pida «solo un borrador».

**Contrato para quien construye una presentación con este sistema** (persona o agente):

1. **Lee esta página entera antes de diseñar nada.** Las demás páginas (`slide-patterns.md`, `component-library.md`, `motion.md`, `pptx-workflow.md`) explican *cómo* hacerlo, siempre dentro de estas reglas.
2. **Cumple las siete reglas sin que nadie las pida.** No preguntes si hace falta que sea visual, si hay que animar, si se puede reutilizar la biblioteca o si se pueden usar muchas diapositivas: **sí, siempre**.
3. **Solo el autor puede relajar una regla, y solo de forma explícita** («esta vez sin animaciones», «en una sola diapositiva»). Ni el formato del encargo, ni la prisa, ni una herramienta que no lo soporte justifican saltársela. Si una herramienta no puede cumplir una regla (por ejemplo, la exportación PPTX de Claude Slides no lleva animaciones), cambia de herramienta según §6; no rebajes la regla.
4. **Antes de entregar, pasa la lista de comprobación final** y di en la respuesta que se cumple, o qué punto no y por qué.
5. **Una entrega que incumple una regla no está terminada**: corrígela antes de presentarla como final.

**Las siete reglas, en una línea cada una:**

1. **Muchísimo más visual**: ≤ 30 palabras por diapositiva, ≥ 3 objetos visuales y una metáfora visual; el guion, en las notas.
2. **Dinamismo**: toda diapositiva de contenido se construye animada; cascadas pieza a pieza; todas las flechas animadas; Morph entre copias.
3. **Reutilizar las diapositivas reales del grupo** (biblioteca) para los temas que ya cuentan: pricing SaaS, espacio de configuración, DevOps, agenda, arquitectura, trabajo futuro…
4. **Portada y cierre del grupo**, siempre los reales.
5. **Arquitecturas como diagramas nativos** (formas, conectores, iconos), construidos y recorridos con animación.
6. **Animaciones en el PowerPoint descargado**: el entregable es un .pptx nativo con Morph y animaciones, nunca el PPTX exportado desde Claude Slides.
7. **Sin límite de diapositivas**: cada idea, una secuencia de copias con Morph.
8. **Paginación estable**: el número de diapositiva conserva en todo el deck el mismo tamaño, posición, color y estilo; solo puede salir del lienzo durante una ampliación/recorrido visual de una figura o arquitectura.

Origen: son las peticiones que el autor ha tenido que repetir a mano en presentaciones anteriores. Literalmente:

> «La presentación debe ser más visual, muchísimo más visual: ahora mismo hay mucho texto y pocas metáforas visuales, elementos y formas visuales, iconos, figuras…»
> «Incluir mejores y más complejas animaciones/transiciones que le den dinamismo, como en las presentaciones del grupo.»
> «Puedes reutilizar sus diapositivas para presentar SaaS pricing y configuration space.»
> «Quiero que la portada sea más parecida a la del grupo.»
> «Incluye diagramas de arquitectura con elementos de PowerPoint.»
> «No me salen las animaciones: las quiero en el PowerPoint descargado.»
> «No importa añadir muchas diapositivas.»

---

## 1. Muchísimo más visual: cada idea es una imagen, no un párrafo

**Qué significa.** El público tiene que entender la diapositiva mirándola, sin leerla. El texto en pantalla solo nombra las piezas del dibujo; la explicación la da el orador, y está escrita en las notas.

**Reglas concretas**

- **Presupuesto de texto.** Título de 3–7 palabras. Etiquetas de ≤ 6 palabras. **≤ 30 palabras visibles por diapositiva**, sin contar el título. Prohibidos los párrafos, las listas de viñetas de más de 3 líneas y las frases con verbo conjugado que expliquen algo. Si hace falta explicarlo, va a las notas (`<aside>` en Claude Slides, notas del orador en el .pptx).
- **Al menos tres objetos visuales por diapositiva de contenido**: iconos, formas, flechas, gráficos, capturas o personajes. El texto ocupa menos del 30 % del área.
- **Toda diapositiva tiene una metáfora visual.** Elige una del catálogo de abajo **antes** de escribir el texto. Si no encuentras ninguna, la idea es demasiado abstracta: pártela.
- **Cada concepto lleva su icono** (plano, de color, en la paleta del sistema), sea una tarea, un proveedor, una restricción, un objetivo o un recurso. El mismo concepto lleva siempre el mismo icono en todo el deck.
- **Los números son objetos**: burbuja (`stat-fill` + `amber`), cifra gigante (`stat-number`), fracción «4 out of 18», barra o reloj. Nunca «se reduce un 20 %» dentro de una frase.
- **Las comparaciones son tablas o paneles**, no párrafos: dos columnas, una tabla de pricing o paneles `card-*` lado a lado.
- **Las capturas reales** (herramientas, demos, páginas de pricing) van grandes, con **marco carmesí** (`crimson-deep` 2,25 pt) sobre la zona de la que se habla, y una etiqueta corta junto al marco.
- **Un personaje** (presentador, *decision-maker*, desarrollador, usuario) cuando hay alguien que decide o actúa: en la biblioteca, `thinking-character-story`, `character-cases` y `hook-pricing-question`.

**Catálogo de metáforas** (con el patrón o componente que la resuelve)

| La idea es… | Metáfora | Cómo |
| --- | --- | --- |
| Un problema que alguien tiene que resolver | Personaje con nube de pensamiento que se va llenando | `thinking-character-story` |
| Un proceso o pipeline | Cajas con icono unidas por flechas que entran una a una | `three-step-flow`, `pipeline-flow`, ChevronSteps |
| Elegir entre candidatos | Rejilla de tarjetas (proveedor + icono + barras de QoS o precio); la elegida, con marco carmesí | tarjetas `card-*` + SpotlightBuild |
| Una combinación o asignación | Árbol o matriz de tareas × proveedores con las celdas elegidas rellenas | formas + conectores |
| Un compromiso u óptimo | Gráfico (frente de Pareto, curva de presupuesto) con el punto elegido destacado y moviéndose entre copias | gráfico de formas + Morph |
| Capas o niveles | Pila de capas pastel, con zoom a una de ellas | LayerCards, `layers-zoom`, `pyramid-levels` |
| Una arquitectura | Diagrama nativo con spotlight que la recorre (ver §5) | `architecture-spotlight`, `diagram-zoom-pan` |
| Un ecosistema o herramientas alrededor de un núcleo | Hub central con radios hacia cada pieza (icono + etiqueta) | `challenges-hub`, `segment-wheel-build` |
| Una línea temporal o un ciclo de vida | Línea o bucle con hitos numerados; el actual, relleno | `pricification-timeline`, `devops-to-pricing-driven` |
| Una explosión combinatoria | Tabla pequeña que se abre en abanico de configuraciones | `curse-of-customization`, `pricing-table-build` |
| Advertencias o límites | Iconos (⚠, 🔒, reloj) con un veredicto en píldora de color | StatBubbles + píldoras |
| Trabajo futuro | Rueda que gira o números 01–04 | `rotating-wheel`, `numbered-points-0104` |
| Una demo | Secuencia de capturas con marco que se mueve y paso numerado arriba | SpotlightBuild sobre captura |

**Comprobación.** Tapa el título y las notas. Si alguien que no conoce el tema distingue de qué va cada diapositiva, está bien. Si lo que queda es sobre todo texto, rehazla.

## 2. Animaciones y transiciones complejas: el movimiento cuenta la historia

**Qué significa.** El dinamismo del grupo no viene de efectos vistosos. Viene de **construir cada diapositiva delante del público**: las piezas aparecen en el orden del razonamiento, y las ideas se transforman de una diapositiva a la siguiente con Morph. Detalle técnico en `motion.md`.

**Mínimos de cada deck**

- **Toda diapositiva de contenido tiene al menos una animación de entrada.** Nada aparece entero de golpe, salvo la copia de una secuencia que continúa la anterior.
- **Cascadas reales.** Los iconos, cajas y burbujas entran **uno tras otro** (Zoom o Wipe *After Previous*, 500 ms), no todos a la vez. Cada pieza tiene su propio paso.
- **Todas las flechas y conectores se animan**: Wipe en el sentido de la flecha, justo después de la caja de origen. Una flecha que ya está ahí cuando aparece su origen es un error.
- **El mensaje clave entra al final**, con clic (Rise Up / Float In).
- **Al menos una técnica Morph por sección**, de entre estas: construcción progresiva, marco que viaja (spotlight), zoom a una zona, entrada desde fuera, rueda que gira, explosión, sustitución de palabra. Recetas en `motion.md` §2.
- **Agenda animada** al empezar cada sección: el arco se dibuja, los círculos y marcos entran en cascada y el círculo de la sección actual se rellena (componente `agenda-arc`).
- Solo **efectos de entrada** (y alguna salida). Sin énfasis, sin trayectorias, sin rebotes ni giros. Morph entre copias; corte o Fade en los cambios de sección.

**Comprobación.** Pasa el deck en modo presentación. Cada clic tiene que añadir o mover algo con sentido. Si una diapositiva no se mueve, o se mueve todo a la vez, no está terminada.

## 3. Reutilizar las diapositivas reales del grupo

**Qué significa.** Si el tema ya está contado en una charla del grupo, se usan **esas** diapositivas, con su diseño y sus animaciones originales, no una imitación.

- Antes de diseñar una sección, busca el tema en `component-library.md` / `kit/library/catalog.json`. Equivalencias frecuentes:

| Tema | Componente |
| --- | --- |
| Qué es un pricing SaaS (planes, features, límites de uso, add-ons) | `pricing-table-build` (pasos 1–5) |
| Espacio de configuración / suscripciones posibles | `pricing-table-build` (pasos 6–7) y `curse-of-customization` |
| Por qué importa el pricing (gancho) | `hook-pricing-question` |
| Pricing-driven DevOps / feature toggles | `devops-to-pricing-driven`, `devops-numbered-overview`, `feature-toggles-codebase`, `feature-toggle-anatomy` |
| QACO → PACO | `strike-replace` |
| Agenda | `agenda-arc` (una copia por sección) |
| Arquitectura por capas | `layers-zoom`, `architecture-spotlight` |
| Trabajo futuro | `rotating-wheel`, `chevron-steps`, `numbered-points-0104` |

- En el .pptx se insertan con `d.insert_component(id, replacements, number, slides)` (Camino A) o desde `map.json` (Camino C), **nunca redibujados**.
- En Claude Slides se deja en su lugar una diapositiva equivalente (puedes partir de los fotogramas de `assets/Library`) y en `map.json` se indica qué diapositivas cubre el componente (`covers`).

## 4. La portada (y el cierre) del grupo

**Qué significa.** La portada es siempre la de las charlas del grupo, no un diseño nuevo.

- En el .pptx se usan las **semillas reales** de la plantilla: `d.title_slide(...)` y `d.closing_slide(...)` (o `title_slide` / `closing_slide` en `map.json`).
- En Claude Slides, reproduce esta composición exacta (lienzo 1920 × 1080, fondo `surface`):

| Elemento | Posición y estilo |
| --- | --- |
| Fila de logos | `isa-logo` (izq., x ≈ 45, w ≈ 305), `score-logo` (centro, x ≈ 786, w ≈ 348), `us-logo` (der., x ≈ 1614, w ≈ 305); arriba (y ≈ 10–25, h ≈ 140–160) |
| Banda | rectángulo a todo el ancho, y = 234, h = 244, `crimson-deep` |
| Título | blanco, negrita, 56 px, centrado en la banda; subtítulo opcional 34 px debajo, también en blanco |
| Ponente | 40 px, **subrayado**, centrado, y ≈ 580; los coautores en la misma línea, sin subrayar |
| Afiliación | 36 px, negrita, centrada, y ≈ 680 |
| Congreso y fecha | 34 px, `muted`, centrado, dos líneas, y ≈ 930 |
| Tipografía | Calibri (`band-title`, `authors`, `affiliation`, `venue`) |
| Movimiento | ninguno, como la semilla real; el dinamismo empieza en la diapositiva 2 (agenda) |

- El cierre usa la misma fila de logos y banda, con «Thank You», el correo del ponente, el QR y los logos de financiación abajo a la derecha.
- Los logos son assets del sistema: ver `assets/Logos/README.md` para copiarlos.

## 5. Diagramas de arquitectura con elementos nativos de PowerPoint

**Qué significa.** Una arquitectura se dibuja con **formas, conectores e iconos editables**, nunca como una imagen pegada ni como una lista. Así se puede animar pieza a pieza y recorrer con Morph.

- **Estructura.** Capas o zonas como tarjetas pastel (`card-blue` / `card-green` / `card-orange` con su `-line` y su `-ink` para el título de la capa). Dentro, componentes como cajas blancas con borde fino, icono y nombre corto. Entre ellos, conectores con punta de flecha y una etiqueta de 1–3 palabras cuando la relación no es obvia.
- **Animación de construcción.** Primera copia: las capas entran en cascada (Wipe desde arriba o desde la izquierda), luego los componentes (Zoom) y luego los conectores (Wipe en el sentido del flujo).
- **Recorrido.** Copias siguientes con Morph: un marco `!!Spotlight` (`crimson-deep`) va de componente en componente siguiendo una petición de ejemplo. En cada copia, una etiqueta lateral breve dice qué hace ese paso. Opcionalmente, un zoom a la capa que importa (`layers-zoom`).
- **Herramientas.** En el kit: `d.card`, `d.text`, `d.arrow`, `d.spotlight`, `d.build_step`. En Claude Slides: `div` con borde para las cajas, `x-shape` y `x-connector`, ids estables en cada pieza; el Camino C los convierte en formas nativas editables.
- Si existe un diagrama oficial (documentación del proyecto, paper), **se copia su estructura y nombres exactos**; no se inventan componentes.

## 6. Que las animaciones estén en el PowerPoint descargado

**Por qué fallaba.** Los decks hechos en Claude Slides animan bien en su visor (modo Presentar). Pero **su exportación a PPTX no escribe ni transiciones ni animaciones**: el .pptx descargado sale estático. Además, el *magic move* solo se ve en modo Presentar y se desactiva si el sistema tiene activado «reducir movimiento».

**Regla.** El entregable final es **siempre** un .pptx nativo generado con el kit:

- **Camino A:** construir directamente con `kit/isa_deck.py`.
- **Camino C:** convertir el deck de Slides con `kit/slides_to_pptx.py` (ver `pptx-workflow.md`).

El resultado lleva Morph (*by object*, con Fade como alternativa) y animaciones de entrada nativas, que se ven en PowerPoint ≥ 2019 / Microsoft 365. Nunca se entrega el PPTX exportado desde Slides.

Equivalencias que aplica el Camino C:

| Claude Slides | PowerPoint |
| --- | --- |
| `data-transition="magic"` en la diapositiva que **sale** | Morph *by object* en la que **entra**; los objetos se emparejan por nombre `!!id` |
| `data-transition="fade"` | Fade en la siguiente |
| `data-build-in` `fade` / `rise` | Fade 500 ms / Float In 600 ms |
| `drop` / `left` / `right` | Wipe desde arriba / izquierda / derecha |
| `scale`, `pop` | Zoom |
| conector (`x-connector`) | Wipe en el sentido de la flecha |
| `order` nuevo sin `auto` / con `auto` / mismo `order` | *On Click* / *After Previous* / *With Previous* |

Para que la conversión sea fiel, en Slides: un `id` en todo lo que deba hacer Morph; un `order` distinto para cada pieza de una cascada; nada con coordenadas negativas; estilos de texto en el propio elemento.

**Comprobación antes de entregar.** El .pptx abre con python-pptx y tiene el mismo número de diapositivas que el deck. Cada diapositiva Morph tiene sus pares `!!`. El recuento de animaciones por diapositiva coincide con los build-ins. Un render con LibreOffice → PDF se ve bien (LibreOffice muestra las animaciones, pero no Morph).

## 7. Muchas diapositivas físicas, pocas lógicas

- **No hay límite de diapositivas físicas.** 60–80 para una charla de 30–40 min es lo normal. Nunca condenses dos ideas en una diapositiva para «ahorrar».
- Cada idea es una **secuencia** de copias. En cada copia cambia una cosa: aparece una pieza, se mueve el marco, se acerca el zoom, cambia una palabra. Las copias van unidas con Morph y llevan el **mismo número lógico**.
- Máximo ≈ 6–8 clics por diapositiva física; si hay más, otra copia.
- La agenda reaparece antes de cada sección.

## Lista de comprobación final

1. Portada y cierre del grupo (semillas reales en el .pptx; composición de §4 en Slides).
2. ≤ 30 palabras visibles por diapositiva, ≥ 3 objetos visuales y una metáfora del catálogo; guion en las notas.
3. Temas ya contados por el grupo → componentes de biblioteca, no rediseños.
4. Arquitecturas como diagramas nativos con construcción animada y spotlight.
5. Cada diapositiva de contenido con animación; cascadas pieza a pieza; todas las flechas animadas; agenda animada en cada sección.
6. Secuencias Morph con número lógico repetido; muchas diapositivas físicas si hace falta.
7. Paginación: todas las cajas `Slide number` visibles tienen la misma firma de tamaño, posición, color y estilo. Una caja fuera del lienzo solo se acepta en una copia Morph que continúe una ampliación de figura o arquitectura; vuelve a la posición normal al terminar el recorrido.
8. Todo el texto en pantalla en inglés.
9. Entregado como .pptx nativo (Camino A o C) y verificado como en §6. Nunca el PPTX exportado desde Slides.
