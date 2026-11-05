# Abschlussbericht Session B: Förderthemen-Seiten (Stand 5. November 2026)

Branch: `claude/cloud-b-foerderthemen`. Neu angelegt wurden nur die 11 Ordner unten und diese Datei. Keine bestehende Datei wurde geändert.

## Seiten

| Slug | Titel | Bediente Suchbegriffe |
|---|---|---|
| /foerdermittelberatung/ | Fördermittelberatung für Unternehmen \| Fundament GmbH | Fördermittelberatung, Fördermittelberater, Fördermittel für Unternehmen |
| /foerdermittel-beantragen/ | Fördermittel beantragen: Ablauf und häufige Fehler \| Fundament | Fördermittel beantragen, Förderantrag Ablauf, Fehler beim Förderantrag |
| /foerdermittel-start-ups-gruender/ | Fördermittel für Start-ups und Gründer \| Fundament GmbH | Fördermittel Start-up, Fördermittel Gründung, Förderung Gründer |
| /foerdermittel-mittelstand/ | Fördermittel für den Mittelstand und KMU \| Fundament GmbH | Fördermittel Mittelstand, Fördermittel KMU |
| /foerderung-innovation-digitalisierung/ | Förderung für Innovation und Digitalisierung \| Fundament | Förderung Innovation, Förderung Digitalisierung, Entwicklung neuer Produkte fördern, Software-Entwicklung Förderung |
| /foerderung-investition/ | Investitionsförderung für Unternehmen \| Fundament GmbH | Investitionsförderung, Förderdarlehen, Zuschuss Investition |
| /foerdermittel-eu-programme/ | EU-Förderprogramme für Unternehmen \| Fundament GmbH | EU-Förderprogramme, EU-Förderung Unternehmen |
| /foerdermittelberatung-erfolgshonorar/ | Fördermittelberatung auf Erfolgsbasis \| Fundament GmbH | Fördermittelberatung Erfolgshonorar, Fördermittelberatung ohne Vorkasse, Fördermittelberatung ohne Risiko |
| /forschungszulage-voraussetzungen/ | Forschungszulage Voraussetzungen: Wer hat Anspruch? \| Fundament | Forschungszulage Voraussetzungen, Forschungszulage Anspruch |
| /forschungszulage-kmu/ | Forschungszulage für KMU: Satz, Grenzen, Ablauf \| Fundament | Forschungszulage KMU, Forschungszulage 35 Prozent |
| /bsfz-bescheinigung/ | BSFZ-Bescheinigung: Was sie ist und wie sie läuft \| Fundament | BSFZ-Bescheinigung, Bescheinigungsstelle Forschungszulage |

Aufbau jeder Seite: Hero mit Termin-Button und Link zum Förder-Check, Fließtext mit Termin-Kasten in der Mitte, Ablauf in 4 Schritten, Kosten als Prinzip (Erfolgshonorar, keine Zahlen), Aufwand für das Team, Weiterführend-Karten, FAQ, Abschluss-Band mit Termin-Button, gruppierter Block "Mehr erfahren" (Klasse `footer-links`, eigenes `<style>` je Seite) vor dem Footer. JSON-LD: WebSite, ProfessionalService, Person, BreadcrumbList, WebPage, Service, FAQPage. `style.css` unverändert.

## Testergebnis (vor dem PR)

- (a) JSON-LD: pro Seite ein Block, alle Knoten parsen fehlerfrei: bestanden.
- (b) genau ein h1: bestanden (11/11).
- (c) Wortzahl: Fließtext (Artikel) 590-624 Wörter, gesamter Hauptbereich inkl. Hero, FAQ und Abschluss-Band 756-842 Wörter. Beide Zählweisen liegen im Bereich 600-900.
- (d) interne Links: alle Ziele vorhanden, außer den Zielen der Sessions A/C im Block "Mehr erfahren" (/ueber-fundament/, /foerdermittel-software-it/, /foerdermittel-lebensmittel/, /foerdermittel-handwerk-bau/, /foerdermittelberatung-muenchen/, /foerdermittelberatung-oberbayern/, /foerdermittelberatung-deutschland/). Sie müssen nach dem Zusammenführen existieren. Meine 11 Seiten verlinken untereinander vollständig.
- (e) FAQ im JSON-LD gleich FAQ im HTML (Wortlaut identisch): bestanden.
- (f) Headless Chrome (Playwright), 360, 390 und 1280 px: kein horizontales Scrollen, keine Konsolenfehler (nach Korrektur der Tabelle auf /forschungszulage-kmu/).
- Zusätzlich: Titel 53-63 Zeichen, Meta-Description 133-158 Zeichen, Canonical korrekt, Calendly-Link und Button "Kostenloses Erstgespräch buchen" je 3-mal, keine externen Ressourcen, kein "Findways", kein "nicht förderfähig" im Sichtbereich.

## Hinweise für das Zusammenführen

- Der Block "Mehr erfahren" ist in jede Seite eingebettet (Session A legt `docs/footer-links.html` an). Bei Umstellung auf einen gemeinsamen Block kann er ersetzt werden.
- Der Header-Button der Vorlage heißt weiter "15-Minuten-Gespräch buchen" (wie in den Bestandsseiten), die Seiten-Buttons "Kostenloses Erstgespräch buchen".
- sitemap.xml und llms.txt (Session A) müssen die 11 neuen Slugs aufnehmen.
- Die Bestandsseite /forschungszulage-erfolgshonorar/ und die Startseite wurden nicht geändert. Die neue Seite verlinkt dorthin, der Rücklink von der Bestandsseite fehlt (keine Änderung bestehender Dateien erlaubt) und sollte beim Zusammenführen ergänzt werden.

## BITTE PRÜFEN

1. KMU-Schwellen auf /forschungszulage-kmu/ ("unterhalb von 250 Mitarbeitenden bzw. 50 Mio. € Umsatz und 43 Mio. € Bilanzsumme"): Zahlen stammen von /forschungszulage/. Der Satz "Verflechtungen mit anderen Unternehmen können die Einordnung beeinflussen" ist eine allgemeine Aussage nach AGVO und steht nicht auf der Website.
2. "KMU können eine Erhöhung um 10 Prozentpunkte beantragen" (aus /wissen/forschungszulage-2026/) so übernommen.
3. Rechenbeispiel (320.000 / 64.000 / 384.000 / 134.400 €) und "fünf bis acht Stunden je Antragsjahr" sind von /forschungszulage/ übernommen.
4. Frist 2022 endet 31.12.2026 (/forschungszulage-voraussetzungen/): aus /wissen/forschungszulage-rueckwirkend/, Stand dort 19.10.2026.
5. BSFZ-Angaben (Entscheidung spätestens drei Monate, Antrag vor/während/nach Vorhaben, Widerspruch binnen eines Monats elektronisch, Gebührenhinweis § 6 Abs. 5 FZulG) aus /wissen/*.
6. Allgemeine Aussagen ohne Quelle auf der Website: "Bei vielen Programmen gilt schon die verbindliche Bestellung oder der Vertragsabschluss als Vorhabensbeginn" und "Angebot einholen ist meist unkritisch" (/foerderung-investition/); "EU-Mittel fließen teils über Bund und Länder", "Projekte mit mehreren Beteiligten, auch aus verschiedenen Ländern", "häufig Eigenanteil", "Fristen meist nur in festgelegten Zeiträumen" (/foerdermittel-eu-programme/); Förderdarlehen "in der Regel über die Hausbank" und "KfW oder Landesförderbanken" stehen auf /foerdermittel/, sind auf der Investitionsseite verallgemeinert.
7. Überschrift "Fördermittelberatung ohne Risiko?" auf /foerdermittelberatung-erfolgshonorar/: Suchbegriff bedient, im Text klar eingeschränkt (kein Kostenrisiko für die Beratung, keine Bewilligungsgarantie). Wettbewerbsrechtlich ggf. gegenlesen.
8. Das Erfolgshonorar-Prinzip ("Honorar entsteht erst, wenn eine Förderung zustande kommt") entspricht der Startseite. Bitte bestätigen, dass es für jede Programmart (z. B. Förderdarlehen über die Hausbank, EU-Anträge) so vereinbart wird. Zahlen sind bewusst nicht genannt.
9. ZIM-Antragsstopp (seit Juli 2026, Wiederaufnahme 2027 angestrebt, nicht zugesagt) steht auf /foerderung-innovation-digitalisierung/ wie auf /foerdermittel/. Bei geändertem Stand anpassen.
10. "Über 20 Förderprojekte" auf /foerdermittelberatung/ nur als persönliche Berufserfahrung des Gründers, Formulierung wie in /wissen/*.
11. Erfolgshonorar-Seite: "Das Risiko liegt überwiegend beim Berater" entspricht /forschungszulage-erfolgshonorar/; "Besonders junge Unternehmen und kleine Teams profitieren davon" ist eine Wertung, ggf. streichen.
12. Start-up-Seite: "Übersteigt die Zulage die Steuer, wird der Überschuss ausgezahlt" (aus /wissen/forschungszulage-2026/) mit dem Hinweis, dass das für Liquidität interessant sein kann; Einzelfall betont.
