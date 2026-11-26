# DCF Model Generator

The interactive discounted cash flow model for FIN 40610 Security Analysis, published at https://jasonrreed.github.io/dcf-model/.

`DCF_Model_Generator.html` is the source. It runs on its own: open it in a browser and it works, which makes it easy to edit and test. It needs an internet connection, because it loads React, Tailwind and Babel from CDNs.

The published copy in `dcf-model/` at the top of the site is built from it ahead of time, so it loads faster and doesn't depend on those CDNs. Don't edit the files in `dcf-model/` by hand.

## Publishing a change

1. Edit `DCF_Model_Generator.html` and check it in a browser.
2. From this folder, with Node.js installed:

   ```
   npm install
   npm run build
   ```

   This rewrites `dcf-model/index.html` and `dcf-model/vendor/` at the top of the site.
3. Commit and push the site repository.
