"""Precise, accessible conceptual figures; illustrative syntheses, not copied models."""
import json,html,math,textwrap
from pathlib import Path
root=Path(__file__).resolve().parents[1]
v=json.loads((root/'content/visuals.json').read_text())
ink='#193e36';green='#205b48';colors=['#e7f0df','#faebd8','#f4f0d5','#e4efee']
def label(x,y,s,size=21,color=ink,width=19):
 lines=textwrap.wrap(s,width=width)
 return ''.join(f'<text x="{x}" y="{y+(j-(len(lines)-1)/2)*26}" text-anchor="middle" dominant-baseline="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{html.escape(line)}</text>' for j,line in enumerate(lines))
def box(x,y,s,c,w=198,h=76):return f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="20" fill="{c}" stroke="#c0cec1"/>'+label(x,y,s,width=int(w/11.5))
def arrow(x1,y1,x2,y2):return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{green}" stroke-width="3" marker-end="url(#arrow)"/>'
for id,d in v.items():
 s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 430" role="img" aria-labelledby="title desc"><title id="title">{html.escape(d["center"])}</title><desc id="desc">{html.escape(d["relation"])}</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10" fill="{green}"/></marker></defs><rect width="480" height="430" rx="22" fill="#fffef9"/>'
 nodes=d['nodes'];kind=d['concept']
 if kind in ['cycle','steps','bridge']:
  pos=[(130,95),(350,95),(350,335),(130,335)]
  s+=arrow(231,95,247,95)+arrow(350,136,350,291)+arrow(249,335,233,335)
  if kind=='cycle':s+=arrow(130,294,130,139)
  for i,((x,y),node) in enumerate(zip(pos,nodes)):
   s+=box(x,y,node,colors[i],196,80)
   s+=f'<circle cx="{x}" cy="{y-57}" r="15" fill="{green}"/>'+label(x,y-57,str(i+1),16,'white')
  s+=label(240,211,d['center'],22,width=22)
  if kind!='cycle':s+=label(240,402,'Sesuaikan dengan konteks',16,width=40)
 elif kind=='orbit' and len(nodes)==5:
  pos=[(240,54),(400,175),(340,354),(140,354),(80,175)]
  for x,y in pos:s+=f'<path d="M240,210 L{x},{y}" stroke="#8ea695" stroke-width="3"/>'
  s+=f'<circle cx="240" cy="210" r="66" fill="{green}"/>'+label(240,210,d['center'],21,'white',13)
  for i,(x,y) in enumerate(pos):s+=box(x,y,nodes[i],colors[i%4],150 if i in [1,4] else 180,80)
 elif kind in ['orbit','converge']:
  pos=[(240,63),(365,212),(240,362),(115,212)]
  for x,y in pos:
   dx=x-240;dy=y-212;mag=math.hypot(dx,dy);ex=240+dx*0.48;ey=212+dy*.48
   if kind=='converge':s+=arrow(240+dx*.72,212+dy*.72,ex,ey)
   else:s+=f'<path d="M240,212 L{x},{y}" stroke="#8ea695" stroke-width="3"/>'
  s+=f'<circle cx="240" cy="212" r="72" fill="{green}"/>'+label(240,212,d['center'],21,'white',14)
  for i,((x,y),node) in enumerate(zip(pos,nodes)):
   if i in [1,3]:
    x=404 if i==1 else 76
    s+=box(x,y,node,colors[i],140,90)
   else:s+=box(x,y,node,colors[i],220,68)
 elif kind=='triangle':
  s+=f'<path d="M240,82 L392,329 L88,329 Z" fill="#e7f0df" stroke="#8ea695" stroke-width="3"/>'
  s+=label(240,220,d['center'],23,width=17)
  for i,(x,y) in enumerate([(240,75),(370,338),(110,338)]):s+=box(x,y,nodes[i],colors[i],195,75)
 elif kind=='ecology':
  for i,(x,y,w,h,c) in enumerate([(20,20,440,390,colors[2]),(47,85,386,300,colors[1]),(78,155,324,210,colors[0])]):
   s+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="40" fill="{c}" stroke="#9fb39b"/>'+label(240,y+31,nodes[3-i],22)
  s+=f'<circle cx="240" cy="280" r="55" fill="{green}"/>'+label(240,280,nodes[0],24,'white')
 s+='</svg>'
 (root/'assets'/f'{id}.svg').write_text(s)
print('Built 14 conceptual figures')
