# dynamicspro.de – Portfolio-Website

Statische Single-File-Site (`index.html`), kein Build, kein Framework. Ausgeliefert über GitHub Pages.

## Regeln
- Alles bleibt in `index.html` (CSS im `<style>`, keine externen JS-Bundles). Bilder nach `assets/`.
- Ausnahme: `solution-admin-console.html`, `impressum.html`, `datenschutz.html` und die
  Angebotsseiten unter `<slug>/index.html` sind eigene Seiten mit eigenem `<style>`. Anschrift, USt-IdNr. und Aufsichtsbehörde nur nach Rücksprache ändern.
- Keine Frameworks, kein Tailwind, kein Build-Schritt einführen.
- Deutsch, Sie-Ansprache, kein Marketing-Sprech. Keine Emojis, keine Bindestrich-Gedankenstriche.
- Kundennamen bleiben anonymisiert (Branche statt Firma). Keine Tagessätze, keine Partner-Methodik.
- Nach jeder Änderung Desktop (1400px) und Mobil (390px) prüfen: `npm run shot` (Playwright) oder Browser.
- Keine Requests an Dritte. Schriften liegen selbst gehostet in `assets/fonts/`, kein Google-Fonts-Link. `npm run shot` bricht ab, sobald ein Fremd-Host angefragt wird.

## Deploy
Push auf `main` löst `.github/workflows/pages.yml` aus. Der Workflow kopiert eine
**explizite Dateiliste** nach `_site`. Neue Top-Level-Dateien (z. B. `impressum.html`)
und neue Verzeichnisse (z. B. `health-check/`) müssen dort eingetragen werden, sonst gehen
sie stillschweigend nicht live.
Einrichtung und DNS stehen in `README.md`.

## Design-Tokens (in `:root`)
- Navy `--navy #0F1E33` (Hero, Nav, Kontakt), Akzent `--sky #6DB4FF`, Papier `--bg #F6F7F9`
- Schrift: Manrope (Überschriften), IBM Plex Sans (Fließtext), selbst gehostet als Variable Fonts in `assets/fonts/`
- Hero-Blaupause: inline SVG `.blueprint` mit animierten Pulsen (`animateMotion`), reduced-motion respektiert
- Skills: Netzdiagramm `.radar` (SVG, Skala 1–5) + Balkengruppen `.sg` (5 Segmente = Niveau, Zahl = Jahre)

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
Beide Seiten markieren den Abschnitt, in dem man gerade steht, und haben unter ihrem
Breakpoint dasselbe Panel von unten. Klassennamen (`.toc-shell`, `.toc`, `.toc-fab`,
`.toc-backdrop`) und Verhalten sind absichtlich gleich, jede Datei trägt ihre eigene
Kopie von CSS und Skript.

- `index.html`: Kopfleiste mit den sechs Abschnitten, aktiver Eintrag weiss mit
  Unterstrich in `--sky`. Unter 900px Panel über den Knopf „Menü" rechts unten.
- `solution-admin-console.html`: mitlaufende Spalte links mit allen 27 Sprungzielen,
  offen ist immer genau eine Gruppe. Unter 1100px Panel über den Knopf „Inhalt",
  dort stehen alle Gruppen offen.
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
SEO-Felder werden nicht ins Englische übersetzt, auch nicht teilweise. Sollte die Site
später englische Fassungen bekommen, kommen sie als eigene Seiten dazu und ersetzen die
deutschen nicht.

**Buchung nur als Link.** Die CTA-Knöpfe verweisen auf Microsoft Bookings, sie betten nichts
ein. Ein eingebettetes Buchungsfenster lädt beim Seitenaufruf von `outlook.office365.com` und
setzt Cookies. Damit wären die Nummern 3 und 4 der Datenschutzerklärung falsch („keine Cookies",
„keine Verbindung zu Servern Dritter"), es bräuchte ein Consent-Management, das es hier nicht
gibt, und `npm run shot` würde abbrechen. Als Link fließen Daten erst nach einem Klick, Abschnitt
6 der Datenschutzerklärung deckt das ab.

**Kein CMS.** Es gibt keine Redaktionsoberfläche und keinen Sync in ein fremdes System.
Seite, Blöcke, SEO-Felder, Navigationseintrag und Teaser sind Code in diesem Repo.

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

### Health Check, verbleibende manuelle Schritte
Alles, was an anderer Stelle Redaktionsarbeit in einem CMS wäre, ist hier bereits Code und
erledigt: Seite angelegt (`health-check/index.html`), Blöcke gesetzt, SEO-Felder im `<head>`,
Navigationseintrag in Kopfleiste und Panel, Teaser unter dem Hero der Startseite,
CTA verdrahtet, Verzeichnis im Deploy-Workflow, Eintrag in `sitemap.xml` und in `scripts/shot.mjs`.
Offen bleibt:

Geprüft und live: `npm run shot` läuft durch (10 Screenshots, keine Fremd-Requests, Schriften
geladen), Desktop 1400px und mobil 390px gesichtet, `https://dynamicspro.de/health-check`
liefert 200 und entspricht dem Stand auf `main`. Offen bleibt:

- [ ] **Buchungsseite fertig einrichten, bevor gemergt wird.** Die Adresse
      `https://bookings.cloud.microsoft/book/DynamicsPro@dynamicspro.de/` ist eingetragen und
      die Seite ist ohne Microsoft-Konto buchbar. Sie ist aber noch englisch, die Zeiten stehen
      in UTC, die Dienstbeschreibung ist der Microsoft-Platzhalter, die Mitarbeiterauswahl ist
      sichtbar, das Adressfeld steht im Formular und der Einwilligungstext fehlt.
      `content/bookings.md` listet alle sechs Punkte mit dem jeweiligen Befund.
- [ ] **Abschnitt 6 der Datenschutzerklärung gegenlesen.** Der Text zu Microsoft Bookings ist
      ein Entwurf, kein geprüfter Rechtstext. Prüfen Sie Anbieterangabe, Auftragsverarbeitung
      und Aufbewahrungsfristen, bevor die Seite live geht.
- [ ] Eigene OG-Karte für die Seite erwägen. Derzeit liegt `assets/og.png` der Startseite darunter,
      Quelle wäre `scripts/og-card.html`.
- [ ] Einen belegbaren Satz zum Analyse-Toolset ergänzen, sobald einer ohne Kundenbezug formulierbar ist.
- [ ] Nach den ersten zwei, drei Durchläufen eine belastbare Kennzahl in den Hero nehmen, etwa die
      Zahl der Befunde je Umgebung und wie viele davon ein Ausfallrisiko tragen. Bis dahin steht
      dort nichts Messbares, und erfunden wird nichts.
- [ ] Muster-Scorecard auf der Seite zeigen, sobald das Ergebnisdokument einmal real erstellt ist.
      Ein Entwurf vorher hieße erfundene Befunde auf der Seite, auch als Beispiel ausgewiesen.
