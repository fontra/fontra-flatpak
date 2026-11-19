import json, sys, urllib.request, urllib.parse, concurrent.futures as cf
src, dst = sys.argv[1:3]
d = json.load(open(src))
todo = {}
for k, v in d['packages'].items():
    if not k or v.get('link') or 'resolved' in v: continue
    if 'node_modules/' not in k: continue          # workspace members
    name = v.get('name') or k.rsplit('node_modules/', 1)[1]
    todo[k] = (name, v['version'])
def fetch(item):
    k, (name, ver) = item
    u = 'https://registry.npmjs.org/%s/%s' % (urllib.parse.quote(name, safe='@').replace('%40','@'), ver)
    for i in range(4):
        try:
            m = json.load(urllib.request.urlopen(u, timeout=60))
            return k, m['dist']['tarball'], m['dist']['integrity']
        except Exception as e:
            err = e
    raise SystemExit('%s: %s' % (u, err))
with cf.ThreadPoolExecutor(16) as ex:
    for k, t, i in ex.map(fetch, todo.items()):
        d['packages'][k]['resolved'] = t
        d['packages'][k]['integrity'] = i
json.dump(d, open(dst, 'w'), indent=2); open(dst, 'a').write('\n')
print('patched', len(todo))
