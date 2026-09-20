# Microsoft Bookings, Einrichtung der Buchungsseite

Ziel der CTA-Knöpfe auf den Angebotsseiten. Diese Datei hält Texte und Einstellungen fest,
damit beim nächsten Angebot der Familie nicht neu geraten werden muss und damit die Texte
versioniert sind. Sie wird nicht ausgeliefert.

Die Seite ist **nur verlinkt, nie eingebettet**. Begründung steht in CLAUDE.md unter
„Produktisierte Angebote", Abschnitt „Buchung nur als Link".

## Anlage

Neue Buchungsseite, die alte „Book an Expert" wird gelöscht. Der Grund: die Adresse einer
Buchungsseite kommt vom Alias des Bookings-Postfachs, das beim Anlegen entsteht. Ein
geänderter Anzeigename ändert die Adresse nicht, `book.ms/b/BookanExpert@dynamicspro.de`
bliebe sonst stehen und stünde in jeder Bestätigungsmail.

Die Seite ist angelegt, die Adresse lautet:

    https://bookings.cloud.microsoft/book/DynamicsPro@dynamicspro.de/

Sie steht an drei Stellen in `health-check/index.html`: Kopfleiste, Hero und Abschluss-CTA.
Bewusst die direkte Adresse und nicht die Kurzform über `book.ms`, das spart zwei
Weiterleitungen und der Gastgeber ist am Hostnamen erkennbar.

`scripts/shot.mjs` bricht ab, sobald irgendein Link auf die reservierte Domain `.invalid`
zeigt. Falls die Adresse je wieder offen ist, gehört der Platzhalter
`https://bookings-url-fehlt.invalid/` zurück an diese drei Stellen, dann blockt der
Prüflauf den Merge von allein.

## Geschäftsinformationen

| Feld | Wert |
| --- | --- |
| Name | DynamicsPro |
| Website | https://dynamicspro.de |
| Telefon, Anschrift | wie im Impressum |
| Logo | Zeichen aus `assets/favicon.svg`, als PNG exportiert |
| Zeitzone | (UTC+01:00) Amsterdam, Berlin, Bern, Rom, Stockholm, Wien |
| Geschäftszeiten | nur die Fenster, in denen tatsächlich Gespräche stattfinden |

Die Zeitzone ist der Punkt, an dem die erste Fassung auffiel: sie stand auf UTC, die Slots
erschienen als 7:30 AM bis 2:30 PM im 12-Stunden-Format.

## Dienst

Genau ein Dienst. Der voreingestellte „IT support" wird gelöscht.

| Einstellung | Wert |
| --- | --- |
| Name | Erstgespräch Health Check |
| Dauer | 30 Minuten |
| Preis | kostenlos, nicht „Preis nicht festgelegt" |
| Ort | Teams-Besprechung |
| Pufferzeit danach | 15 Minuten |
| Vorlaufzeit | mindestens 24 Stunden |
| Buchbar bis | 30 Tage im Voraus |

Beschreibung:

> Kurzes Gespräch zum Dynamics 365 Health Check: Ihre Ausgangslage, offene Fragen zu Umfang
> und Ablauf, Klärung der Zugriffe. Keine Vorbereitung nötig.

Die 30 Minuten und das Wort „kostenfrei" stehen so auch auf der Landingpage im
Kleingedruckten unter dem Abschluss-CTA. Wer eines ändert, ändert beides.

Verfügbarkeit auf eigene Zeiten des Dienstes stellen, nicht auf die vollen Geschäftszeiten,
sonst ist die gesamte Arbeitswoche buchbar. Zwei Blöcke pro Woche reichen.

## Formularfelder

Nur was gebraucht wird, das verkürzt auch den Datenschutzabschnitt.

| Feld | Status |
| --- | --- |
| Name | Pflicht |
| E-Mail | Pflicht |
| Telefon | freiwillig |
| Anliegen | freiwillig, Freitext |
| Anschrift | ausgeblendet |

## Einstellungen der Buchungsseite

- Zugriff ohne Anmeldung mit Microsoft-Konto. War in der ersten Fassung bereits richtig
  gesetzt, die Seite ließ sich anonym öffnen.
- Sprache und Region: Deutsch, Deutschland. Steuert auch Bestätigungs- und Erinnerungsmails.
- Zeitfenster in der Zeitzone des Unternehmens anzeigen. Eine Umrechnung auf die Zeitzone des
  Besuchers hilft bei einer rein deutschen Zielgruppe nicht und verwirrt.
- Mitarbeiterauswahl ausblenden. Bei einer Person ist „Anyone" eine Frage ohne Antwort.
- Indexierung durch Suchmaschinen abschalten, sonst konkurriert die Buchungsseite mit der
  Landingpage.
- Absendername der Bestätigungsmail prüfen. Er folgt dem Namen der Buchungsseite.

## Einwilligungstext

Im Feld für die Einwilligung zur Datenverwendung:

> Ich verarbeite die hier eingegebenen Daten, um den Termin zu vereinbaren und durchzuführen.
> Einzelheiten zu Zweck, Rechtsgrundlage und Speicherdauer stehen in der Datenschutzerklärung
> unter https://dynamicspro.de/datenschutz.html

Der Text greift auf Abschnitt 6 der Datenschutzerklärung zurück. Beide gehören zusammen
gegengelesen, der Abschnitt ist ein Entwurf und kein geprüfter Rechtstext.

## Stand der Einrichtung, geprüft am 20.09.2026

Gesetzt: Adresse, Geschäftsname DynamicsPro, Dienst „Erstgespräch Health Check" mit der
deutschen Beschreibung, 30 Minuten, ohne Microsoft-Konto buchbar, Verfügbarkeit eingegrenzt,
Oberfläche auf Deutsch, Adressfeld aus dem Formular entfernt, Anschrift und Telefon stehen
im Seitenfuß.

Offen:

| Befund auf der Seite | Was fehlt | Wo |
| --- | --- | --- |
| „Alle Zeiten sind in (UTC) Koordinierte Weltzeit" | Zeitzone auf Berlin. Danach Geschäftszeiten erneut prüfen | Unternehmensinformationen |
| Uhrzeiten als 11:00 AM bis 2:30 PM, Woche beginnt sonntags („S M D M D F S") | Region auf Deutschland. Die Sprache steht schon auf Deutsch, die Region noch nicht. Sie steuert 24-Stunden-Format und Wochenbeginn | Buchungsseite, neben der Sprache |
| „MITARBEITER AUSWÄHLEN (OPTIONAL)", „Jeder" | zweiter Schalter für die Auswahl des Dienstleisters | Buchungsseite |
| „Die Richtlinien und Methoden von DynamicsPro gelten für die Verwendung Ihrer Daten." | eigener Einwilligungstext. Das ist der übersetzte Microsoft-Standardsatz, er verlinkt die Datenschutzerklärung nicht | Buchungsseite, Kundendatennutzung |

Zwei Kleinigkeiten nebenbei:

- Das Freitextfeld für das Anliegen ist mit dem Adressfeld zusammen verschwunden. Es war als
  freiwilliges Feld vorgesehen, damit vor dem Gespräch klar ist, worum es geht. Wieder
  einschalten oder bewusst weglassen.
- Der Titel im Browser-Tab lautet „Bookings – – Outlook" statt des Firmennamens.

## Wo die Einstellungen liegen

Einstieg `https://outlook.office.com/bookings/`, Kalender „DynamicsPro". Die Bezeichnungen
in der Oberfläche ändern sich bei Microsoft gelegentlich, die Zuordnung bleibt:

| Bildschirm | Was dort liegt |
| --- | --- |
| Unternehmensinformationen | Name, Website, Logo, **Zeitzone**, Geschäftszeiten |
| Dienste, Eintrag „Erstgespräch Health Check" | **Beschreibung**, Dauer, Preis, Ort, Puffer, Vorlaufzeit, **Mitarbeiterauswahl**, **Formularfelder** samt Adressfeld |
| Buchungsseite | **Sprache und Region**, Anzeige in Unternehmenszeitzone, Zugriff ohne Microsoft-Konto, **Einwilligungstext**, **Suchmaschinenindizierung** |

Zwei Fallen:

- Die Zeitzone verschiebt die Anzeige der Geschäftszeiten, nicht die Zeiten selbst. Nach dem
  Umstellen von UTC auf Berlin müssen die Fenster erneut geprüft werden.
- Die Mitarbeiterauswahl hat zwei Schalter, einen im Dienst und einen auf der Buchungsseite.
  Erst wenn beide aus sind, verschwindet „SELECT STAFF (OPTIONAL)".

Nach dem Speichern neu veröffentlichen und im privaten Fenster nachsehen, sonst zeigt der
Cache die alte Fassung und man ist als angemeldeter Benutzer unterwegs statt als Interessent.

## Prüfen, wenn die Seite steht

- [ ] Seite im privaten Fenster öffnen, also ohne angemeldetes Microsoft-Konto
- [ ] Buchung bis zum Abschluss durchspielen und die Bestätigungsmail ansehen
- [ ] Sprache durchgehend deutsch, auch in der Mail
- [ ] Zeiten in Berliner Zeit und im 24-Stunden-Format
- [ ] Adresse an den drei Stellen in `health-check/index.html` eintragen
- [ ] `npm run shot` muss grün sein, insbesondere ohne Platzhalter-Befund
