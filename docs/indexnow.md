# IndexNow: neue und geänderte Seiten an Bing und Co. melden

Stand: 5. November 2026.

IndexNow teilt Suchmaschinen (Bing, Yandex u. a.) mit, dass sich Seiten geändert haben. Google nutzt IndexNow nicht; für Google gilt die Search Console (siehe `docs/ABSCHLUSSBERICHT_A.md`).

Schlüsseldatei (liegt bereits im Repo): `52c143a254862a7e25c7e86f0bd305e2.txt`, erreichbar unter
`https://fundamentgroup.de/52c143a254862a7e25c7e86f0bd305e2.txt`. Der Inhalt der Datei ist der Schlüssel selbst.

**Wichtig: Die Meldung erst NACH dem Merge der Pull Requests ausführen und erst, wenn die Seite live ist** (GitHub Pages braucht meist ein bis zwei Minuten). Sonst meldet man Adressen, die es noch nicht gibt. Reihenfolge: erst die Pull Requests von Session B und C mergen, dann diesen (A), dann melden.

## Variante 1: ein Befehl (curl) mit allen URLs aus der Sitemap

Bash (Git Bash, macOS, Linux). Liest die URLs aus der live ausgelieferten Sitemap:

```bash
HOST="fundamentgroup.de"
KEY="52c143a254862a7e25c7e86f0bd305e2"
URLS=$(curl -s "https://$HOST/sitemap.xml" | grep -o '<loc>[^<]*</loc>' | sed 's#</\?loc>##g' | sed 's/.*/"&"/' | paste -sd, -)
curl -i -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"https://$HOST/$KEY.txt\",\"urlList\":[$URLS]}"
```

Erwartete Antwort: `200 OK` oder `202 Accepted`. Bei `403` stimmt der Schlüssel oder die Schlüsseldatei nicht, bei `422` stimmen Adressen oder Host nicht, bei `429` waren es zu viele Anfragen (später erneut).

## Variante 2: Python (läuft auch unter Windows)

```python
import json, re, urllib.request
host = "fundamentgroup.de"
key = "52c143a254862a7e25c7e86f0bd305e2"
sitemap = urllib.request.urlopen(f"https://{host}/sitemap.xml").read().decode("utf-8")
urls = re.findall(r"<loc>(.*?)</loc>", sitemap)
body = json.dumps({"host": host, "key": key, "keyLocation": f"https://{host}/{key}.txt", "urlList": urls}).encode("utf-8")
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
print(urllib.request.urlopen(req).status)
```

## Danach

- Bing Webmaster Tools öffnen (die Seite ist über die vorhandene Bing-Verifizierung in `index.html` bereits zuordenbar) und unter "Sitemaps" `https://fundamentgroup.de/sitemap.xml` einreichen.
- Bei künftigen Änderungen genügt es, nur die geänderten URLs zu melden (Liste `urlList` entsprechend kürzen).
- BITTE PRÜFEN: Ob `api.indexnow.org` weiterhin der gültige Sammelendpunkt ist und ob eine Mail- oder Browser-Rückmeldung von Bing zur Schlüsselprüfung kommt.
