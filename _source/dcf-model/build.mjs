// Builds the published DCF Model Generator from DCF_Model_Generator.html.
//
// The source file runs on its own in a browser (it compiles itself with Babel and
// loads Tailwind from a CDN), which is handy for editing. The published page is
// compiled ahead of time instead: JSX becomes plain JavaScript, Tailwind becomes a
// small stylesheet, and React is served from the site, so the page loads quickly
// and doesn't depend on outside CDNs.
//
// Usage, from this folder:  npm install  then  npm run build
// Output goes to ../../dcf-model/ (the published folder at the top of the site).
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import babel from "@babel/core";
import postcss from "postcss";
import tailwindcss from "tailwindcss";

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.resolve(here, process.argv[2] || "../../dcf-model");
const src = fs.readFileSync(path.join(here, "DCF_Model_Generator.html"), "utf8");

const jsx = src.match(/<script type="text\/babel">([\s\S]*?)<\/script>/)[1];
const { code } = babel.transformSync(jsx, {
  babelrc: false, configFile: false, cwd: here,
  presets: [["@babel/preset-react", { runtime: "classic" }]],
});

const css = (await postcss([tailwindcss({ content: [{ raw: src, extension: "html" }] })])
  .process("@tailwind base;\n@tailwind components;\n@tailwind utilities;", { from: undefined })).css
  .replace(/\/\*[\s\S]*?\*\//g, "").replace(/\n\s*\n/g, "\n");

const head = src.slice(0, src.indexOf("</head>"))
  .replace(/\s*<script src="[^"]*"><\/script>/g, "");

const html = `${head}
<style>
${css}
</style>
</head>
<body class="bg-gray-100">
<div id="root"></div>
<script src="vendor/react.production.min.js"></script>
<script src="vendor/react-dom.production.min.js"></script>
<script>
${code}
</script>
</body>
</html>
`;

fs.mkdirSync(path.join(out, "vendor"), { recursive: true });
fs.writeFileSync(path.join(out, "index.html"), html);
for (const [pkg, file] of [["react", "react.production.min.js"], ["react-dom", "react-dom.production.min.js"]]) {
  fs.copyFileSync(path.join(here, "node_modules", pkg, "umd", file), path.join(out, "vendor", file));
}
console.log(`Built ${path.join(out, "index.html")} (${(html.length / 1024).toFixed(0)} KB)`);
