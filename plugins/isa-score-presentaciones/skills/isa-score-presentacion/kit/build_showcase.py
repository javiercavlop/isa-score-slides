# ISA · SCORE Slides — (c) 2026 Francisco Javier Cavero López y Alejandro García Fernández
# (SCORE Lab, I3US, Universidad de Sevilla; Grupo ISA). Licencia CC BY 4.0 — ver LICENSE.
# Las presentaciones generadas con este kit pueden usarse libremente sin atribución (LICENSE, parte 2).
"""Builds ISA-SCORE_showcase.pptx: one example of every slide pattern, transition and animation
of the ISA · SCORE design system, plus two components from the slide library. Run:  python build_showcase.py [out.pptx]"""
import sys
from isa_deck import Deck, ENTRANCE_EFFECTS

out = sys.argv[1] if len(sys.argv) > 1 else "ISA-SCORE_showcase.pptx"
d = Deck()

# 1 · Title ----------------------------------------------------------------
d.title_slide("Pricing Intelligence: Rethinking IS Engineering in Volatile SaaS Environments",
              authors=[("Francisco Javier Cavero", True), "Alejandro García-Fernández", "José Antonio Parejo",
                       "Manuel Resinas", "Antonio Ruiz-Cortés"],
              affiliation="SCORE Lab, I3US, Universidad de Sevilla, Seville, Spain",
              venue="CAiSE'26", date="10th June 2026")

# 2 · Agenda (current = 1) ---------------------------------------------------
ag1 = d.agenda_slide(["Introduction", "Proposal", "Evaluation", "Conclusions"], current=1, number=2)
for i in range(1, 5):
    from isa_deck import find_shape
    d.animate(ag1, find_shape(ag1, f"Agenda item {i}"), "wipe", "from_left", trigger="with" if i > 1 else "after", delay=(i - 1) * 150)

# 3 · Hook statement ----------------------------------------------------------
s = d.section_divider("Pricing Intelligence is the discipline that turns pricing data into actionable knowledge.",
                      number=3, accent_words=["Pricing", "Intelligence"])
# section change: plain cut (no transition), as in the source decks

# 3b · Library component: the group's original pricing build (Morph + animations kept) ----
d.insert_component("pricing-table-build", number=3)

# 4–6 · Morph build with moving spotlight --------------------------------------
s4 = d.content_slide("Pricing Intelligence Interpretation Process (PIIP)", number=4)
d.morph(s4)
c1 = d.card(s4, 4.2, 1.7, 4.9, 1.0, "ACCESSIBILITY LAYER", style="blue", size=22, name="Layer access")
c2 = d.card(s4, 4.2, 3.1, 4.9, 1.0, "ORCHESTRATION LAYER", style="green", size=22, name="Layer orch")
c3 = d.card(s4, 4.2, 4.5, 4.9, 1.0, "CAPABILITY LAYER", style="orange", size=22, name="Layer cap")
d.animate_sequence(s4, [c1, c2, c3], effect="wipe", first="click", then="after", direction="from_top")
d.citation(s4, "Cavero, F. J., et al. (2026). Pricing Intelligence. In CAiSE'26.")

s5 = d.build_step(s4)                                   # duplicate + Morph
from isa_deck import apply_animations
apply_animations(s5, [])
d.spotlight(s5, 4.05, 1.55, 5.2, 1.3)

s6 = d.build_step(s5)
apply_animations(s6, [])
sp = [sh for sh in s6.shapes if sh.name == "!!Spotlight"][0]
from pptx.util import Inches
sp.top = Inches(4.35)                                    # Morph glides the frame down

# 7 · Focus overlay + quote card ---------------------------------------------
s7 = d.build_step(s6)
apply_animations(s7, [])
d.focus_overlay(s7)
q = d.quote_card(s7, 1.2, 2.2, 10.9, 2.4, [("Pricing-driven Development and Operation of SaaS", {"bold": True}),
                                            (" is an alternative DevOps cycle aimed at optimizing the management of pricing events.", {})])
d.animate(s7, q, "zoom", trigger="after")

# 8 · Stat bubbles ---------------------------------------------------------------
s8 = d.content_slide("Evaluating Pricing Validity on a State-of-the-art Dataset", number=8)

b = [d.stat_bubble(s8, 1.0, 1.6, 1.6, "30", "SaaS"), d.stat_bubble(s8, 3.0, 1.4, 2.0, "162", "pricings"),
     d.stat_bubble(s8, 1.9, 3.5, 1.3, "6", "years"), d.stat_bubble(s8, 3.6, 3.7, 2.2, "24223", "configurations")]
d.animate_sequence(s8, b, effect="zoom", first="after", then="after")
big = d.text(s8, 7.0, 2.2, 5.5, 1.2, [[("+20%", {"size": 54, "bold": True, "color": "C00000"}), ("  contain errors", {"size": 28, "bold": True})]], name="Headline stat")
d.animate(s8, big, "float_in", trigger="click")

# 9 · Research questions ---------------------------------------------------------
s9 = d.content_slide("Evaluation", number=9)
d.morph(s9)
rows = [d.rq_row(s9, 1.3, 1.6 + i * 1.05, 10.7, f"RQ{i+1}", lab, qq, note) for i, (lab, qq, note) in enumerate([
    ("Tool coverage", "To what extent do current PI tools cover the elicited PI tasks?", "Characterizes the current scope of PI support."),
    ("Strategy generation", "Can HARVEY generate the correct actions and parameters?", "Structural correctness with weighted precision, recall and F1."),
    ("Value assignment", "When action and parameter match, are the values correct?", "Isolates grounding errors.")])]
for i, r in enumerate(rows):
    group = [sh for sh in s9.shapes if sh.name.startswith(f"RQ RQ{i+1}")]
    for j, sh in enumerate(group):
        d.animate(s9, sh, "wipe", "from_left", trigger="click" if j == 0 else "with")

# 10 · Numbered future-work cards ------------------------------------------------
s10 = d.content_slide("Future Work", number=10)

items = [("01", "PACO Definition", "Formal definition of the problem"), ("02", "PACO Servitization", "Revisit the QACO model and its specification"),
         ("03", "PACO Solution", "An implementation that can solve it"), ("04", "PACO Family", "Explore the problems that are part of it")]
for i, (n, h, t) in enumerate(items):
    x = 0.9 + (i % 2) * 6.0; y = 1.7 + (i // 2) * 2.3
    num = d.text(s10, x, y, 1.6, 1.4, n, size=72, color="crimson", name=f"FW num {n}", font="Roboto Light")
    body = d.text(s10, x + 1.75, y + 0.2, 3.9, 1.2, [[(h, {"bold": True, "color": "A8003B", "size": 22})], t], size=18, name=f"FW body {n}")
    d.animate(s10, num, "float_in", trigger="click")
    d.animate(s10, body, "float_in", trigger="with", delay=150)

# 11 · Agenda (current = 3) — Morph moves the filled circle -------------------------
ag3 = d.agenda_slide(["Introduction", "Proposal", "Evaluation", "Conclusions"], current=3, number=11)
d.morph(ag3)

# 12 · Animation catalogue (every entrance preset, after previous) --------------------
s12 = d.content_slide("Animation catalogue (entrance effects)", number=12)

for i, eff in enumerate(ENTRANCE_EFFECTS):
    x = 0.7 + (i % 5) * 2.45; y = 1.35 + (i // 5) * 1.75
    c = d.card(s12, x, y, 2.2, 1.35, eff.replace("_", " ").upper(), style=["pink", "blue", "green", "orange", "rose"][i % 5], size=16, bold=True,
               name=f"Effect {eff}")
    d.animate(s12, c, eff, direction="from_left" if eff != "fly_in" else "from_bottom", trigger="click" if i == 0 else "after")

# 12b · Library component: rotating future-work wheel ------------------------------------
d.insert_component("rotating-wheel", number=13)

# 13 · Closing --------------------------------------------------------------------
cl = d.closing_slide("Pricing Intelligence: Rethinking IS Engineering in Volatile SaaS Environments",
                     authors=[("Francisco Javier Cavero López", True), "Alejandro García-Fernández", "José Antonio Parejo",
                              "Manuel Resinas", "Antonio Ruiz-Cortés"],
                     email="fcavero@us.es", venue="CAiSE'26", date="10th June 2026")

d.save(out)
print("saved", out)
