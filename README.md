# fundament-website

Website der Fundament GmbH (fundamentgroup.de): Fördermittelberatung für innovative
Unternehmen, Schwerpunkt Forschungszulage.

Statische Seiten. Kein Build, kein Server, keine Datenbank, keine Abhängigkeiten.
Ausgeliefert über GitHub Pages (Branch `main`, Wurzelverzeichnis, eigene Domain über `CNAME`).

## Aufbau

```
index.html                  Startseite (Leistungen, Branchen, Förderrechner, Ablauf, Fragen, Kontakt,
                            Impressum, Datenschutz). Enthält das Porträtfoto als data-URI.
forschungszulage/index.html Unterseite "Forschungszulage beantragen"
foerdermittel/index.html    Unterseite "Fördermittel im Überblick"
404.html                    Fehlerseite (GitHub Pages liefert sie automatisch aus)
style.css                   Gemeinsames Stylesheet aller Seiten (inkl. @font-face)
fonts/                      Selbst gehostete Schriften (woff2)
og-image.png                Vorschaubild für Links (1200 x 630)
favicon*.png/svg, apple-touch-icon.png
robots.txt, sitemap.xml, llms.txt
CNAME
```

Kopfzeile und Fußzeile stehen in jeder HTML-Datei. Wer sie ändert, ändert alle vier Dateien.
Neue Seiten: Datei als `<ordner>/index.html` anlegen, in `sitemap.xml` eintragen und im Kopf
`<link rel="stylesheet" href="/style.css">` einbinden. Alle Pfade zu Dateien beginnen mit `/`.

## Schriften

Die Seite lädt **keine** Google Fonts zur Laufzeit (in Deutschland abmahnfähig) und ruft im
Browser des Besuchers keine externen Ressourcen ab. Instrument Serif und IBM Plex Sans (beide
SIL Open Font License) liegen als woff2 in `fonts/` und sind im Repo versioniert, weil bei
GitHub Pages das Repo selbst die Auslieferung ist.

## Animation und JavaScript

Inhalte erscheinen beim Scrollen per CSS-Übergang. Das greift nur, wenn JavaScript läuft
(`<html class="js">`); ohne JavaScript sind alle Inhalte sofort sichtbar.

## Termin buchen

Alle "15-Minuten-Gespräch"-Knöpfe verlinken auf den Calendly-Termin (externer Link, nichts wird
eingebettet). Der Hinweis dazu steht in der Datenschutzerklärung auf der Startseite.

## Suchmaschinen und KI

- Titel, Beschreibung, Open-Graph- und Twitter-Karten je Seite
- Strukturierte Daten (JSON-LD): Organisation, Person, Website, Brotkrumen, häufige Fragen.
  Die Fragen im JSON-LD müssen mit den sichtbaren Fragen auf der Seite übereinstimmen.
- `robots.txt` erlaubt Suchmaschinen und KI-Crawler ausdrücklich, `llms.txt` fasst die Seite
  für KI-Assistenten zusammen
- Search Console: Eigentümer ist nur das Konto der Fundament GmbH (Bestätigung über DNS)

## Inhaltliche Leitplanken

Keine Kunden-, Firmen- oder Personennamen. Keine Erfolgsgarantien. Keine Aussagen zu einer
Versicherung, solange keine besteht. Keine Steuer- oder Rechtsberatung formulieren.
