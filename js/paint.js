/*
  Brushstroke painting on <canvas>.
  - .hero-canvas    the home-page hero: a simulated price path and an adaptive-learning forecast
  - .band           the painted band at the foot of each page header
  - .art-canvas     small abstract paintings (portrait frame, AIM panel)
  Everything is drawn from a seed, so a page looks the same on every visit until "Repaint" is pressed.
*/
(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  // ---------- helpers ----------
  const rng = (seed) => {
    let a = seed >>> 0;
    return () => {
      a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };
  const hash = (a, b) => {
    let h = (Math.imul(a | 0, 374761393) + Math.imul(b | 0, 668265263)) | 0;
    h = Math.imul(h ^ (h >>> 13), 1274126177);
    return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
  };
  const gauss = (r) => {
    let u = 0, v = 0;
    while (!u) u = r();
    while (!v) v = r();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  };
  const hexRgb = (h) => {
    const n = parseInt(h.trim().replace("#", ""), 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
  };
  const tint = (c, k) => {
    const t = Math.abs(k), f = k < 0 ? 0 : 255;
    return c.map((v) => Math.round(v + (f - v) * t));
  };
  const easeOut = (x) => 1 - Math.pow(1 - x, 3);

  function normals(pts) {
    return pts.map((_, i) => {
      const a = pts[Math.max(0, i - 1)], b = pts[Math.min(pts.length - 1, i + 1)];
      const dx = b.x - a.x, dy = b.y - a.y, len = Math.hypot(dx, dy) || 1;
      return { x: -dy / len, y: dx / len };
    });
  }

  function sizeCanvas(canvas, ctx) {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const W = canvas.clientWidth, H = canvas.clientHeight;
    canvas.width = Math.max(1, Math.round(W * dpr));
    canvas.height = Math.max(1, Math.round(H * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { W, H };
  }

  // ---------- the brush ----------
  // A stroke is a bundle of bristles following one path. Each bristle has its own offset,
  // tone and paint load, so the stroke picks up a lit edge, a shadowed edge and dry-brush gaps.
  function makeStroke(pts, { width, color, alpha = 0.92, seed = 1, bristles }) {
    const r = rng(seed);
    const base = hexRgb(color);
    const count = bristles || Math.max(14, Math.min(60, Math.round(width * 2.2)));
    const list = [];
    for (let i = 0; i < count; i++) {
      const u = (i + r() * 0.9) / count - 0.5;
      const edge = Math.abs(u) * 2;
      let k = (r() - 0.5) * 0.18;
      if (u < -0.22) k += 0.24 * r();
      if (u > 0.22) k -= 0.3 * r();
      list.push({
        off: u * width,
        col: tint(base, k),
        lw: 0.7 + r() * 1.5,
        a: alpha * (0.45 + 0.55 * r()) * (1 - edge * 0.45),
        dry: 0.03 + edge * edge * 0.35,
        ph: r() * 6.283,
        amp: width * (0.02 + r() * 0.05),
        id: (seed * 131 + i * 7919) | 0,
      });
    }
    return { pts, n: normals(pts), list, done: 0 };
  }

  function drawStroke(ctx, s, upto) {
    const N = s.pts.length - 1;
    const end = Math.min(N, Math.floor(upto));
    if (end <= s.done) return;
    ctx.lineCap = "round";
    for (const b of s.list) {
      ctx.strokeStyle = `rgb(${b.col[0]},${b.col[1]},${b.col[2]})`;
      ctx.lineWidth = b.lw;
      for (let i = s.done; i < end; i++) {
        if (hash(b.id, i) < b.dry) continue;
        const t0 = i / N, t1 = (i + 1) / N;
        const tp0 = Math.min(1, t0 * 14 + 0.15, (1 - t0) * 14 + 0.15);
        const tp1 = Math.min(1, t1 * 14 + 0.15, (1 - t1) * 14 + 0.15);
        const o0 = b.off * tp0 + Math.sin(b.ph + i * 0.21) * b.amp;
        const o1 = b.off * tp1 + Math.sin(b.ph + (i + 1) * 0.21) * b.amp;
        const p0 = s.pts[i], p1 = s.pts[i + 1], n0 = s.n[i], n1 = s.n[i + 1];
        ctx.globalAlpha = b.a * (0.7 + 0.3 * hash(b.id + 7, i));
        ctx.beginPath();
        ctx.moveTo(p0.x + n0.x * o0, p0.y + n0.y * o0);
        ctx.lineTo(p1.x + n1.x * o1, p1.y + n1.y * o1);
        ctx.stroke();
      }
    }
    ctx.globalAlpha = 1;
    s.done = end;
  }

  // Linen weave under the paint.
  function weave(ctx, W, H, r, strength = 1) {
    ctx.save();
    for (let y = 0; y < H; y += 3) {
      ctx.globalAlpha = (0.025 + r() * 0.03) * strength;
      ctx.fillStyle = r() < 0.5 ? "#000" : "#fff";
      ctx.fillRect(0, y, W, 1);
    }
    for (let x = 0; x < W; x += 3) {
      ctx.globalAlpha = (0.02 + r() * 0.025) * strength;
      ctx.fillStyle = r() < 0.5 ? "#000" : "#fff";
      ctx.fillRect(x, 0, 1, H);
    }
    ctx.restore();
  }

  // Broad, low-contrast strokes laid down first, like an underpainting.
  function underpaint(ctx, W, H, r, colors, rows = 6) {
    for (let j = 0; j < rows; j++) {
      const y0 = (H * (j + 0.5)) / rows + (r() - 0.5) * H * 0.08;
      const amp = H * (0.02 + r() * 0.04), freq = 0.002 + r() * 0.004, ph = r() * 6.283;
      const tilt = (r() - 0.5) * H * 0.14;
      const pts = [];
      for (let x = -60; x <= W + 60; x += 18) {
        pts.push({ x, y: y0 + Math.sin(ph + x * freq) * amp + tilt * (x / W) });
      }
      const s = makeStroke(pts, {
        width: (H / rows) * (1.15 + r() * 0.5),
        color: colors[j % colors.length],
        alpha: 0.3,
        seed: Math.floor(r() * 1e6),
        bristles: 46,
      });
      drawStroke(ctx, s, Infinity);
    }
  }

  // Redraw when the width changes (not on mobile address-bar height jitter).
  function onWidthChange(el, fn) {
    let last = el.clientWidth, timer = 0;
    window.addEventListener("resize", () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        if (Math.abs(el.clientWidth - last) > 2) {
          last = el.clientWidth;
          fn();
        }
      }, 160);
    });
  }

  const afterFonts = (fn) => {
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fn, fn);
    else fn();
  };

  // ---------- home hero ----------
  function hero(canvas) {
    const ctx = canvas.getContext("2d");
    const section = canvas.closest(".hero");
    const textEl = section.querySelector(".hero-text");
    const capEl = section.querySelector(".hero-caption");
    let seed = Number(canvas.dataset.seed) || 2015;
    let raf = 0;

    function build() {
      const { W, H } = sizeCanvas(canvas, ctx);
      const r = rng(seed);
      ctx.fillStyle = "#142B4C";
      ctx.fillRect(0, 0, W, H);
      underpaint(ctx, W, H, r, ["#0E2039", "#24406A", "#1A3459"]);
      weave(ctx, W, H, r);

      // Fit the chart between the headline block and the caption.
      const top0 = section.getBoundingClientRect().top;
      let top = textEl.getBoundingClientRect().bottom - top0 + 28;
      let bot = capEl.getBoundingClientRect().top - top0 - 18;
      const minBand = Math.min(H * 0.26, 210);
      if (bot - top < minBand) top = bot - minBand;

      // A price that switches between a calm, rising regime and a volatile, falling one,
      // and a constant-gain learning forecast that only sees prices after they happen.
      const n = Math.max(60, Math.min(240, Math.round(W / 7)));
      const regimes = [{ mu: 0.2, s: 0.85, stay: 0.975 }, { mu: -0.3, s: 1.8, stay: 0.93 }];
      const gain = 0.08;
      let reg = 0, p = 0, f = 0;
      const P = [], F = [];
      for (let i = 0; i < n; i++) {
        if (r() > regimes[reg].stay) reg = 1 - reg;
        F.push(f);
        p += regimes[reg].mu + regimes[reg].s * gauss(r);
        P.push(p);
        f += gain * (p - f);
      }
      const all = P.concat(F);
      const lo = Math.min(...all), hi = Math.max(...all);
      const x0 = W * 0.03, x1 = W * 0.97;
      const map = (v, i) => ({
        x: x0 + ((x1 - x0) * i) / (n - 1),
        y: bot - ((v - lo) / (hi - lo || 1)) * (bot - top),
      });
      const pw = Math.max(9, Math.min(22, W * 0.013));
      return {
        price: makeStroke(P.map(map), { width: pw, color: "#ECEEEA", alpha: 0.95, seed: seed + 1 }),
        fc: makeStroke(F.map(map), { width: pw * 0.5, color: "#E2A42B", alpha: 0.95, seed: seed + 2 }),
      };
    }

    function paint(animated) {
      cancelAnimationFrame(raf);
      const { price, fc } = build();
      const N = price.pts.length - 1;
      if (!animated || reduceMotion.matches) {
        drawStroke(ctx, price, N);
        drawStroke(ctx, fc, N);
        return;
      }
      const t0 = performance.now(), dur = 2600, lag = 0.06;
      const tick = (now) => {
        const x = Math.min(1, (now - t0) / dur), e = easeOut(x);
        drawStroke(ctx, price, e * N);
        drawStroke(ctx, fc, (Math.max(0, e - lag) / (1 - lag)) * N);
        if (x < 1) raf = requestAnimationFrame(tick);
      };
      raf = requestAnimationFrame(tick);
    }

    afterFonts(() => paint(true));
    onWidthChange(canvas, () => paint(false));
    const btn = section.querySelector(".repaint");
    if (btn) {
      btn.addEventListener("click", () => {
        seed = Math.floor(Math.random() * 1e9);
        paint(true);
      });
    }
  }

  // ---------- page-header band ----------
  function band(canvas) {
    const ctx = canvas.getContext("2d");
    const kind = canvas.dataset.kind || "flow";
    const colors = (canvas.dataset.colors || "#E2A42B,#ECEEEA").split(",");
    const seed = Number(canvas.dataset.seed) || 7;
    let raf = 0;

    function paint(animated) {
      cancelAnimationFrame(raf);
      const { W, H } = sizeCanvas(canvas, ctx);
      ctx.clearRect(0, 0, W, H);
      const r = rng(seed);
      const strokes = colors.map((c, j) => {
        const amp = H * (0.1 + r() * 0.1), f1 = 0.003 + r() * 0.003, f2 = 0.01 + r() * 0.01;
        const ph1 = r() * 6.283, ph2 = r() * 6.283;
        const pts = [];
        for (let x = -30; x <= W + 30; x += 8) {
          const t = x / W;
          const wave = Math.sin(ph1 + x * f1) * amp + Math.sin(ph2 + x * f2) * amp * 0.35;
          const y = kind === "rise"
            ? H * (0.86 - t * 0.62) + wave * 0.5 + j * H * 0.14
            : H * (0.38 + j * 0.26) + wave;
          pts.push({ x, y });
        }
        const w = j === 0 ? Math.max(10, Math.min(26, W * 0.016)) : Math.max(6, Math.min(14, W * 0.008));
        return makeStroke(pts, { width: w, color: c, alpha: 0.93, seed: seed + j * 17 });
      });
      const N = strokes[0].pts.length - 1;
      if (!animated || reduceMotion.matches) {
        strokes.forEach((s) => drawStroke(ctx, s, N));
        return;
      }
      const t0 = performance.now(), dur = 1700;
      const tick = (now) => {
        const x = Math.min(1, (now - t0) / dur);
        strokes.forEach((s, j) => {
          const d = j * 0.12;
          drawStroke(ctx, s, easeOut(Math.max(0, Math.min(1, (x - d) / (1 - d)))) * N);
        });
        if (x < 1) raf = requestAnimationFrame(tick);
      };
      raf = requestAnimationFrame(tick);
    }

    paint(true);
    onWidthChange(canvas, () => paint(false));
  }

  // ---------- small abstract paintings ----------
  function art(canvas) {
    const ctx = canvas.getContext("2d");
    const seed = Number(canvas.dataset.seed) || 88;
    const palette = (canvas.dataset.palette || "#24406A,#0E2039,#A3283D,#E2A42B,#3A5A86,#ECEEEA").split(",");
    const reach = Number(canvas.dataset.reach) || 0.72;

    function paint() {
      const { W, H } = sizeCanvas(canvas, ctx);
      const r = rng(seed);
      ctx.fillStyle = "#142B4C";
      ctx.fillRect(0, 0, W, H);
      underpaint(ctx, W, H, r, ["#0E2039", "#24406A"], 4);
      weave(ctx, W, H, r);
      const count = 9;
      for (let j = 0; j < count; j++) {
        const yA = r() * H * reach, yB = r() * H * reach;
        const bend = (r() - 0.5) * H * 0.25;
        const pts = [];
        for (let k = 0; k <= 40; k++) {
          const t = k / 40;
          pts.push({ x: -20 + t * (W + 40), y: yA + (yB - yA) * t + Math.sin(t * Math.PI) * bend });
        }
        const s = makeStroke(pts, {
          width: Math.min(W, H) * (0.05 + r() * 0.12),
          color: palette[j % palette.length],
          alpha: 0.55 + r() * 0.4,
          seed: seed + j * 31,
        });
        drawStroke(ctx, s, Infinity);
      }
    }

    paint();
    onWidthChange(canvas, paint);
  }

  document.querySelectorAll(".hero-canvas").forEach(hero);
  document.querySelectorAll("canvas.band").forEach(band);
  document.querySelectorAll("canvas.art-canvas").forEach(art);
})();
