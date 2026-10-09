# Logos

Logos and affiliation marks exactly as they appear in the source decks (raster, copied from the PowerPoint packages). Place them on white only; never recolour, crop or redraw.

- `isa-logo.jpeg` — ISA research group (red ring + "isa" wordmark). Title/closing row, LEFT, ≈ 2.1 in wide.
- `score-logo.png` — SCORE "Unidad de Excelencia Smart Computer Systems Research and Engineering", transparent. Title/closing row, CENTRE, ≈ 2.4 in wide.
- `us-logo.png` — Universidad de Sevilla (angel + "Universidad de Sevilla 1505"), transparent. Title/closing row, RIGHT, ≈ 2.1 in wide.
- `us-seal.png` — circular US seal used by the master's title layout (top-right).
- `i3us-logo.png` — I3US Instituto de Investigación; PhD Forum title row.
- `score-us-lockup.jpeg` — SCORE + US lockup in one piece (CAiSE'25 / ICWE'25 title slides) — replaces the centre + right logos.
- `junta-andalucia.png` — Junta de Andalucía funding mark; closing slide, bottom-right, ≈ 0.72 in tall.
- `funding-ministerio-nextgen.png` — Ministerio de Ciencia, Innovación y Universidades + NextGenerationEU + PRTR + AEI strip; closing slide, right of the Junta mark, ≈ 0.72 in tall.

These are uploads in the system's asset store, not files: a `{artifact, path}` file copy cannot reach them. Copy them into another artifact with an asset copy (`asset: true`, `from_url` = this system, `asset_ids` below) and use the `/_blob/<id>` URL it returns; `read` an id as `path` to get the file.

| file | asset id |
| --- | --- |
| `isa-logo.jpeg` | `9a42961eda95344f8885cb661961d17f` |
| `score-logo.png` | `a66d93d8d4131d2e095b740e46f3d5c1` |
| `us-logo.png` | `fda0a8473d156f6bfe30c354e29106e1` |
| `us-seal.png` | `0ae31f8004eb53f62c533ff4de645391` |
| `i3us-logo.png` | `0ae6538e1feb3ae5462929eb98c8a0c2` |
| `score-us-lockup.jpeg` | `e61f48ec9bf1db0f10c2c10972e3d303` |
| `junta-andalucia.png` | `9331b710110943e22835dad7cbcacb75` |
| `funding-ministerio-nextgen.png` | `f08e65d5c9d5112f3f10d8bb7141ba5e` |

If an id ever differs from the record in `design-system.json` (`assetGroups.Logos.files`), the index is right.

The same files are embedded in `kit/isa-score-template.pptx.b64.txt` (hidden seed slide, shapes named `asset:<file stem>`), so `kit/isa_deck.py` places them with `d.logo(slide, "score-logo", x, y, w)`.
