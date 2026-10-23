"""Check content coverage, bibliography, HTML links/anchors, and accessible basics."""
import json,re,sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parents[1]; out=root/'docs'
L=json.loads((root/'content/course.json').read_text()); R=json.loads((root/'content/references.json').read_text())
errors=[]
def check(ok,msg):
 if not ok: errors.append(msg)
check(len(L)==14,'Expected 14 teaching units')
check(sorted(l['slot'] for l in L)==list(range(1,8))+list(range(9,16)),'Incorrect semester mapping')
check(len({l['id'] for l in L})==len(L),'Duplicate unit identifiers')
refids={r['id'] for r in R}; check(len(refids)==len(R),'Duplicate source identifiers')
words=0
for l in L:
 for field in ['title','summary','question','case','goals','sections','analysis','guided','independent','reflection','quiz','explanation','refs','diagram','takeaways']:check(bool(l.get(field)),l['id']+': missing '+field)
 check(len(l['sections'])>=4,l['id']+': insufficient structured sections')
 check(len(l['quiz'])==4 and 0<=l['answer']<3,l['id']+': invalid quiz')
 check(set(l['refs'])<=refids,l['id']+': unknown citation')
 words+=sum(len(s['text'].split()) for s in l['sections'])
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[];self.h1=0;self.lang=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')=='id'
  if tag=='h1':self.h1+=1
  if 'id' in a:check(a['id'] not in self.ids,'Duplicate anchor: '+a['id']);self.ids.add(a['id'])
  if tag in ['a','link','script','img']:
   u=a.get('href',a.get('src',''))
   if u:self.links.append(u)
  if tag=='img':check('alt' in a,'Image missing alt')
  if tag=='a' and a.get('target')=='_blank':check('noopener' in a.get('rel',''),'External target missing protection')
pages={}
for f in out.glob('*.html'):
 parser=Page();parser.feed(f.read_text());pages[f.resolve()]=parser
 check(parser.h1==1,f.name+': expected one H1');check(parser.lang,f.name+': missing Indonesian language')
 for residual in ['TODO','Lorem ipsum','Catatan uji:','qa-mobile']:check(residual not in f.read_text(),f.name+': residual '+residual)
for f,p in pages.items():
 for u in p.links:
  split=urlsplit(u)
  if split.scheme or split.netloc:continue
  target=(f.parent/unquote(split.path)).resolve() if split.path else f
  check(target.exists(),f.name+': missing target '+u)
  if split.fragment and target in pages:check(unquote(split.fragment) in pages[target].ids,f.name+': missing anchor '+u)
check(len(pages)==23,'Expected 23 HTML pages')
report={'units':len(L),'html_pages':len(pages),'reference_entries':len(R),'main_material_words':words,'errors':errors}
print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(bool(errors))
