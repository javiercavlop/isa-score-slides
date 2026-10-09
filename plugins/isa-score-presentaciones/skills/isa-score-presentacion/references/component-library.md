# Biblioteca de componentes (diapositivas originales)

> **OBLIGATORIO, siempre y en todo momento:** antes de usar esta página, lee y cumple [`00-reglas-obligatorias.md`](00-reglas-obligatorias.md). Toda presentación es **muchísimo más visual** (≤ 30 palabras y una metáfora visual por diapositiva), **dinámica** (cada diapositiva se construye animada, Morph entre copias), **reutiliza la biblioteca y la portada reales**, dibuja las **arquitecturas con formas nativas**, no ahorra diapositivas y se entrega como **.pptx nativo con animaciones** (nunca el PPTX exportado de Claude Slides). Solo el autor puede relajar una regla, y de forma explícita.

46 componentes reutilizables extraídos de las 7 presentaciones: secuencias que se repiten entre charlas o que pueden repetirse (tabla de pricing → espacio de configuración, rueda de *future work* que gira, bucle DevOps, agenda, pirámide, etc.). Cada uno es un .pptx con las diapositivas **originales** —formas, imágenes, SVG, Morph y líneas de tiempo de animación intactas— en `kit/library/<id>.pptx.b64.txt`, y un componente con vista previa animada (`Library · …`). `kit/library/catalog.json` es el índice legible por máquina (id, categoría, descripción, transiciones por diapositiva, efectos, fotogramas).

Uso con el kit:

```python
d.list_components()                      # catálogo
d.component_texts("pricing-table-build") # textos exactos sustituibles
d.insert_component("pricing-table-build", replacements={"Ⓢ(BASIC)": "Ⓢ(FREE)"}, number=4)
d.insert_component("rotating-wheel", slides=[1, 2, 3, 7], number=17)
```

Reglas:

- **Inserta, luego adapta.** Cambia textos con `replacements`; lo que está dentro de imágenes (algunas tablas de pricing, capturas, logos de sistemas) se sustituye en PowerPoint con *Cambiar imagen*, sin renombrar la forma, para que Morph siga emparejando.
- **No rompas la secuencia.** Las copias de un componente comparten nombres de forma; si quitas pasos, quita los intermedios (`slides=[…]`), no formas sueltas.
- **Número lógico.** `number=` escribe el mismo número en todas sus diapositivas, como hace el grupo.
- Los componentes marcados *4:3* vienen de ICSOC'24 y se centran en 16:9 con dos máscaras blancas laterales (`!!4x3 mask left/right`) que conservan el encuadre 4:3 original (zooms y sangrados); su título es el estilo antiguo (izquierda, Roboto 40 pt).
- **Fidelidad.** Cada componente guarda su maestro, tema y layouts originales cuando difieren de los de la plantilla (colores de tema, fuentes y estilos de marcador intactos), conserva los identificadores de relación (SmartArt) y copia las imágenes byte a byte. Auditoría frente a las 152 diapositivas fuente: mismo número de formas, mismo texto, mismos efectos (`presetID`, subtipo, disparador), mismos nodos de tiempo y `bldP`, transiciones idénticas, ningún destino de animación ni relación roto; diferencia visual media del render 0,98/255.


## Apertura y gancho

| id | Componente | Diap. | Transiciones | Animaciones | Qué es |
| --- | --- | --- | --- | --- | --- |
| `hook-pricing-question` | HookPricingQuestion | 3 | 3 Morph | Wipe 1, Zoom 9 | Collage of real pricing pages → decision-maker ‘OPTIMIZE’ → value-cost with the guiding question → two real pricings (GitHub vs CircleCI) with highlighted rows. Morph between the three. |
| `quote-hook` | QuoteHook | 1 | 0 Morph · 1 corte/fade | — | Centred quote with the key fragment in alert red and the author, used as the very first content slide. |
| `statement-hooks` | StatementHooks | 3 | 0 Morph · 3 corte/fade | — | One-word statement (‘Customization’), a claim with a giant crimson word (THOUSANDS) and the thesis title with ‘Pricing’ highlighted. |
| `character-cases` | CharacterCases | 3 | 0 Morph · 3 corte/fade | Zoom 3, Dissolve 2 | Illustrated presenter character at the left; mini pricing tables with red frames marking inconsistent cases, ‘Depends on / Excludes’ arrows. Character reused across slides. |
| `thinking-character-story` | ThinkingCharacterStory | 9 | 3 Morph · 6 corte/fade | Appear 4, Fly In 1, Wipe 15, Rise Up 2, Zoom 34, Appear↓ 4 | Character with a thought cloud whose contents change step by step (travel booking → real SaaS brands → task graph). Zoom/Wipe entrances and Morph to the composition graph. |
| `strike-replace` | StrikeReplace | 3 | 2 Morph · 1 corte/fade | Zoom 1 | QACO / QoS-aware composition → struck through in crimson → PACO / Pricing-aware composition appears below. |

## Agenda

| id | Componente | Diap. | Transiciones | Animaciones | Qué es |
| --- | --- | --- | --- | --- | --- |
| `agenda-arc` | AgendaArcOriginal | 4 | 0 Morph · 4 corte/fade | Appear 1, Wipe 5, Zoom 4 | The real agenda with icons (start flag, bulb, checklist, checkered flag) on the crimson arc; one copy per section with the current circle filled. |
| `toc-numbered` | TocNumbered | 2 | 0 Morph · 2 corte/fade | — | Numbered table of contents with large crimson numerals; the second copy marks the current section. |
| `toc-list` | TocList | 2 | 0 Morph · 2 corte/fade | — | Plain numbered TOC with nested items; current section in bold. Used before each section of a long talk. |

## Pricing y espacio de configuración

| id | Componente | Diap. | Transiciones | Animaciones | Qué es |
| --- | --- | --- | --- | --- | --- |
| `pricing-table-build` | PricingTableBuild | 7 | 7 Morph | Appear 4, Zoom 1 | Icons of features scattered → BASIC/PRO/BUSINESS table with prices → usage-limits legend (Relaxed/Moderate/Strict) → add-on card ($10 / month) → explosion into monitors with every subscription Ⓢ(…) → ‘Configuration Space’. All Morph. |
| `pricing-build-user` | PricingBuildUser (4:3 centrado) | 11 | 6 Morph · 5 corte/fade | Appear 16, Wipe 5, Zoom 25, Zoom↓ 1 | User at a monitor → empty plan table → features → limits → add-ons → fan of user subscriptions on monitors → users coloured per subscription (4:3 deck, centred). |
| `curse-of-customization` | CurseOfCustomization | 2 | 1 Morph · 1 corte/fade | — | Small pricing table whose plans fan out with crimson lines into the full list of subscriptions Ⓢ(…) once add-ons are added. |
| `pricification-timeline` | PricificationTimeline | 4 | 0 Morph · 4 corte/fade | Wipe 16, Blinds 1, Zoom 20, Zoom↓ 1 | Horizontal crimson timeline from a SaaS screen to a pricing table: milestones (identification of features, essential/key features, generation of the pricing structure) and a BPMN detail. |
| `evaluation-ground-truth` | EvaluationGroundTruth (4:3 centrado) | 6 | 5 Morph · 1 corte/fade | Appear 12, Wipe 18 | Point-based evaluation hub (TP, FP, FN, TN) then ground-truth vs extracted pricing tables with crimson frames per case (4:3 deck, centred). |

## Procesos y DevOps

| id | Componente | Diap. | Transiciones | Animaciones | Qué es |
| --- | --- | --- | --- | --- | --- |
| `devops-to-pricing-driven` | DevopsToPricingDriven | 9 | 7 Morph · 2 corte/fade | Fade 3, Peek In 5, Float In 9, Dissolve 5, Dissolve↓ 2 | Traditional DevOps infinity loop with a provider-events timeline (pe1…pen) → effort chart → definition card over a grey veil → codebase with feature toggles → Pricing-driven Dev/Ops loop with its five research lines. |
| `devops-numbered-overview` | DevopsNumberedOverview | 7 | 7 Morph | Peek In 5, Wipe 1, Dissolve 1 | Numbered list of the five lines next to the loop; each copy highlights one line and swaps the illustration (metamodel, design, self-adaptation, testing, analysis). |
| `feature-toggles-codebase` | FeatureTogglesCodebase | 4 | 2 Morph · 2 corte/fade | Blinds 2 | Codebase files with toggles, toggle context database and pricing → evaluation space size ‘8’ → architecture with micro-services. |
| `feature-toggle-anatomy` | FeatureToggleAnatomy | 3 | 1 Morph · 2 corte/fade | Appear 9 | ‘Feature Toggles’ statement → SaaS code file with toggles → zoom into the code with Context / Rule / Feature callouts. |
| `evaluation-expression` | EvaluationExpression | 1 | 0 Morph · 1 corte/fade | Wipe 4, Dissolve 3 | Pricing table + code snippet with dashed frames; the expression is resolved against a plan (GOLD → PLATINUM) with crimson arrows. |
| `three-step-flow` | ThreeStepFlow | 1 | 0 Morph · 1 corte/fade | Wipe 2, Zoom 4 | Three rounded pastel cards (rose → white → blue) joined by thick crimson/teal arrows: Decision-makers → Semantic gap → PI tools. |
| `pipeline-flow` | PipelineFlow | 2 | 1 Morph · 1 corte/fade | Blinds 16 | GitHub → paper → SaaS cloud → YAML with crimson elbow arrows and counters (16, 3, 30 SaaS), then zoom to the charts. |

## Arquitectura y propuesta

| id | Componente | Diap. | Transiciones | Animaciones | Qué es |
| --- | --- | --- | --- | --- | --- |
| `layers-zoom` | LayersZoom | 3 | 3 Morph | Rise Up 3, Zoom 1 | PIIP layers (accessibility / orchestration / capability) → capability layer zoomed with MCP server and tools → the layers beside the system logo. |
| `architecture-spotlight` | ArchitectureSpotlight | 8 | 8 Morph | Zoom 1 | Three-layer architecture image with a crimson frame that Morph moves from the user query to reasoning, tool invocation, MCP server, tools, synthesis and response; final copies isolate layers. |
| `diagram-zoom-pan` | DiagramZoomPan (4:3 centrado) | 5 | 4 Morph · 1 corte/fade | — | Full architecture diagram (extractor / process engine / results modeler) → Morph zooms and pans across its stages (4:3 deck, centred). |
| `acronym-expansion` | AcronymExpansion | 3 | 1 Morph · 2 corte/fade | — | ‘How can we do this?’ → giant red acronym C S O P → Morph spreads it and lines connect each letter to its word. |
| `proposal-stack` | ProposalStack | 3 | 1 Morph · 2 corte/fade | Wipe 2, Rise Up 9, Dissolve 5 | Proposal diagram (iPricing → data/model → CSOP) with crimson frames, then the layered operations stack with a solver logo. |

## Evaluación y resultados

| id | Componente | Diap. | Transiciones | Animaciones | Qué es |
| --- | --- | --- | --- | --- | --- |
| `rq-cards` | RqCards | 1 | 0 Morph · 1 corte/fade | — | Three white RQ cards with crimson pill, label, question and grey note. |
| `rq-circles` | RqCircles | 1 | 1 Morph | Blinds 3 | Numbered crimson circles with each research question beside them. |
| `methodology-funnel` | MethodologyFunnel | 1 | 1 Morph | Wipe 8, Zoom 4 | Participants and LLM logos → pink trapezoids (raw templates → manual review → structural filtering) → final set, with angled connectors. |
| `coverage-panels` | CoveragePanels | 1 | 0 Morph · 1 corte/fade | Zoom 2 | Big pink coverage card (54 %) with formula pill, interpretation card and ‘open gaps’ chips. |
| `results-table` | ResultsTable | 1 | 0 Morph · 1 corte/fade | — | Table with crimson header row, then two pink answer cards for RQ2 / RQ3. |
| `evaluation-stages` | EvaluationStages | 1 | 0 Morph · 1 corte/fade | — | Green and blue ring diagrams for Stage 01 / Stage 02 with short descriptions. |
| `stat-split-panels` | StatSplitPanels | 2 | 1 Morph · 1 corte/fade | Wipe 8, Float In 7, Zoom 4, Dissolve 1 | Slide split in pale yellow (dataset: stat bubbles + SaaS logos) and pink (result: +20 % with breakdown, then trophy 100 %). |
| `split-outcome` | SplitOutcome | 2 | 2 Morph | Wipe 8, Zoom 3 | Pricing files → solver → crimson fork to 65 % / 35 % with pictograms; then the inconsistency cases. |
| `pyramid-levels` | PyramidLevels | 5 | 4 Morph · 1 corte/fade | — | Empty triangle → L1 → L2 → L3 crimson bands, each with a code callout (.js) appearing beside it. |
| `big-stat-out-of` | BigStatOutOf | 1 | 0 Morph · 1 corte/fade | Wipe 2, Float In 6, Zoom 2 | Yellow/pink split with giant fractions (4 out of 18 tools) and tool logos. |
| `tools-arcs` | ToolsArcs | 1 | 0 Morph · 1 corte/fade | Zoom 5 | Tool logos inside partial coloured rings with short verdicts (Togglz, Unleash, LaunchDarkly…). |
| `challenges-hub` | ChallengesHub (4:3 centrado) | 1 | 0 Morph · 1 corte/fade | Wipe 24 | Two central nodes (internal / external) branching to six lettered challenges (4:3 deck, centred). |

## Cierre y trabajo futuro

| id | Componente | Diap. | Transiciones | Animaciones | Qué es |
| --- | --- | --- | --- | --- | --- |
| `rotating-wheel` | RotatingWheel | 7 | 6 Morph · 1 corte/fade | Zoom 1 | Pentagon hub (‘future work’) → coloured segments appear one by one and the wheel rotates with Morph to bring each research line to the top, with its guiding question; ends beside the system logo. |
| `segment-wheel-build` | SegmentWheelBuild | 6 | 5 Morph · 1 corte/fade | — | Framework logo in a pentagon; segments grow around it one per step until the classification wheel is complete. |
| `chevron-steps` | ChevronSteps | 4 | 1 Morph · 3 corte/fade | Peek In 5, Dissolve 4 | Conclusions over the loop, then crimson/amber chevrons 1-2-3 stacking future-work items with partner logos. |
| `numbered-points-0104` | NumberedPoints0104 | 1 | 0 Morph · 1 corte/fade | Zoom 4 | Big thin numerals 01–04 with crimson headings. |
| `conclusions-icons` | ConclusionsIcons | 1 | 0 Morph · 1 corte/fade | Zoom 3 | Three crimson icon tiles with short captions. |
| `conclusions-recap` | ConclusionsRecap | 4 | 1 Morph · 3 corte/fade | — | Numbered contributions growing on the left while the right side re-shows the proposal with a crimson frame on the part being recalled. |
| `ribbon-numbered` | RibbonNumbered | 1 | 1 Morph | Split 3, Dissolve 1 | Crimson ribbons 01/02/03 with white numbered discs and a QR code. |
| `puzzle-pieces` | PuzzlePieces | 1 | 0 Morph · 1 corte/fade | Fly In 4, Wipe 8 | Crimson puzzle with four labelled callouts (icon bars) around it. |

↓ = efecto de salida. Fotogramas de cada paso: `assets/Library/<id>-NN.jpg`.
