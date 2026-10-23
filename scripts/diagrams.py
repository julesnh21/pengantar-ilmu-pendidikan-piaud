import json,html,textwrap
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for l in json.loads((root/'content/course.json').read_text()):
 s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" role="img"><title>'+html.escape(l['title'])+'</title><rect width="720" height="280" rx="16" fill="#fffef9"/><text x="30" y="34" font-family="Arial,sans-serif" font-size="11" font-weight="bold" letter-spacing="2" fill="#52684c">EMPAT PERTIMBANGAN UNTUK MEMBACA KASUS</text>'
 for i,label in enumerate(l['diagram']):
  x=25+(i%2)*345;y=58+(i//2)*103;color=['#e7f0df','#faebd8','#f4f0d5','#e6eeea'][i]
  s+=f'<rect x="{x}" y="{y}" width="325" height="86" rx="14" fill="{color}"/><circle cx="{x+32}" cy="{y+42}" r="18" fill="#205b48"/><text x="{x+32}" y="{y+47}" text-anchor="middle" font-family="Arial" font-size="13" fill="white">{i+1:02}</text>'
  lines=textwrap.wrap(label,width=26)
  for j,line in enumerate(lines):s+=f'<text x="{x+64}" y="{y+40+j*20-(len(lines)-1)*9}" font-family="Arial,sans-serif" font-size="16" fill="#193e36">{html.escape(line)}</text>'
 s+='</svg>'; (root/'assets'/f'{l["id"]}.svg').write_text(s)
