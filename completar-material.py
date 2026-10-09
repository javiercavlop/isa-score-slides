#!/usr/bin/env python3
"""Coloca en el repositorio los ficheros grandes (las 7 presentaciones fuente y la biblioteca de
componentes) a partir de los originales que ya tienes, y comprueba byte a byte que todo está.

    python3 completar-material.py CARPETA [CARPETA ...]

CARPETA: donde estén tus originales (se busca también en subcarpetas). Los ficheros se reconocen por
su huella SHA-256, no por el nombre, así que da igual cómo se llamen en tu equipo:
  - las 7 presentaciones (.pptx): CAiSE'26, CAiSE'25, ICWE'25, JCIS, PhD Forum 2026, SCORE 2025, ICSOC'24
  - isa-score-library-part1.zip, -part2.zip y -part3.zip
Al final verifica TODO el plugin contra plugins/isa-score-presentaciones/MANIFEST.sha256.
Solo usa la biblioteca estándar de Python 3.
"""
import hashlib, os, shutil, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.join(HERE, "plugins", "isa-score-presentaciones")
SKILL = os.path.join(PLUGIN, "skills", "isa-score-presentacion")

DECKS = {
    "9e02cba7640bdd96e354c21e0fe8c05e9427c1ca4a26cd5edf0aaaa8d5566095": "CAiSE_2026_-_FJCL.pptx",
    "3d5b36ed0f491ebdf85c8dfa0e576d9c28a7f58eb775d51f4666590bfee11c0a": "CAISE25-AGF.pptx",
    "d924972553d43a254b03c83c1e506229796db25757afc9861a3a4169ec23bf90": "ICWE25-AGF.pptx",
    "6faa7469d6527acf1aa4a22779730300c5dc9184f8009257261c575b1600d2c3": "JCIS-AGF-v2.pptx",
    "2ea643406ccb01b73fa9615a1448fa089f83065498bf92edc223b3cbe4947421": "PhD_Forum_FEBRERO_2026_-_AGF.pptx",
    "381ae0cc5cc4c6889b944e9e392129dd3e65967487b4219853710c0d1eb99ab3": "SCORE_2025_-_FJCL.pptx",
    "5a31c49bdf8911e482a0b8db2a412badde66165b2e91fccac23c31e180d6984a": "ICSOC24-SOC4AI-FJCL.pptx",
}
LIBRARY_ZIPS = {
    "76e3aa108543c4b96d7a1cd8c630532e988a40edb6bfc5f3dacbd81defa6bd27": "isa-score-library-part1.zip",
    "8f90d700cd998bcda398bb4196e7e209c9798b3b69b010ac32bf4872f602111f": "isa-score-library-part2.zip",
    "e9104916aa9d676579204dd7f3fd354f1dcdf84746e9e52f29977b4612c9c278": "isa-score-library-part3.zip",
}


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main(folders):
    found = {}
    for folder in folders:
        for root, _, files in os.walk(os.path.expanduser(folder)):
            for n in files:
                if n.lower().endswith((".pptx", ".zip")):
                    p = os.path.join(root, n)
                    d = sha(p)
                    if d in DECKS or d in LIBRARY_ZIPS:
                        found.setdefault(d, p)
    os.makedirs(os.path.join(SKILL, "sources"), exist_ok=True)
    lib = os.path.join(SKILL, "kit", "library")
    os.makedirs(lib, exist_ok=True)
    for d, name in DECKS.items():
        if d in found:
            shutil.copyfile(found[d], os.path.join(SKILL, "sources", name))
            print("ok  ", name, "<-", found[d])
    for d, name in LIBRARY_ZIPS.items():
        if d in found:
            with zipfile.ZipFile(found[d]) as z:
                for i in z.infolist():
                    if i.is_dir():
                        continue
                    base = os.path.basename(i.filename)
                    out = "LICENSE-library.txt" if base == "LICENSE" else base
                    with z.open(i) as src, open(os.path.join(lib, out), "wb") as dst:
                        shutil.copyfileobj(src, dst)
            print("ok  ", name, "<-", found[d])
    missing = [n for d, n in {**DECKS, **LIBRARY_ZIPS}.items() if d not in found]
    for n in missing:
        print("FALTA", n, "(no se encontró ningún fichero con su huella)")

    bad = 0
    with open(os.path.join(PLUGIN, "MANIFEST.sha256"), encoding="utf-8") as f:
        for line in f:
            digest, rel = line.rstrip("\n").split("  ", 1)
            p = os.path.join(PLUGIN, rel[2:] if rel.startswith("./") else rel)
            if not os.path.exists(p):
                print("NO ESTÁ ", rel); bad += 1
            elif sha(p) != digest:
                print("DISTINTO", rel); bad += 1
    print("\nTodo completo y verificado." if bad == 0 else f"\n{bad} fichero(s) faltan o difieren.")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
