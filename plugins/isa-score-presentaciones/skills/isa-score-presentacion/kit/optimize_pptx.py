# ISA · SCORE Slides — (c) 2026 Francisco Javier Cavero López y Alejandro García Fernández
# (SCORE Lab, I3US, Universidad de Sevilla; Grupo ISA). Licencia CC BY 4.0 — ver LICENSE.
# Las presentaciones generadas con este kit pueden usarse libremente sin atribución (LICENSE, parte 2).
# ISA · SCORE Slides — optimize_pptx.py
# Reduce el peso de un .pptx SIN tocar formas, Morph ni animaciones: solo recomprime sus imágenes
# según el tamaño al que se muestran realmente en las diapositivas.
#   · Cada imagen se reescala a 2× su mayor tamaño visible (se tiene en cuenta el recorte srcRect y
#     las copias ampliadas por Morph/zoom en otras diapositivas). Nunca se amplía.
#   · PNG opaco y fotográfico → JPEG (q 88), renombrando la parte y sus referencias.
#   · PNG con transparencia → paleta de 256 colores solo si el error visual es imperceptible.
#   · Se eliminan medios huérfanos que ninguna relación referencia.
#   python optimize_pptx.py in.pptx [out.pptx]        (sin out: reescribe in.pptx)
#   python optimize_pptx.py --b64 kit/library/*.pptx.b64.txt   (trabaja sobre las copias base64 del design system)
import base64, io, math, os, posixpath, re, sys, zipfile
from PIL import Image, ImageChops, ImageStat

EMU_PX = 6350          # 1 px de un lienzo de 1920 px
SCALE = 2.0            # margen para pantallas HiDPI y zoom de Morph
MIN_BYTES = 60_000     # imágenes menores no compensan


def _abs(base, target):
    return posixpath.normpath(posixpath.join(posixpath.dirname(base), target))


def _display_sizes(z):
    """{media part: (max visible width px, max visible height px) | None} over every slide/layout/master.
    Group scaling (chExt → ext) and srcRect crops are taken into account; None = size unknown → no resize."""
    from lxml import etree
    A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    sizes, names = {}, set(z.namelist())

    def put(p, w, h):
        if p is None:
            return
        if w is None:
            sizes.setdefault(p, None)
            if p in sizes and sizes[p] is not None:
                sizes[p] = None  # also used somewhere we cannot measure
            return
        if p in sizes and sizes[p] is None:
            return
        ow, oh = sizes.get(p) or (0, 0)
        sizes[p] = (max(ow, w), max(oh, h))

    for n in names:
        if not re.match(r"ppt/(slides|slideLayouts|slideMasters)/[^/]+\.xml$", n):
            continue
        rels = posixpath.join(posixpath.dirname(n), "_rels", posixpath.basename(n) + ".rels")
        rmap = {}
        if rels in names:
            for r in etree.fromstring(z.read(rels)):
                if r.get("TargetMode") != "External":
                    rmap[r.get("Id")] = _abs(n, r.get("Target"))
        root = etree.fromstring(z.read(n))

        def scale_of(el):
            sx = sy = 1.0
            g = el.getparent()
            while g is not None:
                if g.tag.endswith("}grpSp"):
                    x = g.find("{*}grpSpPr/" + A + "xfrm")
                    if x is not None and x.find(A + "chExt") is not None and x.find(A + "ext") is not None:
                        ce, e = x.find(A + "chExt"), x.find(A + "ext")
                        if int(ce.get("cx")) and int(ce.get("cy")):
                            sx *= int(e.get("cx")) / int(ce.get("cx")); sy *= int(e.get("cy")) / int(ce.get("cy"))
                g = g.getparent()
            return sx, sy

        for blip in root.iter(A + "blip"):
            p = rmap.get(blip.get(R + "embed"))
            if p is None:
                continue
            bf = blip.getparent()
            owner = bf.getparent()
            if owner.tag.endswith("}bgPr"):
                put(p, 1920, 1080); continue
            if owner.tag.endswith("}spPr"):
                owner = owner.getparent()
            ext = owner.find("{*}spPr/" + A + "xfrm/" + A + "ext")
            if ext is None:
                put(p, None, None); continue
            sx, sy = scale_of(owner)
            fx = fy = 1.0
            sr = bf.find(A + "srcRect")
            if sr is not None:
                fx = max(0.05, 1 - (int(sr.get("l", 0)) + int(sr.get("r", 0))) / 100000)
                fy = max(0.05, 1 - (int(sr.get("t", 0)) + int(sr.get("b", 0))) / 100000)
            put(p, int(ext.get("cx")) * sx / EMU_PX / fx, int(ext.get("cy")) * sy / EMU_PX / fy)
        for e in root.iter():
            v = e.get(R + "embed") or e.get(R + "link")
            if v and e.tag != A + "blip":
                put(rmap.get(v), None, None)
    return sizes


def _rms(a, b):
    d = ImageChops.difference(a.convert("RGB"), b.convert("RGB"))
    return math.sqrt(sum(v * v for v in ImageStat.Stat(d).rms) / 3)


def _flatten(im):
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bg.paste(im, mask=im.getchannel("A") if im.mode == "RGBA" else None)
    return bg


def _recompress(blob, ext, disp):
    """→ (new blob, new ext) or None."""
    im = Image.open(io.BytesIO(blob))
    im.load()
    if im.mode in ("P", "LA", "L"):
        im = im.convert("RGBA")
    if disp:
        tw = min(im.width, math.ceil(disp[0] * SCALE))
        th = min(im.height, math.ceil(disp[1] * SCALE))
        r = max(tw / im.width, th / im.height)
        if r < 0.97:
            im = im.resize((max(1, round(im.width * r)), max(1, round(im.height * r))), Image.LANCZOS)
    opaque = im.mode != "RGBA" or im.getchannel("A").getextrema()[0] == 255
    cands = []
    if ext in ("jpg", "jpeg"):
        o = io.BytesIO(); im.convert("RGB").save(o, "JPEG", quality=88, optimize=True, progressive=True)
        cands.append((o.getvalue(), ext))
    else:
        o = io.BytesIO(); im.save(o, "PNG", optimize=True); cands.append((o.getvalue(), "png"))
        rgba = im.convert("RGBA")
        q = rgba.quantize(256, method=Image.FASTOCTREE, dither=Image.FLOYDSTEINBERG)
        if _rms(_flatten(rgba), _flatten(q.convert("RGBA"))) < 2.5:
            o = io.BytesIO(); q.save(o, "PNG", optimize=True); cands.append((o.getvalue(), "png"))
        if opaque:
            o = io.BytesIO(); im.convert("RGB").save(o, "JPEG", quality=88, optimize=True, progressive=True)
            cands.append((o.getvalue(), "jpeg"))
    best = min(cands, key=lambda c: len(c[0]))
    # keep PNG unless JPEG is clearly smaller (screenshots with text stay crisp as PNG)
    png = min((c for c in cands if c[1] != "jpeg"), key=lambda c: len(c[0]), default=None)
    if best[1] == "jpeg" and png and len(png[0]) < len(best[0]) * 1.6:
        best = png
    return best if len(best[0]) < len(blob) * 0.92 else None


def optimize(src, dst=None, verbose=True):
    dst = dst or src
    zin = zipfile.ZipFile(src)
    names = zin.namelist()
    data = {n: zin.read(n) for n in names}
    zin.close()
    disp = _display_sizes(zipfile.ZipFile(io.BytesIO(_rezip(data))))
    referenced = set()
    for n, b in data.items():
        if n.endswith(".rels"):
            base = posixpath.dirname(posixpath.dirname(n))
            src_part = posixpath.join(base, posixpath.basename(n)[:-5])
            for t, mode in re.findall(r'Target="([^"]+)"(?:[^>]*TargetMode="(\w+)")?', b.decode("utf8")):
                if mode != "External":
                    referenced.add(_abs(src_part, t) if not t.startswith("/") else t.lstrip("/"))
    renames, before, removed = {}, sum(len(b) for b in data.values()), 0
    for n in [n for n in names if n.startswith("ppt/media/")]:
        if n not in referenced:
            del data[n]; removed += 1; continue
        ext = n.rsplit(".", 1)[-1].lower()
        if ext not in ("png", "jpg", "jpeg") or len(data[n]) < MIN_BYTES:
            continue
        try:
            r = _recompress(data[n], ext, disp.get(n))
        except Exception as ex:  # unreadable image: leave as is
            if verbose: print("  skip", n, ex)
            continue
        if not r:
            continue
        blob, new_ext = r
        if new_ext != ext and new_ext == "jpeg":
            nn = n.rsplit(".", 1)[0] + ".jpeg"
            k = 1
            while nn in data:
                nn = n.rsplit(".", 1)[0] + f"_{k}.jpeg"; k += 1
            del data[n]; data[nn] = blob; renames[n] = nn
        else:
            data[n] = blob
    if renames:
        for n in list(data):
            if n.endswith(".rels"):
                s = data[n].decode("utf8")
                for old, new in renames.items():
                    s = s.replace("/" + posixpath.basename(old) + '"', "/" + posixpath.basename(new) + '"')
                data[n] = s.encode("utf8")
        ct = data["[Content_Types].xml"].decode("utf8")
        for old in renames:
            ct = re.sub(r'<Override PartName="/%s"[^>]*/>' % re.escape(old), "", ct)
        if 'Extension="jpeg"' not in ct:
            ct = ct.replace("<Default ", '<Default Extension="jpeg" ContentType="image/jpeg"/><Default ', 1)
        data["[Content_Types].xml"] = ct.encode("utf8")
    out = _rezip(data, names)
    with open(dst, "wb") as f:
        f.write(out)
    if verbose:
        print(f"{os.path.basename(src):40s} {os.path.getsize(src) if src != dst else before/1:>10,.0f} → {len(out):>10,} B"
              f"  ({len(renames)} → JPEG, {removed} orphan media removed)")
    return len(out)


def _rezip(data, order=None):
    o = io.BytesIO()
    with zipfile.ZipFile(o, "w", zipfile.ZIP_DEFLATED) as z:
        first = [n for n in (order or []) if n in data]
        for n in first + [n for n in data if n not in first]:
            z.writestr(n, data[n], zipfile.ZIP_STORED if n.startswith("ppt/media/") and
                       n.rsplit(".", 1)[-1] in ("png", "jpeg", "jpg") else zipfile.ZIP_DEFLATED)
    return o.getvalue()


def optimize_b64(path):
    raw = base64.b64decode(b"".join(open(path, "rb").read().split()))
    tmp = path + ".tmp.pptx"
    open(tmp, "wb").write(raw)
    n = optimize(tmp, verbose=False)
    out = base64.encodebytes(open(tmp, "rb").read())  # 76-column lines, like the stored copies
    os.remove(tmp)
    if len(out) < os.path.getsize(path):
        open(path, "wb").write(out)
    print(f"{os.path.basename(path):48s} {len(raw):>10,} → {n:>10,} B (pptx)")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--b64":
        for p in a[1:]:
            optimize_b64(p)
    elif a:
        optimize(a[0], a[1] if len(a) > 1 else None)
    else:
        print(__doc__ or "usage: optimize_pptx.py in.pptx [out.pptx] | --b64 files...")
