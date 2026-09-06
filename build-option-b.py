"""Build the option-b/ comparison folder from the main pages.

Option B is a second look for the same site. It uses the same HTML as the
main pages so every copy edit shows up in both designs. This script copies
each page into option-b/, swaps the stylesheet and font link, and repoints
the shared files (css, js) one folder up. Run it after editing any page:

    python build-option-b.py

Delete option-b/ and this script once the owner has picked a design.
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'option-b')
PAGES = ['index.html', 'spaces-parking.html', 'how-to-pay.html', 'about.html',
         'contact.html', 'privacy.html', 'sms-terms.html', '404.html']

FONT_A = re.compile(r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">')
FONT_B = ('<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900'
          '&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">')

os.makedirs(OUT, exist_ok=True)
for name in PAGES:
    s = open(os.path.join(ROOT, name), encoding='utf-8').read()
    s = FONT_A.sub(FONT_B, s, count=1)
    # stylesheet and script live one level up; 404 uses absolute paths
    s = s.replace('href="css/style.css"', 'href="../css/style-b.css"')
    s = s.replace('href="/css/style.css"', 'href="../css/style-b.css"')
    s = s.replace('src="js/nav.js"', 'src="../js/nav.js"')
    s = s.replace('src="/js/nav.js"', 'src="../js/nav.js"')
    # 404 page links are absolute; make them relative inside the folder
    s = s.replace('href="/', 'href="')
    s = s.replace('<title>', '<title>[Option B] ', 1)
    open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(s)
    print('wrote option-b/' + name)
