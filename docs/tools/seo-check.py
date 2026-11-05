#!/usr/bin/env python3
"""Prüft die statische Fundament-Website auf typische Technik- und SEO-Fehler.

Aufruf (im Repo-Hauptordner):
    python docs/tools/seo-check.py            # Ergebnis auf dem Bildschirm
    python docs/tools/seo-check.py --write    # zusätzlich nach docs/seo-check.md schreiben

Geprüft wird je HTML-Seite: Titel, Meta-Description, Canonical, Open Graph, genau ein h1,
Bilder ohne alt, JSON-LD (parsebar, FAQ-Fragen stehen auch auf der Seite), interne Links
(Datei und Anker vorhanden), externe Ressourcen, Calendly-Button oben/Mitte/Ende,
Footer-Linkblock, Aufnahme in die Sitemap. Nur Standardbibliothek.
"""
import sys, re, json, os
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SITE = 'https://fundamentgroup.de'
CAL = 'https://calendly.com/franz-josef-fundamentgroup/fordermoglichkeiten-fur-ihr-unternehmen'
ALLOWED_EXTERNAL = ('https://calendly.com/', 'https://www.linkedin.com/', 'https://fundamentgroup.de', 'https://schema.org', 'http://www.w3.org/')
# Seiten, die in anderen Branches angelegt werden: toter Link ist dort erwartbar
PLANNED = [
    'foerdermittelberatung', 'foerdermittel-beantragen', 'foerdermittel-start-ups-gruender', 'foerdermittel-mittelstand',
    'foerderung-innovation-digitalisierung', 'foerderung-investition', 'foerdermittel-eu-programme',
    'foerdermittelberatung-erfolgshonorar', 'forschungszulage-voraussetzungen', 'forschungszulage-kmu', 'bsfz-bescheinigung',
    'foerdermittel-software-it', 'foerdermittel-lebensmittel', 'foerdermittel-handwerk-bau',
    'foerdermittelberatung-muenchen', 'foerdermittelberatung-oberbayern', 'foerdermittelberatung-deutschland',
]
PLANNED_PATHS = {'/' + p + '/' for p in PLANNED}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ''; self.in_title = False
        self.metas = []; self.links = []; self.h1 = 0; self.imgs = []; self.anchors = []; self.ids = set()
        self.ld = []; self.in_ld = False; self.ld_buf = ''
        self.scripts = []; self.hrefs = []; self.text = []; self.skip = 0
        self.summaries = []; self.in_summary = False; self.sum_buf = ''
        self.cta = []  # (position im Dokument, Text) der Calendly-Links
        self.pos = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'title': self.in_title = True
        elif tag == 'meta': self.metas.append(a)
        elif tag == 'link': self.links.append(a)
        elif tag == 'h1': self.h1 += 1
        elif tag == 'img': self.imgs.append(a)
        elif tag == 'a' and 'href' in a:
            self.anchors.append(a['href'])
        elif tag == 'script':
            if a.get('type') == 'application/ld+json': self.in_ld = True; self.ld_buf = ''
            if 'src' in a: self.scripts.append(a['src'])
            self.skip += 1
        elif tag == 'style': self.skip += 1
        elif tag in ('summary', 'h2', 'h3'): self.in_summary = True; self.sum_buf = ''
        for k in ('src', 'href', 'srcset'):
            if k in a and tag != 'a': self.hrefs.append((tag, a[k]))

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
        elif tag == 'script':
            if self.in_ld: self.ld.append(self.ld_buf); self.in_ld = False
            self.skip = max(0, self.skip - 1)
        elif tag == 'style': self.skip = max(0, self.skip - 1)
        elif tag in ('summary', 'h2', 'h3'): self.in_summary = False; self.summaries.append(self.sum_buf.strip())

    def handle_data(self, d):
        if self.in_title: self.title += d
        if self.in_ld: self.ld_buf += d
        if self.in_summary: self.sum_buf += d
        if not self.skip: self.text.append(d)


def norm(s): return re.sub(r'\s+', ' ', s).strip()


def page_url(rel):
    if rel == 'index.html': return SITE + '/'
    if rel == '404.html': return SITE + '/404.html'
    return SITE + '/' + rel[:-len('index.html')]


def main():
    pages = []
    for d, _, fs in os.walk(ROOT):
        if os.sep + '.git' in d or os.sep + 'docs' in d or os.sep + 'fonts' in d: continue
        for f in fs:
            if f.endswith('.html'):
                pages.append(os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, '/'))
    pages.sort()
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    sm_urls = re.findall(r'<loc>(.*?)</loc>', sm)
    issues = {}; notes = {}; planned = {}
    parsed = {}
    def bad(rel, msg): issues.setdefault(rel, []).append(msg)
    def note(rel, msg): notes.setdefault(rel, []).append(msg)

    for rel in pages:
        raw = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        p = P(); p.feed(raw); parsed[rel] = (p, raw)
    existing_paths = set()
    for rel in pages:
        if rel.endswith('index.html'):
            existing_paths.add('/' + rel[:-len('index.html')])
        existing_paths.add('/' + rel)

    for rel in pages:
        p, raw = parsed[rel]
        url = page_url(rel)
        is404 = rel == '404.html'
        title = norm(p.title)
        if not title: bad(rel, 'Titel fehlt')
        elif len(title) > 70: note(rel, 'Titel länger als 70 Zeichen (%d)' % len(title))
        md = [m for m in p.metas if m.get('name') == 'description']
        if not md: bad(rel, 'Meta-Description fehlt')
        else:
            n = len(md[0].get('content', ''))
            if n < 70 or n > 175: note(rel, 'Meta-Description hat %d Zeichen (Ziel 70 bis 160)' % n)
        can = [l for l in p.links if l.get('rel') == 'canonical']
        if not can: bad(rel, 'Canonical fehlt')
        elif can[0].get('href') != url: bad(rel, 'Canonical %s weicht von %s ab' % (can[0].get('href'), url))
        og = {m.get('property'): m.get('content') for m in p.metas if m.get('property')}
        for k in ('og:title', 'og:description', 'og:url', 'og:image', 'og:image:alt'):
            if not og.get(k): bad(rel, k + ' fehlt')
        if og.get('og:url') and og['og:url'] != url: bad(rel, 'og:url weicht ab')
        if p.h1 != 1: bad(rel, 'h1 kommt %d-mal vor (soll genau 1)' % p.h1)
        for im in p.imgs:
            if not im.get('alt'): bad(rel, 'Bild ohne alt: ' + im.get('src', '?'))
        if not any(m.get('name') == 'viewport' for m in p.metas): bad(rel, 'viewport fehlt')
        if 'lang="de"' not in raw[:200]: bad(rel, 'lang="de" fehlt')
        # JSON-LD
        text = norm(' '.join(p.text))
        for blk in p.ld:
            try:
                data = json.loads(blk)
            except Exception as e:
                bad(rel, 'JSON-LD nicht parsebar: %s' % e); continue
            for node in data.get('@graph', [data]):
                if node.get('@type') == 'FAQPage':
                    for q in node.get('mainEntity', []):
                        if norm(q['name']) not in [norm(s) for s in p.summaries]:
                            bad(rel, 'FAQ-Frage nicht auf der Seite sichtbar: ' + q['name'][:60])
                if node.get('@type') == 'ProfessionalService':
                    an = node.get('alternateName')
                    if an != ["Fundament Group", "Fundament GmbH", "Fundamentgroup", "Fundament Fördermittel"]:
                        bad(rel, 'alternateName der Organisation weicht vom Standard ab')
                    if 'Am Kirchberg 16a' not in json.dumps(node, ensure_ascii=False): bad(rel, 'Geschäftsadresse fehlt in der Organisation')
        # Externe Ressourcen
        for tag, v in p.hrefs:
            if v.startswith(('http://', 'https://', '//')) and not v.startswith(ALLOWED_EXTERNAL):
                bad(rel, 'externe Ressource <%s>: %s' % (tag, v))
        for s in p.scripts:
            if s.startswith(('http', '//')): bad(rel, 'externes Skript: ' + s)
        for l in p.links:
            h = l.get('href', '')
            if h.startswith(('http', '//')) and l.get('rel') != 'canonical': bad(rel, 'externer Link-Tag: ' + h)
        if 'fonts.googleapis' in raw or 'fonts.gstatic' in raw: bad(rel, 'Google Fonts eingebunden')
        # interne Links
        for h in p.anchors:
            if h.startswith(('mailto:', 'tel:', 'javascript:')): continue
            if h.startswith('http'):
                if not h.startswith(SITE) and not h.startswith(ALLOWED_EXTERNAL):
                    note(rel, 'externer Link: ' + h)
                continue
            u = urlparse(h)
            path = u.path or ('/' + ('' if rel == 'index.html' else rel[:-len('index.html')]))
            if not path.startswith('/'):
                base = '/' + os.path.dirname(rel) + '/'
                path = os.path.normpath(base + path).replace(os.sep, '/')
                if not path.endswith('/') and '.' not in os.path.basename(path): path += '/'
            tgt = path if path.endswith('/') or '.' in os.path.basename(path) else path + '/'
            if tgt not in existing_paths:
                if tgt in PLANNED_PATHS: planned.setdefault(rel, set()).add(tgt)
                else: bad(rel, 'toter interner Link: ' + h)
                continue
            if u.fragment:
                tp = tgt + ('' if tgt.endswith('.html') else 'index.html')
                trel = tp.lstrip('/')
                if trel in parsed and u.fragment not in parsed[trel][0].ids:
                    bad(rel, 'Anker nicht vorhanden: ' + h)
        # Calendly oben / Mitte / Ende
        if not is404:
            cal_pos = [m.start() for m in re.finditer(re.escape(CAL), raw)]
            body_start = raw.find('<body'); main_s = raw.find('<main'); main_e = raw.find('</main>')
            top = [x for x in cal_pos if x < main_s + 0.0 or (main_s <= x < main_s + (main_e - main_s) * 0.2)]
            mid = [x for x in cal_pos if main_s + (main_e - main_s) * 0.2 <= x < main_s + (main_e - main_s) * 0.8]
            end = [x for x in cal_pos if x >= main_s + (main_e - main_s) * 0.8]
            if not top: bad(rel, 'Termin-Button oben fehlt')
            if not mid: bad(rel, 'Termin-Button in der Mitte fehlt')
            if not end: bad(rel, 'Termin-Button am Ende fehlt')
            if 'class="footer-links"' not in raw: bad(rel, 'Footer-Linkblock fehlt')
            if url not in sm_urls: bad(rel, 'nicht in der Sitemap')
        for word in ('Findways',):
            if word.lower() in raw.lower(): bad(rel, 'verbotenes Wort: ' + word)
    for u in sm_urls:
        if u == SITE + '/': continue
        path = u[len(SITE):]
        if path not in existing_paths:
            if path in PLANNED_PATHS: note('sitemap.xml', 'Sitemap listet geplante Seite (anderer Branch): ' + path)
            else: bad('sitemap.xml', 'Sitemap-URL ohne Seite: ' + path)

    for rel, ts in planned.items():
        note(rel, '%d Links auf geplante Seiten anderer Branches (erwartbar, bis diese gemergt sind)' % len(ts))
    lines = ['# SEO- und Technik-Check', '', 'Erzeugt mit `python docs/tools/seo-check.py --write`. Geprüft wurden %d HTML-Seiten.' % len(pages), '']
    total = sum(len(v) for v in issues.values())
    lines.append('**Fehler gesamt: %d**' % total); lines.append('')
    lines.append('## Fehler'); lines.append('')
    if not issues: lines.append('Keine Fehler gefunden.')
    for rel in sorted(issues):
        lines.append('- `%s`' % rel)
        for m in issues[rel]: lines.append('  - ' + m)
    lines += ['', '## Hinweise (kein Fehler)', '']
    if not notes: lines.append('Keine Hinweise.')
    for rel in sorted(notes):
        lines.append('- `%s`' % rel)
        seen = set()
        for m in notes[rel]:
            if m in seen: continue
            seen.add(m); lines.append('  - ' + m)
    lines += ['', '## Seitenübersicht', '', '| Seite | Titel (Zeichen) | Beschreibung (Zeichen) | h1 | Wörter |', '|---|---|---|---|---|']
    for rel in pages:
        p, raw = parsed[rel]
        md = [m for m in p.metas if m.get('name') == 'description']
        lines.append('| %s | %d | %d | %d | %d |' % (rel, len(norm(p.title)), len(md[0].get('content', '')) if md else 0, p.h1, len(norm(' '.join(p.text)).split())))
    out = '\n'.join(lines) + '\n'
    sys.stdout.buffer.write(out.encode('utf-8'))
    if '--write' in sys.argv:
        open(os.path.join(ROOT, 'docs', 'seo-check.md'), 'w', encoding='utf-8', newline='\n').write(out)
    sys.exit(1 if issues else 0)


if __name__ == '__main__':
    main()
