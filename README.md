# fundament-website

Website der Fundament GmbH. Förderkapital, Fremdkapital, Beteiligungskapital.

Eine statische Seite. Kein Build, kein Server, keine Datenbank, keine Abhängigkeiten.

---

## Aufbau

```
index.html          Die komplette Seite: HTML, CSS, Browser-JavaScript und das
                    Porträtfoto (als data-URI eingebettet). ~190 KB.
fonts/              Ablage für die selbst gehosteten Schriften, siehe unten.
.gitignore
```

Es gibt bewusst keine `package.json` und keine `package-lock.json` — das Projekt
nutzt kein npm und keine Build-Kette. Kommt später ein Build-Schritt dazu, gehört
die Lock-Datei ins Repo; die `.gitignore` ist darauf schon vorbereitet.

## Deployment

Inhalt des Repositories in den Dokumentenstamm des Hosters kopieren, fertig.

Getestet gedacht für Hetzner Webhosting (`public_html`). Funktioniert genauso auf
Netlify, Cloudflare Pages, GitHub Pages, Vercel, IONOS, Strato oder jedem
beliebigen Webspace-Paket. Ein VPS ist nicht nötig.

## Schriften

Die Seite lädt **keine** Google Fonts zur Laufzeit — das ist in Deutschland
abmahnfähig. Sie ruft im Browser des Besuchers keine externen Ressourcen ab.
Die vier Dateien in `fonts/` sind seit 2026-10-02 fest im Repo committet:

```
fonts/instrument-serif-400.woff2
fonts/ibm-plex-sans-400.woff2
fonts/ibm-plex-sans-500.woff2
fonts/ibm-plex-sans-600.woff2
```

Quellen: [Instrument Serif](https://fonts.google.com/specimen/Instrument+Serif)
und [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans), beide unter
SIL Open Font License — einmalig heruntergeladen, nicht zur Laufzeit nachgeladen.

Bei GitHub Pages ist das Repo selbst die Auslieferung, deshalb müssen die
Binärdateien hier versioniert sein (anders als bei klassischem Webspace, wo man
sie separat hochlädt).

## JavaScript

Rund 120 Zeilen, ausschließlich im Browser des Besuchers: Navigation,
Scroll-Einblendungen, Akkordeon, Linienraster im Kopfbereich und der
Förderrechner. Kein Node, kein serverseitiger Code. Ohne JavaScript bleibt die
Seite vollständig lesbar.

## Datenschutz

Kein Tracking, keine Cookies, kein `localStorage`, keine externen Aufrufe.
Deshalb auch kein Cookie-Banner. Das Kontaktformular sendet nichts an einen
Server, sondern setzt die Eingaben lokal zu einer E-Mail zusammen und öffnet das
Mailprogramm des Besuchers.

## Vor dem Live-Gang noch einzusetzen

| Platzhalter | Stellen |
|---|---|
| `kontakt@fundament-kapital.de` | 4 |
| Telefonnummer | derzeit bewusst keine angegeben |
| Handelsregisternummer und USt-IdNr. | Impressum, sobald die Eintragung vorliegt |

Alles per Suchen-und-Ersetzen in `index.html` änderbar.

## Nicht in diesem Repository

Die Geschäftsunterlagen aus dem Projektordner (Wettbewerbsanalyse, Persona-Test,
Entscheidungsprotokoll, `CLAUDE.md`) sind bewusst **nicht** enthalten. Sie
enthalten Bankverbindungen, Mandantennamen und persönliche Daten, die auch in
einem privaten Repository nichts verloren haben.
