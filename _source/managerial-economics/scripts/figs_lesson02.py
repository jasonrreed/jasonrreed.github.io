"""Figures for Lesson 2: Math review."""
import numpy as np
from econplot import *

# Linear function y = a + bx
fig, ax = figure(5.2, 3.8)
axes(ax, "$x$", "$y$", (0, 10), (0, 10), origin="0")
x = np.linspace(0, 9, 50)
curve(ax, x, 2 + 0.75 * x, NAVY, label="$y = a + bx$", dx=-0.2, dy=0.9, ha="right")
tick(ax, y=2, label="$a$")
ax.plot([4, 7, 7], [5, 5, 7.25], color=GOLD, lw=1.8, zorder=2)
note(ax, 5.5, 4.45, r"$\Delta x$", GOLD, 17, ha="center", va="center")
note(ax, 7.2, 6.1, r"$\Delta y$", GOLD, 17)
save(fig, "l02-linear")

# Linear function and its constant derivative
fig, (a1, a2) = figure(9.6, 3.6, ncols=2)
axes(a1, "$x$", "$y$", (0, 10), (0, 10))
curve(a1, x, 2 + 0.75 * x, NAVY)
tick(a1, y=2, label="$a$")
axes(a2, "$x$", "$y'(x)$", (0, 10), (0, 10))
curve(a2, np.array([0, 9]), np.array([5, 5]), BLUE)
tick(a2, y=5, label="$b$")
save(fig, "l02-linear-derivative")

# Concave function and its declining derivative, with tangent lines
xs = np.linspace(0, 10, 200)
f = lambda v: 8 - 0.32 * (v - 5) ** 2
fp = lambda v: -0.64 * (v - 5)

fig, (a1, a2) = figure(9.6, 3.9, ncols=2)
axes(a1, "$x$", "$y$", (0, 10), (0, 10))
curve(a1, xs, f(xs), NAVY)
for xv, c in [(2, BLUE), (5, GOLD), (8, GREEN)]:
    t = np.linspace(xv - 2.2, xv + 2.2, 10)
    a1.plot(t, f(xv) + fp(xv) * (t - xv), color=c, lw=1.8, ls=(0, (5, 4)), zorder=2)
    point(a1, xv, f(xv), c, 8)
    tick(a1, x=xv, label=f"$x_{{{[2, 5, 8].index(xv) + 1}}}$")
axes(a2, "$x$", "$y'(x)$", (0, 10), (-4, 4), xaxis_at=0)
curve(a2, xs, fp(xs), BLUE)
for xv, c in [(2, BLUE), (5, GOLD), (8, GREEN)]:
    point(a2, xv, fp(xv), c, 8)
note(a2, 5.3, 0.55, "slope is zero", SLATE, 12)
save(fig, "l02-tangents")

# Monotonic functions (appendix)
fig, (a1, a2) = figure(9.6, 3.6, ncols=2)
axes(a1, "$x$", "$f(x)$", (0, 10), (0, 10), origin="0")
xx = np.linspace(0.5, 9, 100)
curve(a1, xx, 1 + 0.1 * xx ** 2, NAVY, label="increasing", dx=0.2, va="bottom", ha="right")
for xv, lab in [(5, "$x_1$"), (7, "$x_2$")]:
    guide(a1, xv, 1 + 0.1 * xv ** 2, lab, None)
tick(a1, y=1 + 0.1 * 25, label="$f(x_1)$")
tick(a1, y=1 + 0.1 * 49, label="$f(x_2)$")
axes(a2, "$x$", "$f(x)$", (0, 10), (0, 10), origin="0")
curve(a2, xx, 9 / (0.5 + 0.35 * xx), BLUE)
note(a2, 3.2, 8.6, "decreasing", BLUE, 15)
for xv, lab in [(3, "$x_1$"), (5, "$x_2$")]:
    guide(a2, xv, 9 / (0.5 + 0.35 * xv), lab, None)
tick(a2, y=9 / (0.5 + 0.35 * 3), label="$f(x_1)$")
tick(a2, y=9 / (0.5 + 0.35 * 5), label="$f(x_2)$")
save(fig, "l02-monotonic")
