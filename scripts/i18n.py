# Zweisprachigkeit: setzt hreflang, Sprachumschalter, Umschalter-CSS und (nur auf deutschen Seiten)
# die Erstbesuch-Umleitung in die statischen Seiten. Wiederholbar: entfernt vorher, was schon da ist.
#   python3 scripts/i18n.py de    deutsche Seiten
#   python3 scripts/i18n.py en    englische Seiten unter en/
# Die Blogseiten tragen dieselben Bausteine; wer dort eine Seite von Hand anlegt, kopiert sie
# aus einem vorhandenen Beitrag. Regeln stehen in CLAUDE.md, Abschnitt Zweisprachigkeit.
import sys, re, pathlib

SITE = 'https://dynamicspro.de'

def en_path(p):
    return '/en' + p

def hreflang(p):
    return (f'<link rel="alternate" hreflang="de" href="{SITE}{p}">\n'
            f'<link rel="alternate" hreflang="en" href="{SITE}{en_path(p)}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{SITE}{p}">')

# Nur auf deutschen Seiten. Leitet einen Besucher, dessen erste Browsersprache nicht Deutsch ist,
# beim Einstieg von aussen auf die englische Fassung derselben Seite. Nie bei Navigation innerhalb
# der Site, nie mit ?lang=de, nie fuer Crawler oder automatisierte Browser. Speichert nichts.
REDIRECT = '''<script>
/* Sprache vorbelegen: siehe CLAUDE.md, Abschnitt Zweisprachigkeit. Speichert nichts. */
(function(){try{
  var q=new URLSearchParams(location.search);
  if(q.get('lang')==='de'){q.delete('lang');var s=q.toString();history.replaceState(null,'',location.pathname+(s?'?'+s:'')+location.hash);return}
  if(navigator.webdriver||/bot|crawl|spider|slurp|preview|facebookexternalhit|lighthouse|headless/i.test(navigator.userAgent))return;
  var r=document.referrer;if(r&&r.indexOf(location.origin+'/')===0)return;
  var l=(navigator.languages&&navigator.languages[0])||navigator.language||'';
  if(/^de(-|$)/i.test(l))return;
  location.replace('/en'+location.pathname+location.search+location.hash);
}catch(e){}})();
</script>'''

def switch(p, lang, tag='a'):
    """Link auf die jeweils andere Sprachfassung derselben Seite."""
    if lang == 'de':
        a = f'<a class="lang" href="{en_path(p)}" hreflang="en" lang="en" aria-label="English version">EN</a>'
    else:
        a = f'<a class="lang" href="{p}?lang=de" hreflang="de" lang="de" aria-label="Deutsche Fassung">DE</a>'
    return f'<li class="lang">{a}</li>' if tag == 'li' else a

CSS = '''
  /* Sprachumschalter in der Kopfleiste */
  .nav .wrap{gap:1rem}
  .nav .mark{margin-right:auto}
  .nav a.lang,.nav li.lang a{font-family:var(--display);font-weight:700;font-size:.78rem;letter-spacing:.12em;line-height:1;color:var(--ink);border:1px solid var(--ink);padding:.38rem .5rem;white-space:nowrap}
  .nav a.lang:hover,.nav li.lang a:hover{background:var(--ink);color:var(--bg,#fbfaf7)}
  @media (max-width:900px){.nav .main li.lang{display:list-item}}
'''


ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [
    ('index.html', '/'),
    ('solution-admin-console.html', '/solution-admin-console.html'),
    ('translation-studio.html', '/translation-studio.html'),
    ('health-check/index.html', '/health-check/'),
    ('impressum.html', '/impressum.html'),
    ('datenschutz.html', '/datenschutz.html'),
]

if __name__ == '__main__':
    LANG = sys.argv[1]
    assert LANG in ('de', 'en')
    for rel, path in PAGES:
        f = ROOT / (rel if LANG == 'de' else 'en/' + rel)
        s = f.read_text(encoding='utf-8')
        # Alles Vorhandene entfernen, damit der Lauf wiederholbar ist und eine aus der deutschen
        # Seite mitkopierte Fassung (falsche Sprache, Umleitung) nicht stehen bleibt.
        s = re.sub(r'<script>\n/\* Sprache vorbelegen.*?</script>\n', '', s, flags=re.S)
        s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', '', s)
        s = re.sub(r'\s*<li class="lang"[^>]*>.*?</li>', '', s, flags=re.S)
        s = re.sub(r'\s*<a class="lang"[^>]*>[A-Z]{2}</a>', '', s)
        s = re.sub(r'\n  /\* Sprachumschalter in der Kopfleiste \*/.*?(?=</style>)', '', s, flags=re.S)
    
        # 1. Kopf: Umleitung (nur deutsch) und hreflang direkt nach dem Viewport-Meta
        m = re.search(r'<meta name="viewport"[^>]*>\n', s)
        assert m, f
        block = (REDIRECT + '\n' if LANG == 'de' else '') + hreflang(path) + '\n'
        s = s[:m.end()] + block + s[m.end():]
    
        # 2. Umschalter in der Kopfleiste
        hs, he = s.index('<header class="nav">'), s.index('</header>')
        nav = s[hs:he]
        if '<li class="cta">' in nav:
            nav = nav.replace('<li class="cta">', switch(path, LANG, 'li').replace('class="lang"', 'class="lang" data-i18n', 1) + '\n        <li class="cta">', 1)
        elif '<a class="cta"' in nav:
            nav = nav.replace('<a class="cta"', switch(path, LANG).replace('class="lang"', 'class="lang" data-i18n', 1) + '\n    <a class="cta"', 1)
        else:
            m2 = re.search(r'<a class="back"[^>]*>.*?</a>', nav, re.S)
            assert m2, f
            nav = nav[:m2.end()] + '\n    ' + switch(path, LANG).replace('class="lang"', 'class="lang" data-i18n', 1) + nav[m2.end():]
        s = s[:hs] + nav + s[he:]
    
        # 3. CSS fuer den Umschalter ans Ende des Stilblocks
        assert s.count('</style>') == 1, f
        s = s.replace('</style>', CSS + '</style>')
    
        f.write_text(s, encoding='utf-8')
        print('ok', f.relative_to(ROOT))
