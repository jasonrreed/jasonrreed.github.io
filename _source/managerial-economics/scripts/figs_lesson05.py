"""Figures for Lesson 5: Production."""
import numpy as np
from econplot import *

# Total, average, and marginal product from the production table (capital fixed at 500)
L = np.arange(1, 11)
Q = np.array([3, 6, 16, 29, 43, 55, 58, 60, 59, 56])
MP = np.diff(Q)                       # MP for L = 2..10
AP = Q / L

fig, (a1, a2) = figure(10.2, 4.0, ncols=2, wspace=0.3)
axes(a1, "$L$", "$Q$", (0, 11.5), (0, 74), origin="0")
a1.plot(L, Q, color=NAVY, lw=3, marker="o", ms=6, mfc="white", mew=2, zorder=3)
note(a1, 9.2, 62.5, "$TP_L$", NAVY, 18)
for v in (2, 4, 6, 8, 10):
    tick(a1, x=v, label=str(v))
for v in (20, 40, 60):
    tick(a1, y=v, label=str(v))

axes(a2, "$L$", "", (0, 11.5), (-4, 16), origin=None, xaxis_at=0)
a2.plot(L[1:], MP, color=BLUE, lw=3, marker="o", ms=6, mfc="white", mew=2, zorder=3)
a2.plot(L, AP, color=GOLD, lw=3, marker="o", ms=6, mfc="white", mew=2, zorder=3)
note(a2, 1.0, 11.5, "$MP_L$", BLUE, 18)
note(a2, 9.3, 7.4, "$AP_L$", GOLD, 18)
point(a2, 6.45, 9.0, NAVY, 9)
note(a2, 6.8, 11.2, "$MP_L = AP_L$\nat the peak of $AP_L$", SLATE, 12)
for v in (2, 4, 6, 8, 10):
    tick(a2, x=v, label=str(v))
for v in (0, 5, 10):
    tick(a2, y=v, label=str(v))
save(fig, "l05-products")
