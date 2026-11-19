"""Figures for Lesson 6: Production, part 2."""
import numpy as np
import matplotlib.pyplot as plt
from econplot import *
from matplotlib.patches import FancyArrowPatch

# Stages of production with TP = 12L^2 - L^3
L = np.linspace(0, 9.6, 300)
TP = 12 * L**2 - L**3
MP = 24 * L - 3 * L**2
AP = 12 * L - L**2

fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.6, 6.4), gridspec_kw={"hspace": 0.32})
for ax in (a1, a2):
    ax.axvspan(0, 6, color=MIST, zorder=0)
    ax.axvspan(6, 8, color=SHADE_GOLD, alpha=0.55, zorder=0)
axes(a1, "$L$", "$TP_L$", (0, 10.5), (0, 320), origin="0")
curve(a1, L, TP, NAVY, label="$TP_L$", at=-1, dx=0.15, dy=-10)
for x, lab in [(4, "A"), (6, "B"), (8, "C")]:
    point(a1, x, 12 * x**2 - x**3, GOLD, 9)
    note(a1, x - 0.15, 12 * x**2 - x**3 + 14, lab, NAVY, 15, ha="right")
a1.plot([0, 7.4], [0, 36 * 7.4], color=GUIDE, lw=1.4, ls=(0, (4, 4)), zorder=1)
for x0, x1, lab in [(0, 6, "Stage I"), (6, 8, "Stage II"), (8, 10.5, "Stage III")]:
    note(a1, (x0 + x1) / 2, 318, lab, SLATE, 12, ha="center")
axes(a2, "$L$", "$AP_L,\\ MP_L$", (0, 10.5), (-30, 52), xaxis_at=0)
L2 = np.linspace(0, 9.05, 300)
curve(a2, L2, 24 * L2 - 3 * L2**2, BLUE, label="$MP_L$", at=-1, dx=0.15, dy=2)
curve(a2, L, AP, GOLD, label="$AP_L$", at=-1, dx=0.15)
point(a2, 4, 48, BLUE, 8)
point(a2, 6, 36, NAVY, 9)
point(a2, 8, 0, BLUE, 8)
note(a2, 3.85, 49.5, "A", NAVY, 14, ha="right", va="bottom")
note(a2, 6.15, 39, "B", NAVY, 14)
note(a2, 8.15, 3, "C", NAVY, 14)
save(fig, "l06-stages")

# A convex isoquant: moving from A to B
fig, ax = figure(5.6, 4.6)
axes(ax, "$L$", "$K$", (0, 10), (0, 10), origin="0")
l = np.linspace(1.15, 9.5, 200)
curve(ax, l, 9 / l, NAVY, label="$Q_0$", dx=0.15)
A = (2.2, 9 / 2.2); B = (4.4, 9 / 4.4); C = (2.2, 9 / 4.4)
point(ax, *A, NAVY, 8); point(ax, *B, NAVY, 8); point(ax, *C, GOLD, 8)
note(ax, A[0] + 0.2, A[1] + 0.25, "A", NAVY, 15)
note(ax, B[0] + 0.15, B[1] + 0.35, "B", NAVY, 15)
note(ax, C[0] - 0.25, C[1] - 0.45, "C", GOLD, 15, ha="right")
ax.add_patch(FancyArrowPatch(A, (C[0], C[1] + 0.12), arrowstyle="-|>", mutation_scale=14, color=GOLD, lw=2, zorder=4))
ax.add_patch(FancyArrowPatch(C, (B[0] - 0.12, B[1]), arrowstyle="-|>", mutation_scale=14, color=BLUE, lw=2, zorder=4))
note(ax, 2.0, 3.05, r"$MP_K \times \Delta K$", GOLD, 14, ha="right")
note(ax, 2.6, 1.4, r"$MP_L \times \Delta L$", BLUE, 14)
save(fig, "l06-isoquant")

# Fixed proportions: 4 tires and 1 steering wheel per car
fig, ax = figure(5.6, 4.2)
axes(ax, "Wheels", "Tires", (0, 3.2), (0, 11), origin="0")
for q, c in [(1, NAVY), (2, BLUE)]:
    ax.plot([q, q, 3.0], [10.6, 4 * q, 4 * q], color=c, lw=2.8, solid_capstyle="round", zorder=3)
    note(ax, 3.03, 4 * q, f"$Q = {q}$", c, 15)
    point(ax, q, 4 * q, GOLD, 8)
ax.plot([0, 2.65], [0, 10.6], color=GUIDE, lw=1.4, ls=(0, (4, 4)), zorder=1)
note(ax, 2.45, 9.0, "$T = 4W$", SLATE, 14)
for q in (1, 2):
    tick(ax, x=q, label=str(q))
    tick(ax, y=4 * q, label=str(4 * q))
save(fig, "l06-leontief")

# Three kinds of isoquant through the same point
fig, ax = figure(6.0, 4.4)
axes(ax, "$L$", "$K$", (0, 10), (0, 10), origin="0")
p0 = (3, 5)
ax.plot([0.3, 8.1], [8.9, 0], color=GREEN, lw=2.8, zorder=3)
note(ax, 0.9, 9.35, "linear", GREEN, 14)
ax.plot([3, 3, 9.2], [9.4, 5, 5], color=NAVY, lw=2.8, zorder=3)
note(ax, 9.25, 5.3, "fixed proportions", NAVY, 14, ha="right", va="bottom")
l = np.linspace(1.75, 9.3, 200)
ax.plot(l, 15 / l, color=GOLD, lw=2.8, zorder=3)
note(ax, 9.3, 1.25, "convex", GOLD, 14, ha="right", va="top")
point(ax, *p0, NAVY, 9)
save(fig, "l06-isoquant-types")
