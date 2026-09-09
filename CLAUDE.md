# dynamicspro.de – Portfolio-Website

Statische Single-File-Site (`index.html`), kein Build, kein Framework. Ausgeliefert über GitHub Pages.

## Regeln
- Alles bleibt in `index.html` (CSS im `<style>`, keine externen JS-Bundles). Bilder nach `assets/`.
- Keine Frameworks, kein Tailwind, kein Build-Schritt einführen.
- Deutsch, Sie-Ansprache, kein Marketing-Sprech. Keine Emojis, keine Bindestrich-Gedankenstriche.
- Kundennamen bleiben anonymisiert (Branche statt Firma). Keine Tagessätze, keine Partner-Methodik.
- Nach jeder Änderung Desktop (1400px) und Mobil (390px) prüfen: `npm run shot` (Playwright) oder Browser.

## Design-Tokens (in `:root`)
- Navy `--navy #0F1E33` (Hero, Nav, Kontakt), Akzent `--sky #6DB4FF`, Papier `--bg #F6F7F9`
- Schrift: Manrope (Überschriften), IBM Plex Sans (Fließtext), Google Fonts
- Hero-Blaupause: inline SVG `.blueprint` mit animierten Pulsen (`animateMotion`), reduced-motion respektiert
- Skills: Netzdiagramm `.radar` (SVG, Skala 1–5) + Balkengruppen `.sg` (5 Segmente = Niveau, Zahl = Jahre)

## Inhaltliche Quelle
Profil-Dokument `Profile_Andy_Schwarz_2026.docx` (englisch). Zahlen auf der Site müssen damit übereinstimmen.

## Offen
- Impressum / Datenschutz als eigene Seiten (`impressum.html`, `datenschutz.html`) anlegen und im Footer verlinken.
- Jahreszahlen zwischen deutschem und englischem Profil abgleichen.
- Pro Referenz eine belastbare Kennzahl ergänzen.
