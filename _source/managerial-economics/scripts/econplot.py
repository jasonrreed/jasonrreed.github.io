"""Small helpers for drawing economics graphs in the slide style.

Every figure is saved as an SVG with its text converted to outlines, so it looks
the same in any browser. Run a lesson's figure script from the repo root, e.g.

    python scripts/figs_lesson02.py

and it writes SVGs into lessons/figures/.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "lessons" / "figures"
FONTS = Path(__file__).resolve().parent / "fonts"

NAVY = "#0C2340"
GOLD = "#C99700"
BLUE = "#3E78B2"
GREEN = "#3F7D5A"
SLATE = "#55657A"
GUIDE = "#9AA8BA"
MIST = "#F3F6FA"
SHADE_GOLD = "#F3E2B0"
SHADE_BLUE = "#D6E3F2"

for f in FONTS.glob("*.ttf"):
    font_manager.fontManager.addfont(str(f))

plt.rcParams.update({
    "svg.fonttype": "path",
    "font.family": "Libre Franklin",
    "font.size": 13,
    "mathtext.fontset": "custom",
    "mathtext.rm": "Newsreader",
    "mathtext.it": "Newsreader:italic",
    "mathtext.bf": "Newsreader:bold",
    "mathtext.fallback": "stix",
    "axes.linewidth": 0,
    "figure.facecolor": "none",
    "axes.facecolor": "none",
    "savefig.transparent": True,
})

LABEL = dict(fontsize=19, color=SLATE)        # axis variable labels (math)
TICK = dict(fontsize=16, color=SLATE)         # labels on the axes (a, x1, Q*)
CURVE = dict(fontsize=18)                     # curve-end labels


def figure(w=6.0, h=4.2, ncols=1, wspace=0.35):
    fig, axs = plt.subplots(1, ncols, figsize=(w, h), gridspec_kw={"wspace": wspace})
    return fig, axs


def axes(ax, xlabel="$Q$", ylabel="$P$", xlim=(0, 10), ylim=(0, 10), origin=None,
         xaxis_at=None):
    """L-shaped axes with arrowheads and the variable names at the ends.

    xaxis_at puts the horizontal axis at that y value (for graphs that go negative).
    """
    ax.set_xlim(xlim[0], xlim[1] * 1.08)
    ax.set_ylim(ylim[0], ylim[1] * 1.08)
    ax.set_xticks([])
    ax.set_yticks([])
    y0 = ylim[0] if xaxis_at is None else xaxis_at
    kw = dict(arrowstyle="-|>", mutation_scale=14, color=SLATE, lw=1.4,
              shrinkA=0, shrinkB=0, zorder=2)
    ax.add_patch(FancyArrowPatch((xlim[0], y0), (xlim[1] * 1.06, y0), **kw))
    ax.add_patch(FancyArrowPatch((xlim[0], ylim[0]), (xlim[0], ylim[1] * 1.06), **kw))
    ax.text(xlim[1] * 1.06, y0 - (ylim[1] - ylim[0]) * 0.035, xlabel, ha="right", va="top", **LABEL)
    ax.text(xlim[0] - (xlim[1] - xlim[0]) * 0.02, ylim[1] * 1.06, ylabel, ha="right", va="top", **LABEL)
    if origin:
        ax.text(xlim[0] - (xlim[1] - xlim[0]) * 0.02, y0, origin, ha="right", va="center", **TICK)
    return ax


def curve(ax, x, y, color=NAVY, lw=3, label=None, at="end", dx=0.15, dy=0.0,
          ls="-", ha="left", va="center", zorder=3):
    ax.plot(x, y, color=color, lw=lw, ls=ls, solid_capstyle="round", zorder=zorder)
    if label:
        i = -1 if at == "end" else 0 if at == "start" else at
        ax.text(x[i] + dx, y[i] + dy, label, color=color, ha=ha, va=va, **CURVE)


def guide(ax, x=None, y=None, xlabel=None, ylabel=None, x0=0, y0=0):
    """Dashed drop lines from (x, y) to the axes, with optional axis labels."""
    kw = dict(color=GUIDE, lw=1.3, ls=(0, (4, 4)), zorder=1)
    if x is not None and y is not None:
        ax.plot([x, x], [y0, y], **kw)
        ax.plot([x0, x], [y, y], **kw)
    if xlabel is not None:
        ax.text(x, y0 - (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.03, xlabel, ha="center", va="top", **TICK)
    if ylabel is not None:
        ax.text(x0 - (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.02, y, ylabel, ha="right", va="center", **TICK)


def point(ax, x, y, color=GOLD, size=9, edge="white"):
    ax.plot([x], [y], "o", ms=size, color=color, mec=edge, mew=2, zorder=5)


def tick(ax, x=None, y=None, label="", x0=0, y0=0):
    if x is not None:
        ax.text(x, y0 - (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.03, label, ha="center", va="top", **TICK)
    if y is not None:
        ax.text(x0 - (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.02, y, label, ha="right", va="center", **TICK)


def note(ax, x, y, text, color=SLATE, size=13, ha="left", va="center", **kw):
    ax.text(x, y, text, color=color, fontsize=size, ha=ha, va=va, **kw)


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    print("wrote", name)
