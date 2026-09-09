# Schriften

Selbst gehostet, damit beim Seitenaufruf kein Request an Google geht
(Art. 6 DSGVO, LG München I, 3 O 17493/20).

| Datei | Familie | Schnitt | Subset |
|---|---|---|---|
| `manrope-latin.woff2`, `manrope-latin-ext.woff2` | Manrope | variabel, 400–800 | latin / latin-ext |
| `plex-latin.woff2`, `plex-latin-ext.woff2` | IBM Plex Sans | variabel, 400–600 | latin / latin-ext |
| `plex-italic-latin.woff2`, `plex-italic-latin-ext.woff2` | IBM Plex Sans | kursiv 400 | latin / latin-ext |

Beide Familien stehen unter der SIL Open Font License 1.1
(`OFL-Manrope.txt`, `OFL-IBMPlexSans.txt`).

Bezogen über die Google-Fonts-CSS-API (`css2?family=...`), es sind die
unveränderten Original-woff2-Dateien. Zum Aktualisieren die CSS-API mit
modernem User-Agent abrufen, die Blöcke `latin` und `latin-ext` nehmen
und die `unicode-range`-Angaben in `index.html` mitziehen.
