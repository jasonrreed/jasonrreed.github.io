"""Figures for Lesson 3: The essentials of supply and demand."""
import numpy as np
from econplot import *
from matplotlib.patches import FancyArrowPatch


def arrow(ax, p0, p1, color=GOLD):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=14, color=color, lw=1.8, zorder=4))


# Law of demand: a fall in price raises quantity demanded
fig, ax = figure(5.2, 4.0)
axes(ax, "$Q$", "$P$", (0, 10), (0, 10), origin="0")
q = np.linspace(1, 9, 50)
curve(ax, q, 10 - q, NAVY, label="$D$", dx=0.15)
guide(ax, 3, 7, "$Q_1$", "$P_1$")
guide(ax, 6, 4, "$Q_2$", "$P_2$")
point(ax, 3, 7, NAVY)
point(ax, 6, 4, GOLD)
save(fig, "l03-law-of-demand")

# Ex 3.2: horizontal summation with a kink at P = 8
fig, ax = figure(6.4, 4.4)
axes(ax, "$Q$", "$P$", (0, 62), (0, 12), origin="0")
ax.plot([0, 20], [10, 0], color=SLATE, lw=1.8, ls=(0, (5, 4)), label="Individual 1: $Q_{D,1} = 20 - 2P$")
ax.plot([0, 40], [8, 0], color=BLUE, lw=1.8, ls=(0, (5, 4)), label="Individual 2: $Q_{D,2} = 40 - 5P$")
ax.plot([0, 4, 60], [10, 8, 0], color=NAVY, lw=3.2, solid_capstyle="round", label="Market demand")
ax.legend(loc="upper right", frameon=False, fontsize=13, handlelength=2.6, labelcolor=SLATE)
note(ax, 30, 4.9, "$Q = 60 - 7P$", NAVY, 16)
guide(ax, 4, 8, "4", "8")
tick(ax, y=10, label="10")
for v in (20, 40, 60):
    tick(ax, x=v, label=str(v))
point(ax, 4, 8, GOLD)
save(fig, "l03-market-demand")

# Problem 3.4 equilibrium
fig, ax = figure(5.6, 4.2)
axes(ax, "$Q$", "$P$", (0, 26), (0, 9), origin="0")
qd = np.linspace(1, 25, 50)
curve(ax, qd, (25 - qd) / 3, NAVY, label="$Q_D = 25 - 3P$", at="start", dx=0.6, dy=0.45, va="bottom")
qs = np.linspace(10, 25, 50)
curve(ax, qs, (qs - 10) / 2, GOLD, label="$Q_S = 10 + 2P$", dx=-0.3, dy=0.4, ha="right", va="bottom")
guide(ax, 16, 3, "$Q^* = 16$", "$P^* = 3$")
point(ax, 16, 3, GOLD)
save(fig, "l03-equilibrium")

# Shifts: demand increase and supply increase
fig, (a1, a2) = figure(9.6, 3.8, ncols=2)
q = np.linspace(1, 9, 50)
for ax in (a1, a2):
    axes(ax, "$Q$", "$P$", (0, 10), (0, 10), origin="0")
curve(a1, q, 10 - q, NAVY, label="$D_1$")
curve(a1, q + 2, 12 - (q + 2) + 0, BLUE, label="$D_2$")
curve(a1, q, 1 + 0.9 * q, GOLD, label="$S$", dy=0.3)
x1 = 9 / 1.9; x2 = 11 / 1.9
point(a1, x1, 10 - x1, NAVY); point(a1, x2, 12 - x2, BLUE)
arrow(a1, (2.6, 7.0), (4.2, 7.0), BLUE)
note(a1, 0.3, -1.9, "Demand rises: $P$ and $Q$ both rise", SLATE, 13)
curve(a2, q, 10 - q, NAVY, label="$D$")
curve(a2, q, 1 + 0.9 * q, GOLD, label="$S_1$", dy=0.3)
curve(a2, q + 2, 1 + 0.9 * q, BLUE, label="$S_2$", dy=0.3)
y1 = 9 / 1.9
xs = (10 - 1 + 1.8) / 1.9
point(a2, y1, 10 - y1, NAVY); point(a2, xs, 10 - xs, BLUE)
arrow(a2, (6.0, 6.7), (7.6, 6.7), BLUE)
note(a2, 0.3, -1.9, "Supply rises: $P$ falls, $Q$ rises", SLATE, 13)
save(fig, "l03-shifts")

# Price ceiling and price floor
fig, (a1, a2) = figure(9.6, 3.8, ncols=2)
for ax in (a1, a2):
    axes(ax, "$Q$", "$P$", (0, 10), (0, 10), origin="0")
    curve(ax, q, 10 - q, NAVY, label="$D$")
    curve(ax, q, 1 + 0.9 * q, GOLD, label="$S$", dy=0.3)
# ceiling at P = 3.5
c = 3.5; qs_c = (c - 1) / 0.9; qd_c = 10 - c
a1.plot([0, 9.3], [c, c], color=BLUE, lw=2.2)
note(a1, 9.4, c, "ceiling", BLUE, 13)
guide(a1, qs_c, c, "$Q_S$"); guide(a1, qd_c, c, "$Q_D$")
a1.annotate("", xy=(qd_c, 2.4), xytext=(qs_c, 2.4), arrowprops=dict(arrowstyle="<->", color=SLATE, lw=1.4))
note(a1, (qs_c + qd_c) / 2, 1.7, "shortage", SLATE, 13, ha="center")
# floor at P = 7
fl = 7; qs_f = (fl - 1) / 0.9; qd_f = 10 - fl
a2.plot([0, 9.3], [fl, fl], color=BLUE, lw=2.2)
note(a2, 9.4, fl, "floor", BLUE, 13)
guide(a2, qd_f, fl, "$Q_D$"); guide(a2, qs_f, fl, "$Q_S$")
a2.annotate("", xy=(qs_f, 8.1), xytext=(qd_f, 8.1), arrowprops=dict(arrowstyle="<->", color=SLATE, lw=1.4))
note(a2, (qs_f + qd_f) / 2, 8.8, "surplus", SLATE, 13, ha="center")
save(fig, "l03-ceiling-floor")
