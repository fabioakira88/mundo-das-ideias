from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,re,html,subprocess
root=Path('/Users/fabiotsugawa/Downloads/DIGITAL_PROJECTS/MUNDO_DAS_IDEIAS');out=root/'AUDIT/2026-10-13/evidence';
paths=['/','/artigos/','/filosofos/','/conceitos/','/enciclopedia/','/dossies/','/dossies/vida-morte-consciencia/','/biblioteca.html','/sobre/','/sitemap.xml','/robots.txt','/Relacoes-Leves-Mundo-das-Ideias.pdf','/artigos/marco-aurelio-imperador-filosofo-estoico/','/assets/article_cards/marco-aurelio-imperador-filosofo-estoico.jpg','/assets/hero/socrates-louvre-bust.webp','/assets/LQHqVnilFspwfHEy.png']
def get(p):
 u='https://procederfilosofico.com.br'+p;row={'url':u,'path':p}
 try:
  dest=out/('http-'+hashlib.sha256(u.encode()).hexdigest()[:12]+'.bin')
  headers=dest.with_suffix('.headers')
  proc=subprocess.run(['/usr/bin/curl','-L','--max-time','18','-sS','-D',str(headers),'-o',str(dest),'-w','%{http_code} %{url_effective}',u],capture_output=True,text=True)
  if proc.returncode:raise RuntimeError(proc.stderr)
  code,final=proc.stdout.split(' ',1);raw=dest.read_bytes();hs=headers.read_text();headerdict={k.lower():v.strip() for k,v in re.findall(r'^([^:\r\n]+):([^\r\n]+)',hs,re.M)}
  row.update(status=int(code),final_url=final,bytes=len(raw),content_type=headerdict.get('content-type'),sha256=hashlib.sha256(raw).hexdigest(),headers={k:headerdict.get(k.lower()) for k in ['Server','Cache-Control','Content-Security-Policy','Strict-Transport-Security','X-Content-Type-Options','Referrer-Policy']})
  local=root/'SITE'/p.lstrip('/');local=local/'index.html' if local.is_dir() or p=='/' else local
  if local.is_file():row['same_as_worktree']=raw==local.read_bytes()
  if row['content_type'] and ('html' in row['content_type'] or 'xml' in row['content_type'] or 'text/plain' in row['content_type']):
   text=raw.decode(errors='replace');m=re.search('<title>(.*?)</title>',text,re.S);row['title']=html.unescape(m.group(1)) if m else None;row['sitemap_urls']=len(re.findall('<loc>',text)) if p=='/sitemap.xml' else None
   (out/('production-'+(p.strip('/').replace('/','_') or 'home')+'.txt')).write_text(text)
  dest.unlink();headers.unlink()
 except HTTPError as e:row.update(status=e.code,error=str(e))
 except Exception as e:row['error']=str(e)
 return row
rows=list(ThreadPoolExecutor(max_workers=5).map(get,paths));(out/'production-audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print(json.dumps(rows,ensure_ascii=False,indent=2))
