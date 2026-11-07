# Last updated 2026-11-07
# Makes manifest.json for Islet's food packs from a folder of pack files (common_*.tsv, fastfood_*.tsv, off_<cc>.tsv).
# Publish the folder and manifest at one https address (for example a GitHub repo's raw files) and enter
# <base>/manifest.json in Islet (Islet screen -> Food packs). A pack's version goes up whenever its content changes.
# Usage: python make_food_manifest.py <pack folder> <https base url>
import hashlib, json, os, re, sys

# -------- Build ----
folder, base = sys.argv[1], sys.argv[2].rstrip('/')
if not base.startswith('https://'):
    sys.exit('base url must be https')
path = os.path.join(folder, 'manifest.json')
old = {}
if os.path.exists(path):
    old = {p['name']: p for p in json.load(open(path, encoding='utf-8')).get('packs', [])}
packs = []
for f in sorted(os.listdir(folder)):
    name = f[:-4]
    if not f.endswith('.tsv') or not re.fullmatch(r'(common_|fastfood_|off_)[a-z0-9_]{1,36}', name):
        continue
    data = open(os.path.join(folder, f), 'rb').read()
    sha = hashlib.sha256(data).hexdigest()
    prev = old.get(name)
    version = prev['version'] if prev and prev['sha256'] == sha else (prev['version'] + 1 if prev else 1)
    packs.append({'name': name, 'version': version, 'url': f'{base}/{f}', 'sha256': sha, 'bytes': len(data)})
json.dump({'format': 1, 'packs': packs}, open(path, 'w', encoding='utf-8', newline='\n'), indent=1)
for p in packs:
    print(f"{p['name']:24} v{p['version']}  {p['bytes']} bytes")
