# Anleitung: Domains und Weiterleitungen (Hetzner DNS)

Stand: 5. November 2026. Für den Inhaber, Schritt für Schritt. Es wird nichts im Code geändert.

**Wichtigste Regel: Die Google-Workspace-Mail-Einträge nie anfassen.** In der Zone `fundamentgroup.de` stehen fünf Einträge für E-Mail: die MX-Einträge sowie SPF, DKIM und DMARC (TXT-Einträge). Diese nicht ändern, nicht löschen, nicht "aufräumen". Wenn Sie unsicher sind, ob ein Eintrag dazugehört: unverändert lassen. Vorher einen Screenshot der kompletten Zone machen.

Ziel:

1. `https://fundamentgroup.de/` ist die Hauptadresse (so steht es in `CNAME` im Repo und in allen Canonical-Links).
2. `www.fundamentgroup.de` führt auf die Hauptadresse.
3. `fundament-group.de` (zweite Domain, mit Bindestrich) führt per Weiterleitung auf `https://fundamentgroup.de/`.

## Teil 1: www.fundamentgroup.de auf GitHub Pages leiten

Was am Ende passiert: GitHub Pages leitet `www.fundamentgroup.de` automatisch auf `fundamentgroup.de` um, solange die Hauptadresse (Apex-Domain) als eigene Domain im Repo hinterlegt ist (Datei `CNAME`, ist bereits so).

1. Bei Hetzner in die DNS-Verwaltung (DNS Console) einloggen, Zone `fundamentgroup.de` öffnen.
2. Prüfen, ob es schon einen Eintrag für `www` gibt. Falls ja: notieren, was drinsteht (Typ, Wert), und diesen einen Eintrag ersetzen. Falls nein: neuen Eintrag anlegen.
3. Eintrag anlegen oder ändern:
   - Typ: `CNAME`
   - Name: `www`
   - Wert: `fundamentgroupe.github.io.` (mit Punkt am Ende, falls die Oberfläche das verlangt; im DNS spielt die Groß-/Kleinschreibung keine Rolle)
   - TTL: 3600 (oder der Standardwert)
4. Speichern. Sonst nichts ändern. Insbesondere die `A`-Einträge der Hauptadresse (`@`), die schon auf GitHub Pages zeigen, und alle `MX`/`TXT`-Einträge unverändert lassen.
5. Auf GitHub: Repository `Fundamentgroupe/fundament-website` > Settings > Pages. Bei "Custom domain" muss `fundamentgroup.de` stehen. "Enforce HTTPS" soll angehakt sein.
6. Warten (meist Minuten, selten einige Stunden). BITTE PRÜFEN: Das Zertifikat für `www` stellt GitHub nach der DNS-Änderung automatisch aus; es kann etwas dauern. Bei einer Zertifikatswarnung im Browser einige Stunden warten und erneut prüfen.

Prüfung (Terminal oder PowerShell):

```
curl -I http://www.fundamentgroup.de/
curl -I https://www.fundamentgroup.de/
curl -I https://fundamentgroup.de/
nslookup -type=CNAME www.fundamentgroup.de
```

Erwartet: Bei den ersten beiden Aufrufen `301` und eine Zeile `location: https://fundamentgroup.de/`. Beim dritten `200`. Die DNS-Abfrage soll `fundamentgroupe.github.io` zeigen.

## Teil 2: fundament-group.de (Domain mit Bindestrich) umleiten

Die einfachste Variante ist eine Weiterleitung (HTTP 301) beim Anbieter, bei dem die Domain `fundament-group.de` liegt. BITTE PRÜFEN: Ich weiß nicht, bei welchem Anbieter diese zweite Domain registriert ist und ob dort eine Weiterleitungsfunktion ("Domain-Weiterleitung", "Redirect", "URL-Forwarding") inklusive ist. Nachsehen im Kundenkonto des Anbieters.

Einfachste Variante: Weiterleitung beim Anbieter

1. Im Kundenkonto des Anbieters die Domain `fundament-group.de` öffnen und die Funktion "Weiterleitung" suchen.
2. Einrichten:
   - Quelle: `fundament-group.de` und, falls getrennt auswählbar, auch `www.fundament-group.de`
   - Ziel: `https://fundamentgroup.de/`
   - Art: dauerhaft (301)
   - Pfad beibehalten: wenn angeboten, ja; sonst ist Weiterleitung auf die Startseite in Ordnung.
3. Speichern.
4. Für `https://fundament-group.de` (mit https) braucht der Anbieter ein Zertifikat. Falls er das nicht kann, funktioniert nur `http://fundament-group.de`. BITTE PRÜFEN: ob der Anbieter https-Weiterleitung unterstützt.

Prüfung:

```
curl -I http://fundament-group.de/
curl -I https://fundament-group.de/
curl -I http://www.fundament-group.de/
```

Erwartet: `301` und `location: https://fundamentgroup.de/`.

Alternative, falls der Anbieter keine Weiterleitung kann:

GitHub Pages kann pro Repository nur eine eigene Domain bedienen, die zweite Domain lässt sich daher nicht einfach auf dasselbe Repo zeigen lassen. Möglich ist ein zweites, winziges Repo, in dem nur eine Weiterleitungsseite liegt (eigene Datei `CNAME` mit `fundament-group.de`), dazu in der DNS-Zone dieser Domain die vier GitHub-A-Einträge `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`. Das ist aufwendiger und nur sinnvoll, wenn die Anbieter-Weiterleitung nicht geht. BITTE PRÜFEN: Eine reine HTML-Weiterleitung (Meta-Refresh) sendet keinen echten 301 und ist für Suchmaschinen schwächer als eine Weiterleitung beim Anbieter.

Falls die zweite Domain auch für E-Mail genutzt wird: dort ebenfalls keine MX-/SPF-/DKIM-/DMARC-Einträge ändern. BITTE PRÜFEN: ob `fundament-group.de` für Mail genutzt wird.

## Nach beiden Teilen

- In der Google Search Console prüfen, dass `https://fundamentgroup.de/` (bzw. die Domain-Property) die bevorzugte ist. `www` und `fundament-group.de` müssen nicht als eigene Property angelegt werden.
- Bing Webmaster Tools: dieselbe Hauptadresse (siehe `docs/indexnow.md`).
- Alle neuen Verlinkungen (LinkedIn, Google-Unternehmensprofil, Verzeichnisse) immer auf `https://fundamentgroup.de/` setzen.

## Was ich nicht sicher weiß (BITTE PRÜFEN)

- Welcher Anbieter für `fundament-group.de` zuständig ist und ob dort eine 301-Weiterleitung inklusive ist.
- Ob für `www.fundamentgroup.de` bei Hetzner bereits ein Eintrag existiert, der ersetzt werden muss.
- Genaue Bezeichnungen der Schaltflächen in der Hetzner-DNS-Oberfläche (sie ändern sich gelegentlich).
- Ob GitHub das Zertifikat für `www` sofort ausstellt.
