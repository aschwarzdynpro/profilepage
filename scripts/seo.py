# SEO-Bausteine, die sich aus den Seiten selbst ableiten lassen: strukturierte Daten (JSON-LD),
# robots-Meta mit grosser Bildvorschau und die Fusszeilen-Links auf die wichtigsten Seiten.
# Wiederholbar: ersetzt nur, was es selbst erzeugt hat (Skripte mit id="ld-…", Marker im CSS,
# <nav class="foot-links">). Titel, Beschreibungen, Person und ProfessionalService der Startseite
# bleiben Handarbeit. Regeln stehen in CLAUDE.md, Abschnitt Suchmaschinen.
#   python3 scripts/seo.py          alle Seiten
#   python3 scripts/seo.py --check  nur pruefen, nichts schreiben (Exit 1 bei Abweichung)
import sys, re, json, html, pathlib, datetime

SITE = 'https://dynamicspro.de'
ROOT = pathlib.Path(__file__).resolve().parent.parent
LINKEDIN = 'https://www.linkedin.com/in/andy-schwarz-70543aa1'

PERSON_ID = SITE + '/#person'
BUSINESS_ID = SITE + '/#business'
WEBSITE_ID = SITE + '/#website'

T = {
    'de': dict(home='Startseite', blog='Blog', hc='Dynamics 365 Health Check', lang='de-DE',
               job='Dynamics 365 Solution Architect', os='Microsoft Power Platform (Power Apps Code App)',
               req={'solution-admin-console': 'Microsoft Dataverse',
                    'translation-studio': 'Microsoft Dataverse mit mehr als einer Sprache',
                    'schedule-board-manager': 'Dynamics 365 Field Service oder Project Operations (Universal Resource Scheduling)'},
               footer='Weitere Seiten',
               links=[('/health-check/', 'Dynamics 365 Health Check'),
                      ('/solution-admin-console.html', 'Solution Administration Console'),
                      ('/translation-studio.html', 'Translation Studio'),
                      ('/schedule-board-manager.html', 'Schedule Board Manager'),
                      ('/blog/', 'Blog')],
               months=['januar', 'februar', 'märz', 'april', 'mai', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'dezember'],
               addendum=re.compile(r'<h2[^>]*>\s*Nachtrag vom (\d{1,2})\. ([A-Za-zäöü]+)')),
    'en': dict(home='Home', blog='Blog', hc='Dynamics 365 Health Check', lang='en-US',
               job='Dynamics 365 Solution Architect', os='Microsoft Power Platform (Power Apps code app)',
               req={'solution-admin-console': 'Microsoft Dataverse',
                    'translation-studio': 'Microsoft Dataverse with more than one language',
                    'schedule-board-manager': 'Dynamics 365 Field Service or Project Operations (Universal Resource Scheduling)'},
               footer='More pages',
               links=[('/en/health-check/', 'Dynamics 365 Health Check'),
                      ('/en/solution-admin-console.html', 'Solution Administration Console'),
                      ('/en/translation-studio.html', 'Translation Studio'),
                      ('/en/schedule-board-manager.html', 'Schedule Board Manager'),
                      ('/en/blog/', 'Blog')],
               months=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'],
               addendum=re.compile(r'<h2[^>]*>\s*Addendum, ([A-Za-z]+) (\d{1,2})')),
}

CSS = '''
  /* Fusszeile: weitere Seiten (scripts/seo.py) */
  footer .foot-links{width:100%;display:flex;flex-wrap:wrap;gap:.35rem 1.4rem;padding-bottom:1rem;border-bottom:1px solid var(--line,var(--rule,#d8d4cc))}
  footer .foot-links a{color:var(--ink-2,#444)}
  footer .foot-links a[aria-current]{color:var(--ink,#1a1a1a)}
'''


def text(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()


def one(pattern, s, name, flags=0):
    m = re.findall(pattern, s, flags)
    assert len(m) == 1, f'{name}: {len(m)} Treffer'
    return m[0]


def meta(s):
    d = {}
    d['title'] = text(one(r'<title>([^<]*)</title>', s, 'title'))
    d['description'] = html.unescape(one(r'<meta name="description" content="([^"]*)">', s, 'description'))
    d['canonical'] = one(r'<link rel="canonical" href="([^"]*)">', s, 'canonical')
    d['image'] = one(r'<meta property="og:image" content="([^"]*)">', s, 'og:image')
    d['h1'] = text(one(r'<h1[^>]*>(.*?)</h1>', s, 'h1', re.S))
    d['lang'] = one(r'<html lang="([a-z]{2})">', s, 'lang')
    m = re.search(r'<meta property="article:published_time" content="(\d{4}-\d{2}-\d{2})">', s)
    d['published'] = m.group(1) if m else None
    m = re.search(r'class="kicker"[^>]*>([^<]*)<', s)
    d['kicker'] = text(m.group(1)) if m else ''
    return d


def absolute(url, page_rel):
    """Relativen Bildpfad einer Seite in eine absolute URL verwandeln."""
    if url.startswith('http'):
        return url
    base = pathlib.PurePosixPath('/' + page_rel).parent
    p = (base / url)
    parts = []
    for part in p.parts:
        if part == '..':
            parts.pop()
        elif part not in ('/', '.'):
            parts.append(part)
    return SITE + '/' + '/'.join(parts)


def modified(s, d, L):
    """Juengster Nachtrag, sonst Erscheinungsdatum."""
    y, m0, _ = (int(x) for x in d['published'].split('-'))
    latest = d['published']
    for a, b in L['addendum'].findall(s):
        day, month = (a, b) if L is T['de'] else (b, a)
        mi = L['months'].index(month.lower()) + 1
        year = y + (1 if mi < m0 else 0)
        latest = max(latest, f'{year:04d}-{mi:02d}-{int(day):02d}')
    return latest


def person(L, home):
    return {'@type': 'Person', '@id': PERSON_ID, 'name': 'Andy Schwarz', 'url': home,
            'jobTitle': L['job'], 'sameAs': [LINKEDIN]}


def org():
    return {'@type': 'Organization', '@id': BUSINESS_ID, 'name': 'DynamicsPro', 'url': SITE + '/'}


def crumbs(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u}
                                for i, (n, u) in enumerate(items)]}


def website(d, L):
    return {'@context': 'https://schema.org', '@type': 'WebSite', '@id': WEBSITE_ID,
            'url': SITE + '/', 'name': 'DynamicsPro', 'alternateName': ['DynamicsPro, Andy Schwarz', 'dynamicspro.de'],
            'inLanguage': ['de-DE', 'en-US'], 'publisher': {'@id': BUSINESS_ID}, 'author': {'@id': PERSON_ID}}


def software(d, L, slug, home):
    return {'@context': 'https://schema.org', '@type': 'SoftwareApplication', '@id': d['canonical'] + '#app',
            'name': d['h1'], 'url': d['canonical'], 'description': d['description'], 'image': d['image'],
            'applicationCategory': 'BusinessApplication', 'operatingSystem': L['os'],
            'softwareRequirements': L['req'][slug], 'inLanguage': L['lang'],
            'author': person(L, home), 'publisher': org()}


def posting(s, d, L, rel, home, blog_url):
    art = one(r'<article class="post">(.*?)</article>', s, 'article', re.S)
    imgs = re.findall(r'<img src="([^"]*)"', art)
    images = [absolute(imgs[0], rel)] if imgs else []
    if d['image'] not in images:
        images.append(d['image'])
    words = len(re.sub(r'<[^>]+>', ' ', art).split())
    section = d['kicker'].split(' · ')[0].strip()
    return {'@context': 'https://schema.org', '@type': 'BlogPosting', '@id': d['canonical'] + '#article',
            'mainEntityOfPage': {'@type': 'WebPage', '@id': d['canonical']},
            'url': d['canonical'], 'headline': d['h1'], 'description': d['description'], 'image': images,
            'datePublished': d['published'], 'dateModified': modified(s, d, L),
            'author': person(L, home), 'publisher': org(),
            'isPartOf': {'@type': 'Blog', '@id': blog_url + '#blog'},
            'articleSection': section, 'inLanguage': L['lang'], 'wordCount': words}


def blog(d, L, posts, home):
    return {'@context': 'https://schema.org', '@type': 'Blog', '@id': d['canonical'] + '#blog',
            'url': d['canonical'], 'name': d['title'].split(' · ')[0], 'description': d['description'],
            'inLanguage': L['lang'], 'author': person(L, home), 'publisher': org(),
            'blogPost': [{'@type': 'BlogPosting', '@id': p['canonical'] + '#article', 'headline': p['h1'],
                          'url': p['canonical'], 'datePublished': p['published'], 'image': p['image']}
                         for p in sorted(posts, key=lambda p: p['published'], reverse=True)]}


def ld(blocks):
    out = []
    for key, obj in blocks:
        j = json.dumps(obj, ensure_ascii=False, indent=2).replace('</', '<\\/')
        out.append(f'<script type="application/ld+json" id="ld-{key}">\n{j}\n</script>\n')
    return ''.join(out)


def apply(rel, s, blocks, L, footer):
    # 1. Eigene JSON-LD-Bloecke erneuern, direkt vor </head>
    s = re.sub(r'<script type="application/ld\+json" id="ld-[a-z]+">.*?</script>\n', '', s, flags=re.S)
    assert s.count('</head>') == 1, rel
    s = s.replace('</head>', ld(blocks) + '</head>')
    # 2. robots: grosse Bildvorschau erlauben
    if 'max-image-preview' not in s:
        if '<meta name="robots" content="index, follow">' in s:
            s = s.replace('<meta name="robots" content="index, follow">',
                          '<meta name="robots" content="index, follow, max-image-preview:large">')
        else:
            s = re.sub(r'(<link rel="canonical" href="[^"]*">\n)',
                       r'\1<meta name="robots" content="index, follow, max-image-preview:large">\n', s, count=1)
    assert s.count('max-image-preview') == 1, rel
    # 3. Fusszeile: Links auf die wichtigsten Seiten
    if footer:
        s = re.sub(r'\s*<nav class="foot-links".*?</nav>', '', s, flags=re.S)
        here = '/' + rel.replace('index.html', '')
        here = re.sub(r'^/en/', '/en/', here)
        links = ' '.join(f'<a href="{u}"{" aria-current=\"page\"" if u == here else ""}>{n}</a>'
                         for u, n in L['links'])
        nav = f'<nav class="foot-links" aria-label="{L["footer"]}">{links}</nav>'
        m = re.search(r'<footer>\n(\s*)<div class="wrap">\n', s)
        assert m, rel
        s = s[:m.end()] + m.group(1) + '  ' + nav + '\n' + s[m.end():]
        s = re.sub(r'\n  /\* Fusszeile: weitere Seiten \(scripts/seo\.py\) \*/.*?(?=</style>)', '', s, flags=re.S)
        assert s.count('</style>') == 1, rel
        s = s.replace('</style>', CSS + '</style>')
    return s


def pages():
    for lang, prefix in (('de', ''), ('en', 'en/')):
        home = SITE + '/' + prefix
        yield lang, prefix + 'index.html', 'home', home
        yield lang, prefix + 'health-check/index.html', 'health-check', home
        for slug in ('solution-admin-console', 'translation-studio', 'schedule-board-manager'):
            yield lang, f'{prefix}{slug}.html', slug, home
        yield lang, prefix + 'blog/index.html', 'blog', home
        for p in sorted((ROOT / prefix / 'blog').glob('*/index.html')):
            yield lang, str(p.relative_to(ROOT)), 'post', home


def main(check=False):
    changed = []
    metas = {}
    for lang, rel, kind, home in pages():
        metas[rel] = meta((ROOT / rel).read_text(encoding='utf-8'))
    for lang, rel, kind, home in pages():
        L = T[lang]
        f = ROOT / rel
        s = f.read_text(encoding='utf-8')
        d = metas[rel]
        assert d['lang'] == lang, rel
        blog_url = home + 'blog/'
        footer = True
        if kind == 'home':
            blocks = [('website', website(d, L))]
        elif kind == 'health-check':
            blocks = [('breadcrumb', crumbs([(L['home'], home), (L['hc'], d['canonical'])]))]
            footer = False  # Angebotsseite: eine Handlung, kein zweites Navigationsangebot
        elif kind == 'blog':
            prefix = 'en/' if lang == 'en' else ''
            posts = [m for r, m in metas.items() if r.startswith(prefix + 'blog/') and r != prefix + 'blog/index.html'
                     and (lang == 'en' or not r.startswith('en/'))]
            blocks = [('blog', blog(d, L, posts, home)),
                      ('breadcrumb', crumbs([(L['home'], home), (L['blog'], d['canonical'])]))]
        elif kind == 'post':
            blocks = [('article', posting(s, d, L, rel, home, blog_url)),
                      ('breadcrumb', crumbs([(L['home'], home), (L['blog'], blog_url), (d['h1'], d['canonical'])]))]
        else:
            blocks = [('software', software(d, L, kind, home)),
                      ('breadcrumb', crumbs([(L['home'], home), (d['h1'], d['canonical'])]))]
        out = apply(rel, s, blocks, L, footer)
        if out != s:
            changed.append(rel)
            if not check:
                f.write_text(out, encoding='utf-8')
    for rel in changed:
        print(('abweichend' if check else 'ok'), rel)
    if check and changed:
        sys.exit(1)
    if not changed:
        print('nichts zu tun')


if __name__ == '__main__':
    main(check='--check' in sys.argv)
