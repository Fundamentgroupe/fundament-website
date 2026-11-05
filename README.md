# fundament-website

Website der Fundament GmbH (Fundament Group, fundamentgroup.de): allgemeine Fördermittelberatung
für Unternehmen, Start-ups und Mittelstand (Forschungszulage, Bundes- und Landesförderung,
Innovation, Digitalisierung, Investitionen, EU-Programme).

Statische Seiten. Kein Build, kein Server, keine Datenbank, keine Abhängigkeiten.
Ausgeliefert über GitHub Pages (Branch `main`, Wurzelverzeichnis, eigene Domain über `CNAME`).

## Aufbau

```
index.html                  Startseite (Positionierung, Förderthemen, Leistungen, Branchen, Förderrechner,
                            Ablauf in vier Schritten, Kosten und Aufwand, Fragen, Kontakt, Impressum, Datenschutz)
<ordner>/index.html         Unterseiten: Förderthemen, Forschungszulage, Branchen, Regionen, Wissen,
                            Förder-Check, Über Fundament, Gründer
404.html                    Fehlerseite (GitHub Pages liefert sie automatisch aus)
style.css                   Gemeinsames Stylesheet aller Seiten (inkl. @font-face)
fonts/                      Selbst gehostete Schriften (woff2)
og-image.png                Vorschaubild für Links (1200 x 630)
favicon*.png/svg, apple-touch-icon.png
robots.txt, sitemap.xml, llms.txt
52c143a254862a7e25c7e86f0bd305e2.txt   IndexNow-Schlüsseldatei
CNAME
docs/                       Anleitungen und Berichte (footer-links.html, cta-snippets.html, seo-check.md,
                            dns-weiterleitung.md, indexnow.md, ABSCHLUSSBERICHT_A.md, tools/seo-check.py)
```

## Kopfzeile, Fußzeile, Termin-Bausteine

Kopfzeile (Navigation) und Fußzeile stehen in jeder HTML-Datei, es gibt kein Build-System.
Wer sie ändert, ändert alle Seiten. Der Footer-Linkblock (Förderthemen, Branchen, Regionen, Fundament)
liegt als Vorlage in `docs/footer-links.html`, die Terminbausteine (Header-Button, Hero, Mitte, Ende)
in `docs/cta-snippets.html`. Die zugehörigen Klassen (`.footer-links`, `.mid-cta`, `.end-cta`) stehen
in `style.css`.

Neue Seiten: Datei als `<ordner>/index.html` anlegen, in `sitemap.xml` und `llms.txt` eintragen, im Kopf
`<link rel="stylesheet" href="/style.css">` einbinden, den Footer-Linkblock einbauen. Alle Pfade zu Dateien
beginnen mit `/`.

## Prüfen vor dem Merge

```
python docs/tools/seo-check.py --write
```

Prüft Titel, Meta-Description, Canonical, Open Graph, genau eine h1, Bilder ohne alt, JSON-LD (parsebar,
FAQ-Fragen stehen sichtbar auf der Seite), interne Links und Anker, externe Ressourcen, Termin-Buttons
(oben, Mitte, Ende), Footer-Linkblock und Sitemap. Ergebnis: `docs/seo-check.md`.

## Schriften

Die Seite lädt **keine** Google Fonts zur Laufzeit (in Deutschland abmahnfähig) und ruft im
Browser des Besuchers keine externen Ressourcen ab. Instrument Serif und IBM Plex Sans (beide
SIL Open Font License) liegen als woff2 in `fonts/` und sind im Repo versioniert, weil bei
GitHub Pages das Repo selbst die Auslieferung ist.

## Animation und JavaScript

Inhalte erscheinen beim Scrollen per CSS-Übergang. Das greift nur, wenn JavaScript läuft
(`<html class="js">`); ohne JavaScript sind alle Inhalte sofort sichtbar.
Der Förder-Check braucht JavaScript; ohne JavaScript zeigt die Seite Terminlink, E-Mail und Telefon.

## Termin buchen

Alle "Kostenloses Erstgespräch"-Knöpfe verlinken auf den Calendly-Termin (externer Link, nichts wird
eingebettet). Der Hinweis dazu steht in der Datenschutzerklärung auf der Startseite.

## Suchmaschinen und KI

- Titel, Beschreibung, Open-Graph- und Twitter-Karten je Seite
- Strukturierte Daten (JSON-LD): Organisation (mit alternativen Namen), Person, Website, Brotkrumen,
  häufige Fragen. Die Fragen im JSON-LD müssen mit den sichtbaren Fragen auf der Seite übereinstimmen.
- `robots.txt` erlaubt Suchmaschinen und KI-Crawler ausdrücklich, `llms.txt` fasst die Seite
  für KI-Assistenten zusammen
- Search Console: Eigentümer ist nur das Konto der Fundament GmbH (Bestätigung über DNS)
- Nach größeren Änderungen: IndexNow-Meldung, siehe `docs/indexnow.md`

## Inhaltliche Leitplanken

Keine Kunden-, Firmen- oder Personennamen. Keine Erfolgsgarantien. Keine Aussagen zu einer
Versicherung, solange keine besteht. Keine Steuer- oder Rechtsberatung formulieren.
Das ZIM-Programm wird wegen des Antragsstopps seit Juli 2026 nicht als verfügbar beworben.
Kennzahlen aus der Berufserfahrung des Gründers erscheinen nur als seine persönliche Berufserfahrung.
