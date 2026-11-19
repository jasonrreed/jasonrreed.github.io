# FIN 30210 Managerial Economics

Lecture slides for FIN 30210 Managerial Economics at the University of Notre Dame, by Jason R. Reed, PhD.

Live site: <https://jasonrreed.github.io/managerial-economics/>

The slides are written in Markdown with [Quarto](https://quarto.org) and rendered to reveal.js presentations. This folder is the source. The rendered slides that visitors see live in the `managerial-economics/` folder at the top of the site repository.

The folder name starts with an underscore so GitHub Pages leaves it out of the public site.

## Layout

```
_quarto.yml            project settings
index.qmd              course landing page
lessons/
  _metadata.yml        slide settings shared by every lesson
  lesson-01.qmd ...    one file per lesson (01 to 11)
  figures/             graphs used in the slides (SVG)
theme/
  slides.scss          slide theme (colors, type, layouts)
  site.css             landing page styles
  title-curves.svg     title slide art
  section-grid.svg     section divider art
scripts/
  econplot.py          shared helpers for drawing graphs in the slide style
  figs_lesson02.py ... one script per lesson that writes its figures
  fonts/               the slide fonts, used to label graphs (SIL Open Font License)
```

## Working on the slides

Install Quarto (<https://quarto.org/docs/get-started/>), then from the repo folder:

```
quarto preview lessons/lesson-01.qmd
```

The preview reloads as you save. In a deck, press `S` for speaker notes, `F` for full screen, and `E` for a print layout you can save as a PDF.

### Changing a graph

Every graph is drawn in Python so it matches the slides. Edit the lesson's script and rerun it from the repo root:

```
pip install matplotlib numpy
python scripts/figs_lesson04.py
```

It rewrites the SVGs in `lessons/figures/`, and the deck picks them up on the next render.

### Slide building blocks

| Markdown                                   | What it makes                                   |
|--------------------------------------------|-------------------------------------------------|
| `## Title`                                 | A new slide                                     |
| `# Title {.section-break ...}`             | A navy section divider (copy one from lesson 1) |
| `::: {.definition}` with `[Term]{.term}`   | A shaded definition box                         |
| `::: {.prompt}`                            | A discussion question, marked with a gold "?"   |
| `::: {.problem}` with `[Problem 1.03]{.problem-label}` | A worked-problem box                |
| `::: {.solution-step .fragment}`           | One solution line, revealed on click            |
| `::: {.cols-2}` / `{.cols-3}` / `{.cols-4}` with `::: {.col}` children | Side-by-side items |
| `::: {.fragment}`                          | Anything revealed on click                      |
| `::: notes`                                | Speaker notes                                   |
| `$$ ... $$`                                | A displayed equation (LaTeX)                    |
| `::: {.split}` with an image and a `::: {.col}` | A graph beside text                        |
| `::: {.terms}` with `.t` / `.d` pairs      | A term-and-definition list                      |
| `<table class="payoff">` (see lesson 11)   | A payoff matrix; `td.ne` marks a Nash equilibrium |

## Publishing changes

From this folder, render the slides and copy them over the published copy:

```
quarto render
rm -rf ../../managerial-economics
cp -r _site ../../managerial-economics
```

Then commit and push the site repository. GitHub Pages updates in a minute or two.
