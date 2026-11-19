"""Figures for Lesson 7: Costs."""
import numpy as np
import matplotlib.pyplot as plt
from econplot import *

# Marginal product and marginal cost are scaled inverses (wage = $5 per hundred hours)
L = np.arange(1, 11)
MP = np.array([0.25, 0.75, 1.00, 0.60, 0.40, 0.30, 0.25, 0.20, 0.15, 0.10])
MC = 5 / MP
fig, (a1, a2) = figure(9.8, 3.6, ncols=2, wspace=0.3)
axes(a1, "$L$", "$MP_L$", (0, 11), (0, 1.3), origin="0")
a1.plot(L, MP, color=NAVY, lw=3, marker="o", ms=6, mfc="white", mew=2)
point(a1, 3, 1.0, GOLD, 10)
for v in (2, 4, 6, 8, 10):
    tick(a1, x=v, label=str(v))
for v in (0.5, 1.0):
    tick(a1, y=v, label=f"{v:.1f}")
axes(a2, "$L$", "$MC$", (0, 11), (0, 62), origin="0")
a2.plot(L, MC, color=BLUE, lw=3, marker="o", ms=6, mfc="white", mew=2)
point(a2, 3, 5, GOLD, 10)
for v in (2, 4, 6, 8, 10):
    tick(a2, x=v, label=str(v))
for v in (25, 50):
    tick(a2, y=v, label=f"\\${v}")
note(a1, 3.4, 1.03, "$MP_L$ peaks", SLATE, 12)
note(a2, 4.3, 2.8, "$MC$ bottoms out", SLATE, 12)
save(fig, "l07-mp-mc")

# Short-run cost curves
q = np.linspace(0.6, 11.5, 300)
AVC = 30 - 6 * q + 0.5 * q**2
MCc = 30 - 12 * q + 1.5 * q**2
AFC = 100 / q
ATC = AFC + AVC
qb = q[np.argmin(ATC)]
fig, ax = figure(6.2, 4.6)
axes(ax, "$Q$", "$\\$$", (0, 12), (0, 50), origin="0")
m = (MCc < 50)
curve(ax, q[m], MCc[m], BLUE, label="$MC$", at=-1, dx=0.1, dy=-1)
m = ATC < 50
curve(ax, q[m], ATC[m], NAVY, label="$ATC$", at=-1, dx=0.15)
curve(ax, q, AVC, GREEN, label="$AVC$", at=-1, dx=0.15)
m = AFC < 50
curve(ax, q[m], AFC[m], GOLD, label="$AFC$", at=-1, dx=0.15)
point(ax, 6, 12, GREEN, 9); note(ax, 6.2, 9.8, "A", GREEN, 15)
point(ax, qb, ATC.min(), NAVY, 9); note(ax, qb + 0.2, ATC.min() - 2.6, "B", NAVY, 15)
guide(ax, 4, 6, "$Q_1$")
save(fig, "l07-cost-curves")

# Problem 7.2: TC = 1000 + 10Q^2
q = np.linspace(2, 20, 200)
fig, ax = figure(5.8, 4.4)
axes(ax, "$Q$", "$\\$$", (0, 21), (0, 420), origin="0")
curve(ax, q, 1000 / q + 10 * q, NAVY, label="$ATC$", at=-1, dx=0.3)
qq = np.linspace(0, 20, 50)
curve(ax, qq, 20 * qq, BLUE, label="$MC = 20Q$", at=-1, dx=0.3, va="top")
curve(ax, qq, 10 * qq, GREEN, label="$AVC = 10Q$", at=-1, dx=0.3)
guide(ax, 10, 200, "10", "200")
point(ax, 10, 200, GOLD, 10)
save(fig, "l07-prob72")

# Learning curves for three learning factors
Qs = 2 ** np.arange(0, 9)
x = np.arange(0, 9)
fig, ax = figure(6.4, 4.2)
axes(ax, "$Q$", "Unit labor cost", (0, 9.4), (0, 11000), origin="0")
for m_, c in [(0.9, NAVY), (0.8, BLUE), (0.7, GOLD)]:
    y = 10000 * m_ ** x
    ax.plot(x, y, color=c, lw=3, marker="o", ms=6, mfc="white", mew=2)
    note(ax, 8.15, y[-1] + (350 if m_ == 0.9 else 0), f"$m = {m_}$", c, 15)
for k in range(0, 9, 2):
    tick(ax, x=k, label=str(Qs[k]))
for v in (5000, 10000):
    tick(ax, y=v, label=f"\\${v:,}")
save(fig, "l07-learning")

# Long-run total product and long-run total cost
s = np.linspace(0, 10, 300)
LRTP = 100 / (1 + np.exp(-(s - 5) * 1.1))
LRTP = LRTP - LRTP[0]
fig, (a1, a2) = figure(9.8, 3.8, ncols=2, wspace=0.45)
for ax, yl in ((a1, "$Q$"), (a2, "$LRTC$")):
    axes(ax, "Scale" if ax is a1 else "$Q$", yl, (0, 10.6), (0, 105), origin="0")
    for xb in (4, 6):
        ax.axvline(xb, color=GUIDE, lw=1.2, ls=(0, (4, 4)), ymax=0.9)
    for xa, lab in ((2, "IRTS"), (5, "CRTS"), (8.2, "DRTS")):
        note(ax, xa, 103, lab, SLATE, 12, ha="center")
curve(a1, s, LRTP, NAVY)
note(a1, 9.8, 92, "$LRTP$", NAVY, 18, ha="right", va="top")
qq = np.linspace(0, 10, 300)
LRTC = 18 * qq ** 0.55 + 0.004 * np.exp(0.9 * qq)
LRTC = np.where(qq < 4, 20 * qq ** 0.6, 0)
LRTC = 14 * qq - 3.2 * qq**2 + 0.27 * qq**3
curve(a2, qq, LRTC, BLUE, label="$LRTC$", at=-1, dx=0.1)
save(fig, "l07-long-run")

# The LRATC envelope of short-run ATC curves
fig, ax = figure(6.8, 4.4)
axes(ax, "$Q$", "$\\$$", (0, 12), (0, 10), origin="0")
lr = lambda v: 2.5 + 0.12 * (v - 6) ** 2
qx = np.linspace(0.8, 11.4, 300)
for c0 in (1.8, 3.2, 4.6, 6.0, 7.4, 8.8, 10.2):
    w = np.linspace(c0 - 1.3, c0 + 1.3, 80)
    # short-run curve tangent to the envelope at c0
    k = 0.75
    y = lr(c0) + 0.24 * (c0 - 6) * (w - c0) + k * (w - c0) ** 2
    ax.plot(w, y, color=GUIDE, lw=1.8, zorder=2)
curve(ax, qx, lr(qx), NAVY, lw=3.2, label="$LRATC$", at=-1, dx=0.1)
guide(ax, 6, 2.5, "$Q^*$ (MES)")
point(ax, 6, 2.5, GOLD, 10)
note(ax, 2.6, 9.0, "$SRATC$ curves", SLATE, 13)
save(fig, "l07-envelope")

# LRATC need not be U-shaped
fig, axs = figure(10.2, 2.9, ncols=3, wspace=0.28)
qx = np.linspace(0.5, 9.5, 100)
shapes = [(2 + 12 / (qx + 1.5), "Utilities"), (np.full_like(qx, 5), "Finance"), (2 + 0.08 * qx**2, "Real estate")]
for ax, (y, lab) in zip(axs, shapes):
    axes(ax, "$Q$", "$\\$$", (0, 10), (0, 10), origin="0")
    curve(ax, qx, y, NAVY, label="$LRATC$", at=-1, dx=-0.1, dy=0.8 if lab != "Utilities" else 0.9, ha="right", va="bottom")
    note(ax, 5, -2.6, lab, SLATE, 14, ha="center")
save(fig, "l07-lratc-shapes")

# Electric utilities: LRAC and the size distribution of firms
fig, ax = figure(7.6, 4.2)
edges = np.arange(0, 80, 5)
freq = np.array([57, 21, 12, 7, 4, 5, 4, 1, 0, 0, 1, 1, 0, 0, 1])
axes(ax, "$Q$", "$AC$", (0, 80), (4300, 6700))
ax.set_ylim(4300, 6700 * 1.03)
for e, f in zip(edges, freq):
    if f:
        ax.bar(e + 2.5, f * 30, width=4.4, bottom=4300, color=SHADE_BLUE, edgecolor="white", lw=1, zorder=1)
xq = np.linspace(1, 76, 300)
lrac = 4560 + 2100 * np.exp(-xq / 5.2) + 0.9 * np.maximum(0, xq - 62) ** 2.4
curve(ax, xq, lrac, NAVY, label="$LRAC$", at=-1, dx=0.8)
for xb in (20, 65):
    ax.plot([xb, xb], [4300, 6500], color=GUIDE, lw=1.2, ls=(0, (4, 4)))
for xa, lab in ((10, "Economies"), (42.5, "Constant returns"), (72, "Diseconomies")):
    note(ax, xa, 6600, lab, SLATE, 12, ha="center")
for v in (20, 42, 65, 75):
    tick(ax, x=v, label=str(v), y0=4300)
for v in (4500, 5500, 6500):
    tick(ax, y=v, label=f"{v:,}")
save(fig, "l07-utilities")
