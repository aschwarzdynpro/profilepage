# dynamicspro.de – Portfolio-Website

Statische Single-File-Site (`index.html`), kein Build, kein Framework. Ausgeliefert über GitHub Pages.

## Regeln
- Alles bleibt in `index.html` (CSS im `<style>`, keine externen JS-Bundles). Bilder nach `assets/`.
- Ausnahme: `impressum.html` und `datenschutz.html` sind eigene Seiten mit eigenem `<style>`. Anschrift, USt-IdNr. und Aufsichtsbehörde dort nur nach Rücksprache ändern.
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
