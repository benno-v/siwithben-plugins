#!/usr/bin/env python3
"""Render a plan as one self-contained interactive HTML Gantt chart (inline CSS, JS and SVG, no network).

By Benjamin Vermeulen, @SIwithBen. MIT licence.
"""
import datetime as dt
import html
import json

from gantt_core import ISSUE_LABELS, phase_rows

CSS = """
:root{--navy:#1b2a4a;--teal:#13838f;--teal-d:#0d5f68;--amber:#f0a202;--amber-d:#b97a00;--red:#c8423b;
--ink:#1d2433;--muted:#5b6578;--line:#dfe4ec;--band:#f3f6fa;--bg:#ffffff;--rowh:30px;--headh:52px}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;color:var(--ink);background:#f6f8fb;font-size:14px}
header.top{background:var(--navy);color:#fff;padding:18px 24px}
header.top h1{margin:0 0 4px;font-size:22px;font-weight:600}
header.top p{margin:0;color:#c9d3e6;font-size:13px}
main{padding:16px 24px 32px}
.cards{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:14px}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 14px;min-width:120px}
.card b{display:block;font-size:20px;color:var(--navy)}
.card span{font-size:12px;color:var(--muted)}
.card.warn b{color:var(--amber-d)}
.toolbar{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:10px}
.toolbar button{font:inherit;font-size:13px;border:1px solid var(--line);background:#fff;color:var(--navy);padding:5px 12px;border-radius:6px;cursor:pointer}
.toolbar button.on{background:var(--teal);border-color:var(--teal);color:#fff}
.toolbar .hint{color:var(--muted);font-size:12px;margin-left:6px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:12px;color:var(--muted);margin-left:auto}
.legend i{display:inline-block;width:18px;height:10px;border-radius:2px;vertical-align:middle;margin-right:5px}
.legend i.d{width:10px;height:10px;transform:rotate(45deg);border-radius:0}
.gantt{display:flex;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.left{flex:0 0 540px;border-right:1px solid var(--line);overflow:hidden}
.right{flex:1 1 auto;overflow-x:auto;overflow-y:hidden;position:relative}
table.tt{border-collapse:collapse;width:100%;table-layout:fixed}
table.tt th,table.tt td{height:var(--rowh);padding:0 8px;border-bottom:1px solid var(--line);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:12.5px;text-align:left}
table.tt thead th{height:var(--headh);background:var(--band);color:var(--muted);font-weight:600;font-size:12px;vertical-align:bottom;padding-bottom:8px}
table.tt tr.phase td{background:var(--band);font-weight:600;color:var(--navy)}
table.tt tr.task:hover td{background:#eef7f8}
table.tt tr.crit td.name{box-shadow:inset 3px 0 0 var(--amber)}
.c-id{width:48px}.c-own{width:112px}.c-d{width:92px}
.right svg{display:block}
.bar{fill:var(--teal)}.bar-p{fill:var(--teal-d)}
.ms{fill:var(--navy)}
.show-crit .bar.crit{fill:var(--amber)}.show-crit .bar-p.crit{fill:var(--amber-d)}.show-crit .ms.crit{fill:var(--amber-d)}
.dep{fill:none;stroke:#8a96aa;stroke-width:1.2}
.show-crit .dep.crit{stroke:var(--amber-d);stroke-width:1.6}
.today{stroke:var(--red);stroke-width:2;stroke-dasharray:4 3}
.today-l{fill:var(--red);font-size:10px;font-weight:600}
.grid{stroke:var(--line)}.grid.major{stroke:#c3cad6}
.wkend{fill:#f7f8fb}
.phase-band{fill:var(--band)}
.hdr{fill:var(--muted);font-size:11px}.hdr.top{fill:var(--navy);font-weight:600}
.lbl{fill:var(--ink);font-size:11px}
#tip{position:fixed;pointer-events:none;background:var(--navy);color:#fff;font-size:12px;line-height:1.45;padding:8px 10px;border-radius:6px;box-shadow:0 4px 14px rgba(0,0,0,.2);display:none;z-index:10;max-width:320px}
#tip b{display:block;font-size:13px;margin-bottom:2px}
.panels{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}
.panel{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px 16px}
.panel h2{font-size:15px;margin:0 0 8px;color:var(--navy)}
.panel table{border-collapse:collapse;width:100%;font-size:12.5px}
.panel td,.panel th{border-bottom:1px solid var(--line);padding:5px 6px;text-align:left;vertical-align:top}
.panel ul{margin:0;padding-left:18px;font-size:12.5px}
.panel li{margin:3px 0}
.panel .tag{display:inline-block;background:#fff4dc;color:#7a5200;border-radius:4px;padding:0 6px;font-size:11px;margin-right:6px}
.empty{color:var(--muted);font-style:italic}
.cp{font-size:12.5px;color:var(--muted);margin:10px 0 0}
footer{color:var(--muted);font-size:12px;margin-top:18px}
@media (max-width:860px){.left{flex-basis:230px}.c-own,.c-d,td.own,td.d{display:none}.panels{grid-template-columns:1fr}main{padding:12px}}
@media print{@page{size:landscape;margin:10mm}body{background:#fff}.toolbar button,.toolbar .hint{display:none}
header.top{background:#fff;color:var(--navy);padding:0 0 8px}header.top p{color:var(--muted)}
.right{overflow:visible}.gantt,.panel,.card{border-color:#bbb}.panels{grid-template-columns:1fr 1fr;break-inside:avoid}
#tip{display:none!important}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""

JS = r"""
(function(){
var D=JSON.parse(document.getElementById('plan-data').textContent);
var DAY=86400000, ROWH=30, HEADH=52, PAD=2;
var ZOOM={day:30,week:9,month:3};
var px=D.rows.length?ZOOM[D.defaultZoom]:ZOOM.week, zoomName=D.defaultZoom;
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function ms(s){var p=s.split('-');return Date.UTC(+p[0],+p[1]-1,+p[2]);}
var MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
function fmt(s){if(!s)return 'Not set';var d=new Date(ms(s));return d.getUTCDate()+' '+MON[d.getUTCMonth()]+' '+d.getUTCFullYear();}
var right=document.getElementById('chart'), tip=document.getElementById('tip');
if(!D.rows.length){right.innerHTML='<p class="empty" style="padding:16px">No scheduled tasks to draw yet. See the unscheduled list below.</p>';return;}
var t0=ms(D.range[0])-PAD*DAY, t1=ms(D.range[1])+(PAD+1)*DAY, days=Math.round((t1-t0)/DAY);
var rowOf={}; D.rows.forEach(function(r,i){if(r.kind==='task')rowOf[r.id]=i;});
function x(s){return (ms(s)-t0)/DAY*px;}
function draw(){
  var W=Math.max(days*px+180, right.clientWidth||600), H=HEADH+D.rows.length*ROWH, o=[];
  o.push('<svg width="'+W+'" height="'+H+'" role="img" aria-label="Gantt chart"><defs>'+
    '<marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#8a96aa"/></marker>'+
    '<marker id="ahc" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b97a00"/></marker></defs>');
  D.rows.forEach(function(r,i){if(r.kind==='phase')o.push('<rect class="phase-band" x="0" y="'+(HEADH+i*ROWH)+'" width="'+W+'" height="'+ROWH+'"/>');});
  var lastMonth=-1, lastYear=-1;
  for(var i=0;i<days;i++){
    var d=new Date(t0+i*DAY), dx=i*px, wd=d.getUTCDay(), dd=d.getUTCDate();
    if(zoomName!=='month'&&px>=6&&(wd===0||wd===6))o.push('<rect class="wkend" x="'+dx+'" y="'+HEADH+'" width="'+px+'" height="'+(H-HEADH)+'"/>');
    var top = zoomName==='month' ? d.getUTCFullYear()!==lastYear : d.getUTCMonth()!==lastMonth;
    if(top){
      o.push('<line class="grid major" x1="'+dx+'" x2="'+dx+'" y1="0" y2="'+H+'"/>');
      var segEnd = zoomName==='month' ? Date.UTC(d.getUTCFullYear()+1,0,1) : Date.UTC(d.getUTCFullYear(),d.getUTCMonth()+1,1);
      var segDays = Math.min((segEnd-(t0+i*DAY))/DAY, days-i);
      if(segDays*px>=70) o.push('<text class="hdr top" x="'+(dx+4)+'" y="18">'+(zoomName==='month'?d.getUTCFullYear():MON[d.getUTCMonth()]+' '+d.getUTCFullYear())+'</text>');
      lastMonth=d.getUTCMonth(); lastYear=d.getUTCFullYear();
    }
    if(zoomName==='day'){o.push('<line class="grid" x1="'+dx+'" x2="'+dx+'" y1="28" y2="'+H+'"/><text class="hdr" x="'+(dx+px/2)+'" y="44" text-anchor="middle">'+dd+'</text>');}
    else if(zoomName==='week'&&wd===1){o.push('<line class="grid" x1="'+dx+'" x2="'+dx+'" y1="28" y2="'+H+'"/><text class="hdr" x="'+(dx+3)+'" y="44">'+dd+'</text>');}
    else if(zoomName==='month'&&dd===1){o.push('<line class="grid" x1="'+dx+'" x2="'+dx+'" y1="28" y2="'+H+'"/><text class="hdr" x="'+(dx+3)+'" y="44">'+MON[d.getUTCMonth()]+'</text>');}
  }
  o.push('<line class="grid major" x1="0" x2="'+W+'" y1="'+(HEADH-0.5)+'" y2="'+(HEADH-0.5)+'"/>');
  D.rows.forEach(function(r,i){
    if(r.kind!=='task')return;
    var y=HEADH+i*ROWH, cy=y+ROWH/2;
    r.deps.forEach(function(p){
      if(!(p in rowOf))return;
      var a=D.rows[rowOf[p]], ay=HEADH+rowOf[p]*ROWH+ROWH/2;
      var x1=a.milestone?x(a.end)+px+7:x(a.end)+px, x2=r.milestone?x(r.end)+px-8:x(r.start);
      var c=(a.critical&&r.critical)?' crit':'', m=c?'ahc':'ah', path;
      if(x2-x1>=10){path='M'+x1+','+ay+' H'+(x1+5)+' V'+cy+' H'+x2;}
      else{var mid=cy+(cy>ay?-ROWH/2:ROWH/2);path='M'+x1+','+ay+' h5 V'+mid+' H'+(x2-8)+' V'+cy+' H'+x2;}
      o.push('<path class="dep'+c+'" d="'+path+'" marker-end="url(#'+m+')"/>');
    });
  });
  D.rows.forEach(function(r,i){
    if(r.kind!=='task')return;
    var y=HEADH+i*ROWH, cy=y+ROWH/2, c=r.critical?' crit':'';
    if(r.milestone){
      var mx=x(r.end)+px, s=7;
      o.push('<polygon class="ms'+c+'" data-i="'+i+'" points="'+mx+','+(cy-s)+' '+(mx+s)+','+cy+' '+mx+','+(cy+s)+' '+(mx-s)+','+cy+'"/>');
      o.push('<text class="lbl" x="'+(mx+11)+'" y="'+(cy+4)+'">'+esc(r.task)+'</text>');
    }else{
      var bx=x(r.start), bw=Math.max(x(r.end)+px-bx,2);
      o.push('<rect class="bar'+c+'" data-i="'+i+'" x="'+bx+'" y="'+(y+7)+'" width="'+bw+'" height="'+(ROWH-14)+'" rx="3"/>');
      if(r.pct>0)o.push('<rect class="bar-p'+c+'" data-i="'+i+'" x="'+bx+'" y="'+(y+ROWH-10)+'" width="'+(bw*Math.min(r.pct,100)/100)+'" height="3" rx="1"/>');
      if(bw<160)o.push('<text class="lbl" x="'+(bx+bw+6)+'" y="'+(cy+4)+'">'+esc(r.task)+'</text>');
    }
  });
  if(D.todayInRange){var tx=x(D.today)+px/2;o.push('<line class="today" x1="'+tx+'" x2="'+tx+'" y1="'+HEADH+'" y2="'+H+'"/><text class="today-l" x="'+(tx+4)+'" y="'+(HEADH+11)+'">Today</text>');}
  o.push('</svg>');
  right.innerHTML=o.join('');
}
function setZoom(name){
  zoomName=name; px=ZOOM[name];
  document.querySelectorAll('[data-zoom]').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-zoom')===name);});
  draw();
}
document.querySelectorAll('[data-zoom]').forEach(function(b){b.addEventListener('click',function(){setZoom(b.getAttribute('data-zoom'));});});
var critBtn=document.getElementById('crit');
critBtn.addEventListener('click',function(){var on=document.body.classList.toggle('show-crit');critBtn.classList.toggle('on',on);});
right.addEventListener('wheel',function(e){
  if(!e.ctrlKey)return;
  e.preventDefault();
  var rect=right.getBoundingClientRect(), mx=e.clientX-rect.left+right.scrollLeft, dayAt=mx/px;
  px=Math.min(60,Math.max(1,px*(e.deltaY<0?1.15:1/1.15)));
  zoomName=px>=20?'day':(px>=5?'week':'month');
  document.querySelectorAll('[data-zoom]').forEach(function(b){b.classList.remove('on');});
  draw(); right.scrollLeft=dayAt*px-(e.clientX-rect.left);
},{passive:false});
function showTip(i,e){
  var r=D.rows[i]; if(!r||r.kind!=='task'){tip.style.display='none';return;}
  tip.innerHTML='<b>'+esc(r.id+'  '+r.task)+'</b>'+(r.phase?esc(r.phase)+'<br>':'')+'Owner: '+esc(r.owner||'Not set')+'<br>'+
    (r.milestone?'Date: '+fmt(r.end):fmt(r.start)+' to '+fmt(r.end))+'<br>Status: '+esc(r.status||'Not set')+
    (r.pct!=null?' ('+Math.round(r.pct)+'%)':'')+(r.deps.length?'<br>Depends on: '+esc(r.deps.join(', ')):'')+
    (r.critical?'<br>On the critical path':(r.float!=null?'<br>Float: '+r.float+' '+D.unit:''))+(r.derived?'<br>Dates derived from dependencies or duration':'');
  tip.style.display='block';
  var x0=e.clientX+14, y0=e.clientY+14;
  if(x0+tip.offsetWidth>window.innerWidth-8)x0=e.clientX-tip.offsetWidth-14;
  if(y0+tip.offsetHeight>window.innerHeight-8)y0=e.clientY-tip.offsetHeight-14;
  tip.style.left=x0+'px'; tip.style.top=y0+'px';
}
function onMove(e){var el=e.target.closest('[data-i]');if(el)showTip(+el.getAttribute('data-i'),e);else tip.style.display='none';}
right.addEventListener('mousemove',onMove); right.addEventListener('mouseleave',function(){tip.style.display='none';});
var left=document.getElementById('left');
left.addEventListener('mousemove',onMove); left.addEventListener('mouseleave',function(){tip.style.display='none';});
var saved=null;
window.addEventListener('beforeprint',function(){saved=[px,zoomName];var avail=Math.max(400,document.querySelector('.gantt').clientWidth-document.getElementById('left').clientWidth-4);px=avail/days;zoomName=px>=20?'day':(px>=5?'week':'month');draw();});
window.addEventListener('afterprint',function(){if(saved){px=saved[0];zoomName=saved[1];draw();}});
window.addEventListener('resize',draw);
setZoom(D.defaultZoom);
if(D.todayInRange&&x(D.today)>right.clientWidth-40){right.scrollLeft=Math.max(0,x(D.today)-right.clientWidth/3);}
})();
"""


def _e(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def _fmt(d):
    return f"{d.day} {d.strftime('%b %Y')}" if d else "Not set"


def render_html(plan, out_path):
    rows = []
    for kind, item in phase_rows(plan):
        if kind == "phase":
            rows.append({"kind": "phase", "name": item})
        else:
            t = item
            rows.append({"kind": "task", "id": t["id"], "task": t["task"], "phase": t["phase"], "owner": t["owner"],
                         "start": t["start"].isoformat(), "end": t["end"].isoformat(), "milestone": t["milestone"],
                         "status": t["status"], "pct": t["percent_complete"], "critical": t["critical"],
                         "deps": t["depends_on"], "derived": t["derived"], "float": t["float_days"]})
    rng = plan["range"]
    span = (rng[1] - rng[0]).days + 1 if rng else 0
    unit = "working days" if plan["day_mode"] == "working" else "calendar days"
    data = {"rows": rows, "range": [rng[0].isoformat(), rng[1].isoformat()] if rng else None,
            "today": plan["today"].isoformat(), "todayInRange": plan["today_in_range"], "unit": unit,
            "defaultZoom": "day" if span <= 45 else ("week" if span <= 200 else "month")}
    payload = json.dumps(data).replace("</", "<\\/")

    trs = []
    for i, r in enumerate(rows):
        if r["kind"] == "phase":
            trs.append(f'<tr class="phase"><td colspan="5">{_e(r["name"])}</td></tr>')
        else:
            t = next(x for x in plan["tasks"] if x["id"] == r["id"])
            mark = "&#9670; " if t["milestone"] else ""
            trs.append(f'<tr class="task{" crit" if t["critical"] else ""}" data-i="{i}"><td>{_e(t["id"])}</td>'
                       f'<td class="name">{mark}{_e(t["task"])}</td><td class="own">{_e(t["owner"] or "Not set")}</td>'
                       f'<td class="d">{_fmt(t["start"])}</td><td class="d">{_fmt(t["end"])}</td></tr>')

    if plan["unscheduled"]:
        uns = "<table><tr><th>ID</th><th>Task</th><th>Owner</th><th>Why it is not drawn</th></tr>" + "".join(
            f"<tr><td>{_e(t['id'])}</td><td>{_e(t['task'])}</td><td>{_e(t['owner'] or 'Not set')}</td><td>{_e(t['reason'])}</td></tr>"
            for t in plan["unscheduled"]) + "</table>"
    else:
        uns = '<p class="empty">None. Every task has dates or can be derived.</p>'
    warns = [i for i in plan["issues"] if i["type"] != "unscheduled"]
    if warns:
        warn_html = "<ul>" + "".join(
            f'<li><span class="tag">{_e(ISSUE_LABELS.get(i["type"], i["type"]))}</span>{_e(i["message"])}</li>' for i in warns) + "</ul>"
    else:
        warn_html = '<p class="empty">No issues found.</p>'
    if plan.get("date_note"):
        warn_html += f'<p class="cp">{_e(plan["date_note"])}</p>'

    counts = [(sum(t["state"] == "scheduled" for t in plan["tasks"]), "tasks drawn", False),
              (sum(t["milestone"] and t["state"] == "scheduled" for t in plan["tasks"]), "milestones", False),
              (len(plan["critical_path"]), "on the critical path", False),
              (len(plan["unscheduled"]), "unscheduled, needs dates", bool(plan["unscheduled"])),
              (len(warns), "warnings", bool(warns))]
    cards = "".join(f'<div class="card{" warn" if w else ""}"><b>{n}</b><span>{label}</span></div>' for n, label, w in counts)
    sub = (f"{_fmt(rng[0])} to {_fmt(rng[1])} ({span} days). Durations in {unit}." if rng else f"No scheduled tasks yet. Durations in {unit}.")
    cp = (f'<p class="cp"><b>Critical path:</b> {_e(" > ".join(plan["critical_path"]))}</p>' if plan["critical_path"] else "")

    doc = f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{_e(plan['name'])}: Gantt chart</title><style>{CSS}</style></head>
<body class="show-crit">
<header class="top"><h1>{_e(plan['name'])}</h1><p>Gantt chart. {_e(sub)}</p></header>
<main>
<div class="cards">{cards}</div>
<div class="toolbar">
<button data-zoom="day">Day</button><button data-zoom="week">Week</button><button data-zoom="month">Month</button>
<button id="crit" class="on">Critical path</button><span class="hint">Ctrl + scroll to zoom</span>
<div class="legend"><span><i style="background:var(--teal)"></i>Task</span><span><i style="background:var(--amber)"></i>Critical</span>
<span><i class="d" style="background:var(--navy)"></i>Milestone</span><span><i style="background:var(--red);height:2px"></i>Today</span></div>
</div>
<div class="gantt">
<div class="left" id="left"><table class="tt"><thead><tr><th class="c-id">ID</th><th>Task</th><th class="c-own">Owner</th><th class="c-d">Start</th><th class="c-d">End</th></tr></thead>
<tbody>{''.join(trs)}</tbody></table></div>
<div class="right" id="chart"></div>
</div>
{cp}
<div class="panels">
<section class="panel"><h2>Unscheduled, needs dates ({len(plan['unscheduled'])})</h2>{uns}</section>
<section class="panel"><h2>Checks ({len(warns)})</h2>{warn_html}</section>
</div>
<footer>Generated {_fmt(plan['today'])}. Draft for review: check every date, owner and dependency before sharing.</footer>
</main>
<div id="tip"></div>
<script type="application/json" id="plan-data">{payload}</script>
<script>{JS}</script>
</body></html>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return out_path
