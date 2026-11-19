"""Figures for Lesson 8: Profit and revenue maximization."""
import numpy as np
from econplot import *
from matplotlib.patches import FancyArrowPatch


def arrow(ax, p0, p1, color=GOLD):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=14, color=color, lw=1.8, zorder=4))


# Isocost shifts: smaller budget (parallel) and higher wage (rotation)
fig, (a1, a2) = figure(9.8, 3.9, ncols=2, wspace=0.3)
for ax in (a1, a2):
    axes(ax, "$L$", "$K$", (0, 27), (0, 36), origin="0")
    tick(ax, y=33.33, label="33.3")
L = np.linspace(0, 25, 50)
curve(a1, L, 33.33 - 1.333 * L, NAVY, label="$TC_0 = 500$", at=18, dx=0.6, dy=3)
L2 = np.linspace(0, 12.5, 50)
curve(a1, L2, 16.67 - 1.333 * L2, BLUE)
note(a1, 7.2, 9.6, "$TC_0' = 250$", BLUE, 15)
tick(a1, y=16.67, label="16.7")
note(a1, 1, -6.5, "Budget falls: parallel shift in", SLATE, 13)
curve(a2, L, 33.33 - 1.333 * L, NAVY, label="$P_L = \\$20$", at=18, dx=0.6, dy=3)
L3 = np.linspace(0, 20, 50)
curve(a2, L3, 33.33 - 1.667 * L3, BLUE)
note(a2, 12.2, 10.6, "$P_L = \\$25$", BLUE, 15)
tick(a2, x=20, label="20"); tick(a2, x=25, label="25")
note(a2, 1, -6.5, "Wage rises: isocost pivots in, steeper", SLATE, 13)
save(fig, "l08-isocost-shifts")

# Tangency: A and C on the isocost and the lower isoquant, B the tangency
fig, ax = figure(5.8, 4.6)
axes(ax, "$L$", "$K$", (0, 11), (0, 11), origin="0")
L = np.linspace(0, 10, 100)
lq = np.linspace(2, 8, 100)
ax.fill_between(lq, 16 / lq, 10 - lq, color=SHADE_GOLD, zorder=0)
curve(ax, L, 10 - L, NAVY, label="$TC_0$", at=4, dx=0.3, dy=0.6, va="bottom")
l0 = np.linspace(1.65, 10, 200)
curve(ax, l0, 16 / l0, BLUE, label="$Q_0$", at=-1, dx=0.15)
l1 = np.linspace(2.6, 10, 200)
curve(ax, l1, 25 / l1, GOLD, label="$Q_1$", at=-1, dx=0.15)
for (x, y, lab) in [(2, 8, "A"), (8, 2, "C")]:
    point(ax, x, y, BLUE, 9)
    note(ax, x + 0.3, y + 0.35, lab, NAVY, 15)
point(ax, 5, 5, GOLD, 11)
note(ax, 5.3, 5.45, "B", NAVY, 15)
save(fig, "l08-tangency")

# Expansion path through successive tangencies
fig, ax = figure(5.8, 4.6)
axes(ax, "$L$", "$K$", (0, 15), (0, 15), origin="0")
for c, col in [(6, SLATE), (10, NAVY), (14, BLUE)]:
    Lc = np.linspace(0, c, 50)
    ax.plot(Lc, c - Lc, color=GUIDE, lw=1.6, ls=(0, (5, 4)), zorder=1)
    q = (c / 2) ** 2
    lq = np.linspace(q / 14.5, 14.5, 200)
    ax.plot(lq, q / lq, color=col, lw=2.6, zorder=2)
    point(ax, c / 2, c / 2, GOLD, 9)
xs = np.linspace(0, 13.5, 20)
curve(ax, xs, xs, NAVY, lw=3)
note(ax, 13.2, 14.2, "expansion path", NAVY, 15, ha="right")
save(fig, "l08-expansion")

# Problem 8.5: perfect substitutes
fig, (a1, a2) = figure(9.6, 3.8, ncols=2, wspace=0.3)
for ax in (a1, a2):
    axes(ax, "$L$", "$K$", (0, 11), (0, 11), origin="0")
L = np.linspace(0, 10, 50)
a1.plot(L, 2.5 - 0.25 * L, color=NAVY, lw=4.5, zorder=2)
a1.plot(L, 2.5 - 0.25 * L, color=GOLD, lw=2, ls=(0, (5, 4)), zorder=3)
note(a1, 4, 3.0, "isoquant = isocost", NAVY, 14)
note(a1, 0.3, -2.6, "$P_K = \\$100$: any mix on the line is optimal", SLATE, 13)
c = 6
a2.plot(L[L <= c], c - L[L <= c], color=NAVY, lw=2.8, zorder=2)
note(a2, 3.6, 3.0, "isocost", NAVY, 14)
for k, col in [(3, GUIDE), (6, GOLD)]:
    a2.plot(L, k - 0.25 * L, color=col, lw=2.4, ls=(0, (5, 4)) if col == GUIDE else "-", zorder=3)
note(a2, 6.4, 5.5, "highest isoquant", GOLD, 14)
point(a2, 0, 6, GOLD, 11)
note(a2, 0.3, -2.6, "$P_K = \\$25$: corner solution, all capital", SLATE, 13)
save(fig, "l08-substitutes")
