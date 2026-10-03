"""Check the static deployment tree with Python's standard library only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'website'
errors = []
references = 0
ORIGIN = 'https://justinsejinpark.com'

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.headings = [], [], []
        self.title = False
        self.description = False
        self.canonical = None
        self.metadata = {}
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(int(tag[1]))
        if tag == 'title':
            self.title = True
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = bool(attrs.get('content'))
        if tag == 'meta':
            self.metadata[attrs.get('property', attrs.get('name'))] = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        if tag == 'img' and not attrs.get('alt'):
            errors.append(f'{current}: image missing useful alt text')
        self.links.extend(attrs[a] for a in ('href', 'src') if a in attrs)

pages = {}
for current in sorted(SITE.rglob('*.html')):
    parser = Page()
    text = current.read_text(encoding='utf-8')
    parser.feed(text)
    pages[current.resolve()] = parser
    if not parser.title or not parser.description:
        errors.append(f'{current}: missing title/description')
    if parser.headings.count(1) != 1 or any(b > a + 1 for a, b in zip(parser.headings, parser.headings[1:])):
        errors.append(f'{current}: invalid heading hierarchy')
    if len(parser.ids) != len(set(parser.ids)):
        errors.append(f'{current}: duplicate IDs')
    if re.search(r'source-materials|(?<![A-Za-z])[A-Za-z]:[/\\]|WE-\d+|jira|confluence', text, re.I):
        errors.append(f'{current}: private reference in public HTML')

expected_urls = set()
for current, page in pages.items():
    if current.name == '404.html':
        continue
    route = current.parent.relative_to(SITE.resolve()).as_posix()
    expected = ORIGIN + '/' + (route + '/' if route != '.' else '')
    expected_urls.add(expected)
    if page.canonical != expected or page.metadata.get('og:url') != expected:
        errors.append(f'{current}: incorrect production canonical/Open Graph URL')
    for key in ('og:image', 'twitter:image'):
        image = page.metadata.get(key, '')
        if not image.startswith(ORIGIN + '/assets/images/') or not (SITE / urlsplit(image).path.lstrip('/')).is_file():
            errors.append(f'{current}: invalid public social image {key}')

try:
    sitemap = ET.parse(SITE / 'sitemap.xml')
    sitemap_urls = [node.text for node in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    if set(sitemap_urls) != expected_urls or len(sitemap_urls) != len(expected_urls):
        errors.append('Sitemap does not match all indexable production routes')
except (OSError, ET.ParseError) as error:
    errors.append(f'Invalid sitemap: {error}')
if f'Sitemap: {ORIGIN}/sitemap.xml' not in (SITE / 'robots.txt').read_text(encoding='utf-8'):
    errors.append('Robots file is missing the production sitemap URL')

for current, page in pages.items():
    for reference in page.links:
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        target = (SITE / unquote(url.path).lstrip('/') if url.path.startswith('/') else current.parent / unquote(url.path)) if url.path else current
        target = target.resolve()
        if target.is_dir():
            target /= 'index.html'
        references += 1
        if not target.is_relative_to(SITE.resolve()) or not target.is_file():
            errors.append(f'{current}: broken/unsafe reference {reference}')
        elif url.fragment and target.suffix == '.html' and unquote(url.fragment) not in pages[target.resolve()].ids:
            errors.append(f'{current}: missing anchor {reference}')

for path in SITE.rglob('*'):
    if not path.is_file():
        continue
    if path.suffix.lower() not in {'.html', '.css', '.js', '.svg', '.webp', '.png', '.jpg', '.pdf', '.txt', '.xml'} and path.name != '_headers':
        errors.append(f'{path}: unexpected public file type')
    if path.suffix.lower() in {'.html', '.css', '.js', '.svg', '.txt'}:
        text = path.read_text(encoding='utf-8')
        if re.search(r'AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{24,}|-----BEGIN .*PRIVATE KEY-----', text):
            errors.append(f'{path}: possible credential')

resume = SITE / 'assets/documents/justin-park-resume.pdf'
source = ROOT / 'source-materials/resume/Drone Resume.pdf'
if not resume.read_bytes().startswith(b'%PDF-'):
    errors.append('Public resume is not a PDF')
if source.exists() and hashlib.sha256(resume.read_bytes()).digest() != hashlib.sha256(source.read_bytes()).digest():
    errors.append('Public resume differs from the designated current resume')

print(f'Checked {len(pages)} pages and {references} local references.')
for error in errors:
    print(error)
if errors:
    raise SystemExit(1)
print('Static checks passed.')
