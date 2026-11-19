# jasonrreed.github.io

Personal site for Jason Reed, Wade Family Associate Teaching Professor of Finance at the University of Notre Dame.

It's plain HTML, CSS and JavaScript with no build step. GitHub Pages serves the files as they are.

## Pages

| File | Page |
|---|---|
| `index.html` | About (home), with the painted market chart, bio, education, research, recent commentary and contact |
| `teaching.html` | Courses and work beyond the classroom |
| `materials.html` | Notes and materials: links to course slides, such as the Managerial Economics decks in the `managerial-economics` repository |
| `awards.html` | Awards timeline |
| `media.html` | Media mentions with filters and search |

## Course slides

`managerial-economics/` holds the rendered FIN 30210 Managerial Economics slides, served at https://jasonrreed.github.io/managerial-economics/. Don't edit those files by hand. The source is in `_source/managerial-economics/`, and its README explains how to change a lesson and republish.

## Common updates

**Add a media mention.** Open `js/media-data.js`, copy an entry and edit it. The Media page and the home page's "Recent commentary" both read from this file and sort by date on their own.

**Add a headshot.** Save a portrait as `images/headshot.jpg` (portrait orientation, about 800 × 1000 pixels). It replaces the painted "JR" panel on the home page automatically.

**Add an award.** Copy one `<li>` block inside `<ol class="timeline">` in `awards.html`.

**Change the colors or fonts.** They're defined at the top of `css/style.css`.

## Hosting

The repository must be named `jasonrreed.github.io` for the site to appear at https://jasonrreed.github.io/.

The `.nojekyll` file tells GitHub Pages to serve the files directly instead of running Jekyll. If an old `index.md` or `_config.yml` is still in the repository, delete them so they don't compete with `index.html`.

`sitemap.xml` and `robots.txt` help search engines find the pages. To get indexed faster, add the site in Google Search Console and submit `https://jasonrreed.github.io/sitemap.xml`.
