# Abschlussbericht E: 10 neue Branchenseiten (Stand 5. November 2026)

Branch: `claude/cloud-e-branchen2` (Basis: `main`), PR gegen `main`. Es wurden keine bestehenden Dateien geändert, nichts gelöscht.

## Neue Seiten (je `<slug>/index.html`)

| Slug | Titel (Zeichen) | Meta (Zeichen) | Wörter Hauptteil / ganze Seite |
|---|---|---|---|
| /foerdermittel-energie-erneuerbare/ | 52 | 153 | 692 / 749 |
| /foerdermittel-umwelttechnik/ | 56 | 150 | 673 / 730 |
| /foerdermittel-kunststoff-verpackung/ | 54 | 153 | 665 / 722 |
| /foerdermittel-metallverarbeitung/ | 57 | 144 | 663 / 720 |
| /foerdermittel-landwirtschaft-agrartechnik/ | 60 | 155 | 674 / 731 |
| /foerdermittel-logistik-mobilitaet/ | 56 | 141 | 662 / 719 |
| /foerdermittel-elektronik-hardware-startups/ | 50 | 154 | 677 / 734 |
| /foerdermittel-ki-und-datenprojekte/ | 54 | 146 | 694 / 751 |
| /foerdermittel-textil-und-materialien/ | 56 | 142 | 661 / 718 |
| /foerdermittel-bildung-und-weiterbildung/ | 54 | 149 | 667 / 724 |

`/foerdermittel-medizintechnik-und-gesundheit/` wurde nicht angelegt (existiert als `forschungszulage-medizintechnik`).

Aufbau 1:1 von `forschungszulage-maschinenbau/`: head (Canonical, Open Graph, Twitter), JSON-LD-@graph (WebSite, ProfessionalService, Person, BreadcrumbList, WebPage, Service, FAQPage), Header, Hero, Mobile-CTA, Footer, Skript. `style.css` unverändert; Zusatzstyling in einem kleinen `<style>` je Seite (Mid-CTA, Mehr-erfahren-Block, Listen).

Inhalt je Seite: 4 bis 5 Praxisfälle, "Was ... meist nicht gefördert wird", drei Fragen zur ersten Einordnung (branchenspezifisch), Ablauf in 4 Schritten, "Was kostet es?" (nur Erfolgshonorar-Prinzip, keine Zahlen), "Aufwand für Ihr Team", 4 FAQ, Block "Weiterführend" (3 Branchenlinks) und am Ende vor dem Footer der Block "Mehr erfahren" mit den 8 geforderten Links. Calendly-Button "Kostenloses Erstgespräch buchen" im Hero, zweimal im Text (Mitte, Ende), dazu Link zum Förder-Check. Header und Mobile-CTA unverändert aus der Bestandsseite ("15-Minuten-Gespräch buchen").

## Testergebnis (Skript, lokal gegen die Dateien, Chrome headless via Playwright)

- JSON-LD parsebar, alle 7 Typen vorhanden: alle 10 OK
- genau ein h1: alle 10 OK
- Title 50 bis 60 Zeichen, Meta 140 bis 155 Zeichen, Canonical, OG/Twitter: alle OK
- Wortzahl 650 bis 900: Hauptteil 661 bis 694 (die Seite insgesamt mit Navigation und Footer 718 bis 751)
- FAQ-JSON-LD identisch mit sichtbarer FAQ (4 Fragen, wortgleich): alle OK
- Interne Links: alle Ziele vorhanden, außer den sechs Seiten aus anderen PRs (siehe unten); keine externen Ressourcen, keine Google Fonts
- Verbotene Begriffe (Findways, ZIM, "garantiert", "nicht förderfähig" u. a.) nicht gefunden
- 360 px und 390 px: scrollWidth gleich clientWidth, kein horizontales Scrollen, alle 10 Seiten

Links, deren Ziele aus anderen PRs kommen (bis dahin 404): /foerdermittelberatung/, /foerdermittel-mittelstand/, /foerderung-innovation-digitalisierung/, /foerderung-investition/, /foerdermittelberatung-erfolgshonorar/, /ueber-fundament/. Die Links /foerdercheck/, /forschungszulage/ und /wissen/forschungszulage-software/ existieren bereits.

## BITTE PRÜFEN

1. Landwirtschaft: Aussage, Flächen- und Tierprämien seien "ein eigenes Verfahren" und nicht Teil der Beratung (Abgrenzung, nicht auf der Website belegt).
2. Elektronik/Hardware: "Je nach Rechtsform und Vertrag kann auch die eigene Arbeit der Gründer eine Rolle spielen" und "noch kein Umsatz: kann sein". Beides allgemein gehalten; bitte fachlich bestätigen. Zudem ein Satz, dass nicht zu Beteiligungskapital beraten wird (bewusst minimal).
3. Bildung: "rein pädagogische Konzepte, Lehrmaterial und Kursinhalte zählen meist nicht"; bitte gegen die Praxis der Bescheinigungsstelle prüfen. Außerdem die Abgrenzung "Förderung für Teilnehmende gehört nicht zu unserer Beratung".
4. Allgemeine Aussagen zu Investitionsprogrammen ("Antrag in der Regel vor Bestellung/Projektbeginn") stützen sich auf die Seite /foerdermittel/; bei Metallverarbeitung steht "vor der Bestellung" etwas konkreter.
5. Genannte Programme: nur BAFA/EEW (Energie-Seite), sonst keine Programmnamen, keine Sätze, Fristen oder Beträge. Forschungszulage: nur allgemein und "bis zu vier Jahre rückwirkend" (steht auf /foerdermittel/ und Bestandsseiten); sonst keine Zahlen.
6. Die Seite Energie nennt Wärmespeicher und Wasserstoffkomponenten, Logistik Elektromobilität (beides wie auf der Startseite/den Branchenseiten bereits erwähnt).
7. Kein Kundenbezug und keine Referenzen; alle Praxisfälle sind erfundene typische Konstellationen ohne Namen. Bitte kurz bestätigen, dass das so gewollt ist.
8. "Mehr erfahren"-Block ist eine einfache Linkliste (8 Links), kein Vorbild aus Bestandsseiten; Gestaltung bei Bedarf an den Integrations-PR angleichen.

## Offene Folgearbeit (nicht Teil dieses PR)

Eintrag der 10 Slugs in `sitemap.xml`, `llms.txt` und in Branchen-/Footer-Links: Daten in `docs/wiring_E.json`.
