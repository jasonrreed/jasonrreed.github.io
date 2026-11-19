"""Figures for Lesson 11: Introduction to game theory (game trees)."""
import matplotlib.pyplot as plt
from econplot import *


def tree(name, root, mids, leaves, payoff_note, chosen=(), w=7.2, h=4.0, groups=None):
    """root: (label, x, y); mids: list of (label, x, y, edge_label);
    leaves: list of (mid_index, x, y, edge_label, payoff_text, tag).
    chosen: set of edge ids ('r0', 'm0-1', ...) to draw heavier in gold."""
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    box = dict(boxstyle="round,pad=0.45", fc="white", ec=NAVY, lw=1.6)
    rl, rx, ry = root
    if groups:
        for (x0, y0, x1, y1) in groups:
            ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, ec=GUIDE, lw=1.3, ls=(0, (5, 4))))
    for i, (ml, mx, my, el) in enumerate(mids):
        on = f"r{i}" in chosen
        ax.plot([rx, mx], [ry, my], color=GOLD if on else NAVY, lw=3.2 if on else 1.6, zorder=1)
        ax.text((rx + mx) / 2, (ry + my) / 2 + (0.45 if my > ry else -0.45), el, ha="center", va="center",
                fontsize=13, color=SLATE, style="italic")
    for j, (mi, lx, ly, el, pay, tag) in enumerate(leaves):
        ml, mx, my, _ = mids[mi]
        on = f"m{j}" in chosen
        ax.plot([mx, lx], [my, ly], color=GOLD if on else NAVY, lw=3.2 if on else 1.6, zorder=1)
        ax.text((mx + lx) / 2, (my + ly) / 2 + (0.4 if ly > my else -0.4), el, ha="center", va="center",
                fontsize=12, color=SLATE, style="italic")
        ax.plot([lx], [ly], "o", color=NAVY, ms=7, zorder=3)
        ax.text(lx + 0.25, ly, pay, ha="left", va="center", fontsize=13, color=NAVY)
        if tag:
            ax.text(lx - 0.2, ly + 0.55, tag, ha="right", va="bottom", fontsize=12, color=SLATE)
    ax.text(rx, ry, rl, ha="center", va="center", fontsize=13, color=NAVY, bbox=box, zorder=4)
    for (ml, mx, my, _) in mids:
        ax.text(mx, my, ml, ha="center", va="center", fontsize=13, color=NAVY, bbox=box, zorder=4)
    ax.text(5.4, 0.2, payoff_note, ha="center", va="bottom", fontsize=12, color=SLATE)
    save(fig, name)


# The parts of a game tree
tree("l11-tree",
     ("Player A", 1.6, 5.2),
     [("Player B", 5.0, 7.6, "Yes"), ("Player B", 5.0, 2.8, "No")],
     [(0, 8.0, 9.0, "Yes", "(15, 20)", ""), (0, 8.0, 6.3, "No", "(5, 5)", ""),
      (1, 8.0, 4.2, "Yes", "(0, 0)", ""), (1, 8.0, 1.5, "No", "(10, 25)", "")],
     "Payoffs: (Player A, Player B)")

# Solving by backward induction
tree("l11-subgames",
     ("Player A", 1.6, 5.2),
     [("Player B", 5.0, 7.6, "Yes"), ("Player B", 5.0, 2.8, "No")],
     [(0, 8.0, 9.0, "Yes", "(15, 20)", ""), (0, 8.0, 6.3, "No", "(5, 5)", ""),
      (1, 8.0, 4.2, "Yes", "(0, 0)", ""), (1, 8.0, 1.5, "No", "(10, 25)", "")],
     "Payoffs: (Player A, Player B)",
     chosen={"r0", "m0", "m3"},
     groups=[(4.0, 5.6, 9.95, 9.8), (4.0, 0.9, 9.95, 4.9)])

# The software game
tree("l11-software",
     ("Macrosoft", 1.6, 5.2),
     [("Microcorp", 4.8, 7.6, "Slick"), ("Microcorp", 4.8, 2.8, "Simple")],
     [(0, 7.6, 9.0, "Enter", r"(\$380,000, −\$250,000)", ""), (0, 7.6, 6.3, "Stay out", r"(\$430,000, \$0)", ""),
      (1, 7.6, 4.2, "Enter", r"(\$400,000, \$100,000)", ""), (1, 7.6, 1.5, "Stay out", r"(\$800,000, \$0)", "")],
     "Payoffs: (Macrosoft, Microcorp)",
     chosen={"r0", "m1", "m2"}, w=8.4)
