# DynamicsPro – Portfolio

Statische Website für dynamicspro.de. Eine Datei (`index.html`), kein Build, keine Laufzeit-Abhängigkeiten.

## Lokal ansehen
```bash
npm run serve   # dann http://localhost:8080
```

## Prüfen nach jeder Änderung
```bash
npm install && npx playwright install chromium   # einmalig
npm run shot
```
Schreibt je einen Screenshot in 1400px und 390px für alle vier Seiten nach `shots/` und bricht ab, wenn eine Seite keinen HTTP 200 liefert,
einen Fremd-Request absetzt oder eine der beiden Schriften nicht lädt.

## Deploy
GitHub Actions, Workflow `.github/workflows/pages.yml`. Jeder Push auf `main` deployt.
Ausgeliefert werden nur `index.html`, `solution-admin-console.html`, `impressum.html`,
`datenschutz.html`, `assets/`, `robots.txt`, `sitemap.xml`, `CNAME` und `.nojekyll`; `README.md`, `CLAUDE.md`, `package.json` und `scripts/` bleiben aus dem Web heraus.

Einmalige Einrichtung im Repository:

1. **Settings → Pages → Source: „GitHub Actions“.** Ohne diesen Schritt schlägt der
   Workflow im Schritt `configure-pages` fehl.
2. **Settings → Pages → Custom domain: `dynamicspro.de`.** Die Datei `CNAME` liegt bereits
   im Repo und wird mit ausgeliefert.
3. **DNS beim Domain-Anbieter:**
   - `dynamicspro.de` A-Records auf `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - optional AAAA auf `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
   - `www.dynamicspro.de` CNAME auf `aschwarzdynpro.github.io`
4. **Settings → Pages → „Enforce HTTPS“** aktivieren, sobald das Zertifikat ausgestellt ist
   (dauert nach der DNS-Umstellung bis zu einer Stunde).

## Social-Preview-Bild
`assets/og.png` (1200x630) wird aus `scripts/og-card.html` gerendert. Nur neu bauen,
wenn sich Claim oder Layout der Karte ändern:
```bash
npm run og
```
