# ISA · SCORE Slides — (c) 2026 Francisco Javier Cavero López y Alejandro García Fernández
# (SCORE Lab, I3US, Universidad de Sevilla; Grupo ISA). Licencia CC BY 4.0 — ver LICENSE.
"""Arregla las cascadas de un deck de Claude Slides para que las piezas aparezcan UNA A UNA.

En Claude Slides, todas las piezas con el mismo `order` aparecen a la vez; un paso es automático solo
si todas sus piezas llevan `auto`. Un error típico es escribir varias piezas con «order 3 auto»
esperando una cascada. Este script renumera los `data-build-in` de cada diapositiva:
  - las piezas de un mismo `order` SIN `auto` siguen juntas (un clic);
  - cada pieza con `auto` pasa a tener su propio paso, en el orden en que aparece en el HTML;
  - en los conectores (`<x-connector x1 y1 x2 y2>`) el efecto se ajusta al sentido de la flecha
    (left →, right ←, drop ↓, rise ↑).

    python3 slides_cascade_fix.py DECK_DIR/project/slides [id ...]     (sin ids: todas)
Reescribe los .html en su sitio; revisa el resultado en el visor antes de convertir.
"""
import glob, os, re, sys

RX = re.compile(r'data-build-in="(\w+) order (\d+)( auto)?"')


def fix(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    ents = []
    for i, l in enumerate(lines):
        m = RX.search(l)
        if m:
            ents.append((i, m.group(1), int(m.group(2)), bool(m.group(3))))
    groups = {}
    for e in ents:
        groups.setdefault(e[2], []).append(e)
    step, assign = 0, {}
    for o in sorted(groups):
        g = groups[o]
        clicks = [e for e in g if not e[3]]
        autos = [e for e in g if e[3]]
        if clicks:
            step += 1
            for e in clicks:
                assign[e[0]] = (step, False)
        for e in sorted(autos, key=lambda e: e[0]):
            step += 1
            assign[e[0]] = (step, True)
    for i, eff, _, _ in ents:
        l = lines[i]
        n, auto = assign[i]
        if l.lstrip().startswith("<x-connector"):
            c = {k: float(v) for k, v in re.findall(r'\b(x1|y1|x2|y2)="(-?[\d.]+)"', l)}
            if len(c) == 4:
                dx, dy = c["x2"] - c["x1"], c["y2"] - c["y1"]
                eff = ("left" if dx > 0 else "right") if abs(dx) >= abs(dy) else ("drop" if dy > 0 else "rise")
        lines[i] = RX.sub(f'data-build-in="{eff} order {n}{" auto" if auto else ""}"', l)
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return step


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    d = sys.argv[1]
    ids = sys.argv[2:] or [os.path.basename(p)[:-5] for p in sorted(glob.glob(os.path.join(d, "*.html")))]
    for sid in ids:
        print(sid, fix(os.path.join(d, sid + ".html")), "pasos")
