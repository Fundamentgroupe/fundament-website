# Abschlussbericht Session C: Branchen- und Regionalseiten

Stand: 5. November 2026. Branch `claude/cloud-c-branchen-regionen`. Geändert wurden keine bestehenden Dateien, nur sechs neue Ordner mit `index.html` und dieser Bericht.

## Seiten

| Slug | Titel | Bediente Suchbegriffe |
|---|---|---|
| /foerdermittel-software-it/ | Fördermittel für Software und IT-Unternehmen \| Fundament | Förderung Softwareentwicklung, Fördermittel IT-Unternehmen, Förderung KI-Projekte, Digitalisierung Förderung, Forschungszulage Software |
| /foerdermittel-lebensmittel/ | Fördermittel für Lebensmittelhersteller \| Fundament GmbH | Förderung Lebensmittelhersteller, Fördermittel Lebensmittelindustrie, Förderung Produktentwicklung Lebensmittel, Förderung Energieeffizienz Lebensmittelproduktion |
| /foerdermittel-handwerk-bau/ | Fördermittel für Handwerk und Bau \| Fundament GmbH | Fördermittel Handwerk, Förderung Handwerksbetriebe, Förderung Bauunternehmen, Förderung Energieeffizienz Handwerk, Digitalisierung Handwerk Förderung |
| /foerdermittelberatung-muenchen/ | Fördermittelberatung München für Unternehmen \| Fundament | Fördermittelberatung München, Fördermittel München, Förderberatung München Start-ups, Förderung Unternehmen München |
| /foerdermittelberatung-oberbayern/ | Fördermittelberatung Oberbayern für Unternehmen \| Fundament | Fördermittelberatung Oberbayern, Fördermittel Oberbayern, Förderung Mittelstand Oberbayern, Förderung Handwerk Oberbayern |
| /foerdermittelberatung-deutschland/ | Fördermittelberatung Deutschland bundesweit \| Fundament | Fördermittelberatung bundesweit, Fördermittelberatung online, Fördermittelberater Deutschland, Fördermittelberatung per Videocall |

Jede Seite: genau ein h1, drei Calendly-Buttons (Hero, Mitte, Ende) mit "Kostenloses Erstgespräch / Termin buchen", Link zum Förder-Check, Ablauf in vier Schritten, "Was kostet es?" (nur Erfolgshonorar-Prinzip, ohne Zahlen), "Aufwand für Ihr Team", vier FAQ (im JSON-LD identisch), Linkblock "Mehr erfahren" (`footer-links`, vier Gruppen, einspaltig ab 640 px) vor dem Footer. JSON-LD: WebSite, ProfessionalService, Person (wie bestehend), BreadcrumbList, WebPage, Service, FAQPage. Zusatzstyling nur per `<style>` im head, `style.css` unverändert.

## Testergebnis (Skript lokal, nicht im Repo)

- JSON-LD: alle Blöcke parsen fehlerfrei, 7 Typen je Seite: OK
- genau ein h1 je Seite: OK
- Wortzahl (sichtbarer Text in `<main>`): 641 bis 751; gesamter Body 721 bis 831. Beides liegt in 600 bis 900: OK
- Titel 50 bis 59 Zeichen, Meta 143 bis 155 Zeichen: OK
- interne Links: alle auflösbar, außer den Zielen von Session A/B (9 Stück: /foerdermittelberatung/, /foerdermittel-beantragen/, /foerdermittel-start-ups-gruender/, /foerdermittel-mittelstand/, /foerderung-innovation-digitalisierung/, /foerderung-investition/, /foerdermittel-eu-programme/, /foerdermittelberatung-erfolgshonorar/, /ueber-fundament/). Diese Seiten müssen nach dem Zusammenführen existieren, sonst 404.
- FAQ im JSON-LD gleich FAQ im HTML (Text): OK, 4 je Seite
- 360 und 390 px (und 1280 px), headless Chrome über Playwright: kein horizontales Scrollen auf allen sechs Seiten: OK
- keine externen Ressourcen außer Calendly- und LinkedIn-Link (wie bestehend), keine Google Fonts

## BITTE PRÜFEN

1. Button-Text: wörtlich "Kostenloses Erstgespräch / Termin buchen" wie beauftragt; Header und Mobil-Leiste behalten den bestehenden Text "15-Minuten-Gespräch buchen". Ggf. vereinheitlichen.
2. Forschungszulage-Sätze (25 %, KMU 35 %, 12 Mio. €, 70 % Auftragsforschung, 20 % Pauschale für Vorhaben nach dem 31.12.2025, Rückwirkung bis vier Jahre) stammen von den bestehenden Seiten. Auf den Branchenseiten Software/Lebensmittel/Handwerk wiederholt, nicht neu geprüft.
3. Allgemeine Aussage "Bei vielen Zuschussprogrammen muss der Antrag vor Bestellung/Beginn gestellt sein" (Lebensmittel, Handwerk): allgemein bekannt, aber nicht auf der Website belegt. Bitte bestätigen oder streichen.
4. "Landesangebote etwa über die LfA Förderbank Bayern und die Bayerische Forschungsstiftung" (München, Oberbayern) übernommen von /foerdermittelberatung-bayern/.
5. Oberbayern: "Münsing liegt im Landkreis Bad Tölz-Wolfratshausen am Starnberger See" sowie "Wirtschaftsförderungen und Kammern vor Ort informieren über regionale Angebote" sind allgemeine Aussagen; bitte kurz bestätigen.
6. München: "München ist ein Standort mit vielen Start-ups, Technologieunternehmen und Mittelständlern" ist eine allgemeine Aussage ohne Zahl.
7. ZIM-Hinweis (Antragsstopp seit Juli 2026) steht auf Software-IT und Deutschland, Wortlaut wie auf der Bayern-Seite.
8. Praxisfälle sind typisierte Beispiele ohne Namen und Zahlen; die Eignung im Einzelfall wird jeweils ausdrücklich "im Gespräch" geprüft. Bitte fachlich gegenlesen, besonders Lebensmittel (Rezeptur, Verfahren) und Handwerk/Bau (Bauteil, Vorfertigung).
9. Footer der Seiten ist 1:1 die Vorlage der Bayern-Seite; Session A sollte die neuen Seiten in Sitemap, llms.txt und ggf. globale Footer/Navigation aufnehmen.
10. Hinweis (Datum): "Stand der Angaben" und dateModified stehen auf 5. November 2026.
