# Recetario SPARK: qué copiar de cada diapositiva

Cada fila es una solución reutilizable: abre `deck/project/slides/<id>.html`, copia la estructura y cambia contenido, colores de capa e iconos. Las cifras «steps/clics» salen de los `data-build-in` (pasos distintos / pasos que esperan clic); «M» = `data-transition="magic"` hacia la siguiente.

> Aviso de densidad: varias diapositivas de SPARK superan las 30 palabras de `00-reglas-obligatorias.md` (marcadas ⚠). Al reutilizarlas, recorta texto o pásalo a las notas: el patrón visual es bueno, la cantidad de texto no.

## Mapa del deck

| # | id | Metáfora / técnica | Reutilízala para… |
| ---: | --- | --- | --- |
| 1 | `cover` | Portada del grupo (logos, banda, ponente subrayado) | Toda portada en Slides; en el .pptx la sustituye la semilla real |
| 2, 13, 23, 35 | `agenda1…4` | Agenda en arco; la sección actual en círculo relleno + banda rosa | Cada inicio de sección (en el .pptx → `agenda-arc` con `timing_from`) |
| 3 | `qaco-think` | Personaje con nube de pensamiento que se llena de iconos (13 pasos) | Plantear el problema desde el punto de vista de alguien |
| 4 | `qaco-flow` | Workflow de tareas en círculos con icono + conectores animados en orden + rama alternativa discontinua; leyenda de patrones (secuencia, paralelo, alternativa, bucle) | Cualquier proceso o pipeline con ramas |
| 5 | `qaco-cand` | Rejilla tarea × candidatos con barras de QoS | Elegir entre opciones con atributos |
| 6 | `qaco-bind` | Todas las combinaciones = bindings (árbol + contador «8 bindings») | Explosión combinatoria |
| 7 ⚠ | `qaco-agg` | Agregación por patrón (secuencia suma, paralelo máx…) con conectores | Fórmulas como diagrama |
| 8 ⚠ | `qaco-budget` | Restricción vs objetivo: tabla ordenada con la línea del presupuesto | «Factible ≠ óptimo» |
| 9–12 | `front-a…d` | Frente de Pareto; el punto elegido se mueve con Morph al cambiar los pesos (3 copias sin build-ins) | Compromisos / preferencias |
| 14 | `domains` | Hub central (QACO) con radios a dominios, cada uno con icono | Un patrón aplicado a varios contextos |
| 15–16 | `place-a/b` | Capas Cloud / Edge / IoT y servicios que Morph recoloca | Despliegue, colocación, asignación espacial |
| 17 ⚠ | `quantum` | Recursos cuánticos como tarjetas con atributos + elegido con marco | Selección con restricciones técnicas |
| 18–21 | `alloc-1…4` | Escalera qué → dónde → cuánto → cuándo: cada copia añade un peldaño (Morph) | Generalizar un concepto paso a paso |
| 22 | `status` | Línea «dónde estamos / hacia dónde vamos» con hitos | Estado del proyecto |
| 24 | `ob-hub` | Hub de herramienta con radios (entradas, salidas, motores) | Presentar un sistema y su ecosistema |
| 25–29 ⚠ | `arch-0…4` | **Arquitectura por capas con formas nativas + spotlight que Morph mueve** (paso 1→5) con una tarjeta carmesí que explica el paso | Toda arquitectura (receta abajo) |
| 30 | `ob-caveats` | Advertencias como iconos con veredicto en píldora | Limitaciones, amenazas a la validez |
| 31–33 | `bim-a/b/c` | Paquete como caja que se abre en sus recursos; extensión «A + B + C» | Modelos, paquetes, lenguajes |
| 34 | `bench` | Herramientas como tarjetas con logo + flecha a casos de uso | Benchmarks, generadores |
| 36–43 | `pr-*` | **Componente `pricing-table-build`** (iconos → tabla → límites → relojes → add-on → espacio de configuración) | Pricings SaaS (en el .pptx, el componente original) |
| 44–45 | `curse-a/b` | **`curse-of-customization`**: abanico de suscripciones | Explosión de configuraciones |
| 46 ⚠ | `ipricing` | Modelo → artefactos generados (YAML, UI, API) | Un modelo y sus derivados |
| 47 ⚠ | `clasp-cost` | Ecuación visual «A × B = C» con tarjetas | Combinar dos modelos |
| 48 | `renderer` | Entrada → herramienta → salida con capturas pequeñas | Herramientas de transformación |
| 49–53 | `dlv-*` | **Capturas reales a pantalla completa con marco carmesí que salta de zona** (Morph) + tarjeta carmesí con el dato | Demos y herramientas reales (receta abajo) |
| 54–55 | `sphere-a/b` | Dos sistemas lado a lado con flujo entre ellos | Integración de dos componentes |
| 56 | `lifecycle` | Bucle Dev/Ops con piezas sobre él | Ciclos de vida |
| 57–61 | `tomato-1…5` | **Stepper 1–5 con el paso actual relleno y un aro ámbar que Morph desplaza**; debajo, el detalle del paso | Demos guiadas, procedimientos (receta abajo) |
| 62 ⚠ | `ob-pricing` | Dos mundos que se conectan (pricing ↔ binding) | Trabajo futuro que une líneas |
| 63 | `next` | Números 01–04 con icono | Próximos pasos |
| 64 | `closing` | Cierre del grupo | Toda despedida; en el .pptx, la semilla real |

## Recetas (HTML de Claude Slides, lienzo 1920 × 1080)

**Cascada con flechas** (`qaco-flow`): cajas sin build-in o con `scale`; cada conector con `data-build-in="left order N auto"` en orden de lectura (N = 1, 2, 3…). El sentido del efecto sigue al de la flecha: `left` (→), `right` (←), `drop` (↓), `rise` (↑).

```html
<x-connector x1="295" y1="465" x2="445" y2="465" style="color:#7e0029;border-width:5px" data-build-in="left order 1 auto"></x-connector>
<x-connector x1="595" y1="465" x2="745" y2="465" style="color:#7e0029;border-width:5px" data-build-in="left order 2 auto"></x-connector>
```

**Arquitectura con spotlight** (`arch-0…4`): capas `div` con `card-blue/green/orange` + su `-line`; componentes como cajas blancas con borde de su capa; el marco y la tarjeta explicativa con **id estable** y `data-transition="magic"` en cada copia; solo cambian la posición del marco y el texto de la tarjeta.

```html
<div id="spot" style="position:absolute;left:118px;top:408px;width:324px;height:194px;border:7px solid #7e0029;border-radius:14px;box-shadow:0 0 0 8px rgba(168,0,59,.15)"></div>
<div id="call" style="position:absolute;left:1340px;top:690px;width:484px;height:250px;background:#7e0029;border-radius:12px;padding:24px 28px">…</div>
```

La primera copia (`arch-0`) construye: capas (`drop`) → componentes (`scale`) → conectores (en su sentido). Las copias siguientes no llevan build-ins (Morph hace el movimiento).

**Captura con foco** (`dlv-plans`): `img` a ancho completo con borde fino `ink`; marco `#a8003b` 7 px con `data-build-in="scale order 1"`; tarjeta carmesí con `rise order 2 auto`; nota gris abajo si los valores son ilustrativos. Copias siguientes: mismo `id` del marco en otra zona (Morph).

**Stepper** (`tomato-1…5`): círculos 1–5 sobre una línea rosa; el paso actual relleno `#7e0029`, los futuros blancos con texto `muted`; un aro `amber` con id `tstep` que Morph mueve de paso en paso; panel inferior con el detalle del paso.

**Personaje que piensa** (`qaco-think`): personaje a la izquierda; nube (SVG o forma) a la derecha; dentro, iconos que entran uno a uno (`pop order N auto`), y el mensaje al final con clic.

**Agenda** (`agenda1`): arco SVG + círculos `p` redondos + marcos `div` + iconos + etiquetas cortas (≤ 22 caracteres por etiqueta: «OPENBINDING AND BIM V1» no cabe en el marco original del .pptx, usa «OPENBINDING & BIM»); sección actual: círculo relleno `ag-cur` y banda rosa `ag-hl`.

## Conversión

`map.json` de este ejemplo sustituye: `cover`/`closing` por las semillas reales, `agenda1…4` por `agenda-arc` (copias 1–4, números lógicos 2/8/14/21, `timing_from: agenda1`), `pr-icons` (+ `covers` de `pr-table…pr-config-b`) por `pricing-table-build`, y `curse-a` (+ `curse-b`) por `curse-of-customization`. Las demás 52 diapositivas se convierten a formas nativas.
