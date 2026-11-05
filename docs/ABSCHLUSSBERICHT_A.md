# Abschlussbericht Session A: Technik, Marke, Conversion

Stand: 5. November 2026. Branch `claude/cloud-a-technik-marke-conversion`, Pull Request gegen `main`. Nichts wurde direkt auf `main` geändert.

## Wichtig vor dem Merge

- **Merge-Reihenfolge:** Erst die Pull Requests von Session B (Förderthemen) und Session C (Branchen/Regionen) mergen, dann diesen. Sitemap, Footer-Linkblock, Navigation und Startseite verlinken die 17 Seiten von B und C bereits. Solange diese Seiten nicht live sind, laufen diese Links ins Leere (404). Das Prüfskript führt diese Links als erwartbar auf.
- Danach: `python docs/tools/seo-check.py --write` erneut laufen lassen (Ziel: keine Fehler, keine "geplanten" Seiten mehr), dann IndexNow melden (`docs/indexnow.md`).

## Was geändert wurde

1. **Startseite (`index.html`):** Neue Positionierung "Fördermittelberatung für Unternehmen, Start-ups und Mittelstand" in Titel, Meta-Description, Open Graph, genau einer H1 und Hero. Neuer Abschnitt "Förderthemen" mit Verlinkung auf alle Förderthemen-Seiten (B). Forschungszulage bleibt ein eigener Baustein, ist aber nicht mehr der alleinige Schwerpunkt. Ablauf jetzt in vier Schritten (vorher fünf), neuer Abschnitt "Was kostet es, und was bedeutet es für Ihr Team?" (Erfolgshonorar-Prinzip ohne Zahlen, Aufwand wie bereits auf der Seite angegeben), drei neue häufige Fragen (HTML und JSON-LD übereinstimmend), Kontaktformular mit zusätzlichen Themen, Branchen- und Regionen-Links.
2. **Conversion:** Termin-Button (Calendly, derselbe Link wie bisher) oben (Header und Hero), in der Mitte (`.mid-cta`) und am Ende (`.end-cta`) auf allen Seiten. Beschriftung vereinheitlicht auf "Kostenloses Erstgespräch (buchen)". Mobil bleibt die feste Schnellkontakt-Leiste.
3. **Förder-Check (`foerdercheck/`):** Allgemeinere Fragen (Vorhaben: Entwicklung, Digitalisierung, Investition, Gründung, offen; Phase; Größe; Sitz; bei Entwicklung die Kriterien der Forschungszulage; bei Investition das Volumen). Fünf bis sieben Fragen je nach Pfad. Neutrale Einschätzungen ("Gute Anhaltspunkte", "Möglich", "Prüfung im Gespräch"), niemand wird als "nicht förderfähig" bezeichnet. Ende immer mit Termin-Button, Mail-Fallback und Telefon; ohne JavaScript erscheint ein Hinweis mit Termin-Link, E-Mail und Telefon. Bedienung per Tastatur, Fieldset/Legend, Fokus auf der Frage bzw. dem Ergebnis, `aria-live`-Bereich. Getestet im Browser mit sechs Antwortkombinationen (Entwicklung mit/ohne Unsicherheit, Investition, Start-up in Gründung, Digitalisierung mit Standort im Ausland, unklares Vorhaben).
4. **Marke:** Organisation und Website-JSON-LD auf allen Seiten mit `alternateName` ["Fundament Group", "Fundament GmbH", "Fundamentgroup", "Fundament Fördermittel"]; `sameAs` nur mit dem bereits vorhandenen LinkedIn-Link. Neue Seite `ueber-fundament/` (rund 800 Wörter, FAQ mit passendem FAQPage-JSON-LD, BreadcrumbList, AboutPage, Termin-Buttons oben/Mitte/Ende). Nur die Geschäftsadresse Am Kirchberg 16a, 82541 Münsing. Kennzahl "über zwanzig Förderprojekte" ausdrücklich als persönliche Berufserfahrung des Gründers. Gründerseite an die neue Positionierung angepasst. Neues Vorschaubild `og-image.png` (neue Positionierung), Alt-Texte angepasst.
5. **Technik-SEO:** Prüfskript `docs/tools/seo-check.py`, Bericht `docs/seo-check.md` (0 Fehler). Footer-Linkblock (`.footer-links`, mobil einspaltig) in allen Seiten und als Vorlage in `docs/footer-links.html`; Terminbausteine als Vorlage in `docs/cta-snippets.html`. Sitemap mit 38 URLs (alle vereinbarten Slugs, `lastmod` 2026-11-05). `robots.txt` um weitere Crawler ergänzt (Applebot, Bingbot, Amazonbot, DuckAssistBot), Sitemap-Verweis vorhanden. Keine externen Ressourcen außer den normalen Links (Calendly, LinkedIn, in Wissensartikeln Gesetze-im-Internet und BSFZ). Mobilansicht bei 360, 390, 768 und 1280 px geprüft: kein horizontales Scrollen; Kopfzeile bei 1021 bis 1230 px angepasst (Platz für die längeren Navigationspunkte).
6. **llms.txt:** Neu gefasst: Wer ist Fundament, Angebot, Zielgruppen, Erfolgshonorar-Prinzip ohne Zahlen, Ort, Kontakt, alle Seiten inklusive der vereinbarten Slugs, Hinweise für Zusammenfassungen (keine Garantie, ZIM-Stopp, Kennzahlen des Gründers nur persönlich).
7. **Domain-Weiterleitung:** `docs/dns-weiterleitung.md` (www per CNAME, zweite Domain per 301 beim Anbieter, Prüfung mit `curl -I`, Mail-Einträge nie anfassen).
8. **IndexNow:** `docs/indexnow.md` (Befehl und Python-Skript, erst nach dem Merge ausführen).

## Welche Seite bedient welche Suchbegriffe

| Seite | Suchbegriffe |
|---|---|
| `/` | Fördermittelberatung, Fördermittelberatung für Unternehmen, Fördermittelberatung Start-ups, Fördermittel Mittelstand, Fundament GmbH, Fundament Group, Fundament Fördermittel, Fördermittelberater München |
| `/ueber-fundament/` | Fundament GmbH, Fundament Group, fundamentgroup, Fördermittelberatung Münsing, wer ist Fundament |
| `/foerdercheck/` | Förder-Check, Fördermittel Check, welche Förderung passt, Fördermittel Selbsttest |
| `/franz-josef-kaiser/` | Franz-Josef Kaiser Fördermittel, Geschäftsführer Fundament GmbH |
| `/404.html` | kein Suchbegriff (noindex), leitet Besucher weiter |
| Footer-Block, Navigation | interne Verlinkung auf alle Förderthemen-, Branchen- und Regionenseiten (Anker-Texte wie "Fördermittelberatung", "Mittelstand", "Start-ups und Gründer", "München") |

Die Förderthemen-, Branchen- und Regionenseiten selbst (Sessions B und C) bedienen die jeweiligen Themen- und Ortssuchen.

## BITTE PRÜFEN

- **LinkedIn-Seite:** `https://www.linkedin.com/company/fundament-gmbh/` stand schon im Repo und ist in `sameAs`. Bitte bestätigen, dass die Seite existiert und diese Adresse stimmt. Weitere Profile (Google-Unternehmensprofil, Bing, XING) sind nicht eingetragen, weil im Repo keine bekannt sind.
- **Namensvarianten:** "Fundamentgroup" und "Fundament Fördermittel" stehen als alternative Namen im JSON-LD (so vorgegeben). "Fundament Fördermittel" ist keine rechtliche Firmierung; bitte bestätigen, dass sie so geführt werden soll.
- **Hinweis zum Vorhabenbeginn im Förder-Check:** "Bei Projektförderung muss der Antrag in der Regel vor Projektbeginn gestellt werden" steht schon so auf `/foerdermittel/`; im Check wird er auch bei Investitions-, Digitalisierungs- und Gründungsvorhaben gezeigt. Bitte fachlich bestätigen.
- **Hinweis zum Standort im Förder-Check:** "Viele Programme setzen einen Sitz oder eine Betriebsstätte in Deutschland voraus" ist allgemein formuliert; bitte prüfen.
- **Fristhinweise im Förder-Check** (2022 bis 31.12.2026, Übergangsregel 2020/2021) und die Überschlagsbeträge (Fördersatz 35 bzw. 25 %, Pauschale 20 %) sind unverändert aus dem früheren Check übernommen; bitte mit dem Rechtsstand prüfen. Nach 31.12.2026 blendet der Check die Wochenangabe selbst aus; den Fristtext danach überarbeiten.
- **Vier statt fünf Schritte:** Startseite und `/ueber-fundament/` zeigen vier Schritte; auf den Seiten `/foerdermittel/`, `/forschungszulage-*` und den Branchenseiten stehen noch fünf Schritte (Erstgespräch, Analyse, Aufbereitung, Einreichung und Bescheid, Auszahlung und Folgejahre). Inhaltlich identisch (Schritt 4 fasst 4 und 5 zusammen); bei Gelegenheit angleichen.
- **"Nicht förderfähig" auf bestehenden Seiten:** Auf einigen bestehenden Seiten (z. B. Branchenseiten, Wissensartikel, Fußnote Startseite) steht weiterhin "nicht förderfähig" für Tätigkeiten (Konstruktion nach Norm, Routine), nicht für Kunden. Auf der Startseite und im Förder-Check wurde Kunden gegenüber neutral formuliert. Bitte prüfen, ob die übrigen Stellen ebenfalls angepasst werden sollen.
- **Bestehende Aussagen auf der Startseite** wie "Wann wir nicht der Richtige sind" (u. a. Hinweis auf Investoren und Beteiligungskapital) und "wir lehnen manche Vorhaben ab" wurden nicht ausgebaut und nicht gelöscht.
- **Gründer-Kennzahlen:** Die Startseite nennt weiterhin ">2 Mio. € bewilligtes Fördervolumen" und "20+ Projekte" im Abschnitt "Erfahrung des Gründers" (mit Hinweis, dass es persönliche Berufserfahrung ist). Auf `/ueber-fundament/` und `/franz-josef-kaiser/` steht nur "über zwanzig Förderprojekte". Bitte entscheiden, ob die Zahl 2 Mio. so bleiben soll.
- **Header-Navigation:** "Fördermittel" (`/foerdermittel/`) und "Gründer" wurden aus der Kopfzeile genommen und durch "Fördermittelberatung" und "Über uns" ersetzt (Platzgründe). `/foerdermittel/` bleibt im Footer, `/franz-josef-kaiser/` im Footer-Block "Fundament". Bitte bestätigen.
- **Vorschaubild:** `og-image.png` wurde neu erzeugt (Georgia/Segoe UI statt der Hausschriften). Sozialnetzwerke cachen alte Vorschaubilder; ggf. mit dem Facebook-/LinkedIn-Debugger neu einlesen lassen.
- **Domain-Anleitung:** siehe Abschnitt "Was ich nicht sicher weiß" in `docs/dns-weiterleitung.md` (Anbieter der zweiten Domain, vorhandener www-Eintrag, Zertifikat).
- **Pull Request:** Der PR zu diesem Branch ist #3 (Titel "A: Startseite, Förder-Check, Über Fundament, Navigation, Sitemap, llms.txt"); die Kurzfassung steht als Kommentar darunter.

## Schritte des Inhabers außerhalb des Codes (nach Wirkung sortiert)

1. **Google Search Console:** Die Website ist bereits verifiziert und die Sitemap eingereicht. Nach dem Merge: unter "Sitemaps" prüfen, dass `sitemap.xml` neu gelesen wurde und 38 URLs meldet. Dann in der "URL-Prüfung" die Startseite und die wichtigsten Seiten (`/foerdermittelberatung/`, `/foerdermittel-start-ups-gruender/`, `/foerdermittel-mittelstand/`, `/forschungszulage/`, `/ueber-fundament/`, `/foerdercheck/`) einzeln aufrufen und "Indexierung beantragen" wählen (täglich nur eine begrenzte Anzahl möglich). Nach einigen Tagen unter "Seiten" kontrollieren, ob Fehler (z. B. 404 bei den Seiten von B und C) auftauchen.
2. **Google-Unternehmensprofil** anlegen (Dienstleister mit Standort/Einzugsgebiet, Geschäftsadresse Am Kirchberg 16a, 82541 Münsing; Telefon, Website `https://fundamentgroup.de/`, Kategorie Unternehmensberatung o. ä.). Verifizierung per Postkarte, Anruf oder Video. BITTE PRÜFEN: ob die Adresse im Profil öffentlich sichtbar sein soll (sonst "Dienstleistungsgebiet" ohne Adressanzeige wählen).
3. **Bing Webmaster Tools** (Sitemap einreichen) und **IndexNow** melden (`docs/indexnow.md`, erst nach dem Merge).
4. **LinkedIn-Unternehmensseite** mit Link auf `https://fundamentgroup.de/`, Kurzbeschreibung aus der Meta-Description, Spezialgebiete (Fördermittelberatung, Forschungszulage, Förderung für Start-ups); Gründerprofil mit Link auf die Seite verknüpfen. Keine Privatadresse eintragen.
5. **Verlinkungen:** IHK, Verbände (z. B. Gründer- und Mittelstandsverbände), Partner (Steuerberater, Kanzleien), Branchenverzeichnisse und Gründerzentren um einen Link auf `https://fundamentgroup.de/` bitten. Immer die Hauptadresse ohne www verwenden.
6. **Domain-Weiterleitungen** laut `docs/dns-weiterleitung.md` einrichten (www und fundament-group.de).
