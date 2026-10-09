# isa-score-slides

Marketplace de plugins de Claude con **ISA · SCORE Presentaciones**: presentaciones académicas con el estilo del ISA Research Group / SCORE Lab (Universidad de Sevilla), entregadas como PowerPoint nativo con Morph y animaciones.

Autores: **Francisco Javier Cavero López** y **Alejandro García Fernández**.

Guía de uso (qué hace, qué necesita, cómo pedirlo): [`plugins/isa-score-presentaciones/README.md`](plugins/isa-score-presentaciones/README.md).

## Montar el repositorio (primera vez)

Si recibiste el zip completo en partes (`isa-score-slides.zip.part-aa`, `-ab`, …), únelas y descomprime:

```bash
cat isa-score-slides.zip.part-* > isa-score-slides.zip     # Windows: copy /b isa-score-slides.zip.part-* isa-score-slides.zip
unzip isa-score-slides.zip && cd isa-score-slides
```

Si recibiste la versión ligera (sin las presentaciones fuente ni la biblioteca), complétala con tus originales: los 7 .pptx (CAiSE'26, CAiSE'25, ICWE'25, JCIS, PhD Forum 2026, SCORE 2025, ICSOC'24) y los 3 `isa-score-library-part*.zip`. Se reconocen por su huella, da igual el nombre:

```bash
python3 completar-material.py ~/Descargas          # la carpeta (o carpetas) donde estén
git init -b main && git add -A && git commit -m "ISA · SCORE Presentaciones"
gh repo create javiercavlop/isa-score-slides --private --source . --push
```

Sin `gh`: crea el repositorio privado vacío `isa-score-slides` en github.com y haz `git remote add origin https://github.com/javiercavlop/isa-score-slides.git && git push -u origin main`.

## Instalar

**Cowork (app de escritorio):** *Customize → Plugins → Add marketplace* → `javiercavlop/isa-score-slides` → instala **isa-score-presentaciones**. Para recibir cambios: *Update* en el marketplace.

**Claude Code:**

```bash
/plugin marketplace add javiercavlop/isa-score-slides
/plugin install isa-score-presentaciones@isa-score-slides
```

El repositorio es privado: quien lo instale necesita acceso de lectura en GitHub.

**Claude Design / Claude Slides (claude.ai):** no instalan plugins. Diseña allí con el sistema de diseño publicado «Presentaciones SCORE Lab - ISA Group» (ya incluye las reglas obligatorias) y, para el PowerPoint con Morph y animaciones, abre el deck en Cowork con el plugin instalado y pide convertirlo.

## Comprobar que no falta nada

```bash
cd plugins/isa-score-presentaciones && sha256sum -c MANIFEST.sha256
```

## Tamaño

≈ 180 MB (límite de un plugin: 200 MB descomprimido; ningún fichero supera los 100 MB de GitHub). La mayor parte son las 7 presentaciones fuente (`sources/`) y la biblioteca de componentes sin pérdidas (`kit/library/`).

## Licencia

CC BY 4.0 + autorización adicional para las presentaciones generadas — ver [`LICENSE`](LICENSE).
