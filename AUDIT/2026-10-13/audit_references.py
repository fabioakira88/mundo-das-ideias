from pathlib import Path
import fitz, json, zipfile, xml.etree.ElementTree as ET, hashlib
from PIL import Image,ImageOps,ImageDraw
src=Path('/Users/fabiotsugawa/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Mundo das Ideias 🪑')
out=Path('/Users/fabiotsugawa/Downloads/DIGITAL_PROJECTS/MUNDO_DAS_IDEIAS/AUDIT/2026-10-13/evidence'); (out/'manual-pages').mkdir(exist_ok=True)
info=[]
for p in sorted(src.iterdir()):
 row={'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 if p.suffix.lower()=='.pdf':
  doc=fitz.open(p);row['pages']=len(doc);texts=[]; thumbs=[]
  for i,page in enumerate(doc):
   texts.append(f'\n--- PÁGINA {i+1} ---\n'+page.get_text())
   pix=page.get_pixmap(matrix=fitz.Matrix(.72,.72),alpha=False)
   dest=out/'manual-pages'/f'{p.stem}-{i+1:02d}.png';pix.save(dest)
   im=Image.open(dest);im.thumbnail((300,420)); thumbs.append((i+1,im.copy()))
  (out/(p.stem+'.txt')).write_text(''.join(texts))
  for start in range(0,len(thumbs),12):
   group=thumbs[start:start+12];sheet=Image.new('RGB',(1240,460*((len(group)+3)//4)), '#dedbd5'); draw=ImageDraw.Draw(sheet)
   for j,(num,im) in enumerate(group):
    x=j%4*310; y=j//4*460;sheet.paste(im,(x,y+25));draw.text((x+8,y+7),f'p. {num}',fill='black')
   sheet.save(out/'manual-pages'/f'{p.stem}-sheet-{start//12+1}.jpg')
 elif p.suffix.lower()=='.docx':
  with zipfile.ZipFile(p) as z:
   root=ET.fromstring(z.read('word/document.xml'));ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
   paras=[''.join(t.text or '' for t in para.findall('.//w:t',ns)) for para in root.findall('.//w:p',ns)]
   (out/(p.stem+'-docx.txt')).write_text('\n'.join(paras));row['paragraphs']=len(paras)
 elif p.suffix.lower()=='.png':
  im=Image.open(p);row.update(width=im.width,height=im.height,mode=im.mode)
  a=im.getchannel('A') if 'A' in im.getbands() else None
  row['alpha_extrema']=a.getextrema() if a else None
  row['transparent_pixels']=sum(a.histogram()[:255]) if a else 0
  row['fully_transparent_pixels']=a.histogram()[0] if a else 0
  row['corner_rgba']=im.convert('RGBA').getpixel((0,0))
  if a: row['alpha_bbox']=a.getbbox()
 info.append(row)
(out/'references-inventory.json').write_text(json.dumps(info,indent=2,ensure_ascii=False))
print(json.dumps(info,indent=2,ensure_ascii=False))
