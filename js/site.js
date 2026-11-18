/* Media list (media.html) and recent commentary (index.html). Data lives in js/media-data.js. */
(() => {
  const DATA = (window.MEDIA || []).slice().sort((a, b) => (a.date < b.date ? 1 : -1));
  const TYPES = {
    written: "Written by Jason",
    quoted: "Interview or quote",
    nd: "Notre Dame News",
    podcast: "Podcast",
  };
  const MONTHS = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"];

  function formatDate(m) {
    if (m.dateLabel) return m.dateLabel;
    const [y, mo, d] = m.date.split("-").map(Number);
    if (m.precision === "year") return String(y);
    if (m.precision === "month") return `${MONTHS[mo - 1]} ${y}`;
    return `${MONTHS[mo - 1]} ${d}, ${y}`;
  }

  const el = (tag, cls, text) => {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  };

  function mentionItem(m) {
    const li = el("li", "mention" + (m.type === "written" ? " is-written" : ""));
    const meta = el("div", "mention-meta");
    meta.append(el("span", "outlet", m.outlet), el("span", "kind", TYPES[m.type] || ""));
    const body = el("div", "mention-body");
    const a = el(m.url ? "a" : "span", (m.described ? "described " : "") + (m.url ? "" : "unlinked"), m.title);
    if (m.url) a.href = m.url;
    body.append(a, el("span", "date", formatDate(m)));
    if (m.note) body.append(el("span", "note", m.note));
    li.append(meta, body);
    return li;
  }

  // ----- home: recent commentary -----
  const recent = document.querySelector("[data-recent]");
  if (recent) {
    const n = Number(recent.dataset.recent) || 4;
    DATA.filter((m) => m.url && !m.described && m.type !== "podcast").slice(0, n).forEach((m) => {
      const li = el("li");
      const a = el("a", "", m.title);
      a.href = m.url;
      li.append(el("span", "outlet", m.outlet), a, el("span", "date", formatDate(m)));
      recent.append(li);
    });
  }

  // ----- media page -----
  const list = document.querySelector("#media-list");
  if (!list) return;

  const state = { type: "all", outlet: "all", q: "" };
  const typeButtons = document.querySelectorAll("[data-type]");
  const outletSelect = document.querySelector("#outlet");
  const search = document.querySelector("#search");
  const count = document.querySelector("#media-count");

  [...new Set(DATA.map((m) => m.outlet))].sort((a, b) => a.localeCompare(b)).forEach((o) => {
    const opt = el("option", "", o);
    opt.value = o;
    outletSelect.append(opt);
  });

  function matches(m) {
    if (state.type !== "all" && m.type !== state.type) return false;
    if (state.outlet !== "all" && m.outlet !== state.outlet) return false;
    if (state.q) {
      const hay = `${m.title} ${m.outlet} ${m.note || ""}`.toLowerCase();
      if (!state.q.split(/\s+/).every((w) => hay.includes(w))) return false;
    }
    return true;
  }

  function render() {
    const shown = DATA.filter(matches);
    list.replaceChildren();
    if (!shown.length) {
      const empty = el("div", "empty");
      empty.append(el("p", "", "Nothing matches these filters."));
      const reset = el("button", "reset", "Show everything");
      reset.type = "button";
      reset.addEventListener("click", clearFilters);
      empty.append(reset);
      list.append(empty);
    } else {
      const years = new Map();
      shown.forEach((m) => {
        const y = m.date.slice(0, 4);
        if (!years.has(y)) years.set(y, []);
        years.get(y).push(m);
      });
      years.forEach((items, y) => {
        const section = el("section", "year-group");
        section.setAttribute("aria-label", y);
        section.append(el("h2", "year-label", y));
        const ul = el("ul", "mentions");
        items.forEach((m) => ul.append(mentionItem(m)));
        section.append(ul);
        list.append(section);
      });
    }
    count.textContent = shown.length === DATA.length
      ? `${DATA.length} pieces`
      : `Showing ${shown.length} of ${DATA.length} pieces`;
  }

  function clearFilters() {
    state.type = "all";
    state.outlet = "all";
    state.q = "";
    outletSelect.value = "all";
    search.value = "";
    typeButtons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.type === "all")));
    render();
  }

  typeButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      state.type = btn.dataset.type;
      typeButtons.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      render();
    });
  });
  outletSelect.addEventListener("change", () => {
    state.outlet = outletSelect.value;
    render();
  });
  search.addEventListener("input", () => {
    state.q = search.value.trim().toLowerCase();
    render();
  });
  document.querySelector(".filters").addEventListener("submit", (e) => e.preventDefault());

  render();
})();
