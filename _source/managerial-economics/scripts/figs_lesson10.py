"""Figures for Lesson 10: Monopolistic competition and oligopoly."""
import numpy as np
from econplot import *

SHADE_RED = "#F2C9C4"

q = np.linspace(0.7, 10.5, 300)
MC = 5.5 - 1.9 * q + 0.24 * q**2
AVC = 5.5 - 0.95 * q + 0.08 * q**2
ATC = AVC + 4.0 / q


def panel(ax, a, b, title, profit=True):
    axes(ax, "$Q$", "$P$", (0, 11), (0, 11), origin="0")
    Q = np.linspace(0, min(a / b * 0.97, 10.4), 50)
    curve(ax, Q, a - b * Q, NAVY, label="$D = AR$", at=-1, dx=0.15, dy=0.2)
    Qm = np.linspace(0, a / (2 * b), 50)
    curve(ax, Qm, a - 2 * b * Qm, BLUE, label="$MR$", at=-1, dx=0.15, dy=-0.3)
    m = MC < 10.5
    curve(ax, q[m], MC[m], GOLD, label="$MC$", at=-1, dx=0.1)
    m = ATC < 10.5
    curve(ax, q[m], ATC[m], SLATE, label="$ATC$", at=-1, dx=0.1)
    i = np.argmin(np.abs(MC - (a - 2 * b * q)) + (q < 2.5) * 99)
    qs = q[i]; p = a - b * qs; c = ATC[i]
    ax.fill_between([0, qs], [min(p, c)] * 2, [max(p, c)] * 2, color=SHADE_GOLD if p > c else SHADE_RED, zorder=0)
    guide(ax, qs, max(p, c), "$Q^*$")
    tick(ax, y=p, label="$P^*$")
    tick(ax, y=c, label="$ATC$")
    point(ax, qs, p, NAVY, 8)
    point(ax, qs, c, SLATE, 8)
    note(ax, 5.5, 11.6, title, SLATE, 14, ha="center")
    return qs, p, c


fig, (a1, a2) = figure(10.2, 4.0, ncols=2, wspace=0.3)
panel(a1, 10.2, 0.75, "Positive economic profit")
panel(a2, 3.4, 0.18, "Negative economic profit")
save(fig, "l10-short-run")

# Long run: demand tangent to ATC
fig, ax = figure(6.0, 4.4)
axes(ax, "$Q$", "$P$", (0, 11), (0, 11), origin="0")
# find a linear demand tangent to ATC at q0 with MR = MC at q0
q0 = 4.6
i0 = np.argmin(np.abs(q - q0)); q0 = q[i0]
slope = np.gradient(ATC, q)[i0]
b = -slope; a = ATC[i0] + b * q0
Q = np.linspace(0, min(a / b, 10.3), 50)
curve(ax, Q, a - b * Q, NAVY, label="$D = AR$", at=-1, dx=0.15)
Qm = np.linspace(0, a / (2 * b), 50)
curve(ax, Qm, a - 2 * b * Qm, BLUE, label="$MR$", at=-1, dx=0.15, dy=-0.3)
mcl = MC + (a - 2 * b * q0 - MC[i0])  # shift MC so MR = MC at q0
m = mcl < 10.5
curve(ax, q[m], mcl[m], GOLD, label="$MC$", at=-1, dx=0.1)
m = ATC < 10.5
curve(ax, q[m], ATC[m], SLATE, label="$ATC$", at=-1, dx=0.1)
guide(ax, q0, ATC[i0], "$Q^*$", "$P^* = ATC$")
ax.plot([q0, q0], [0, a - 2 * b * q0], color=GUIDE, lw=1.3, ls=(0, (4, 4)))
point(ax, q0, ATC[i0], GOLD, 10)
point(ax, q0, a - 2 * b * q0, BLUE, 8)
save(fig, "l10-long-run")

# Kinked demand from Problem 10.3
fig, ax = figure(6.6, 4.6)
axes(ax, "$Q$", "$P$", (0, 30), (0, 15.5))
Qa = np.linspace(0, 21.2, 50); Qb = np.linspace(21.2, 28, 50)
ax.plot(Qa, 10.25 - Qa / 8, color=NAVY, lw=3, zorder=3)
ax.plot(Qb, 10.25 - Qb / 8, color=NAVY, lw=1.4, ls=(0, (5, 4)), zorder=2)
ax.plot(Qb, 44 / 3 - Qb / 3, color=NAVY, lw=3, zorder=3)
Q0 = np.linspace(0, 21.2, 50)
ax.plot(Q0, 44 / 3 - Q0 / 3, color=NAVY, lw=1.4, ls=(0, (5, 4)), zorder=2)
note(ax, 28.3, 10.25 - 28 / 8, "$D_1$", NAVY, 16)
note(ax, 28.3, 44 / 3 - 28 / 3, "$D_2$", NAVY, 16)
ax.plot(Qa, 10.25 - Qa / 4, color=BLUE, lw=2.6, zorder=3)
Qr = np.linspace(21.2, 22.0, 20)
ax.plot(Qr, 44 / 3 - 2 * Qr / 3, color=BLUE, lw=2.6, zorder=3)
ax.plot([21.2, 21.2], [0.533, 4.95], color=BLUE, lw=2.6, ls=(0, (2, 3)), zorder=3)
note(ax, 13.5, 6.0, "$MR$", BLUE, 16)
mcq = np.linspace(4, 27, 50)
ax.plot(mcq, 1 + 0.1 * mcq, color=GOLD, lw=2.6, zorder=3)
note(ax, 27.3, 1 + 0.1 * 27, "$MC$", GOLD, 16)
mcq2 = np.linspace(4, 25, 50)
ax.plot(mcq2, 5 + 0.2 * mcq2, color=GOLD, lw=2.2, ls=(0, (6, 3)), zorder=3)
note(ax, 25.3, 5 + 0.2 * 25, "$MC'$", GOLD, 16)
guide(ax, 21.2, 7.6, "21.2", "7.6")
point(ax, 21.2, 7.6, NAVY, 10)
tick(ax, y=4.95, label="4.95"); tick(ax, y=0.53, label="0.53")
for y in (4.95, 0.53):
    ax.plot([0, 21.2], [y, y], color=GUIDE, lw=1.1, ls=(0, (2, 4)))
guide(ax, 11.67, 8.79, "11.67", "8.79")
point(ax, 11.67, 8.79, GOLD, 9)
note(ax, 1.0, 14.5, "Above the kink rivals hold price ($D_1$); below it they match ($D_2$)", SLATE, 11)
save(fig, "l10-kinked")

# Cournot reaction functions for Problem 10.4
fig, ax = figure(5.6, 4.6)
axes(ax, "$q_1$", "$q_2$", (0, 105), (0, 105), origin="0")
x = np.linspace(0, 98, 50)
curve(ax, x, 49 - x / 2, BLUE)
note(ax, 70, 18, "Firm 2: $q_2 = 49 - 0.5q_1$", BLUE, 13)
y = np.linspace(0, 98, 50)
ax.plot(49 - y / 2, y, color=NAVY, lw=3)
note(ax, 6, 92, "Firm 1: $q_1 = 49 - 0.5q_2$", NAVY, 13)
guide(ax, 196 / 6, 196 / 6, "32.67", "32.67")
point(ax, 196 / 6, 196 / 6, GOLD, 11)
note(ax, 36, 40, "Nash equilibrium", SLATE, 13)
tick(ax, x=98, label="98"); tick(ax, y=98, label="98")
tick(ax, x=49, label="49"); tick(ax, y=49, label="49")
save(fig, "l10-cournot")
