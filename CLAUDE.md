# dynamicspro.de – Portfolio-Website

Statische Single-File-Site (`index.html`), kein Build, kein Framework. Ausgeliefert über GitHub Pages.

## Regeln
- Alles bleibt in `index.html` (CSS im `<style>`, keine externen JS-Bundles). Bilder nach `assets/`.
- Ausnahme: `solution-admin-console.html`, `impressum.html` und `datenschutz.html` sind eigene Seiten mit eigenem `<style>`. Anschrift, USt-IdNr. und Aufsichtsbehörde nur nach Rücksprache ändern.
- Keine Frameworks, kein Tailwind, kein Build-Schritt einführen.
- Deutsch, Sie-Ansprache, kein Marketing-Sprech. Keine Emojis, keine Bindestrich-Gedankenstriche.
- Kundennamen bleiben anonymisiert (Branche statt Firma). Keine Tagessätze, keine Partner-Methodik.
- Nach jeder Änderung Desktop (1400px) und Mobil (390px) prüfen: `npm run shot` (Playwright) oder Browser.
- Keine Requests an Dritte. Schriften liegen selbst gehostet in `assets/fonts/`, kein Google-Fonts-Link. `npm run shot` bricht ab, sobald ein Fremd-Host angefragt wird.

## Deploy
Push auf `main` löst `.github/workflows/pages.yml` aus. Der Workflow kopiert eine
**explizite Dateiliste** nach `_site`. Neue Top-Level-Dateien (z. B. `impressum.html`)
müssen dort eingetragen werden, sonst gehen sie stillschweigend nicht live.
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
