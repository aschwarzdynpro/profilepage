# dynamicspro.de – Portfolio-Website

Statische Single-File-Site (`index.html`), kein Build, kein Framework. Ausgeliefert über GitHub Pages.

## Regeln
- Alles bleibt in `index.html` (CSS im `<style>`, keine externen JS-Bundles). Bilder nach `assets/`.
- Ausnahme: `solution-admin-console.html`, `translation-studio.html`, `impressum.html`, `datenschutz.html`,
  die Angebotsseiten unter `<slug>/index.html` und der Blog unter `blog/` sind eigene Seiten mit eigenem `<style>`. Anschrift, USt-IdNr. und Aufsichtsbehörde nur nach Rücksprache ändern.
- Keine Frameworks, kein Tailwind, kein Build-Schritt einführen.
- Deutsch, Sie-Ansprache, kein Marketing-Sprech (die englische Fassung unter `en/` siehe Zweisprachigkeit). Keine Emojis, keine Bindestrich-Gedankenstriche.
- Kundennamen bleiben anonymisiert (Branche statt Firma). Keine Tagessätze, keine Partner-Methodik.
- Nach jeder Änderung Desktop (1400px) und Mobil (390px) prüfen: `npm run shot` (Playwright) oder Browser.
- Keine Requests an Dritte. Schriften liegen selbst gehostet in `assets/fonts/`, kein Google-Fonts-Link. `npm run shot` bricht ab, sobald ein Fremd-Host angefragt wird.

## Deploy
Push auf `main` löst `.github/workflows/pages.yml` aus. Der Workflow kopiert eine
**explizite Dateiliste** nach `_site`. Neue Top-Level-Dateien (z. B. `impressum.html`)
und neue Verzeichnisse (z. B. `health-check/`) müssen dort eingetragen werden, sonst gehen
sie stillschweigend nicht live.
Die englische Fassung geht als ganzes Verzeichnis mit (`cp -r en _site/en`).
Einrichtung und DNS stehen in `README.md`.

## Zweisprachigkeit (seit Oktober 2026)
Deutsch ist die Hauptsprache, Englisch liegt unter `en/` mit **identischen Pfaden**:
`/` ↔ `/en/`, `/impressum.html` ↔ `/en/impressum.html`, `/blog/<slug>/` ↔ `/en/blog/<slug>/`
(die Slugs bleiben deutsch, damit die Zuordnung ohne Tabelle geht). Wer eine Seite ändert,
ändert beide Fassungen. Englische Seiten verweisen mit `../` bzw. `../../` auf `assets/`.

- **SEO:** jede Seite hat `hreflang` de, en und `x-default` (= deutsch), eigenes `canonical`,
  `og:locale` `de_DE` bzw. `en_US`. `sitemap.xml` führt beide Fassungen (24 URLs).
- **Vorbelegung ohne Speichern:** Nur die deutschen Seiten tragen im `<head>` ein kleines Skript
  („Sprache vorbelegen"). Kommt ein Besucher **von außen** (Referrer leer oder fremd) und ist seine
  erste Browsersprache nicht Deutsch, ersetzt es die URL durch die englische Fassung derselben
  Seite. Nie bei Navigation innerhalb der Site, nie für Crawler oder `navigator.webdriver`, nie mit
  `?lang=de`; diesen Parameter entfernt es per `history.replaceState`. Englische Seiten leiten nie
  um, dort gilt die URL. Kein Cookie, kein `localStorage`: die Datenschutzerklärung sagt „keine
  Cookies", und das bleibt so.
- **Umschalter:** Kasten `EN` bzw. `DE` in der Kopfleiste vor dem Kontakt-Knopf. `EN` zeigt auf
  `/en/<pfad>`, `DE` auf `/<pfad>?lang=de`, damit ein englischer Browser die deutsche Seite nicht
  sofort wieder verlässt.
- **Werkzeug:** `python3 scripts/i18n.py de|en` setzt hreflang, Umschalter, dessen CSS und (nur
  deutsch) das Skript in die sechs statischen Seiten und ist wiederholbar. Die Blogseiten tragen
  dieselben Bausteine; ein neuer Beitrag übernimmt sie aus einem vorhandenen.
- **Englische Texte:** dieselben Regeln wie deutsch (kein Marketing-Sprech, keine Gedankenstriche,
  Kunden nach Branche), Anrede „you". Impressum und Datenschutz sind Lesefassungen mit dem Hinweis,
  dass nur die deutsche Fassung verbindlich ist; Anschrift, USt-IdNr. und Behördenname stehen dort
  unverändert.

## Erscheinungsbild: Magazin (seit Oktober 2026)
Die ganze Site sieht aus wie eine gedruckte Fachzeitschrift: helles Papier `--bg #fbfaf7`,
Schwarz `--ink #1a1a1a`, **Rot `--red #b5342b` als einzige Akzentfarbe**, Doppellinien
(`3px double`) statt dunkler Flächen, Kopfleiste auf Papier mit schwarzer Linie, Kontakt-Knopf
schwarz. Keine abgerundeten Ecken, keine Schatten. Überschriften Manrope 800 mit engem
Zeichenabstand, Kicker rot in Versalien mit Sperrung. Die frühere Navy-Fassung (`#0F1E33` mit
Hellblau `#6DB4FF`) ist weg; `--navy` und `--sky` existieren in den Tokens nur noch als Alias auf
Schwarz und Rot, damit alte Regeln nicht brechen.

Der Blog wurde zuerst in diesem Bild gebaut (Generator `build_main.py` im Scratchpad der
Session, Quelle ist das HTML). Die übrigen Seiten tragen am Ende ihres `<style>` einen Block
„Magazin-Theme", der Kopfleiste, Hero, Kontakt und Karten überschreibt. Wer dort eine neue
Komponente baut, baut sie gleich in diesem Bild und hängt nichts Dunkles mehr an.

- Tokens: `--bg`, `--bg-2 #f1efe9`, `--line #d8d4cc`, `--ink`, `--ink-2 #444`, `--ink-3 #7a766f`, `--red`
- Schrift: Manrope (Überschriften), IBM Plex Sans (Fließtext), selbst gehostet als Variable Fonts in `assets/fonts/`
- OG-Vorschaukarten: `node scripts/og.mjs` rendert aus `scripts/og-card.html` zehn Karten nach
  `assets/`: `og.png` (Startseite, Impressum, Datenschutz), `og-health-check.png`, `og-blog.png`
  (Übersicht und alle Beiträge), `og-konsole.png`, `og-studio.png`, dazu dieselben fünf englisch als
  `og-en.png`, `og-en-health-check.png`, `og-en-blog.png`, `og-en-konsole.png`, `og-en-studio.png`. Die Texte je Karte stehen in
  `og.mjs`; die Karte liest sie als Query-Parameter. Wer Claim oder Titel einer Seite ändert, zieht
  die Karte nach und rendert neu.
- Skills: Balkengruppen `.sg` (5 Segmente = Niveau, Zahl = Jahre), neben dem Werdegang. Das frühere Netzdiagramm ist bewusst weg, eine Selbsteinschätzung auf 1 bis 5 überzeugt niemanden.

## Screenshots der Konsole
`assets/screenshots/*.webp` sind **selbst aufgenommen**, nicht vom Kunden geliefert.
Verfahren, falls sie erneuert werden müssen:

1. `apps/solution-forge` aus dem Repo `aschwarzdynpro/CodeApps` lokal starten (`npx vite`).
   Ohne Power-Bridge fällt die App automatisch auf `local-mock`, Badge oben rechts sagt
   „Demo data". **Nur mit diesen Beispieldaten aufnehmen, nie mit Kundendaten.**
2. Beim ersten Start blockiert der Environment-Setup-Assistent. Sechs Mal Next, dann
   „Create configuration". Danach zeigt Validate 10 Einträge statt 9 (Dual-Write erscheint).
3. Aufnehmen bei Viewport 1600 breit, `deviceScaleFactor: 2`, geclippt auf `main.content`.
4. Auf 1600px Breite herunterrechnen und als WebP mit Qualität 0.92 speichern. Das spart
   gegenüber PNG rund zwei Drittel (516 kB statt 1,4 MB für sieben Bilder).

Karten mit Screenshot müssen `feat wide` sein, in der halben Spalte ist das Bild unlesbar.

## Produktseite Translation Studio
`translation-studio.html` beschreibt die zweite Code App nach demselben Muster wie die
Konsolenseite (Hero mit Faktenleiste, Inhaltsverzeichnis, Gruppen aus `feat`-Karten, Panels
„Quer durch die App", Kontakt). Quelle ist `CodeApps/apps/translation-studio/README.md`
und die In-App-Hilfe `src/help/helpContent.ts` im Repo `aschwarzdynpro/CodeApps`; bei
Änderungen an der App dort abgleichen. Verlinkt ist die Seite aus der Werkzeuge-Karte
der Startseite. **Keine Referenzkarte und keine Mandatszeile**, solange die App nicht
beim Kunden läuft: Die Seite sagt ehrlich „vor dem ersten Kundeneinsatz" (Kicker, letzter
Absatz unter „Wofür", Kontaktblock, Werkzeuge-Karte). Sobald die App deployt ist und ein
Kunde sie nutzt, diese vier Stellen nachziehen.

Die Screenshots `assets/screenshots/ts-*.webp` sind wie die der Konsole selbst
aufgenommen, mit den eingebauten Mock-Daten (fiktives Fuhrpark-Szenario in en/de/fr):

1. `apps/translation-studio` aus dem CodeApps-Repo lokal starten (`npx vite`). Ohne
   Power-Host läuft die App automatisch mit Mock-Daten, Badge oben rechts sagt „Mock-Daten".
   Kein Setup-Assistent. Solution „Fuhrpark" wählen, „Übersetzungen laden".
2. Matrix: Element-Screenshot von `main.studio`. Dialoge (Vorschau, Import-Ergebnis) als
   Viewport-Ausschnitt unterhalb der Kopfleiste, damit das Overlay über dem abgedunkelten
   Studio liegt und das Bild 1600px breit bleibt; einen Dialog allein zu clippen ergibt
   600px und ist in der `feat wide`-Karte unscharf. Vor dem Foto den Toast abwarten (5 s).
3. Aufnahme bei 1600 Breite, `deviceScaleFactor: 2`, auf 1600px herunterrechnen, WebP 0,92.

## Blog
`blog/index.html` ist die Übersicht, jeder Beitrag liegt unter `blog/<slug>/index.html`, dazu
`blog/feed.xml` (RSS, neuester zuerst: neuer Beitrag = neues `<item>`). Der Workflow kopiert
das ganze Verzeichnis, neue Beiträge brauchen dort keinen Eintrag, wohl aber in `sitemap.xml`
und in `scripts/shot.mjs`. Jede Datei trägt ihre eigene Kopie von CSS. Die englischen Beiträge
liegen unter `en/blog/` mit eigenem Feed `en/blog/feed.xml`; ein neuer Beitrag kommt in beide.

**Wöchentliche Routine „Blog-Woche":** montags früh schlägt eine eigene Sitzung drei Beiträge aus
den Erkenntnissen der Vorwoche vor (Quellen: Git-Log und Doku-Diffs in CodeApps, dieses Repo,
eigene Sitzungen) und veröffentlicht erst nach Andys Freigabe, deutsch und englisch. Ablauf in
`.claude/skills/blog-woche/SKILL.md`, Themenprotokoll in `content/blog-themen.md`.

**Layout (Magazin):** Kopfleiste mit „Werkstattnotizen" als Nebenzeile, Beitragskopf mit
Kicker, breiter Titelzeile bis 4.4rem, Vorspann in leichter Schrift und Autorenzeile über
einer Linie, darunter Doppellinie. Text in 68ch mit Initial im ersten Absatz, Kapitelnummern
01, 02 in Rot über den Zwischenüberschriften, je Beitrag **ein Satz aus dem Text als Zitat**
zwischen Doppellinien vor der zweiten Zwischenüberschrift (der Satz bleibt im Text), Abbildungen
900px breit über die Spalte hinaus, Bildunterschrift mit rotem Strich, Nachträge mit Linie
darüber und Etikett „Nachtrag" statt Nummer. Die Übersicht ist eine Titelseite: neuester
Beitrag als Aufmacher mit Bild, die übrigen zweispaltig. Zwei frühere Fassungen (Pop-up-Buch,
Blaupause) sind verworfen und gelöscht.

Die Beiträge erzählen die Entstehung der eigenen Werkzeuge: Problem, bisherige Umgehung
(XrmToolBox, Excel, Configuration Migration Tool, manuelle Prüfungen), was gebaut wurde, was
schiefging. Quelle für die Konsole sind `apps/solution-forge/releases/CHANGELOG.md`, die
Gotchas in `apps/solution-forge/CLAUDE.md` und der Git-Log im Repo `aschwarzdynpro/CodeApps`;
Daten und Zahlen in den Beiträgen stammen von dort, nichts ist geschätzt. **Kundennamen,
Tenants, Präfixe und Tabellennamen von Kunden bleiben draußen**, Kunden heißen wie in den
Referenzkarten nach Branche. Die Screenshots sind dieselben wie auf den Produktseiten. Die vier Konsolen-Beiträge
tragen zusätzlich `assets/blog/devops-loop.jpg` (DevOps-Zyklus als liegende Acht, 1024px),
jeweils nach dem Einstieg mit einer Bildunterschrift, die den Teil im Zyklus verortet. Der
Translation-Studio-Beitrag trägt an derselben Stelle `assets/blog/translation-globe.jpg`.

Serie zur Konsole in vier Teilen, je eine Bauphase, **datiert auf das Ende der Phase im
Git-Log** (25.06. Workbench und Merge, 20.07. Validate, 10.08. Betrieb, 21.09. Transfer Hub
und Produkt), dazu der Beitrag zum Translation Studio vom 03.10. Ein Beitrag weiß nur, was
an seinem Datum bekannt war; spätere Ereignisse stehen als „Nachtrag vom <Datum>" am Ende.
Die Übersicht und der Feed sortieren neueste zuerst, die Serie liest man von Teil 1 aus. Der Kasten „alle Teile" am Ende jedes Teils listet die Serie;
ein neuer Teil muss in jeden anderen Teil eingetragen werden. Ton: erste Person, Sie-Ansprache
für den Leser, konkrete Daten, eigene Fehler mit Datum. Keine Fazit-Listen, keine
Dreierreihen, kein Produktton. Die Produktseiten bleiben als Funktionskatalog bestehen und
werden aus den Beiträgen verlinkt.

## Produktseite Solution Administration Console
`solution-admin-console.html` beschreibt alle 21 Arbeitsbereiche der Code App. Quelle ist
`CodeApps/apps/solution-forge/README.md` im Repo `aschwarzdynpro/CodeApps`; bei Änderungen
an der App dort abgleichen. **ALM Detective und Job Monitor stehen bewusst nicht drauf** —
beide sind aus dem Menü der App entfernt. Verlinkt ist die Seite aus der Referenzkarte
und aus dem Werkzeuge-Abschnitt der Startseite.

Jeder Arbeitsbereich braucht eine `id` am `<article>` und einen Eintrag im
Inhaltsverzeichnis, sonst fehlt er in der Navigation. Wie das aussieht, steht unter
Navigation.

## Navigation
Startseite und Produktseiten markieren den Abschnitt, in dem man gerade steht, und haben
unter ihrem Breakpoint dasselbe Panel von unten. Klassennamen (`.toc-shell`, `.toc`, `.toc-fab`,
`.toc-backdrop`) und Verhalten sind absichtlich gleich, jede Datei trägt ihre eigene
Kopie von CSS und Skript.

- `index.html`: Kopfleiste mit den sechs Einträgen Leistungen, Health Check, Referenzen,
  Arbeitsweise, Skills und Werdegang, Blog plus Kontakt, aktiver Eintrag schwarz mit
  Unterstrich in `--red`. Unter 900px Panel über den Knopf „Menü" rechts unten.
- Blog (`blog/index.html` und die Beiträge): wie die Angebotsseiten **kein Panel und kein
  Inhaltsverzeichnis**, nur Kopfleiste mit Marke, Rückweg („Alle Beiträge" bzw. „Zurück zur
  Startseite") und Kontakt-Knopf. Ein Beitrag ist eine Lesespalte, die man scrollt.
- `solution-admin-console.html`: mitlaufende Spalte links mit allen 27 Sprungzielen,
  offen ist immer genau eine Gruppe. Unter 1100px Panel über den Knopf „Inhalt",
  dort stehen alle Gruppen offen.
- `translation-studio.html`: dieselbe Spalte mit 18 Sprungzielen in fünf Gruppen
  (Wofür, Studio, Weitere Bereiche, Quer durch die App, Kontakt), CSS und Skript sind
  eine Kopie der Konsolenseite.
- Angebotsseiten (`health-check/index.html` und was nach dem Muster folgt): **kein Panel
  und kein Inhaltsverzeichnis.** Nur Kopfleiste mit Marke, Rückweg zur Startseite und
  dem CTA-Knopf, der auch mobil stehen bleibt. Das ist Absicht: eine Angebotsseite hat
  genau eine Handlung, ein zweites Navigationsangebot würde davon ablenken. Die Seite
  ist kurz genug, um sie zu scrollen.

Das Panel schliesst nach einem Sprung über drei unabhängige Wege: den Klick selbst,
`hashchange` und das Scrollen des Fensters um mehr als 120px. Das ist Absicht und darf
nicht auf einen Weg eingedampft werden, ein `<details>`-Menü blieb hier offen stehen.
Ohne JavaScript bleiben alle Links erreichbar.

## Produktisierte Angebote
Neben der Arbeit nach Aufwand gibt es Angebote mit festem Preis und festem Umfang, die
mit einem Maßnahmenplan enden. Die Umsetzung der Maßnahmen wird getrennt verkauft und
ist in keinem dieser Angebote enthalten.

Die Familie, in der geplanten Reihenfolge:

| Angebot | Stand |
| --- | --- |
| Health Check | live unter `/health-check`, 5 Tage, 5.000 € zzgl. USt. |
| ALM Check | geplant, keine Seite |
| Security Report | geplant, keine Seite |
| License & Capacity Report | geplant, keine Seite |
| Adoption Report | geplant, keine Seite |

**Preise sind fest.** 5.000 € zzgl. USt. für den Health Check, ohne Stufen, ohne Rabatt,
ohne Varianten auf der Seite. Wer den Betrag ändern will, ändert ihn im Angebotsdokument
und danach hier.

**Seitenmuster.** Jede Angebotsseite liegt unter `<slug>/index.html`, damit die URL ohne
`.html` auskommt, und folgt den acht Blöcken aus `content/offer-page-template.md`:
Hero mit Kennzahlenleiste, Problem, Prüfumfang als Kacheln, Ablauf als nummerierte Liste,
Ergebnis als Dreierraster, Warum DynamicsPro, Abschluss-CTA, Voraussetzungen und Abgrenzung.
Der Rahmen steht bewusst hinter dem CTA, der Einwand wird schon unter den Kacheln in einem
Satz benannt. Drei Absagen unmittelbar vor dem Knopf bremsen den Abschluss.
Gestaltung und Design-Tokens sind die der übrigen Seiten, jede Datei trägt ihre eigene
Kopie von CSS.

**Quellen in `content/`.** `content/health-check.md` hält die Seite blockweise fest,
`content/startseite.md` den Teaser und die Anschlüsse auf der Startseite,
`content/offer-page-template.md` die Vorlage. Die Dateien werden nicht ausgeliefert, sie
stehen nicht in der Dateiliste des Workflows. Sie sind Redaktionsquelle, das HTML bleibt
das, was live geht: wer Text ändert, ändert beides.

**Sprache.** Die Angebotsseiten sind deutsch mit Sie-Ansprache, wie die ganze Site. Das ist
hier zusätzlich eine Vertriebsentscheidung und keine Formalie: die Käufer sind
Mittelstandsunternehmen im DACH-Raum, die auf Deutsch suchen. Die Seiten und ihre
SEO-Felder bleiben deutsch und werden nicht teilweise übersetzt. Die englische Fassung
(`en/health-check/`) ist eine eigene Seite daneben und ersetzt die deutsche nicht; `x-default`
zeigt auf die deutsche.

**Buchung nur als Link.** Die CTA-Knöpfe verweisen auf Microsoft Bookings, sie betten nichts
ein. Ein eingebettetes Buchungsfenster lädt beim Seitenaufruf von `outlook.office365.com` und
setzt Cookies. Damit wären die Nummern 3 und 4 der Datenschutzerklärung falsch („keine Cookies",
„keine Verbindung zu Servern Dritter"), es bräuchte ein Consent-Management, das es hier nicht
gibt, und `npm run shot` würde abbrechen. Als Link fließen Daten erst nach einem Klick, Abschnitt
6 der Datenschutzerklärung deckt das ab.

**Kein CMS.** Es gibt keine Redaktionsoberfläche und keinen Sync in ein fremdes System.
Seite, Blöcke, SEO-Felder, Navigationseintrag und Teaser sind Code in diesem Repo.

## Aufbau der Startseite
Problem-first, nicht Lebenslauf-first: Hero, Kennzahlen, Leistungen, Referenzen,
Arbeitsweise, Skills und Werdegang, Kontakt. Die Seite verkauft direkt an Entscheider,
die fragen „löst er mein Problem, hat er das schon gemacht". Skills und Werdegang stehen
deshalb hinten als Nachweis, nicht vorn als Argument. Wer sie an den Anfang schieben will,
baut die Seite für Recruiter um, und das ist nicht die Zielgruppe.

- Der Health Check ist die erste Karte unter „Was ich übernehme" (`.service.offer`), kein
  eigener Streifen unter dem Hero. Die Karte „Systemanalyse und Reviews" bleibt daneben der
  Einstieg für den individuell geschnittenen Auftrag.
- Die Mandatsliste unter den Referenzkarten ist eine Zeile je Einsatz. Die Geschichten
  stehen in den Karten, die Details im Profil-Dokument. Nicht wieder zu Absätzen aufblasen.
  Hat ein Mandat eine Karte, wiederholt die Zeile deren Lösung nicht: Stichwort plus Link
  „Fallbeispiel oben“ auf die `id` der Karte, und nur, was die Karte nicht schon sagt.
  Zeitraum steht in der Karte, Branche heisst in Karte und Zeile gleich.
- „Wie ich arbeite" bündelt Foto, Kurzvorstellung, die vier Grundsätze und die Werkzeuge.
  Es gibt keinen eigenen Abschnitt „Über mich" mehr, die Fakten (Standort, Verfügbarkeit,
  Zertifizierungen) stehen unter dem Werdegang.

## Inhaltliche Quelle
Massgeblich ist das **englische** Profil-Dokument `Profile_Andy_Schwarz_2026.docx`
(in `OneDrive/Dokumente/Job/`). Zahlen auf der Site folgen ihm, mit einer bewussten Ausnahme:

- **Solution Architecture steht auf der Site mit 7 Jahren, nicht mit 12.** Solution Architect
  ist er seit 01/2019, das sind 7 Jahre. Die 12 in beiden Dokumenten ist der Fehler und wird
  dort korrigiert. Nicht auf 12 zurückdrehen.

Das deutsche `Profil_Andy_Schwarz_2026_DE.docx` ist mit dem englischen nicht deckungsgleich
(sechs abweichende Zahlen, Stand 09.09.2026). Bei Widersprüchen gilt das englische.

Rollenbezeichnungen müssen über Referenzkarte, Mandatsliste und Profil-Dokument
zusammenpassen. Payment Services heisst überall `Dynamics 365 Specialist`.

## Offen
- Jahreszahlen zwischen deutschem und englischem Profil abgleichen.
- Pro Referenz eine belastbare Kennzahl ergänzen.
- Link „Profil als PDF" im Hero für Recruiter und Vendor Management, sobald eine PDF-Fassung des
  Profil-Dokuments in `assets/` liegt. Bis dahin kein Link, ein toter Link wäre schlimmer als keiner.

### Health Check, verbleibende manuelle Schritte
Alles, was an anderer Stelle Redaktionsarbeit in einem CMS wäre, ist hier bereits Code und
erledigt: Seite angelegt (`health-check/index.html`), Blöcke gesetzt, SEO-Felder im `<head>`,
Navigationseintrag in Kopfleiste und Panel, Angebotskarte unter „Was ich übernehme",
CTA verdrahtet, Verzeichnis im Deploy-Workflow, Eintrag in `sitemap.xml` und in `scripts/shot.mjs`.
Offen bleibt:

Geprüft und live: `npm run shot` läuft durch (10 Screenshots, keine Fremd-Requests, Schriften
geladen), Desktop 1400px und mobil 390px gesichtet, `https://dynamicspro.de/health-check`
liefert 200 und entspricht dem Stand auf `main`. Offen bleibt:

- [ ] **Abschnitt 6 der Datenschutzerklärung gegenlesen.** Der Text zu Microsoft Bookings ist
      ein Entwurf, kein geprüfter Rechtstext. Prüfen Sie Anbieterangabe, Auftragsverarbeitung
      und Aufbewahrungsfristen, bevor die Seite live geht. Das ist der letzte Punkt vor dem
      Merge, die Buchungsseite selbst ist fertig und geprüft (`content/bookings.md`).
- [x] Eigene OG-Karte: `assets/og-health-check.png`, siehe Erscheinungsbild.
- [ ] Einen belegbaren Satz zum Analyse-Toolset ergänzen, sobald einer ohne Kundenbezug formulierbar ist.
- [ ] Nach den ersten zwei, drei Durchläufen eine belastbare Kennzahl in den Hero nehmen, etwa die
      Zahl der Befunde je Umgebung und wie viele davon ein Ausfallrisiko tragen. Bis dahin steht
      dort nichts Messbares, und erfunden wird nichts.
- [ ] Muster-Scorecard auf der Seite zeigen, sobald das Ergebnisdokument einmal real erstellt ist.
      Ein Entwurf vorher hieße erfundene Befunde auf der Seite, auch als Beispiel ausgewiesen.
