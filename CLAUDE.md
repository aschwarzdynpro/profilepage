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
Profil-Dokument `Profile_Andy_Schwarz_2026.docx` (englisch). Zahlen auf der Site müssen damit übereinstimmen.

## Offen
- Jahreszahlen zwischen deutschem und englischem Profil abgleichen.
- Pro Referenz eine belastbare Kennzahl ergänzen.
