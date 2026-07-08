# Vineland Development — marketing website

A small, static five-page website for **Vineland Development**, a family-run
flex-space, storage, and parking facility in Winter Haven, Florida. Plain
HTML + CSS with one tiny vanilla-JS file for the mobile menu — **no build
step, no framework, no server code.** Open any `.html` file in a browser and
it works.

Hosted on **GitHub Pages** from the `main` branch. Preview URL lives at the
GitHub Pages address for this repo; the custom domain
(`vinelanddevelopment.com`) gets connected in a later step.

## Pages

| File | Page |
|------|------|
| `index.html` | Home |
| `spaces-parking.html` | Spaces & Parking |
| `how-to-pay.html` | How to Pay |
| `about.html` | About |
| `contact.html` | Contact |
| `404.html` | Not-found page |

Shared styles are in `css/style.css`; the mobile-menu toggle is `js/nav.js`.
The header and footer are copy-pasted into each page (no templating), so if
you change a nav link or the footer, change it in **every** `.html` file.

## Editing the text

All the words you see on the site live directly in the `.html` files as plain
text. To change a headline or a paragraph, open the page in a text editor,
find the sentence, edit it, and save. Then commit and push (see below) and the
live site updates in a minute or two. You do not need to touch the CSS to
change wording.

## Adding photos

Photo spots currently show light-gray placeholder blocks. To drop in a real
photo:

1. Put the image file in the `images/` folder (e.g. `images/home-hero.jpg`).
   The expected filenames are listed in `images/.gitkeep` and in a comment
   right above each photo spot in the HTML.
2. In the page, find the matching `<!-- Photo slot: ... -->` comment and
   replace the placeholder line
   `<div class="img-slot">Facility photo …</div>`
   with
   `<img src="images/home-hero.jpg" alt="Short description of the photo">`.
3. Commit and push. That's the whole job — one file dropped in, one line
   changed.

Keep photos reasonably sized (roughly 1600px wide is plenty) so pages stay
fast on phones.

## Still to be filled in later

Two things are intentionally left as placeholders and get pasted in once
they're ready:

- **Online card payment link.** On `how-to-pay.html`, the card section shows a
  gray "Online card payments coming soon — call the office" button. When the
  secure payment page (Stripe) is live, replace that `<span class="btn-soon">`
  with a real link to it.
- **Card processing fee percentage.** The same section says
  "**[X]% processing fee**". Replace `[X]` with the real number when it's
  confirmed. (It is deliberately not filled in yet — do not guess it.)

## Publishing changes

```
git add -A
git commit -m "Describe what you changed"
git push
```

GitHub Pages rebuilds automatically from `main` within a minute or two.

## Design of record

The original Claude-design mockups are kept in `design/` (the `.dc.html`
files). Those are the source the live pages were converted from — reference
only, not served to visitors.
