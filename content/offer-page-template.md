# Vorlage für Angebotsseiten

Muster für die produktisierten Festpreis-Angebote. Gilt für den Health Check und für
alles, was danach kommt: ALM Check, Security Report, License & Capacity Report,
Adoption Report.

Platzhalter in spitzen Klammern ersetzen, Struktur und Reihenfolge stehen lassen.
Wer Blöcke umsortiert, verliert die Wiedererkennung zwischen den Angeboten.

## Kopfdaten

- Slug: `/<slug>`
- Datei: `<slug>/index.html` (eigenes Verzeichnis, damit die URL ohne `.html` auskommt)
- Sprache: Deutsch, Sie-Ansprache
- Preis: `<Betrag>` € zzgl. USt., fest, ohne Stufen
- CTA-Ziel: die Bookings-Seite als Link mit `target="_blank" rel="noopener"`, niemals als
  eingebettetes Fenster. E-Mail und Telefon bleiben in der Kontaktkarte als Ausweichweg.
  Einrichtung und Texte der Buchungsseite stehen in `content/bookings.md`.

## Block 1 — Hero (navy, Kopfbereich mit Kennzahlenleiste)

Kicker: Festpreis-Angebot · `<Durchführung>` · `<Dauer>`

Headline: eine Frage, die der Käufer sich selbst schon gestellt hat.
Keine Produktbezeichnung als Überschrift.

Subline: was geprüft wird, in welcher Zeit, mit welchem Ergebnis, zu welchem Preis.
Ein Satz Gegenstand, ein Satz Ergebnis, ein Satz Preis.

Button primär: Erstgespräch vereinbaren
Button sekundär: Sprung auf Block 3

Kennzahlenleiste, vier Einträge, immer dieselben Felder:

| Label | Wert |
| --- | --- |
| Dauer | `<Anzahl>` Tage, Start in der Regel `<Vorlauf>` nach Beauftragung |
| Preis | `<Betrag>` € zzgl. USt., fester Umfang |
| Ihr Aufwand | Rund `<Stunden>` Stunden im Team, verteilt auf `<Termine>` |
| Eingriff | Keiner. Lesezugriff, an Ihren Umgebungen wird nichts verändert |

## Block 2 — Textabschnitt: das Problem

Überschrift: der Zustand, nicht die Lösung. Vier Symptome, ein Satz zur Unsicherheit,
ein Satz, was das Angebot daran ändert. Drei bis vier Zeilen, mehr nicht.

## Block 3 — Kachelraster: der Prüfumfang

Überschrift: Was geprüft wird

Sechs bis acht Kacheln, je Titel und eine Leitfrage. Die Leitfrage ist eine echte
Frage mit Fragezeichen und wird im Ergebnis beantwortet.

**Die Kacheltitel sind die Kapitel des Ergebnisdokuments, nicht freie Überschriften.**
Wo ein Werkzeug den Bericht erzeugt, werden die Namen von dort übernommen; beim Health
Check sind es die neun Dimensionen aus `DIMS` in `scripts/health_analysis.py` (Repo
`Healthcheck`), die zehnte kommt bei Dual Write dazu. Eine Kachel, die das Ergebnisdokument nicht als Kapitel kennt, verspricht
etwas, das der Kunde nicht wiederfindet.

Den Zusatz „(Überblick)" trägt eine Dimension nur, wenn das Werkzeug dort tatsächlich
weniger liefert. Beim Health Check stand er an Sicherheit und ALM, obwohl beide
vollwertige Dimensionen sind und die Fachberichte im Lieferpaket liegen; er ist dort
entfernt. Wer ihn setzt, prüft vorher im Werkzeug, was der Lauf wirklich ausgibt.

Hinweis unter den Kacheln: was der Lauf zusätzlich liefert oder weglässt, und welches
Angebot eine Dimension vertieft. Dieser Hinweis hält die Familie zusammen und begrenzt
den Umfang.

## Block 4 — Nummerierte Liste: der Ablauf

Drei bis fünf Schritte mit Dauer in Klammern, wo es eine gibt. Jeder Schritt eine
Zeile Erläuterung.

Hinweis: Gesamtaufwand beim Kunden in Stunden und der Satz, dass nichts verändert
wird. Beides sind Einwandbehandlungen und bleiben stehen.

## Block 5 — Dreierraster: das Ergebnis

Genau drei Lieferobjekte, je Titel und ein Satz. Mehr als drei liest niemand, weniger
wirkt dünn.

Hinweis: dass die Ergebnisse dem Kunden gehören und er sie ohne den Ersteller
weiterverwenden kann. Das trennt den Report vom Projektverkauf.

## Block 6 — Dreierraster: warum DynamicsPro

Erfahrung, Unabhängigkeit, Werkzeug. Je Titel und ein Satz Beleg.

Keine Kundennamen, keine Logos, keine Stimmen, keine Fallzahlen. NDA.
Jahreszahlen folgen der Startseite und dem englischen Profil-Dokument.

## Block 7 — Häufige Fragen

Überschrift: die Themen der Fragen in einer Zeile, nicht das Wort „FAQ".
Kicker: Häufige Fragen zum `<Angebot>`

Sechs bis acht Fragen, so formuliert, wie ein Käufer sie in die Suche tippt: Preis,
Dauer, eigener Aufwand, nötige Zugriffe, Ergebnis, Abgrenzung, und eine Frage, die den
naheliegenden Einwand aufnimmt („Lohnt sich das, wenn mein System läuft?").

Jede Antwort besteht aus Zahlen, die weiter oben auf der Seite stehen. Eine Antwort, die
etwas Neues behauptet, ist ein Fehler im Rest der Seite.

Der Block steht **vor** dem Abschluss-CTA: Er beantwortet Einwände, er erhebt keine. Die
Absagen bleiben im Rahmenblock dahinter.

Sichtbarer Text und `FAQPage`-Schema im `<head>` müssen wörtlich übereinstimmen, und der
Text steht ohne Aufklappen auf der Seite. Kein `<details>`.

## Block 8 — Abschluss-CTA (navy, mit Kontaktkarte)

Headline: Preis, Dauer, Nutzen in drei kurzen Sätzen.
Subline: Durchführungsform und Vorlauf.
Button: Erstgespräch vereinbaren
Kleingedrucktes: Preis zzgl. USt. und die Länge des Erstgesprächs.
Kontaktkarte: E-Mail, Telefon, Zum Profil.

## Block 9 — Zwei Listen nebeneinander: Rahmen, hinter dem CTA

Letzter Abschnitt der Seite, hinter dem Abschluss-CTA. Drei Absagen unmittelbar vor dem
Knopf bremsen den Abschluss. Der Einwand wird stattdessen schon unter den Kacheln in
einem Satz benannt, zusammen mit dem Hinweis, dass der ausführliche Block am Seitenende
steht.

Voraussetzungen: drei Punkte, was der Kunde beistellt, Zugriffe zuerst.

Nicht enthalten: drei Punkte, was das Angebot nicht leistet. Immer dabei ist die
Umsetzung der Maßnahmen, weil sie getrennt verkauft wird.

## SEO

| Feld | Muster |
| --- | --- |
| Title | `<Angebot>` zum Festpreis \| DynamicsPro |
| Meta description | Ein Satz Gegenstand, ein Satz Ergebnis, Preis am Ende. Unter 160 Zeichen. |
| Slug | /`<slug>` |
| Canonical | https://dynamicspro.de/`<slug>`/ |
| OG title | wie Title, ohne den Zusatz hinter dem Strich |
| OG description | wie Meta description, darf länger sein |
| OG image | assets/og.png, bis es eine eigene Karte gibt |

Fünf bis acht deutsche Zielbegriffe festhalten und in Überschriften und Fließtext
unterbringen. Kein `meta name="keywords"`.

Strukturierte Daten, zwei Blöcke `application/ld+json` im `<head>`: `Service` mit
`Offer` und Preis, dazu `FAQPage` mit den Fragen aus Block 7, wörtlich wie im Text.

Jeder Abschnittskopf trägt einen Kicker mit dem Zielbegriff, die Überschrift darunter
bleibt der menschliche Satz. Der Kicker ist die Suchzeile, die Überschrift die Lesezeile.

## Anschlüsse auf der Startseite

- Teaser unter dem Hero, siehe `content/startseite.md`
- Eintrag in Kopfleiste und mobilem Panel
- Verweis aus der thematisch nächsten Leistungskarte

## Checkliste vor dem Deploy

- [ ] Verzeichnis in `.github/workflows/pages.yml` eingetragen, sonst geht die Seite stillschweigend nicht live
- [ ] Eintrag in `sitemap.xml`
- [ ] Seite in `scripts/shot.mjs` unter `PAGES` ergänzt
- [ ] `npm run shot` grün: HTTP 200, keine Fremd-Requests, beide Schriften geladen
- [ ] Desktop 1400px und mobil 390px gesichtet
- [ ] Preis, Dauer und Aufwand stimmen mit dem Angebotsdokument überein
