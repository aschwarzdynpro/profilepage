# DynamicsPro – Portfolio

Statische Website für dynamicspro.de. Eine Datei (`index.html`), keine Abhängigkeiten.

## Lokal ansehen
```bash
python3 -m http.server 8080   # dann http://localhost:8080
```

## Deploy mit GitHub Pages
1. Repository anlegen (z. B. `dynamicspro-site`), Inhalt pushen.
2. Settings → Pages → Source: *Deploy from a branch*, Branch `main`, Ordner `/ (root)`.
3. Eigene Domain: Datei `CNAME` mit `dynamicspro.de` ins Repo, beim DNS-Anbieter A-Records auf die GitHub-Pages-IPs bzw. CNAME `www` → `<user>.github.io`. Unter Settings → Pages *Enforce HTTPS* aktivieren.

## Screenshots für die Prüfung (optional)
```bash
npm install -D playwright && npx playwright install chromium
npm run shot   # schreibt shots/desktop.png und shots/mobile.png
```
