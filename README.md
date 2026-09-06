# Vineland Development — marketing website

A small, static eight-page website for **Vineland Development**, a family-run
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
| `privacy.html` | Privacy policy (carrier requirement for texting) |
| `sms-terms.html` | SMS terms (carrier requirement for texting) |
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

Photo spots currently render as quiet stone-colored blocks with a small
caption, so the pages look finished before any photos exist. To drop in a
real photo:

1. Put the image file in the `images/` folder (e.g. `images/home-hero.jpg`).
   The expected filename is in a comment right above each photo spot in
   the HTML.
2. In the page, find the matching `<!-- Photo slot: ... -->` comment. The
   line under it looks like
   `<figure class="ph r-45" data-label="The property, Executive Road"></figure>`.
   Put an `<img>` inside it and add `has-img` to the class, like this:
   `<figure class="ph r-45 has-img"><img src="images/home-hero.jpg" alt="Row of drive-up units"></figure>`
3. Commit and push. That's the whole job.

The `r-45`, `r-43`, `r-32`, `r-11` classes set the shape of the box (4:5,
4:3, 3:2, square). The photo is cropped to fit, so leave the class alone.
Keep photos reasonably sized (roughly 1600px wide is plenty) so pages stay
fast on phones.

## Showing the site on a phone before it is live

Double-click `preview.cmd` in this folder and leave the black window open.
Then on this PC open `http://localhost:8765/`, or on a phone that is on the
Tailscale network open `http://backofficetower:8765/`. Add `/option-b/` or
`/themes/c.html` to the address to see the other designs. Close the black
window when done. If Windows asks about the firewall the first time, click
Allow, otherwise the phone will not be able to reach it.

## Two designs to compare (temporary)

While the owner picks a look, the repo carries two designs that share the
same words:

- **Option A** is the main pages in the repo root, styled by `css/style.css`.
- **Option B** is the `option-b/` folder, styled by `css/style-b.css`. Open
  `option-b/index.html` to see it.

There are also three front-page-only sketches in `themes/` (`c.html`,
`d.html`, `e.html`), each self-contained with its own styles, plus the small
animated line drawing `themes/model.svg` they share. They exist only to
compare looks. Delete `themes/` once a direction is chosen.

The pages in `option-b/` are generated copies. Do not edit them by hand.
Edit the main pages, then run `python build-option-b.py` to refresh the
folder. Once a design is chosen, delete `option-b/`, `build-option-b.py`,
and the losing stylesheet.

## Still to be filled in later

Two things are intentionally left as placeholders and get pasted in once
they're ready:

- **Online card payment link.** On `how-to-pay.html`, the card section shows a
  dashed "Online payments coming soon" button. When the secure payment page
  is live and linking it is approved, replace that `<span class="btn-soon">`
  with a real link to it.
- **Card processing fee wording.** The same section says 3%, credit cards
  only. That came from the office payment policy notes, not from a signed
  document. Confirm before the page goes live.

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
