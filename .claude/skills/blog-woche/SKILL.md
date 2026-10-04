---
name: blog-woche
description: Bereitet aus den Erkenntnissen der vergangenen Woche drei Blogbeiträge vor, legt sie zur Auswahl vor und veröffentlicht nach Freigabe die gewählten auf deutsch und englisch. Läuft wöchentlich als Routine; von Hand mit "Blog-Woche", "Blogentwürfe der Woche" oder "/blog-woche".
---

# Blog-Woche

Zwei Phasen in derselben Sitzung, getrennt durch die Freigabe von Andy:

1. **Vorbereiten** (läuft von selbst): Quellen der Woche lesen, drei Entwürfe schreiben, vorlegen, warten.
2. **Veröffentlichen** (nur nach ausdrücklicher Freigabe): gewählte Beiträge als Seiten bauen, deutsch und englisch, prüfen, auf `main` pushen.

Vor der Freigabe wird **nichts** committet oder gepusht, auch kein Zwischenstand. Kommt keine
Antwort, bleibt es bei den Entwürfen. Regeln für Ton, Layout und Inhalt stehen in `CLAUDE.md`,
Abschnitte Blog, Zweisprachigkeit und Regeln. Vorher lesen.

## Phase 1: Vorbereiten

### Zeitraum
Die sieben Tage vor dem Start der Sitzung (Europe/Berlin). Beim Montagslauf ist das die Vorwoche
von Montag bis Sonntag.

### Quellen
Repo `aschwarzdynpro/CodeApps` ist die Hauptquelle. Fehlt es in der Sitzung, mit `add_repo`
holen und nach `/home/user/CodeApps` klonen.

- `git log --since=<Start> --until=<Ende> --stat` über alle Apps, dazu die Diffs von
  `AGENTS.md`, `apps/*/CLAUDE.md`, `apps/*/README.md`, `apps/solution-forge/releases/CHANGELOG.md`,
  `Roadmap.md`, `TODO.md`, `docs/`. Neue Gotchas, Fehlerbeschreibungen, verworfene Ansätze und
  Commit-Bodies mit „weil" sind die eigentlichen Erkenntnisse.
- `git log` dieses Repos für Erkenntnisse an der Site selbst.
- Eigene Claude-Sitzungen der Woche (`list_sessions` mit `mine: true`, dann `list_events` mit
  `kinds: ["user","assistant"]`), soweit lesbar. Nur als Hinweis, was Andy beschäftigt hat:
  Jede Aussage im Beitrag muss sich in einem Commit oder einer Datei belegen lassen.

### Themen wählen
Drei Themen, je eins pro Beitrag. Ein Thema taugt, wenn es ein Problem, die bisherige Umgehung,
die Lösung und etwas, das schiefging oder überraschte, hergibt. Gute Kandidaten: ein Gotcha, das
Stunden gekostet hat, eine Plattformgrenze (Dataverse, PAC, Gen Pages, Code Apps), eine
Entscheidung mit Begründung, ein eigener Fehler mit Datum. Keine Release-Notes, keine
Funktionslisten, kein Produktton.

- Bereits erschienene Beiträge (`blog/*/index.html`) und `content/blog-themen.md` (bisher
  vorgeschlagene und abgelehnte Themen) prüfen. Nichts erneut vorschlagen, was abgelehnt wurde,
  außer es gibt neue Fakten.
- Gibt die Woche keine drei tragfähigen Themen her, weniger vorschlagen und das sagen. Nichts
  erfinden, nichts schätzen, keine Zahl ohne Quelle.
- Kundennamen, Tenants, Umgebungs-URLs, Präfixe, Tabellennamen und Personen von Kunden bleiben
  draußen. Kunden heißen nach Branche wie in den Referenzkarten. Im Zweifel weglassen.

### Entwürfe schreiben
Je Entwurf, auf deutsch:

- Kicker, Titel (Satzschreibung), Vorspann (2 bis 3 Sätze), Lesezeit
- Text mit 600 bis 1.000 Wörtern, 2 bis 4 Zwischenüberschriften, erste Person, Leser in
  Sie-Ansprache, konkrete Daten. Aufbau wie die vorhandenen Beiträge: Problem, bisherige Umgehung,
  was gebaut oder geändert wurde, was schiefging.
- Ein Satz aus dem Text, der als Zitat zwischen die Doppellinien kommt (bleibt im Text stehen)
- Bildvorschlag: passender vorhandener Screenshot aus `assets/screenshots/` oder `assets/blog/`,
  sonst „Bild fehlt, bitte liefern"
- Quellen für das Review (Commit-Hashes mit Datum, Dateien). Werden nicht veröffentlicht.
- Vorgeschlagener Slug (deutsch, kurz, Kleinbuchstaben, Bindestriche)

Prüfen vor dem Vorlegen: keine Gedankenstriche (`—`, `–` als Satzzeichen), keine Emojis, keine
Fazit-Listen, keine Dreierreihen, kein „In diesem Beitrag". Liest sich ein Absatz nach
Werbetext, neu schreiben.

### Vorlegen
1. Alle Entwürfe in eine Datei `blog-entwuerfe-<JJJJ>-KW<nn>.md` im Scratchpad schreiben und mit
   `SendUserFile` schicken (`status: proactive`).
2. In der Antwort je Entwurf: Nummer, Titel, zwei Sätze, worum es geht, Hauptquelle.
3. Fragen: „Welche soll ich veröffentlichen? Zum Beispiel ‚1 und 3‘, ‚2, aber …‘ oder ‚keinen‘.
   Änderungswünsche können Sie direkt dazuschreiben."
4. Turn beenden und auf die Antwort warten. Nicht selbst weitermachen.

Änderungswünsche einarbeiten und erneut vorlegen, bis eine eindeutige Freigabe kommt
(„veröffentlichen", „passt, raus damit", „1 und 3 freigegeben"). Eine Auswahl allein ohne
Änderungswunsch gilt als Freigabe der gewählten Entwürfe in der vorgelegten Fassung.

## Phase 2: Veröffentlichen

Je freigegebenem Beitrag, Datum = Tag der Freigabe:

1. **Deutsche Seite** `blog/<slug>/index.html`: Kopie des jüngsten Beitrags als Vorlage
   (Kopf mit Meta, `canonical`, OG mit `og-blog.png`, hreflang, Skript „Sprache vorbelegen",
   Umschalter `EN` in der Kopfleiste, CSS, Kopfleiste, Beitragskopf, Fuß). Inhalt ersetzen, alle
   Pfade und Daten anpassen, Kapitelnummern 01, 02 …, Initial im ersten Absatz, Zitat vor der
   zweiten Zwischenüberschrift, Bild mit Bildunterschrift nach dem Einstieg.
2. **Englische Seite** `en/blog/<slug>/index.html`: aus der englischen Fassung desselben
   Vorlagebeitrags, Text übersetzt (gleiche Regeln, Anrede „you", Zitat wörtlich im Text),
   gleicher Slug, Umschalter `DE` auf `/blog/<slug>/?lang=de`, `og-en-blog.png`, `en_US`.
3. **Übersichten** `blog/index.html` und `en/blog/index.html`: neuester Beitrag wird Aufmacher
   (`article.lead` mit Bild), der bisherige Aufmacher wandert als `article.story` an den Anfang
   des Rasters. Bei mehreren Beiträgen am selben Tag in der Reihenfolge der Freigabe.
4. **Feeds** `blog/feed.xml` und `en/blog/feed.xml`: neues `<item>` oben.
5. `sitemap.xml` (beide URLs) und `scripts/shot.mjs` (beide Einträge).
6. Gehört der Beitrag zu einer Serie, den Kasten „alle Teile" in jedem Teil nachziehen.
7. `content/blog-themen.md` fortschreiben: Woche, alle vorgeschlagenen Themen, je
   „veröffentlicht <slug>" oder „abgelehnt" (bei „keinen" nur diese Datei committen).

### Prüfen
- `npm run shot` muss durchlaufen (keine Fremd-Requests, Schriften geladen). In der Cloud-Sitzung
  passt der installierte Playwright nicht zum Browser: eine Kopie von `scripts/shot.mjs` im
  Scratchpad nehmen, Importe auf absolute Pfade unter `node_modules/playwright/index.mjs` und
  `scripts/server.mjs` stellen und `chromium.launch({ executablePath: '/opt/pw-browsers/chromium' })`.
- Neue Seiten bei 1400px und 390px ansehen, deutsch und englisch.
- Interne Links und Sprungziele auf allen geänderten Seiten prüfen, keine 404.
- Grep über die neuen Seiten: Gedankenstriche, Kundennamen und Umgebungs-URLs aus den Quellen,
  bei der englischen Seite deutsche Reste.

### Ausliefern
Commit auf `main` (`feat(blog): <Titel>`, Body mit dem Warum, Trailer wie in der Sitzung
vorgegeben), `git push -u origin main`, nach dem Pages-Lauf beide URLs auf 200 prüfen. Dann Andy
die beiden Links schicken und sagen, was abgelehnt wurde.
