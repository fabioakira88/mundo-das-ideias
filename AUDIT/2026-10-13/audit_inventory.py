"""Read-only inventory of the worktree; writes only this audit directory."""
from pathlib import Path
from collections import Counter, defaultdict
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import csv, hashlib, json, re, subprocess
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SITE = ROOT / 'SITE'
EXCLUDE = {'.git', 'AUDIT', '__pycache__', 'node_modules', '.venv'}
ASSET_EXT = {'.png','.jpg','.jpeg','.webp','.avif','.gif','.svg','.ico','.pdf','.woff','.woff2','.ttf','.otf','.mp4','.webm','.mp3','.wav','.css','.js'}
files = sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in EXCLUDE for x in p.relative_to(ROOT).parts) and not p.name.startswith('.env'))
tracked = set(subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0'))
sources = {p:p.read_text(errors='replace') for p in files if p.suffix.lower() in {'.html','.css','.js','.mjs','.json','.md','.py','.yml','.svg'} or p.name in {'css','css(1)','css(2)','css2','CNAME','robots.txt'}}
refs = defaultdict(set)
external = defaultdict(set)
boundaries = []
for p,txt in sources.items():
    if not p.is_relative_to(SITE) or 'docs' in p.relative_to(SITE).parts: continue
    values=[]
    values.extend(m.group(2) for m in re.finditer(r'\b(?:src|href|poster)\s*=\s*([\x22\x27])(.*?)\1',txt))
    values.extend(m.group(2) for m in re.finditer(r'url\(([\x22\x27]?)(.*?)\1\)',txt))
    values.extend(m.group(2) for m in re.finditer(r'([\x22\x27])([^\x22\x27\n<>]*?\.(?:png|jpe?g|webp|svg|gif|pdf|woff2?|css|js)(?:\?[^\x22\x27]*)?)\1',txt,re.I))
    for raw in set(values):
        raw=raw.replace('\\/','/').strip()
        if raw.startswith(('http://','https://','//')):
            external[raw].add(str(p.relative_to(ROOT)));continue
        if not raw or re.search(r'[${}<>\\]',raw) or raw.startswith(('data:','mailto:','tel:','#')):continue
        clean=unquote(urlsplit(raw).path)
        if Path(clean).suffix.lower() not in ASSET_EXT or clean == '-L.jpg':continue
        if clean.startswith('/'): target=SITE/clean.lstrip('/')
        elif p.suffix in {'.json','.js'} and clean.startswith('assets/'):target=SITE/clean
        else:target=p.parent/clean
        target=target.resolve()
        refs[target].add(str(p.relative_to(ROOT)))
        if not target.is_relative_to(SITE):boundaries.append({'source':str(p.relative_to(ROOT)),'reference':raw,'target':str(target)})

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.images=[];self.forms=[];self.links=[];self.h1=0;self.ids=[];self.styles=0;self.inline_scripts=0;self.scripts=[];self.title='';self.in_title=False;self.canonical='';self.description='';self.og_image='';self.lang=''
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='html':self.lang=a.get('lang','')
        if tag=='h1':self.h1+=1
        if tag=='title':self.in_title=True
        if tag=='img':self.images.append(a)
        if tag=='form':self.forms.append(a)
        if tag=='style':self.styles+=1
        if tag=='script':
            if a.get('src'):self.scripts.append(a['src'])
            elif a.get('type')!='application/ld+json':self.inline_scripts+=1
        if tag=='a':self.links.append(a.get('href',''))
        if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href','')
        if tag=='meta' and a.get('name')=='description':self.description=a.get('content','')
        if tag=='meta' and a.get('property')=='og:image':self.og_image=a.get('content','')
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
    def handle_data(self,data):
        if self.in_title:self.title+=data

pages=[];brand=[];rows=[];hashes=defaultdict(list);thumbs=[];errors=[]
for p in files:
    rel=str(p.relative_to(ROOT));raw=p.read_bytes();sha=hashlib.sha256(raw).hexdigest();hashes[sha].append(rel)
    asset=p.suffix.lower() in ASSET_EXT or p.name in {'css','css(1)','css(2)','css2'}
    row={'path':rel,'bytes':len(raw),'sha256':sha,'extension':p.suffix.lower(),'asset':asset,'git_tracked':rel in tracked,'width':'','height':'','mode':'','alpha_min':'','alpha_max':'','reference_count':len(refs[p.resolve()]),'references':' | '.join(sorted(refs[p.resolve()])),'publication_scope':'SITE' if p.is_relative_to(SITE) and 'docs' not in p.relative_to(SITE).parts else 'outside-publication','review_action':'review' if asset else 'preserve'}
    if asset and p.suffix.lower() in {'.png','.jpg','.jpeg','.webp','.gif','.avif','.ico'}:
        try:
            with Image.open(p) as im:
                im.load();row.update(width=im.width,height=im.height,mode=im.mode)
                if 'A' in im.getbands():row['alpha_min'],row['alpha_max']=im.getchannel('A').getextrema()
                small=im.convert('RGBA');small.thumbnail((160,135));bg=Image.new('RGBA',small.size,'#ece8df');bg.alpha_composite(small);thumbs.append((rel,bg.convert('RGB')))
        except Exception as exc:errors.append({'file':rel,'error':str(exc)})
    if asset:
        if rel.startswith('BRANDING/LOGO/'):row['review_action']='retire-old-brand-preserve-original'
        elif not refs[p.resolve()]:row['review_action']='candidate-unreferenced-do-not-delete'
        elif len(raw)>1048576:row['review_action']='optimize-after-visual-review'
        else:row['review_action']='preserve-and-check-MI-fit'
    rows.append(row)
    if p in sources:
        txt=sources[p]
        for i,line in enumerate(txt.splitlines(),1):
            if re.search(r'mundo-das-ideias|Mundo das Ideias|MUNDO_DAS_IDEIAS',line):brand.append({'file':rel,'line':i,'occurrences':len(re.findall('mundo-das-ideias',line,re.I)),'snippet':line[:240]})
        if p.suffix=='.html' and p.is_relative_to(SITE) and 'docs' not in p.relative_to(SITE).parts:
            d=Page();d.feed(txt)
            pages.append({'path':rel,'route':'/'+str(p.relative_to(SITE)).replace('index.html',''),'title':d.title,'h1_count':d.h1,'canonical':d.canonical,'description':d.description,'og_image':d.og_image,'lang':d.lang,'image_count':len(d.images),'images_missing_alt':sum('alt' not in a for a in d.images),'images_missing_dimensions':sum(not (a.get('width') and a.get('height')) for a in d.images),'inline_style_blocks':d.styles,'inline_scripts':d.inline_scripts,'scripts':d.scripts,'forms':d.forms,'duplicate_ids':[k for k,v in Counter(d.ids).items() if v>1],'links':d.links})

def savecsv(name,data):
    if not data:return
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
savecsv('inventario_arquivos.csv',rows)
savecsv('inventario_assets.csv',[r for r in rows if r['asset']])
savecsv('mapa_marca_legada.csv',brand)
duplicates=[{'sha256':h,'paths':v,'bytes_per_file':(ROOT/v[0]).stat().st_size,'redundant_bytes':(len(v)-1)*(ROOT/v[0]).stat().st_size} for h,v in hashes.items() if len(v)>1]
summary={'files':len(rows),'total_bytes':sum(r['bytes'] for r in rows),'assets':sum(r['asset'] for r in rows),'asset_bytes':sum(r['bytes'] for r in rows if r['asset']),'html_pages':len(pages),'groups':{k:{'files':sum(r['path'].split('/')[0]==k for r in rows),'bytes':sum(r['bytes'] for r in rows if r['path'].split('/')[0]==k)} for k in sorted(set(r['path'].split('/')[0] for r in rows if '/' in r['path']))},'duplicate_groups':len(duplicates),'redundant_bytes':sum(d['redundant_bytes'] for d in duplicates),'image_decode_errors':errors,'assets_over_1MiB':[r['path'] for r in rows if r['asset'] and r['bytes']>1048576],'candidate_unreferenced_assets':sum(r['asset'] and not r['reference_count'] for r in rows),'old_brand_files':len(set(r['file'] for r in brand)),'old_brand_occurrences':sum(r['occurrences'] for r in brand),'external_hosts':dict(Counter(urlsplit(u if not u.startswith('//') else 'https:'+u).netloc for u in external))}
for name,data in [('summary',summary),('duplicates',duplicates),('pages',pages),('external-references',[{'url':u,'sources':sorted(v)} for u,v in external.items()]),('publish-boundaries',boundaries),('references',[{'target':str(k),'exists':k.exists(),'sources':sorted(v)} for k,v in refs.items()])]:
    (OUT/'evidence'/(name+'.json')).write_text(json.dumps(data,indent=2,ensure_ascii=False))
(OUT/'evidence'/'asset-contact-sheets').mkdir(exist_ok=True)
for start in range(0,len(thumbs),40):
    group=thumbs[start:start+40];sheet=Image.new('RGB',(1000,200*((len(group)+4)//5)),'white');draw=ImageDraw.Draw(sheet)
    for i,(rel,im) in enumerate(group):
        x=i%5*200;y=i//5*200;sheet.paste(im,(x+(200-im.width)//2,y));name=rel.split('/')[-1];draw.text((x+4,y+140),str(start+i+1)+' '+name[:26],fill='black');draw.text((x+4,y+156),name[26:52],fill='black');draw.text((x+4,y+174),'/'.join(rel.split('/')[-3:-1])[:28],fill='black')
    sheet.save(OUT/'evidence'/'asset-contact-sheets'/f'sheet-{start//40+1:02d}.jpg')
print(json.dumps(summary,indent=2,ensure_ascii=False))
