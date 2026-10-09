# ISA · SCORE Presentaciones

Plugin para Claude (Cowork y Claude Code) que prepara presentaciones académicas con el estilo del **ISA Research Group / SCORE Lab (I3US, Universidad de Sevilla)** a partir de un contexto y una descripción breve.

Autores: **Francisco Javier Cavero López** y **Alejandro García Fernández** (SCORE Lab, I3US, Universidad de Sevilla; Grupo ISA).

## Instalar

- **Cowork:** *Customize → Plugins → Add marketplace* → `javiercavlop/isa-score-slides` → instala **isa-score-presentaciones**.
- **Claude Code:**

```
/plugin install isa-score-presentaciones --marketplace javiercavlop/isa-score-slides
```

## Qué hace

Le das el tema, el evento, los autores y tus fuentes; la skill `isa-score-presentacion`:

1. Revisa el encargo y **te pregunta** lo imprescindible que falte (o si algo no encaja).
2. Lee el sistema de diseño y sus **reglas obligatorias**.
3. Investiga el contenido en tus fuentes, sin inventar resultados.
4. Diseña el guion como **secuencias visuales**: una metáfora visual por idea, ≤ 30 palabras por diapositiva, el guion en las notas, y los temas que el grupo ya contó con sus **diapositivas originales** (pricing SaaS, espacio de configuración, DevOps, agenda, arquitectura, trabajo futuro…).
5. Construye un deck en Claude Slides para revisar y lo convierte en un **PowerPoint nativo** con la **portada y el cierre reales**, **Morph** entre copias y **animaciones de entrada** (cascadas, flechas, agenda).
6. Verifica el fichero y te entrega el .pptx con una lista de comprobación.

Siempre: muchísimo más visual, dinámico, sin límite de diapositivas y entregado como .pptx con animaciones. Solo tú puedes relajar una regla, diciéndolo explícitamente.

## Qué necesita

| | Dato |
| --- | --- |
| **Imprescindible** | Tema y contexto (2–10 líneas) · evento, público y duración · ponente y coautores · congreso/reunión y fecha |
| Recomendado | Fuentes (paper, repo, docs, URLs, capturas) · secciones · 3–5 mensajes clave · cautelas (lo que no se puede afirmar) |
| Opcional | Correo y QR del cierre · financiación sí/no · componentes de la biblioteca concretos · fecha de entrega |

Plantilla lista para copiar y un ejemplo real: [`skills/isa-score-presentacion/references/encargo-plantilla.md`](skills/isa-score-presentacion/references/encargo-plantilla.md).

Si falta algo imprescindible o el encargo no encaja (sin contenido, otro estilo, afirmaciones sin respaldo, contradicciones), Claude pregunta antes de empezar. Lo opcional lo completa con valores por defecto y te lo dice.

## Cómo pedirlo

> «Prepara una presentación ISA · SCORE» + la plantilla rellena + tus ficheros o enlaces.

Ejemplo corto:

> Prepara una presentación ISA · SCORE. Tema: nuestro paper sobre X (adjunto PDF): proponemos Y para resolver Z en sistemas SaaS. Evento: CAiSE'27, 20 min. Ponente: Francisco Javier Cavero; coautores: Alejandro García-Fernández, Antonio Ruiz-Cortés. Fecha: CAiSE'27 · 10th June 2027. Mensajes: … Cautelas: la evaluación es preliminar.

## Qué entrega

- **`.pptx` nativo** (PowerPoint ≥ 2019 / Microsoft 365 para ver Morph; en versiones antiguas o Google Slides, Morph cae a Fade).
- **Deck de Claude Slides** para revisar y editar.
- Resumen: qué reglas se cumplen, qué se asumió y qué falta.

## Contenido del plugin

| Ruta (en `skills/isa-score-presentacion/`) | Qué es |
| --- | --- |
| `SKILL.md` | Procedimiento que sigue Claude |
| `references/` | Reglas obligatorias, **lecciones y recetas** (lo aprendido en charlas reales), plantilla de encargo y copia del sistema de diseño |
| `references/fuentes/` | **Índice diapositiva a diapositiva** de las 7 charlas y sus **miniaturas numeradas**, para inspirarse o importar diapositivas concretas |
| `kit/` | Kit Python, conversor Slides → .pptx, arreglo de cascadas, verificador con hoja de miniaturas, plantilla con portada y cierre reales, ejemplo y **biblioteca de 46 componentes originales** |
| `sources/` | **Las 7 presentaciones originales** del grupo y capturas de Delivera (editables, importables diapositiva a diapositiva) |
| `examples/spark/` | Ejemplo completo: deck de 64 diapositivas, `map.json`, miniaturas y **recetario** (qué técnica usa cada diapositiva y cómo adaptarla) |
| `MANIFEST.sha256` (en la raíz del plugin, no en la skill) | Huella SHA-256 de cada fichero: `sha256sum -c MANIFEST.sha256` desde la raíz del plugin |

Sistema de diseño publicado: «Presentaciones SCORE Lab - ISA Group» (https://claude.ai/artifact/GQ3oB24oKr1Kz7X31QoR63).

## Dónde funciona

| Producto | Qué puedes usar |
| --- | --- |
| **Cowork** y **Claude Code** | El plugin completo: la skill, el kit, la biblioteca y la conversión a .pptx con animaciones |
| **Claude Design / Claude Slides** (claude.ai) | No instalan plugins. Usa el sistema de diseño publicado (ya incluye las reglas obligatorias) para diseñar; para el .pptx con Morph y animaciones, abre el deck en Cowork y pide «conviértelo a PowerPoint nativo con la skill ISA · SCORE». La exportación a PowerPoint de Design/Slides no lleva animaciones. |

## Licencia

Sistema, kit, plantilla y biblioteca: **CC BY 4.0** con autorización adicional para usar las presentaciones generadas sin atribución. Logos, marcas y materiales de terceros quedan fuera. Texto completo en [`LICENSE`](LICENSE).
