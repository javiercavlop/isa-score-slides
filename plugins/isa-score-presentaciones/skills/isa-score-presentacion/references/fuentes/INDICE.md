# Índice de las presentaciones fuente

Las 7 charlas originales del grupo (en `sources/`), diapositiva a diapositiva, para inspirarse, adaptar o importar. Miniaturas con el número real de diapositiva en `references/fuentes/<deck>-NN.jpg` (las ocultas no se renderizan). Mírala con Read antes de diseñar una sección: es el catálogo visual del estilo.

- **Importar tal cual** una o varias diapositivas de cualquier deck, con animaciones y Morph: `import_slides(d.prs, "sources/<deck>.pptx", {n1, n2})` del kit (`x_offset=1524000` para ICSOC'24, que es 4:3). Si ya es un componente (columna *Componente*), usa `d.insert_component(id)`.
- **Adaptar**: importa y cambia textos con `replace_text(slides, {...})`; si el contenido es distinto, reconstruye la idea con los patrones copiando su composición.
- Columnas: T = transición (M = Morph, F = fade u otra, — = corte); Anim = efectos de entrada/salida; Img = imágenes; Formas = nº de formas de primer nivel.

## CAiSE'25 (AGF) — CSOP / validez de pricings

`sources/CAISE25-AGF.pptx` · 56 diapositivas · miniaturas: `CAISE25-AGF-01.jpg`, `CAISE25-AGF-02.jpg`

| # | Título / texto principal | T | Anim | Img | Formas | Componente | Oculta |
| ---: | --- | :-: | :-: | :-: | :-: | --- | :-: |
| 1 | Automated Analysis of Pricings in SaaS-based Information Systems | — | 0/0 | 1 | 4 |  |  |
| 2 |  | — | 8/0 | 7 | 8 |  |  |
| 3 | 1 | — | 10/0 | 4 | 11 | agenda-arc |  |
| 4 | User-oriented Pricings | — | 0/0 | 18 | 21 |  |  |
| 5 | User-oriented Pricings | M | 0/0 | 19 | 22 |  |  |
| 6 | User-oriented Pricings | M | 4/0 | 24 | 27 |  |  |
| 7 | User-oriented Pricings | M | 0/0 | 24 | 27 |  |  |
| 8 | User-oriented Pricings | M | 4/0 | 27 | 34 |  |  |
| 9 | How to Measure the Complexity of a Pricing? | M | 0/0 | 83 | 87 |  |  |
| 10 | ConfigurationSpace | M | 1/0 | 81 | 84 |  |  |
| 11 | Pricings’ Configuration Space | — | 0/0 | 1 | 10 |  |  |
| 12 | Pricings’ Configuration Space | M | 0/0 | 5 | 34 |  |  |
| 13 | Traditional DevOps life cyle | — | 9/0 | 0 | 22 | devops-to-pricing-driven |  |
| 14 | Traditional DevOps life cyle | — | 0/0 | 0 | 37 | devops-to-pricing-driven |  |
| 15 | Traditional DevOps life cyle | M | 0/0 | 2 | 30 | devops-to-pricing-driven |  |
| 16 | Pricing-driven Development and Operation of SaaS | M | 2/0 | 8 | 41 | devops-to-pricing-driven |  |
| 17 | Pricing-driven Development and Operation of SaaS | M | 2/0 | 9 | 43 | devops-to-pricing-driven |  |
| 18 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 9 | 43 | devops-to-pricing-driven |  |
| 19 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 11 | 42 | devops-to-pricing-driven |  |
| 20 | Pricing-driven Development and Operation of SaaS | M | 5/0 | 8 | 44 | devops-to-pricing-driven |  |
| 21 | Pricing-driven Development and Operation of SaaS | M | 4/2 | 14 | 48 | devops-to-pricing-driven |  |
| 22 | Automated Analysis of Pricings | — | 0/0 | 8 | 27 |  | sí |
| 23 | 1 | — | 0/0 | 4 | 11 | agenda-arc |  |
| 24 | Our Goals | — | 0/0 | 0 | 4 |  |  |
| 25 | 7 | — | 3/0 | 6 | 6 | character-cases |  |
| 26 | 8 | — | 1/0 | 5 | 12 | character-cases |  |
| 27 | 8 | — | 1/0 | 6 | 16 | character-cases |  |
| 28 | Our Goals | — | 0/0 | 0 | 5 |  |  |
| 29 | Empty Subscription | — | 0/0 | 4 | 5 |  | sí |
| 30 | $ | — | 0/0 | 5 | 7 |  | sí |
| 31 | $$$ | — | 0/0 | 5 | 14 |  | sí |
| 32 | $$$ | — | 0/0 | 6 | 17 |  | sí |
| 33 | Dead add-on | M | 2/0 | 5 | 16 |  | sí |
| 34 | Our Goals | — | 0/0 | 0 | 6 |  |  |
| 35 | Our Goals | — | 0/0 | 0 | 7 |  |  |
| 36 | 18 | — | 3/0 | 5 | 13 |  | sí |
| 37 | How can we do this? | — | 0/0 | 0 | 2 | acronym-expansion |  |
| 38 | C S O P | — | 0/0 | 0 | 2 | acronym-expansion |  |
| 39 | C S O P | M | 0/0 | 0 | 10 | acronym-expansion |  |
| 40 | Our Proposal | — | 1/0 | 1 | 4 | proposal-stack |  |
| 41 | Our Proposal | M | 0/0 | 1 | 4 | proposal-stack |  |
| 42 | Our Proposal | — | 15/0 | 2 | 18 | proposal-stack |  |
| 43 | 1 | — | 0/0 | 4 | 11 | agenda-arc |  |
| 44 | Evaluation Process | — | 0/0 | 2 | 12 | evaluation-stages |  |
| 45 | Evaluating Pricing Validity on a State-of-the-art Dataset | F | 19/0 | 7 | 24 | stat-split-panels |  |
| 46 | Comparing Configuration Space Metrics with State-of-the-art | M | 1/0 | 8 | 17 | stat-split-panels |  |
| 47 | Design of Pricing Inconsistencies Benchmark(Stage two) | — | 9/0 | 23 | 11 |  |  |
| 48 | Detection of Pricing Inconsistencies in Benchmark(Stage two) | M | 8/0 | 33 | 21 | split-outcome |  |
| 49 | Detection of Pricing Inconsistencies in Benchmark(Stage two) | M | 3/0 | 11 | 6 | split-outcome |  |
| 50 | 1 | — | 0/0 | 4 | 11 | agenda-arc |  |
| 51 | Conclusions | — | 0/0 | 1 | 9 | conclusions-recap |  |
| 52 | Conclusions | M | 0/0 | 1 | 10 | conclusions-recap |  |
| 53 | Conclusions | — | 0/0 | 1 | 11 | conclusions-recap |  |
| 54 | Conclusions | — | 2/0 | 2 | 9 |  |  |
| 55 | Conclusions | — | 0/0 | 1 | 13 | conclusions-recap |  |
| 56 | Automated Analysis of Pricings in SaaS-based Information Systems | — | 0/0 | 4 | 8 |  |  |

## CAiSE'26 (FJCL) — Pricing Intelligence / H.A.R.V.E.Y.

`sources/CAiSE_2026_-_FJCL.pptx` · 49 diapositivas · miniaturas: `CAiSE_2026_-_FJCL-01.jpg`, `CAiSE_2026_-_FJCL-02.jpg`

| # | Título / texto principal | T | Anim | Img | Formas | Componente | Oculta |
| ---: | --- | :-: | :-: | :-: | :-: | --- | :-: |
| 1 | Pricing Intelligence: Rethinking IS Engineering in Volatile SaaS Envir | — | 0/0 | 3 | 6 |  |  |
| 2 | SaaS Pricings | M | 0/0 | 27 | 30 |  | sí |
| 3 | 2 | M | 0/0 | 1 | 2 | hook-pricing-question |  |
| 4 | What is the best subscription option among all these SaaS products for | M | 5/0 | 2 | 6 | hook-pricing-question |  |
| 5 | 3 | M | 5/0 | 4 | 11 | hook-pricing-question |  |
| 6 | SaaS Pricings | M | 0/0 | 18 | 21 | pricing-table-build |  |
| 7 | SaaS Pricings | M | 0/0 | 19 | 22 | pricing-table-build |  |
| 8 | SaaS Pricings | M | 4/0 | 24 | 27 | pricing-table-build |  |
| 9 | SaaS Pricings | M | 0/0 | 24 | 27 | pricing-table-build |  |
| 10 | SaaS Pricings | M | 0/0 | 27 | 30 | pricing-table-build |  |
| 11 | 4 | M | 0/0 | 80 | 81 | pricing-table-build |  |
| 12 | ConfigurationSpace | M | 1/0 | 80 | 82 | pricing-table-build |  |
| 13 | Curse of Customization | — | 0/0 | 1 | 11 | curse-of-customization |  |
| 14 | Curse of Customization | M | 0/0 | 5 | 34 | curse-of-customization |  |
| 15 | Intelligent Pricing (iPricing) | M | 0/0 | 1 | 4 |  |  |
| 16 | Intelligent Pricing (iPricing) | M | 2/0 | 3 | 5 |  |  |
| 17 | Intelligent Pricing (iPricing) | M | 3/0 | 3 | 8 |  |  |
| 18 | 7 | M | 6/0 | 2 | 10 |  | sí |
| 19 | Pricing Intelligence (PI) | M | 4/0 | 4 | 8 |  |  |
| 20 | 10 | — | 6/0 | 1 | 9 | three-step-flow |  |
| 21 | Pricing Intelligence Interpretation Process (PIIP) | M | 3/0 | 0 | 5 | layers-zoom |  |
| 22 | Capability Layer | M | 0/0 | 2 | 17 | layers-zoom |  |
| 23 | Holistic Agent for Reasoning on Value and Economic analYsis (H.A.R.V.E | M | 1/0 | 1 | 6 | layers-zoom |  |
| 24 | H.A.R.V.E.Y. Architecture | M | 1/0 | 1 | 7 | architecture-spotlight |  |
| 25 | H.A.R.V.E.Y. Architecture | M | 0/0 | 1 | 7 | architecture-spotlight |  |
| 26 | H.A.R.V.E.Y. Architecture | M | 0/0 | 1 | 7 | architecture-spotlight |  |
| 27 | H.A.R.V.E.Y. Architecture | M | 0/0 | 1 | 7 | architecture-spotlight |  |
| 28 | H.A.R.V.E.Y. Architecture | M | 0/0 | 1 | 7 | architecture-spotlight |  |
| 29 | H.A.R.V.E.Y. Architecture | M | 0/0 | 1 | 7 | architecture-spotlight |  |
| 30 | H.A.R.V.E.Y. Architecture | M | 0/0 | 1 | 7 | architecture-spotlight |  |
| 31 | H.A.R.V.E.Y. Architecture | M | 0/0 | 1 | 7 | architecture-spotlight |  |
| 32 | Evaluation | — | 0/0 | 0 | 17 | rq-cards |  |
| 33 | Methodology | M | 17/0 | 3 | 19 |  | sí |
| 34 | Methodology | M | 12/0 | 3 | 14 | methodology-funnel |  |
| 35 | Current Coverage of PI Needs | — | 2/0 | 0 | 9 | coverage-panels |  |
| 36 | Strategy and Value Accuracy | M | 2/0 | 5 | 5 |  | sí |
| 37 | Strategy and Value Accuracy | — | 0/0 | 0 | 24 | results-table |  |
| 38 | Strategy and Value Accuracy | — | 0/0 | 0 | 22 |  | sí |
| 39 | Strategy and Value Accuracy | — | 0/0 | 0 | 22 |  | sí |
| 40 | 17 | — | 0/0 | 1 | 7 | rotating-wheel |  |
| 41 | 17 | M | 0/0 | 2 | 14 | rotating-wheel |  |
| 42 | 17 | M | 0/0 | 3 | 19 | rotating-wheel |  |
| 43 | 17 | M | 0/0 | 4 | 26 | rotating-wheel |  |
| 44 | 17 | M | 0/0 | 5 | 31 | rotating-wheel |  |
| 45 | 17 | M | 0/0 | 6 | 39 | rotating-wheel |  |
| 46 | 17 | M | 0/0 | 6 | 38 |  | sí |
| 47 | 18 | M | 1/0 | 9 | 39 | rotating-wheel |  |
| 48 | Conclusions | M | 5/0 | 3 | 7 |  |  |
| 49 | Pricing Intelligence: Rethinking IS Engineering in Volatile SaaS Envir | — | 0/0 | 6 | 9 |  |  |

## ICSOC'24 SOC4AI (FJCL, 4:3) — extracción de pricings con LLMs

`sources/ICSOC24-SOC4AI-FJCL.pptx` · 45 diapositivas · miniaturas: `ICSOC24-SOC4AI-FJCL-01.jpg`, `ICSOC24-SOC4AI-FJCL-02.jpg`

| # | Título / texto principal | T | Anim | Img | Formas | Componente | Oculta |
| ---: | --- | :-: | :-: | :-: | :-: | --- | :-: |
| 1 | From Static to Intelligent: Evolving SaaS Pricing with LLMs | — | 0/0 | 3 | 8 |  |  |
| 2 | What is a pricing? | — | 12/1 | 12 | 15 | pricing-build-user |  |
| 3 | What is a pricing? | — | 2/0 | 30 | 26 | pricing-build-user |  |
| 4 | What is a pricing? | M | 0/0 | 30 | 26 | pricing-build-user |  |
| 5 | What is a pricing? | — | 5/0 | 35 | 17 | pricing-build-user |  |
| 6 | What is a pricing? | M | 0/0 | 35 | 17 | pricing-build-user |  |
| 7 | What is a pricing? | — | 8/0 | 63 | 41 | pricing-build-user |  |
| 8 | What is a pricing? | M | 5/0 | 68 | 46 | pricing-build-user |  |
| 9 | What is a pricing? | — | 12/0 | 77 | 55 | pricing-build-user |  |
| 10 | What is a pricing? | M | 0/0 | 79 | 57 | pricing-build-user |  |
| 11 | What is a pricing? | M | 2/0 | 81 | 59 | pricing-build-user |  |
| 12 | What is a pricing? | M | 0/0 | 81 | 59 | pricing-build-user |  |
| 13 | What is Pricing4SaaS? | — | 0/0 | 2 | 5 |  |  |
| 14 | What is Pricing4SaaS? | M | 4/0 | 2 | 9 |  |  |
| 15 | What is Pricing2Yaml? | M | 2/0 | 3 | 11 |  |  |
| 16 | What is Pricing2Yaml? | M | 0/0 | 3 | 11 |  |  |
| 17 | What is an iPricing? | — | 12/0 | 1 | 15 |  |  |
| 18 |  | — | 5/0 | 4 | 7 |  |  |
| 19 | What are we proposing? | — | 0/0 | 2 | 4 | diagram-zoom-pan |  |
| 20 |  | M | 0/0 | 1 | 1 | diagram-zoom-pan |  |
| 21 |  | M | 0/0 | 1 | 1 | diagram-zoom-pan |  |
| 22 |  | M | 0/0 | 1 | 1 | diagram-zoom-pan |  |
| 23 |  | M | 0/0 | 1 | 1 | diagram-zoom-pan |  |
| 24 | What is AI4Pricing? | — | 4/0 | 4 | 7 |  |  |
| 25 |  | — | 0/0 | 3 | 4 |  |  |
| 26 |  | M | 0/0 | 3 | 4 |  |  |
| 27 |  | M | 0/0 | 3 | 4 |  |  |
| 28 | How did we evaluate it? | — | 16/0 | 1 | 19 | evaluation-ground-truth |  |
| 29 | How did we evaluate it? | M | 2/0 | 26 | 33 | evaluation-ground-truth |  |
| 30 | How did we evaluate it? | M | 2/0 | 40 | 47 | evaluation-ground-truth |  |
| 31 | How did we evaluate it? | M | 2/0 | 28 | 35 | evaluation-ground-truth |  |
| 32 | How did we evaluate it? | M | 2/0 | 34 | 44 | evaluation-ground-truth |  |
| 33 | How did we evaluate it? | M | 6/0 | 31 | 42 | evaluation-ground-truth |  |
| 34 | What are the results? | — | 8/0 | 1 | 11 |  |  |
| 35 | What are the results? | — | 4/0 | 2 | 8 |  |  |
| 36 | What are the results? | M | 0/0 | 2 | 5 |  |  |
| 37 | What would be the ideal extraction? | — | 1/0 | 2 | 4 |  |  |
| 38 | What would be the ideal extraction? | M | 1/0 | 3 | 5 |  |  |
| 39 | What would be the ideal extraction? | M | 1/0 | 4 | 6 |  |  |
| 40 | What would be the ideal extraction? | M | 1/0 | 5 | 7 |  |  |
| 41 | What would be the ideal extraction? | M | 0/0 | 5 | 7 |  |  |
| 42 |  | M | 0/0 | 5 | 6 |  |  |
| 43 | What challenges arise? | — | 24/0 | 1 | 27 | challenges-hub |  |
| 44 | What are the conclusions? | — | 3/0 | 1 | 6 |  |  |
| 45 | Thanks! | — | 0/0 | 5 | 9 |  |  |

## ICWE'25 (AGF) — feature toggles y herramientas

`sources/ICWE25-AGF.pptx` · 43 diapositivas · miniaturas: `ICWE25-AGF-01.jpg`

| # | Título / texto principal | T | Anim | Img | Formas | Componente | Oculta |
| ---: | --- | :-: | :-: | :-: | :-: | --- | :-: |
| 1 | HORIZON: a Classification and Comparison Framework for Pricing-driven | — | 0/0 | 1 | 4 |  |  |
| 2 |  | — | 8/0 | 7 | 8 |  | sí |
| 3 | 1 | — | 10/0 | 4 | 11 |  |  |
| 4 | User-oriented Pricings | — | 0/0 | 18 | 21 |  |  |
| 5 | User-oriented Pricings | M | 0/0 | 19 | 22 |  |  |
| 6 | User-oriented Pricings | M | 4/0 | 24 | 27 |  |  |
| 7 | User-oriented Pricings | M | 0/0 | 24 | 27 |  |  |
| 8 | User-oriented Pricings | M | 0/0 | 27 | 30 |  |  |
| 9 | How to Measure the Complexity of a Pricing? | M | 0/0 | 83 | 87 |  |  |
| 10 | Traditional DevOps life cyle | — | 9/0 | 0 | 22 |  | sí |
| 11 | Traditional DevOps life cyle | — | 0/0 | 0 | 37 |  | sí |
| 12 | Traditional DevOps life cyle | M | 0/0 | 2 | 30 |  | sí |
| 13 | Pricing-driven Development and Operation of SaaS | — | 0/0 | 8 | 27 |  |  |
| 14 | Pricing-driven Self-adaptation | M | 2/0 | 9 | 29 |  |  |
| 15 | Pricing-driven Self-adaptation | M | 0/0 | 9 | 29 |  |  |
| 16 | Traditional DevOps Life Cycle | — | 0/0 | 0 | 22 |  | sí |
| 17 | Traditional DevOps Life Cycle | — | 0/0 | 0 | 22 |  | sí |
| 18 | Pricing-driven Development and Operation of SaaS | M | 1/0 | 9 | 28 |  | sí |
| 19 | Pricing-driven Development and Operation of SaaS | F | 0/0 | 9 | 30 |  | sí |
| 20 | Pricing-driven Self-adaptation | — | 0/0 | 8 | 27 |  | sí |
| 21 | Pricing-driven Self-adaptation | — | 0/0 | 8 | 27 |  | sí |
| 22 | Feature Toggles | — | 0/0 | 0 | 2 | feature-toggle-anatomy |  |
| 23 | Anatomy of a feature toggle | — | 0/0 | 1 | 4 | feature-toggle-anatomy |  |
| 24 | Anatomy of a feature toggle | M | 9/0 | 2 | 16 | feature-toggle-anatomy |  |
| 25 | 1 | — | 0/0 | 4 | 11 |  |  |
| 26 | 7 | — | 0/0 | 1 | 6 | segment-wheel-build |  |
| 27 | 8 | M | 0/0 | 2 | 12 | segment-wheel-build |  |
| 28 | 8 | M | 0/0 | 3 | 17 | segment-wheel-build |  |
| 29 | 8 | M | 0/0 | 4 | 24 | segment-wheel-build |  |
| 30 | 8 | M | 0/0 | 5 | 29 | segment-wheel-build |  |
| 31 | 8 | M | 0/0 | 6 | 37 | segment-wheel-build |  |
| 32 | 1. Features CRUD Operations | M | 14/11 | 4 | 25 |  | sí |
| 33 | 1. Dynamic evaluation of features | M | 14/8 | 5 | 30 |  | sí |
| 34 | 1. Single feature evaluation | M | 6/0 | 4 | 30 |  | sí |
| 35 | 1. SDK Based | M | 7/0 | 5 | 36 |  | sí |
| 36 | 1. Pricing Model Support | M | 8/0 | 10 | 45 |  | sí |
| 37 | 8 | M | 0/0 | 6 | 37 |  |  |
| 38 | 1 | — | 0/0 | 4 | 11 |  |  |
| 39 | Previous analysis on the support of industry solutions to pricing-driv | — | 10/0 | 6 | 15 | big-stat-out-of |  |
| 40 | Revisiting and Extending Literature Results with HORIZON | — | 5/0 | 6 | 8 | tools-arcs |  |
| 41 | 1 | — | 0/0 | 4 | 11 |  |  |
| 42 | Conclusions | — | 2/0 | 9 | 4 |  |  |
| 43 | HORIZON: a Classification and Comparison Framework for Pricing-driven | — | 0/0 | 3 | 6 |  |  |

## JCIS (AGF) — Pricing-driven DevOps, pirámide L1–L3

`sources/JCIS-AGF-v2.pptx` · 57 diapositivas · miniaturas: `JCIS-AGF-v2-01.jpg`, `JCIS-AGF-v2-02.jpg`

| # | Título / texto principal | T | Anim | Img | Formas | Componente | Oculta |
| ---: | --- | :-: | :-: | :-: | :-: | --- | :-: |
| 1 | Racing the Market: An Industry Support Analysis for Pricing-Driven De | — | 0/0 | 1 | 4 |  |  |
| 2 |  | — | 8/0 | 7 | 8 |  |  |
| 3 | What is this about? | — | 0/0 | 0 | 12 | toc-numbered |  |
| 4 | User-oriented Pricings | — | 0/0 | 18 | 21 |  |  |
| 5 | User-oriented Pricings | M | 0/0 | 19 | 22 |  |  |
| 6 | User-oriented Pricings | M | 4/0 | 24 | 27 |  |  |
| 7 | User-oriented Pricings | M | 0/0 | 24 | 27 |  |  |
| 8 | User-oriented Pricings | M | 0/0 | 27 | 30 |  |  |
| 9 | How to Measure the Complexity of a Pricing? | M | 0/0 | 83 | 87 |  |  |
| 10 | ConfigurationSpace | M | 1/0 | 81 | 84 |  |  |
| 11 | Pricings’ Configuration Space | — | 0/0 | 1 | 10 |  | sí |
| 12 | Pricings’ Configuration Space | M | 0/0 | 5 | 34 |  | sí |
| 13 | Operation of SaaS with Pricing | — | 0/0 | 9 | 20 |  |  |
| 14 | 7 | — | 0/0 | 2 | 5 | feature-toggles-codebase |  |
| 15 | 7 | F | 0/0 | 3 | 8 | feature-toggles-codebase |  |
| 16 | 8 | M | 2/0 | 2 | 16 | feature-toggles-codebase |  |
| 17 | : Evaluation Space | M | 0/0 | 4 | 17 | feature-toggles-codebase |  |
| 18 | What is this about? | — | 0/0 | 0 | 7 | toc-numbered |  |
| 19 | Analysis of the Industry: Research Questions | M | 3/0 | 0 | 5 | rq-circles |  |
| 20 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | — | 16/0 | 12 | 29 | pipeline-flow |  |
| 21 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | M | 0/0 | 12 | 29 | pipeline-flow |  |
| 22 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | M | 0/0 | 1 | 11 |  |  |
| 23 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | M | 0/0 | 1 | 10 |  |  |
| 24 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | M | 0/0 | 1 | 11 |  |  |
| 25 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | M | 0/0 | 1 | 13 |  |  |
| 26 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | M | 0/0 | 1 | 8 |  |  |
| 27 | RQ1: How are pricings’ configuration and evaluation spaces evolving in | M | 1/0 | 2 | 12 |  |  |
| 28 | RQ2: Are current feature toggling tools appropriate for optimizing pri | M | 0/0 | 5 | 15 | pyramid-levels |  |
| 29 | RQ2: Are current feature toggling tools appropriate for optimizing pri | M | 0/0 | 0 | 3 | pyramid-levels |  |
| 30 | RQ2: Are current feature toggling tools appropriate for optimizing pri | — | 0/0 | 5 | 9 | pyramid-levels |  |
| 31 | RQ2: Are current feature toggling tools appropriate for optimizing pri | M | 0/0 | 5 | 10 | pyramid-levels |  |
| 32 | RQ2: Are current feature toggling tools appropriate for optimizing pri | M | 0/0 | 2 | 8 | pyramid-levels |  |
| 33 | RQ2: Are current feature toggling tools appropriate for optimizing pri | M | 0/0 | 3 | 10 |  |  |
| 34 | RQ2: Are current feature toggling tools appropriate for optimizing pri | M | 5/1 | 1 | 8 |  |  |
| 35 | RQ3: Does current feature toggling tools’ underlying models provide en | M | 0/0 | 0 | 2 |  |  |
| 36 | RQ3: Does current feature toggling tools’ underlying models provide en | M | 3/0 | 0 | 5 |  |  |
| 37 | RQ3: Does Pricing2Yaml provide enough expressiveness to represent real | M | 4/0 | 2 | 6 | ribbon-numbered |  |
| 38 | What is this about? | — | 0/0 | 0 | 7 |  |  |
| 39 | Conclusions | M | 2/0 | 2 | 5 |  |  |
| 40 | Pricing-driven Development & Operation of SaaS | — | 0/0 | 1 | 3 |  |  |
| 41 | Traditional DevOps life cyle | — | 9/0 | 0 | 22 |  |  |
| 42 | Traditional DevOps life cyle | — | 0/0 | 0 | 37 |  |  |
| 43 | Traditional DevOps life cyle | M | 0/0 | 2 | 30 |  |  |
| 44 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 11 | 42 |  |  |
| 45 | Pricing-driven Development and Operation of SaaS | F | 0/0 | 12 | 40 |  |  |
| 46 | Racing the Market: An Industry Support Analysis for Pricing-Driven De | — | 0/0 | 2 | 5 |  |  |
| 47 | Extra Slides | M | 0/0 | 0 | 1 |  |  |
| 48 | Pricing-driven Development and Operation of SaaS | M | 5/0 | 8 | 44 | devops-numbered-overview |  |
| 49 | Pricing-driven Development and Operation of SaaS | M | 1/0 | 9 | 45 | devops-numbered-overview |  |
| 50 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 9 | 47 | devops-numbered-overview |  |
| 51 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 8 | 44 | devops-numbered-overview |  |
| 52 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 9 | 45 | devops-numbered-overview |  |
| 53 | Pricing-driven Development and Operation of SaaS | M | 1/0 | 9 | 45 | devops-numbered-overview |  |
| 54 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 8 | 44 | devops-numbered-overview |  |
| 55 | Pricing-driven Development and Operation of SaaS | — | 0/0 | 10 | 45 |  |  |
| 56 | Pricing-driven Development and Operation of SaaS | M | 4/2 | 14 | 48 |  |  |
| 57 | Pricing-driven Development and Operation of SaaS | M | 0/0 | 8 | 39 |  |  |

## PhD Forum feb. 2026 (AGF) — tesis Pricing-driven DevOps

`sources/PhD_Forum_FEBRERO_2026_-_AGF.pptx` · 57 diapositivas · miniaturas: `PhD_Forum_FEBRERO_2026_-_AGF-01.jpg`, `PhD_Forum_FEBRERO_2026_-_AGF-02.jpg`

| # | Título / texto principal | T | Anim | Img | Formas | Componente | Oculta |
| ---: | --- | :-: | :-: | :-: | :-: | --- | :-: |
| 1 | Pricing-driven Development and Operation of SaaS | — | 0/0 | 2 | 5 |  |  |
| 2 | Table of Contents | — | 0/0 | 0 | 3 | toc-list |  |
| 3 | “The best software is the software that knows exactly what you need,   | — | 0/0 | 0 | 4 | quote-hook |  |
| 4 | Customization | — | 0/0 | 0 | 2 | statement-hooks |  |
| 5 | Web systems have exploded from offering tens of configurations to lite | — | 0/0 | 0 | 3 | statement-hooks |  |
| 6 | Pricing-driven Development & Operation | — | 0/0 | 0 | 2 | statement-hooks |  |
| 7 | 5 | M | 0/0 | 18 | 21 |  |  |
| 8 | 5 | M | 0/0 | 19 | 22 |  |  |
| 9 | 5 | M | 4/0 | 24 | 27 |  |  |
| 10 | 5 | M | 0/0 | 24 | 27 |  |  |
| 11 | 5 | M | 0/0 | 27 | 30 |  |  |
| 12 | 5 | M | 0/0 | 189 | 83 |  |  |
| 13 | ConfigurationSpace | M | 1/0 | 189 | 84 |  |  |
| 14 | Pricing-driven Development and Operation | — | 0/0 | 0 | 2 |  |  |
| 15 | Feature Toggles | M | 0/0 | 9 | 22 |  |  |
| 16 | Anatomy of a Feature Toggle | — | 4/0 | 1 | 7 |  |  |
| 17 | Anatomy of an Evaluation Expression | — | 7/0 | 9 | 10 | evaluation-expression |  |
| 18 | Curse of Customization | — | 0/0 | 1 | 11 |  |  |
| 19 | Curse of Customization | M | 0/0 | 5 | 34 |  |  |
| 20 | Curse of Customization | — | 0/0 | 1 | 8 |  |  |
| 21 | Curse of Customization | — | 0/0 | 1 | 4 |  |  |
| 22 | Pricing-driven Development and Operation | — | 0/0 | 0 | 2 |  |  |
| 23 | Traditional DevOps life cyle | M | 0/0 | 2 | 29 |  |  |
| 24 | Pricing-driven Development and Operation | M | 0/0 | 11 | 10 |  |  |
| 25 | Table of Contents | — | 0/0 | 0 | 3 | toc-list |  |
| 26 | Pricing & Subscription Modeling | M | 0/0 | 8 | 9 |  |  |
| 27 | The iPricing metamodel | M | 0/0 | 1 | 4 |  |  |
| 28 | The iSubscription metamodel | M | 3/0 | 1 | 7 |  |  |
| 29 | Table of Contents | — | 0/0 | 0 | 3 |  |  |
| 30 | Pricing Design | M | 0/0 | 8 | 11 |  |  |
| 31 | The “Pricification” Process | — | 23/1 | 15 | 27 | pricification-timeline |  |
| 32 | The “Pricification” Process | — | 7/0 | 12 | 29 | pricification-timeline |  |
| 33 | The “Pricification” Process | — | 0/0 | 1 | 3 | pricification-timeline |  |
| 34 | The “Pricification” Process | — | 7/0 | 12 | 36 | pricification-timeline |  |
| 35 | The “Pricification” Process | — | 1/0 | 1 | 3 |  | sí |
| 36 | The “Pricification” Process | — | 0/0 | 1 | 2 |  | sí |
| 37 | Table of Contents | — | 0/0 | 0 | 3 |  |  |
| 38 | Pricing-driven Self-Adaptation | M | 0/0 | 8 | 5 |  |  |
| 39 | SPACE: Subscription and Pricing Access Control Engine | M | 0/0 | 1 | 4 |  |  |
| 40 | Table of Contents | — | 0/0 | 0 | 3 |  |  |
| 41 | Pricing Design | M | 0/0 | 8 | 11 |  |  |
| 42 | Subscription Compliance Testing | — | 1/0 | 3 | 4 |  |  |
| 43 | Table of Contents | — | 0/0 | 0 | 3 |  |  |
| 44 | Automated Analysis of Pricings | M | 0/0 | 8 | 11 |  |  |
| 45 | Automated Analysis of Pricings | M | 3/0 | 6 | 11 |  |  |
| 46 | PRIME: PRicing Model analysis Engine | M | 0/0 | 1 | 5 |  |  |
| 47 | PRIME: PRicing Model analysis Engine | M | 15/0 | 2 | 18 |  |  |
| 48 | ACCESIBILITY LAYER | M | 3/0 | 1 | 5 |  |  |
| 49 | HARVEY | M | 1/0 | 1 | 7 |  |  |
| 50 | HARVEY | — | 2/0 | 2 | 9 |  |  |
| 51 | HARVEY | M | 4/0 | 4 | 24 |  |  |
| 52 | Table of Contents | — | 0/0 | 0 | 3 |  |  |
| 53 | Conclusions & Future Work | — | 6/0 | 8 | 9 | chevron-steps |  |
| 54 | Conclusions & Future Work | — | 1/0 | 1 | 4 | chevron-steps |  |
| 55 | Conclusions & Future Work | M | 0/0 | 1 | 4 | chevron-steps |  |
| 56 | Conclusions & Future Work | F | 2/0 | 3 | 6 | chevron-steps |  |
| 57 | Pricing-driven Development and Operation of SaaS | — | 0/0 | 3 | 6 |  |  |

## SCORE 2025 (FJCL) — QACO → PACO, personaje que piensa

`sources/SCORE_2025_-_FJCL.pptx` · 49 diapositivas · miniaturas: `SCORE_2025_-_FJCL-01.jpg`

| # | Título / texto principal | T | Anim | Img | Formas | Componente | Oculta |
| ---: | --- | :-: | :-: | :-: | :-: | --- | :-: |
| 1 | QoS meets Pricing | — | 0/0 | 3 | 6 |  |  |
| 2 | QoS-Aware Composition (QACO/QSWSC) | — | 2/0 | 2 | 4 |  | sí |
| 3 | QoS-Aware Composition (QACO) | — | 0/0 | 1 | 3 | thinking-character-story |  |
| 4 | QoS-Aware Composition (QACO) | — | 10/0 | 5 | 12 | thinking-character-story |  |
| 5 | QoS-Aware Composition (QACO) | M | 7/0 | 5 | 19 | thinking-character-story |  |
| 6 | QoS-Aware Composition (QACO) | M | 4/0 | 5 | 20 | thinking-character-story |  |
| 7 | QoS-Aware Composition (QACO) | — | 5/4 | 1 | 16 | thinking-character-story |  |
| 8 | QoS-Aware Composition (QACO) | — | 13/0 | 9 | 16 | thinking-character-story |  |
| 9 | QoS-Aware Composition (QACO) | — | 11/0 | 1 | 22 | thinking-character-story |  |
| 10 | QoS-Aware Composition (QACO) | — | 5/0 | 5 | 15 | thinking-character-story |  |
| 11 | QoS-Aware Composition (QACO) | — | 14/4 | 0 | 25 |  | sí |
| 12 | QoS-Aware Composition (QACO) | M | 1/0 | 0 | 24 | thinking-character-story |  |
| 13 | QACO Servitization | — | 12/0 | 0 | 16 |  |  |
| 14 | QoS-Aware Composition (QACO) | — | 6/0 | 1 | 9 |  | sí |
| 15 | QACO Model | — | 10/0 | 0 | 12 |  | sí |
| 16 | QACO Model | — | 1/0 | 0 | 13 |  | sí |
| 17 | QACO Model | M | 0/0 | 0 | 13 |  | sí |
| 18 | QACO Model | M | 0/0 | 0 | 13 |  | sí |
| 19 | QACO Model | M | 0/0 | 0 | 12 |  | sí |
| 20 | QACO Servitization | — | 12/0 | 0 | 16 |  |  |
| 21 | QACO Servitization | — | 1/1 | 0 | 17 |  |  |
| 22 | QACO Servitization | — | 1/0 | 0 | 17 |  |  |
| 23 | QACO Servitization | M | 6/0 | 0 | 22 |  | sí |
| 24 | QACO Servitization | M | 0/0 | 0 | 20 |  | sí |
| 25 | QACO Servitization | — | 0/0 | 2 | 4 |  |  |
| 26 | QACO Limitations: Pricing | — | 0/0 | 27 | 29 |  |  |
| 27 | QACO Limitations: Mono-configuration vs multi-configuration | — | 2/0 | 3 | 7 |  |  |
| 28 | QoS and Pricing: Extra-functional features vs functional feautres | — | 1/0 | 27 | 5 |  |  |
| 29 | QoS and Pricing | — | 8/0 | 27 | 37 |  | sí |
| 30 | QoS and Pricing | — | 0/0 | 0 | 3 | strike-replace |  |
| 31 | QoS and Pricing | M | 1/0 | 0 | 4 | strike-replace |  |
| 32 | QoS and Pricing | M | 0/0 | 0 | 4 | strike-replace |  |
| 33 | Pricing-Aware Composition (PACO) | — | 1/0 | 0 | 19 |  |  |
| 34 | Pricing-Aware Composition (PACO) | M | 18/0 | 0 | 37 |  |  |
| 35 | Pricing-Aware Composition (PACO) | M | 1/0 | 0 | 38 |  |  |
| 36 | Pricing-Aware Composition (PACO) | — | 0/0 | 0 | 11 |  | sí |
| 37 | Pricing-Aware Composition (PACO) | — | 0/0 | 0 | 8 |  | sí |
| 38 | Pricing-Aware Composition (PACO) | — | 0/0 | 0 | 12 |  | sí |
| 39 | Pricing-Aware Composition (PACO) | — | 0/0 | 0 | 16 |  |  |
| 40 | 37 SaaS Config Space (13568;11776;11268;10367;1896;1152;786;85;79;44;4 | — | 0/0 | 0 | 2 |  |  |
| 41 | Pricing-Aware Composition (PACO) | — | 12/0 | 0 | 14 | puzzle-pieces |  |
| 42 | Future Work | — | 4/0 | 0 | 6 | numbered-points-0104 |  |
| 43 | Conclusions | — | 3/0 | 0 | 5 | conclusions-icons |  |
| 44 | QoS meets Pricing | — | 0/0 | 5 | 8 |  |  |
| 45 | Capacity Analysis | — | 0/0 | 1 | 4 |  |  |
| 46 | Capacity Curves | — | 0/0 | 1 | 3 |  |  |
| 47 | Capacity Curves with Overage | — | 0/0 | 1 | 3 |  |  |
| 48 | Combined Capacity Curves | — | 0/0 | 1 | 3 |  |  |
| 49 | Combined Capacity Curves | — | 0/0 | 1 | 5 |  |  |
