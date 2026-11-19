"""Figures for Lesson 9: Perfect competition and monopoly."""
import numpy as np
from econplot import *
from matplotlib.patches import FancyArrowPatch

SHADE_RED = "#F2C9C4"
SHADE_GREEN = "#CFE3D6"


def arrow(ax, p0, p1, color=GOLD):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=14, color=color, lw=1.8, zorder=4))


# Firm cost curves shared by the perfect-competition figures
q = np.linspace(0.6, 10.6, 300)
AVC = 4 - 0.9 * q + 0.09 * q**2 + 1.2
MC = 4 - 1.8 * q + 0.27 * q**2 + 1.2
AFC = 3.2 / q
ATC = AVC + AFC


def firm(ax, price=None, shade=None, show_avc=False, ylim=10):
    axes(ax, "$q$", "$P$", (0, 11), (0, ylim), origin="0")
    m = MC < ylim
    curve(ax, q[m], MC[m], BLUE, label="$MC$", at=-1, dx=0.1)
    m = ATC < ylim
    curve(ax, q[m], ATC[m], NAVY, label="$ATC$", at=-1, dx=0.1)
    if show_avc:
        m = AVC < ylim
        curve(ax, q[m], AVC[m], GREEN, label="$AVC$", at=-1, dx=0.1)
    if price is not None:
        ax.plot([0, 10.6], [price, price], color=GOLD, lw=2.6, zorder=3)
        # quantity where P = MC on the rising part
        i = np.where((MC >= price) & (q > 3.3))[0][0]
        qs = q[i]
        return qs, np.interp(qs, q, ATC)
    return None


def market(ax, shift=0.0, label_p="$P^*$"):
    axes(ax, "$Q$", "$P$", (0, 10), (0, 10), origin="0")
    Q = np.linspace(1, 9, 50)
    curve(ax, Q, 10 - Q, NAVY, label="$D$")
    curve(ax, Q, 1 + 0.9 * Q, GOLD, label="$S$", dy=0.3)
    if shift:
        curve(ax, Q + shift, 1 + 0.9 * Q, BLUE, label="$S'$", dy=0.3)


# Short-run profit for a perfectly competitive firm
fig, (a1, a2) = figure(10.2, 4.0, ncols=2, wspace=0.3)
market(a1)
x = 9 / 1.9; p = 10 - x
guide(a1, x, p, "$Q^*$", "$P^*$")
point(a1, x, p, GOLD)
note(a1, 5, 10.6, "Market", SLATE, 14, ha="center")
qs, atc = firm(a2, price=p)
a2.fill_between([0, qs], [atc, atc], [p, p], color=SHADE_GOLD, zorder=0)
guide(a2, qs, p, "$q^*$", "$P^* = MR$")
tick(a2, y=atc, label="$ATC(q^*)$")
a2.plot([0, qs], [atc, atc], color=GUIDE, lw=1.3, ls=(0, (4, 4)))
point(a2, qs, p, GOLD)
note(a2, qs * 0.74, (p + atc) / 2, "profit", NAVY, 13, ha="center")
note(a2, 5.5, 10.6, "Firm", SLATE, 14, ha="center")
save(fig, "l09-pc-short-run")

# Long run: entry shifts supply until price = min ATC
fig, (a1, a2) = figure(10.2, 4.0, ncols=2, wspace=0.3)
market(a1, shift=1.4)
x1 = 9 / 1.9; p1 = 10 - x1
x2 = (9 + 0.9 * 1.4) / 1.9; p2 = 10 - x2
point(a1, x1, p1, GUIDE); point(a1, x2, p2, GOLD)
guide(a1, x2, p2, "$Q'$", "$P'$")
arrow(a1, (6.2, 7.2), (7.4, 7.2), BLUE)
note(a1, 5, 10.6, "Market: entry", SLATE, 14, ha="center")
pmin = ATC.min(); qmin = q[np.argmin(ATC)]
firm(a2, price=pmin)
guide(a2, qmin, pmin, "$q'$", "$P' = \\min ATC$")
point(a2, qmin, pmin, GOLD)
note(a2, 5.5, 10.6, "Firm: zero economic profit", SLATE, 14, ha="center")
save(fig, "l09-pc-long-run")

# Shutdown and exit (larger fixed cost so the AVC and ATC minimums separate)
ATC2 = AVC + 10 / q
fig, (a1, a2) = figure(10.2, 4.2, ncols=2, wspace=0.3)
pavc = AVC.min(); qavc = q[np.argmin(AVC)]
p2 = ATC2.min(); q2 = q[np.argmin(ATC2)]
for ax, title in ((a1, "Short run"), (a2, "Long run")):
    axes(ax, "$q$", "$P$", (0, 11), (0, 10), origin="0")
    m = MC < 10
    curve(ax, q[m], MC[m], BLUE, label="$MC$", at=-1, dx=0.1)
    m = ATC2 < 10
    curve(ax, q[m], ATC2[m], NAVY, label="$ATC$", at=-1, dx=0.1)
    point(ax, q2, p2, NAVY, 9)
    tick(ax, y=p2, label="$\\min ATC$")
    note(ax, 5.5, 10.6, title, SLATE, 14, ha="center")
m = AVC < 10
curve(a1, q[m], AVC[m], GREEN, label="$AVC$", at=-1, dx=0.1, dy=-0.2)
point(a1, qavc, pavc, GREEN, 9)
tick(a1, y=pavc, label="$\\min AVC$")
a1.axhspan(pavc, p2, xmax=0.88, color=SHADE_GOLD, alpha=0.6, zorder=0)
a1.axhspan(0, pavc, xmax=0.88, color=SHADE_RED, alpha=0.5, zorder=0)
note(a1, 0.5, (pavc + p2) / 2, "operate at a loss", NAVY, 12)
note(a1, 0.5, pavc / 2, "shut down", NAVY, 12)
a2.axhspan(0, p2, xmax=0.88, color=SHADE_RED, alpha=0.5, zorder=0)
note(a2, 0.5, p2 / 2, "exit", NAVY, 12)
save(fig, "l09-shutdown")

# Monopoly: MR = MC, price on demand
fig, ax = figure(6.0, 4.6)
axes(ax, "$Q$", "$P$", (0, 10), (0, 10), origin="0")
Q = np.linspace(0, 9.5, 50)
curve(ax, Q, 10 - Q, NAVY, label="$D$")
Qm = np.linspace(0, 5, 50)
curve(ax, Qm, 10 - 2 * Qm, BLUE, label="$MR$", dx=0.15, dy=-0.3)
qq = np.linspace(0.8, 7.2, 100)
mc = 5.5 - 2.2 * qq + 0.36 * qq**2
qs = qq[np.argmin(np.abs(mc - (10 - 2 * qq)))]
curve(ax, qq, mc, GOLD, label="$MC$", at=-1, dx=0.1)
pm = 10 - qs
guide(ax, qs, pm, "$Q_M$", "$P_M$")
ax.plot([qs, qs], [0, 10 - 2 * qs], color=GUIDE, lw=1.3, ls=(0, (4, 4)))
point(ax, qs, 10 - 2 * qs, BLUE, 9); note(ax, qs + 0.25, 10 - 2 * qs - 0.5, "A", NAVY, 14)
point(ax, qs, pm, GOLD, 10); note(ax, qs + 0.25, pm + 0.3, "B", NAVY, 14)
save(fig, "l09-monopoly")

# Consumer and producer surplus at the competitive equilibrium
fig, ax = figure(5.6, 4.4)
axes(ax, "$Q$", "$P$", (0, 10), (0, 10), origin="0")
Q = np.linspace(0, 9, 50)
x = 9 / 1.9; p = 10 - x
ax.fill_between([0, x], [10, p], [p, p], color=SHADE_BLUE, zorder=0)
ax.fill_between([0, x], [1, p], [p, p], color=SHADE_GOLD, zorder=0)
curve(ax, Q, 10 - Q, NAVY, label="$D$")
curve(ax, Q, 1 + 0.9 * Q, GOLD, label="$S = MC$", dy=0.3)
guide(ax, x, p, "$Q^*$", "$P^*$")
point(ax, x, p, NAVY)
note(ax, 0.35, 6.1, "consumer\nsurplus", NAVY, 12)
note(ax, 0.35, 3.7, "producer\nsurplus", NAVY, 12)
save(fig, "l09-surplus")

# Problem 9.8: monopoly versus perfect competition, with numbers
P = lambda v: 110 - 5 * v
MCf = lambda v: 10 + 2 * v
qm, pm, mcm = 25 / 3, 110 - 5 * 25 / 3, 10 + 2 * 25 / 3
qpc = 100 / 7; ppc = P(qpc)
fig, (a1, a2) = figure(10.2, 4.2, ncols=2, wspace=0.32)
for ax in (a1, a2):
    axes(ax, "$Q$", "$P$", (0, 23), (0, 125), origin="0")
    Q = np.linspace(0, 22, 50)
    curve(ax, Q, P(Q), NAVY, label="$D$", dx=0.3, dy=3)
    Q2 = np.linspace(0, 19, 50)
    curve(ax, Q2, MCf(Q2), GOLD, label="$MC$", dx=0.3)
    tick(ax, y=110, label="110"); tick(ax, y=10, label="10")
# monopoly panel
Qa = np.linspace(0, qm, 50)
a1.fill_between([0, qm], [110, pm], [pm, pm], color=SHADE_BLUE, zorder=0)
a1.fill_between(Qa, MCf(Qa), pm, color=SHADE_GREEN, zorder=0)
Qd = np.linspace(qm, qpc, 50)
a1.fill_between(Qd, MCf(Qd), P(Qd), color=SHADE_RED, zorder=0)
Qr = np.linspace(0, 11, 50)
curve(a1, Qr, 110 - 10 * Qr, BLUE, label="$MR$", dx=0.3, dy=2)
guide(a1, qm, pm, "8.33", "68.33")
tick(a1, y=mcm, label="26.67")
a1.plot([0, qm], [mcm, mcm], color=GUIDE, lw=1.2, ls=(0, (4, 4)))
point(a1, qm, pm, NAVY, 8)
note(a1, 4.0, 75, "CS", NAVY, 14); note(a1, 2.6, 45, "PS", NAVY, 14); note(a1, 9.3, 44, "DWL", NAVY, 13)
note(a1, 11.5, 131, "Monopoly", SLATE, 14, ha="center")
# competitive panel
Qb = np.linspace(0, qpc, 50)
a2.fill_between([0, qpc], [110, ppc], [ppc, ppc], color=SHADE_BLUE, zorder=0)
a2.fill_between(Qb, MCf(Qb), ppc, color=SHADE_GREEN, zorder=0)
guide(a2, qpc, ppc, "14.29", "38.57")
point(a2, qpc, ppc, NAVY, 8)
note(a2, 3.0, 62, "CS", NAVY, 14); note(a2, 3.0, 26, "PS", NAVY, 14)
note(a2, 11.5, 131, "Perfect competition", SLATE, 14, ha="center")
save(fig, "l09-welfare")
