# Health Check (Seitenquelle)

Quelle für `health-check/index.html`. Ein Abschnitt hier entspricht genau einem
Block auf der Seite, in derselben Reihenfolge. Wer Text ändert, ändert beides.

- Slug: `/health-check`
- Datei: `health-check/index.html`
- Sprache: Deutsch, Sie-Ansprache. Gilt für die ganze Site, siehe CLAUDE.md.
- Preis: 5.000 € zzgl. USt. Fest, ohne Stufen und ohne Rabatt.
- CTA-Ziel: die Bookings-Seite, als Link in einem neuen Tab. Adresse und Einrichtung
  stehen in `content/bookings.md`. Kopfleiste, Hero und
  Abschluss-CTA zeigen dorthin. Die Kontaktkarte behält E-Mail und Telefon als Ausweichweg.
  Kein eingebettetes Buchungsfenster: das wäre ein Request an Microsoft beim Seitenaufruf
  und würde die Aussagen in den Nummern 3 und 4 der Datenschutzerklärung aufheben.

## Block 1 — Hero (navy, Kopfbereich mit Kennzahlenleiste)

Kicker: Festpreis-Angebot · Remote · 5 Tage

Headline: Wie gesund ist Ihr Dynamics 365?

Subline: Unabhängiger Health Check für Dynamics 365 CE und Power Platform.
In 5 Tagen zu Scorecard, Risikoliste und konkretem Maßnahmenplan. Festpreis 5.000 €.

Button primär: Erstgespräch vereinbaren
Button sekundär: Was geprüft wird (Sprung auf Block 3)

Kennzahlenleiste (vier Einträge, `dl.facts`):

| Label | Wert |
| --- | --- |
| Dauer | 5 Tage, Start in der Regel zwei bis drei Wochen nach Beauftragung |
| Preis | 5.000 € zzgl. USt., fester Umfang |
| Ihr Aufwand | Rund 4 bis 5 Stunden im Team, verteilt auf Kickoff, Interviews und Präsentation |
| Eingriff | Keiner. Lesezugriff, an Ihren Umgebungen wird nichts verändert |

## Block 2 — Textabschnitt

Überschrift: Über Jahre gewachsen, selten geprüft

Customizing-Altlasten, langsame Formulare, fehlerhafte Flows, unklare Berechtigungen.
Die meisten Systeme laufen, aber niemand weiß genau, wie stabil. Der Health Check
schafft Klarheit, bevor aus Risiken Ausfälle werden.

## Block 3 — Kachelraster, 8 feste Kacheln plus eine bedingte (2 Spalten, ab 900px eine Spalte)

Überschrift: Was geprüft wird
Unterzeile: Acht Dimensionen, dazu die Code-Analyse, wenn die Umgebung sie hergibt. Jede mit
einer Leitfrage, die am Ende beantwortet ist.

Die Namen und ihre Reihenfolge sind **nicht frei wählbar**: sie sind die Kapitel des
Gesamtberichts, wie `scripts/health_analysis.py` sie in `DIMS` erzeugt (Repo
`Healthcheck`). Wer sie hier umbenennt, erzeugt eine Seite, die andere Kapitel verspricht
als der Kunde bekommt.

| Nr. | Dimension | Leitfrage |
| --- | --- | --- |
| 01 | Kapazität und Lizenzen | Wie entwickeln sich Speicher, Audit-Log und Wachstum, und wo liegen gekaufte Lizenzen ungenutzt? |
| 02 | Performance und Betrieb | Wo bremsen Abfragen, überladene Formulare, synchrone Logik oder Drosselungen die Anwender? |
| 03 | Sicherheit | Wer darf tatsächlich was: Rollen, Administratoren, organisationsweite Zugriffe und Zuweisungen? |
| 04 | ALM und Customizing | Sind Solutions sinnvoll geschnitten, Publisher konsistent, Layer beherrscht und die Solution-Checker-Befunde abgearbeitet? |
| 05 | Automatisierung | Laufen Flows und Workflows stabil, mit Dienstkonten als Eigentümer und ohne veraltete Technik? |
| 06 | Datenmodell und Datenqualität | Wie viel Altlast steckt in Tabellen und Formularen, und sind Duplikate, Pflichtfelder und Füllgrade im Griff? |
| 07 | Nutzung und Adoption | Wer arbeitet tatsächlich im System, und welche Lizenzen und Funktionen bleiben ungenutzt? |
| 08 | Umgebungen und Governance | Tragen Umgebungslandschaft, DLP-Richtlinien, Backups und Plattformstand? |
| 09 | Code und Erweiterungen (`wenn vorhanden`) | Ist das Kunden-JavaScript wartbar, frei von abgekündigten APIs und ohne fest verdrahtete Umgebungs-URLs oder Geheimnisse im Code? |

Kachel 09 ist D10 im Werkzeug und steht unter der Bedingung `CODE_ON`: sie erscheint, sobald
Kundenbibliotheken gefunden werden oder ein Repository ausgewertet werden konnte. Sie trägt
deshalb die Marke „wenn vorhanden" (`span.opt`, dieselbe wie der optionale Workshop in Block 4)
und läuft als `.dim.cond` über beide Spalten, sonst bliebe die letzte Rasterzeile halb leer.
**Die Kachel darf nicht wieder in den Hinweistext wandern:** die Code-Analyse ist ein
Kaufargument und gehört in den Prüfumfang, nicht in die Fußnote. In gewachsenen Umgebungen
greift die Bedingung praktisch immer.

Hinweis unter den Kacheln (`p.note`): Die neunte Dimension setzt voraus, dass sich
Kunden-JavaScript, Plugins oder ein Repository auswerten lassen; in gewachsenen Umgebungen
ist das praktisch immer der Fall. Hinzu kommt Integration (Dual Write), wenn Strecken laufen.
Die Fachberichte zu Sicherheitsmodell, Performance und Formularfüllgraden, aus denen die
Bewertung stammt, liegen dem Ergebnis bei. Die Umsetzung der Maßnahmen ist nicht
enthalten. Voraussetzungen und Abgrenzung stehen am Seitenende.

Die beiden letzten Sätze nehmen den Einwand vorweg, den Block 8 sonst erst unmittelbar
vor dem Abschluss-Knopf bringen würde, und weisen den Weg zum ausführlichen Block.

Die beiden Zusatzdimensionen stehen im Werkzeug unter einer Bedingung (`DW_ON`, `CODE_ON`
in `health_analysis.py`), deshalb stehen sie als Hinweis und nicht als Kachel. In der
Praxis erscheint „Code und Erweiterungen" fast immer, weil die Skriptauswertung zum
Standardlauf gehört; „Integration (Dual Write)" nur bei Kunden mit laufenden Strecken.

Der Hinweis nannte Sicherheit, ALM, Lizenzen und Kapazität früher als Überblick und
verwies für die Tiefe auf eigene Reports. Das stimmte nicht: alle vier sind vollwertige
Dimensionen, und `Build-Index.py` legt die Fachberichte zu Sicherheitsmodell, Performance
und Formularfüllgraden in dasselbe Lieferpaket. **Offen bleibt damit der Zuschnitt der
restlichen Angebotsfamilie**: Wenn die Fachberichte im Festpreis liegen, verkaufen die
geplanten Tiefenanalyse-Seiten die Auswertung und die Umsetzung, nicht den Bericht.

## Block 4 — Nummerierte Liste, 4 Schritte

Überschrift: Ablauf
Unterzeile: Vier Termine über fünf Tage, dazwischen die toolgestützte Analyse. Der Workshop
danach ist optional.

1. Kickoff (90 Minuten) — Ist-Situation, Schmerzpunkte, Ziele, Zugriffe klären
2. Toolgestützte Analyse mit Lesezugriff — Auswertung der Umgebungen mit eigenem Analyse-Toolset
3. Zwei bis drei Kurzinterviews — mit Entwicklung, Makern und Betrieb, je 45 Minuten
4. Ergebnispräsentation (1 Stunde) — Scorecard, Risiken und Maßnahmenplan im Gespräch durchgehen
5. Workshop nach Bedarf, gekennzeichnet als **optional** — Die Handlungsempfehlungen
   konzeptionell durchsprechen: Zuschnitt der Maßnahmen, Reihenfolge und wer was übernimmt.
   Umfang und Aufwand stimmen wir vorher ab, nicht im Festpreis enthalten.

Bewusst ohne feste Dauer und ohne Betrag. „Nach Bedarf" statt „nach Aufwand": Letzteres ist
eine Abrechnungsart und klingt auf einer Festpreisseite nach einem Bruch im Modell.

Der fünfte Eintrag trägt die Klasse `optional`: Nummer in `--ink-3` statt `--sky` und ein
Kennzeichen neben der Überschrift, wie die `.gate`-Marke auf der Konsolenseite. Die vier
Schritte davor sind der Festpreis-Umfang, der fünfte steht sichtbar daneben.

Hinweis (`p.note`): Ihr Team ist für den Health Check insgesamt rund 4 bis 5 Stunden
eingebunden. An Ihren Umgebungen wird nichts verändert.

Rechnung dahinter: Kickoff 1,5 Stunden, zwei bis drei Interviews zu 45 Minuten, Präsentation
1 Stunde, macht 4 bis 4,75 Stunden. Der Workshop zählt nicht mit, er hat keine feste Dauer.
Deshalb steht dort „für den Health Check". Wer eine der Dauern ändert, rechnet hier und in
der Kennzahlenleiste des Hero nach.

## Block 5 — Dreierraster Lieferobjekte

Überschrift: Ihr Ergebnis
Unterzeile: Drei Dokumente, die Sie ohne mich weiterverwenden können, dazu die
Fachberichte, aus denen die Bewertung stammt.

| Lieferobjekt | Inhalt |
| --- | --- |
| Health-Scorecard | Über acht Dimensionen und die Code-Analyse, jeweils mit Ampel und Begründung. |
| Top-10-Risiken | Mit Auswirkung und betroffenen Umgebungen. |
| Priorisierter Maßnahmenkatalog | In drei Stufen nach Fahrplan: 30, 60 und 90 Tage. |

Die drei Stufen sind die Phasen aus `scripts/action_plan.py`: der Fahrplan kennt 30, 60
und 90 Tage, gelbe Befunde rutschen eine Phase nach hinten, rote Sofortmaßnahmen stehen
immer in Phase 30. Eine Stufe „Zielarchitektur" stand hier früher, das Werkzeug erzeugt
sie nicht.

Hinweis (`p.note`): Der Maßnahmenkatalog gehört Ihnen. Sie setzen ihn intern, mit
Ihrem Partner oder mit mir um.

## Block 6 — Dreierraster Argumente

Überschrift: Warum DynamicsPro

| Argument | Beleg |
| --- | --- |
| Über 16 Jahre Dynamics 365 und Power Platform | Vom Entwickler zum Solution Architect, ohne den Code aus der Hand zu geben. |
| Unabhängig | Kein Lizenzvertrieb, keine Bindung an einen Implementierungspartner. |
| Eigenes Analyse-Toolset statt Bauchgefühl | Befunde sind gemessen und belegt, nicht geschätzt. |

Die Jahreszahl steht bewusst auf „über 16", passend zu Hero und OG-Beschreibung der
Startseite. Siehe CLAUDE.md, Abschnitt Inhaltliche Quelle.

## Block 7 — Häufige Fragen

Überschrift: Preis, Dauer, Zugriffe und Grenzen
Kicker: Häufige Fragen zum Dynamics 365 Health Check
Unterzeile: Die Antworten stehen verteilt auf dieser Seite, hier zusammengefasst.

Acht Fragen, Formulierung wie gesucht wird, nicht wie intern geredet wird. Jede Antwort
nennt nur Zahlen, die weiter oben auf der Seite stehen: 5.000 €, fünf Tage, 4 bis 5
Stunden, acht Dimensionen plus Code-Analyse, Top 10, drei Stufen zu 30, 60 und 90 Tagen.

| Frage | Kern der Antwort |
| --- | --- |
| Was kostet ein Dynamics 365 Health Check? | 5.000 € zzgl. USt., fester Umfang, Umsetzung getrennt |
| Wie lange dauert der Health Check, und wann kann er starten? | fünf Tage, Start zwei bis drei Wochen nach Beauftragung, remote |
| Wie viel Zeit muss mein Team einplanen? | rund 4 bis 5 Stunden, aufgeteilt auf die vier Termine |
| Welche Zugriffe brauchen Sie, und wird an meinen Umgebungen etwas verändert? | Lesezugriff auf zwei Umgebungen, PPAC, optional DevOps; es wird nichts geschrieben |
| Was erhalte ich am Ende? | Scorecard, Top-10-Risiken, Maßnahmenkatalog in drei Stufen, dazu die Fachberichte |
| Ist die Umsetzung der Maßnahmen enthalten? | nein, auch der Workshop nicht |
| Für welche Systeme gilt der Health Check? | D365 CE und Power Platform auf Dataverse, nicht F&O; von Dual Write die Dataverse-Seite |
| Lohnt sich der Health Check, wenn das System läuft? | ja, genau dafür; Befunde sind gemessen, nicht geschätzt |

Der Block steht vor dem Abschluss-CTA, nicht dahinter: er beantwortet Einwände, er
erhebt keine. Die Absagen bleiben in Block 9.

Sichtbarer Text und `FAQPage`-Schema im `<head>` müssen **wörtlich** übereinstimmen.
Kein `<details>`, nichts zum Aufklappen: Was im Schema steht, muss ohne Klick auf der
Seite stehen.

## Block 8 — Abschluss-CTA (navy, mit Kontaktkarte)

Headline: 5.000 € Festpreis. 5 Tage. Klare Antworten.

Subline: Durchführung remote, Start in der Regel innerhalb von zwei bis drei Wochen
nach Beauftragung.

Button: Erstgespräch vereinbaren

Kleingedrucktes: Preis zzgl. USt. Das Erstgespräch dauert rund 30 Minuten und ist
kostenfrei.

Kontaktkarte: E-Mail, Telefon, Zum Profil. Dieselben drei Wege wie auf der Startseite.

## Block 9 — Zwei Listen nebeneinander, hinter dem CTA

Steht bewusst als letzter Abschnitt hinter dem Abschluss-CTA. Drei Absagen unmittelbar
vor dem Knopf bremsen den Abschluss, gebraucht wird der Block trotzdem: wer bis hier
liest, prüft gerade die Machbarkeit.

Überschrift: Voraussetzungen und Abgrenzung
Unterzeile: Damit vor der Beauftragung klar ist, was Sie beistellen und was der
Health Check nicht leistet.

Voraussetzungen:

- Lesezugriff auf die produktive und eine vorgelagerte Dataverse-Umgebung sowie das Power Platform Admin Center
- Lesezugriff auf Azure DevOps oder GitHub, sofern vorhanden
- Ein fester Ansprechpartner und zwei bis drei Interviewpartner

Nicht enthalten:

- Umsetzung von Maßnahmen
- Fachliche Prozessberatung und Lizenzberatung
- Finance & Operations selbst sowie Integrationen außerhalb der Power Platform

„Selbst" steht dort, weil Dimension D9 die Dual-Write-Strecken bewertet, allerdings nur
aus Dataverse gelesen. Initial-Sync-Stand und Fehlerliste des Dienstes liegen in F&O und
sind lesend nicht erreichbar, siehe Konzept des Werkzeugs, Abschnitt D9.

## SEO

| Feld | Wert |
| --- | --- |
| Title | Dynamics 365 Health Check zum Festpreis \| DynamicsPro |
| Meta description | Unabhängiger Health Check für Dynamics 365 CE und Power Platform: Scorecard, Risiken und Maßnahmenplan in 5 Tagen. Festpreis 5.000 €. |
| Slug | /health-check |
| Canonical | https://dynamicspro.de/health-check/ |
| OG title | Dynamics 365 Health Check zum Festpreis |
| OG description | In 5 Tagen zu Scorecard, Top-10-Risiken und priorisiertem Maßnahmenplan für Dynamics 365 CE und Power Platform. Unabhängig, toolgestützt, ohne Eingriff in Ihre Umgebungen. |
| OG image | https://dynamicspro.de/assets/og.png (die Karte der Startseite, bis eine eigene existiert) |

Strukturierte Daten im `<head>`: `Service` mit `Offer` und Preis, dazu `FAQPage` mit den
acht Fragen aus Block 7. Beide als eigenes `application/ld+json`.

Zielbegriffe, DACH-Mittelstand, deutschsprachige Suche:

1. Dynamics 365 Health Check
2. Power Platform Assessment
3. Dynamics 365 Audit
4. Dataverse Analyse
5. Dynamics 365 Performance Analyse
6. Power Platform Governance Check
7. Solution-Architektur Review Dynamics 365
8. CRM Health Check Festpreis

Kein `meta name="keywords"`. Suchmaschinen werten es nicht aus, die Begriffe stehen
hier als Redaktionsziel und gehören in Überschriften und Fließtext.

## Manuelle Schritte

Die Aufgabenliste steht in CLAUDE.md unter „Offen". Auf dieser Site gibt es kein CMS:
Seite, Blöcke, SEO-Felder, Navigationseintrag und Teaser sind Code und liegen im Repo.
Manuell bleiben nur Prüfung, Deploy und die Entscheidung zum Buchungsziel.
