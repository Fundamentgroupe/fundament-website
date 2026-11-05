# Abschlussbericht Teil J (Stand 05.11.2026)

Branch: `claude/cloud-j-glossar-faq`. Neue Dateien: `glossar/`, `haeufige-fragen/`, `fundament-auf-einen-blick/`, `docs/wiring_J.json`, dieser Bericht. Bestehende Dateien unverändert.

| Seite | Inhalt | Prüfung |
|---|---|---|
| /glossar/ | 50 Begriffe alphabetisch, Anker-IDs, Buchstabenleiste, DefinedTermSet mit 50 DefinedTerm (= sichtbare Begriffe) | OK |
| /haeufige-fragen/ | 40 Fragen in 6 Gruppen, FAQPage-JSON-LD mit 16 Fragen (alle sichtbar, identischer Wortlaut) | OK |
| /fundament-auf-einen-blick/ | rund 450 Wörter Steckbrief | OK |

Tests (Testskript im Scratchpad): JSON-LD parsebar, ein h1, Titel 50-60 und Meta 140-155 Zeichen, Wortzahl, FAQ-/Begriffs-Abgleich, interne Links und Anker, kein horizontales Scrollen bei 360 und 390 px (Chromium).

Hinweise:
- Linkziele aus anderen PRs (/foerdermittelberatung/, /foerdermittel-beantragen/, /foerdermittel-mittelstand/, /foerderung-innovation-digitalisierung/, /foerdermittelberatung-erfolgshonorar/, /ueber-fundament/, /bsfz-bescheinigung/) existieren auf main noch nicht, bis die PRs gemergt sind.
- Alle Zahlen stammen aus Bestandsseiten (35/25 %, 12 Mio. €, 20 % Pauschale, 70 % Auftragsforschung, vier Jahre, Frist 2022 am 31.12.2026).
- Der unabhängige Prüf-Unteragent konnte im Fork nicht gestartet werden; Selbstprüfung gegen die harten Regeln erfolgte durch die Testskripte und Durchsicht. Empfehlung: kurze Sichtprüfung vor dem Merge.
- Sitemap und Navigation wurden bewusst nicht geändert (siehe wiring_J.json).
