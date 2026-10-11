# Zielbegriffe für die Suche

Redaktionsquelle, wird nicht ausgeliefert. Je Seite die Begriffe, für die sie bei Google gefunden
werden soll, in der Reihenfolge ihrer Bedeutung. Der erste Begriff steht im Suchtitel (`<title>`) und
im ersten Satz der `meta description`, die Regeln dazu stehen in `CLAUDE.md`, Abschnitt
Suchmaschinen. Die Begriffe sind Annahmen über das Suchverhalten der Zielgruppe; ob sie stimmen,
zeigt die Search Console nach vier bis acht Wochen unter „Leistung“. Keine Suchvolumen, nichts ist
gemessen.

## Lagebild (11.10.2026)

Für die Kopfbegriffe („Dynamics 365 Berater“, „Dynamics 365 Partner“, „Power Platform Beratung“)
sitzen auf Seite 1 Microsoft, Partnerhäuser mit hunderten Seiten und Jobportale. Dort kommt eine
Einzelperson mit 33 Seiten nicht hin, und muss es auch nicht: wer so sucht, sucht ein Haus.
Realistisch sind drei Gruppen von Suchen:

1. **Namens- und Markensuchen**: „Andy Schwarz Dynamics 365“, „DynamicsPro“. Hier gehört die Site
   auf Platz 1, vor LinkedIn.
2. **Spitze Angebotssuchen**: „Dynamics 365 Health Check Festpreis“, „Dynamics 365 Solution Architect
   freiberuflich“, „Power Platform Architekt Freelancer DACH“. Wenige Suchen, hohe Absicht, wenig
   Wettbewerb mit Preis auf der Seite.
3. **Problemsuchen von Admins und Entwicklern**, die auf den Blog führen: „Schedule Board kopieren“,
   „Dataverse Übersetzungen fehlen“, „Solution Import fehlgeschlagen Dataverse“. Hier ist Seite 1
   erreichbar, weil die Beiträge konkreter sind als die Microsoft-Doku und es kaum deutsche Treffer
   gibt. Jeder Beitrag ist eine eigene Landeseite.

## Startseite `/`

1. Dynamics 365 Solution Architect freiberuflich
2. Dynamics 365 Freelancer (Sales, Customer Service, Field Service)
3. Power Platform Architekt freiberuflich
4. Dynamics 365 Berater Nürnberg
5. Dataverse ALM Azure DevOps Beratung

## Health Check `/health-check/`

Die Liste in `content/health-check.md`, Abschnitt SEO, bleibt maßgeblich: Dynamics 365 Health
Check, Power Platform Assessment, Dynamics 365 Audit, Dataverse Analyse, Dynamics 365 Performance
Analyse, Power Platform Governance Check, Solution-Architektur Review Dynamics 365, CRM Health Check
Festpreis.

## Produktseiten

| Seite | 1. Begriff | weitere |
| --- | --- | --- |
| `/solution-admin-console.html` | Dataverse Solutions verwalten | Solution Merge Dataverse, Solution Import prüfen, Security Role Analyse Dataverse, Plugin Trace Log auswerten |
| `/translation-studio.html` | Dataverse Übersetzungen pflegen | Dynamics 365 Übersetzungen exportieren importieren, fehlende Übersetzungen Dataverse, Translation Export Excel Dynamics 365 |
| `/schedule-board-manager.html` | Schedule Board Manager Field Service | Schedule Board Settings kopieren, Schedule Board Tab konfigurieren, Project Operations Schedule Board |

## Blog

| Beitrag | 1. Begriff | weitere |
| --- | --- | --- |
| `admin-console-1-working-solutions` | Dataverse ALM Working Solution je Work Item | Solution Merge Dataverse, Solution-Strategie Power Platform |
| `admin-console-2-vor-dem-import` | Solution Import Dataverse fehlgeschlagen | Deployment Readiness Dataverse, Solution Layer Inspector, Import Log Dataverse |
| `admin-console-3-betrieb` | Dataverse Sicherheitsrollen vergleichen | Plugin Trace Log Dataverse, Flow deaktiviert Produktion, Dual Write Version |
| `admin-console-4-datentransfer` | Konfigurationsdaten Dataverse übertragen | Configuration Migration Tool Alternative, Dataverse Referenzdaten Umgebung |
| `schedule-board-1-kopie-und-filter` | Schedule Board kopieren Field Service | Schedule Board Settings Management, Schedule Board Filterlayout, Ressourcenabfrage Schedule Board |
| `schedule-board-2-vorschau-und-transfer` | Schedule Board Buchungskachel anpassen | Schedule Board Ressourcenzelle, Schedule Board in Produktion übertragen |
| `translation-studio` | fehlende Übersetzungen Dataverse finden | Dynamics 365 Übersetzungen exportieren, CrmTranslations.xml, Übersetzung Auswahlwerte Dataverse |
| `translation-studio-designer` | Dataverse Formulare übersetzen | Translation Studio Designer, Übersetzung Formular Dynamics 365 |

## Themen mit Suchnachfrage für die Blog-Woche

Vorschläge, für die Suchabsicht und eigene Erfahrung zusammenkommen. Jeder Beitrag braucht wie
bisher Problem, bisherige Umgehung, Lösung und etwas, das schiefging; die Fakten kommen aus
CodeApps und den Mandaten, nichts wird geschätzt.

- Solution Import fehlgeschlagen: die fünf häufigsten Ursachen aus dem geparsten Import-Log und wie
  man sie vorher sieht (Begriffe: „Solution Import Fehler Dataverse“, „missing dependency import“).
- Managed oder unmanaged in Produktion: was die Layer-Ansicht nach drei Jahren zeigt („managed vs
  unmanaged solution Dataverse“).
- Sicherheitsrollen in Dataverse prüfen: warum die Rollentabelle lügt und wie effektive Rechte bis
  zum Schnittstellenkonto aussehen („Dynamics 365 Sicherheitsrollen prüfen“).
- Schedule Board langsam: was die Ressourcenabfrage damit zu tun hat („Schedule Board langsam Field
  Service“), sobald es dazu belegbare Messungen gibt.
- Dataverse Übersetzungen: warum Auswahlwerte und Ansichten in der Excel-Datei fehlen und wie der
  Import sie trotzdem annimmt („Dataverse Auswahlwerte übersetzen“).
- Health Check: was ein Befund mit Schweregrad „Ausfallrisiko“ konkret ist, anonymisiert, sobald
  der erste Durchlauf gelaufen ist („Dynamics 365 Health Check Beispiel“).

## Was außerhalb des Repos zählt

In dieser Reihenfolge, weil es so am schnellsten Wirkung zeigt:

1. **Search Console** für `dynamicspro.de` (Domain-Property, Verifizierung per DNS-TXT),
   `sitemap.xml` einreichen, danach für Startseite, Health Check und Blog-Übersicht „Indexierung
   beantragen“. Bing Webmaster Tools importiert die Property aus der Search Console.
2. **`www` reparieren**: `https://www.dynamicspro.de/` liefert 503. Settings → Pages, Custom Domain
   entfernen und `dynamicspro.de` neu setzen, bis das Zertifikat auch `www` enthält.
3. **LinkedIn**: Website-Feld und „Info“ mit Link auf `https://dynamicspro.de/`, jeder Blogbeitrag
   als Beitrag mit Link. LinkedIn-Links zählen wenig für das Ranking, aber viel für die Namenssuche.
4. **Google Unternehmensprofil** für DynamicsPro, Stein bei Nürnberg, Kategorie
   „IT-Berater“ oder „Softwareunternehmen“, Website-Link, Dienstleistungen: Health Check,
   Solution Architecture, ALM. Das bedient „Dynamics 365 Berater Nürnberg“ über die lokale Box.
5. **Freelancer-Profile** (freelancermap, GULP, freelance.de) mit Link auf die Site und den
   gleichen Rollenbezeichnungen wie in den Referenzkarten.
6. **CodeApps-Repo**: READMEs der drei Apps verlinken auf ihre Produktseite und den passenden
   Blogbeitrag, sobald das Repo öffentlich ist.
7. **Fachbeiträge anderswo**: ein Gastbeitrag oder eine Antwort in der Power-Platform-Community mit
   Link auf einen Blogbeitrag ist mehr wert als zehn Verzeichniseinträge.
