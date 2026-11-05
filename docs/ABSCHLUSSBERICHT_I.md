# Abschlussbericht Teil I: Ratgeber (Stand 05.11.2026)

- 14 Praxisratgeber unter `/ratgeber/<slug>/` plus Übersicht `/ratgeber/` (CollectionPage/ItemList).
- Je Ratgeber: Titel 50-60 Zeichen, Meta 140-155 Zeichen, Antwort in den ersten zwei Sätzen, Sprungmarken, typisiertes Beispiel ohne Zahlen, 3 FAQ (sichtbar = FAQPage-JSON-LD), Stand-Hinweis, drei Calendly-Buttons, Block „Mehr erfahren".
- Wortzahl 710-864 je Ratgeber (inkl. Navigations- und Linkblöcke).
- Nur Bestandsfakten (Forschungszulage 35 %/25 %, Vierjahresfrist, 70 % Auftragsforschung, ZIM-Antragsstopp nicht erwähnt); Einstellung/Nachhaltigkeit nur Prinzipien.
- Keine bestehenden Dateien geändert. Wiring: `docs/wiring_I.json`.
- Linkziele aus anderen PRs (noch nicht vorhanden): /foerdermittelberatung/, /foerdermittel-beantragen/, /foerdermittel-mittelstand/, /foerderung-innovation-digitalisierung/, /foerdermittelberatung-erfolgshonorar/, /ueber-fundament/.
- Tests: JSON-LD parsebar, ein h1, Wortzahl, Titel/Meta-Länge, FAQ = JSON-LD, verbotene Wörter, 360/390 px ohne horizontales Scrollen.
- Hinweis: Die unabhängige Prüfung durch einen Unteragenten war in diesem Lauf nicht möglich; stattdessen automatisierte Regeltests und Selbstprüfung.
