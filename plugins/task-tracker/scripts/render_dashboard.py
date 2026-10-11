#!/usr/bin/env python3
"""Render TASKS.md as a self-contained dashboard.html (no external files or URLs).

Python 3 standard library only.

  render_dashboard.py --tasks TASKS.md --out dashboard.html [--today YYYY-MM-DD] [--title "Tasks"]

The page cannot write TASKS.md. Ticks and edits become a task-tracker-changes block (Copy changes)
or a tasks-changes.json file (Download changes) that apply_changes.py applies.
Prints a JSON summary.
"""
import argparse
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tasks_md as tm  # noqa: E402

URL_RE = re.compile(r"(https?://[^\s<>()\[\]]+)")
PLACEHOLDER_RE = re.compile(r"\{\{([A-Z_]+)\}\}")
JSON_ESCAPES = {"<": "\\u003c", ">": "\\u003e", "&": "\\u0026", "\u2028": "\\u2028", "\u2029": "\\u2029"}


def esc(text):
    return html.escape(text or "", quote=True)


def inline_json(data):
    """JSON that is safe inside <script>: no <, >, & or JS line separators survive as raw characters."""
    text = json.dumps(data, ensure_ascii=False)
    return re.sub("[<>&\u2028\u2029]", lambda m: JSON_ESCAPES[m.group(0)], text)


def fill(template, values):
    """Substitute every {{KEY}} in one pass, so placeholders inside the values are never expanded."""
    return PLACEHOLDER_RE.sub(lambda m: values.get(m.group(1), m.group(0)), template)


def d(iso):
    return dt.date.fromisoformat(iso) if tm.is_date(iso) else None


def fmt_date(day):
    return f"{day:%a} {day.day} {day:%b}"


def due_info(due, today, week_end):
    day = d(due)
    if not day:
        return ("no due date", "muted") if not due else (due, "muted")
    n = (day - today).days
    if n < 0:
        return f"{fmt_date(day)} ({-n} day{'s' if n < -1 else ''} overdue)", "overdue"
    if n == 0:
        return "today", "today"
    return fmt_date(day), "soon" if day <= week_end else ""


def source_html(source):
    parts = URL_RE.split(source or "")
    out = []
    for i, part in enumerate(parts):
        if i % 2:
            out.append(f'<a href="{esc(part)}" target="_blank" rel="noopener noreferrer">link</a>')
        else:
            out.append(esc(part))
    return "".join(out) or '<span class="flag">no source</span>'


def task_item(row, kind, today, week_end, duplicate=False):
    rid = esc(row["id"])
    owner = row["owner"] if not tm.is_unassigned(row["owner"]) else ""
    due_text, due_class = due_info(row["due"], today, week_end)
    tick = ""
    buttons = ""
    if duplicate:
        tick = '<span class="needs" title="Duplicate ID, so no controls">!</span>'
        buttons = '<div class="acts flag">Duplicate ID: fix it in TASKS.md before changing this task.</div>'
    elif kind == "open":
        tick = (f'<label class="tick-wrap"><input type="checkbox" class="tick" data-id="{rid}" '
                f'aria-label="Mark {rid} done"></label>')
        buttons = f'<div class="acts no-print"><button type="button" data-act="edit" data-id="{rid}">Edit</button></div>'
    elif kind == "proposed":
        tick = '<span class="needs" title="Needs your input, so no tick box">?</span>'
        buttons = (f'<div class="acts no-print">'
                   f'<button type="button" class="ok" data-act="approve" data-id="{rid}">Approve</button>'
                   f'<button type="button" class="no" data-act="reject" data-id="{rid}">Reject</button>'
                   f'<button type="button" data-act="edit" data-id="{rid}">Edit</button></div>')
    else:
        tick = '<span class="donemark" aria-hidden="true">&#10003;</span>'
    meta = [f'<span class="owner{" flag" if not owner else ""}" data-f="owner">{esc(owner or "Unassigned")}</span>']
    if kind == "done":
        meta.append(f'<span class="due muted">{esc(tm.done_date(row) and "done " + fmt_date(d(tm.done_date(row))))}</span>')
    else:
        meta.append(f'<span class="due {due_class}" data-f="due">{esc(due_text)}</span>')
        meta.append(f'<span class="status st-{esc(row["status"].lower().replace(" ", "-"))}" data-f="status">{esc(row["status"])}</span>')
    notes = f'<div class="notes">{esc(row["notes"])}</div>' if row["notes"] else ""
    return (f'<li class="task {kind}" data-id="{rid}">{tick}<div class="body">'
            f'<div class="line1"><span class="tid">{rid}</span> <span class="action" data-f="action">{esc(row["action"])}</span>'
            f' <span class="pending-label"></span></div>'
            f'<div class="meta">{" ".join(meta)}</div>'
            f'<div class="src">Source: {source_html(row["source"])}</div>{notes}</div>{buttons}</li>')


def panel(pid, title, items, empty, intro=""):
    body = "".join(items) if items else f'<li class="empty">{esc(empty)}</li>'
    return (f'<section id="panel-{pid}" class="panel"><h2>{esc(title)} <span class="n">{len(items)}</span></h2>'
            f'{intro}<ul class="tasks">{body}</ul></section>')


def due_key(row):
    return (row["due"] or "9999-99-99", row["id"])


def build(doc, today, title="Tasks", generated=None):
    rev = tm.revision(doc)
    generated = generated or dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    week_start = today - dt.timedelta(days=today.weekday())
    week_end = week_start + dt.timedelta(days=6)
    open_rows = sorted(doc.rows("open"), key=due_key)
    proposed = doc.rows("proposed")
    done_rows = doc.rows("done")
    overdue = [r for r in open_rows if d(r["due"]) and d(r["due"]) < today]
    this_week = [r for r in open_rows if d(r["due"]) and today <= d(r["due"]) <= week_end]
    due_today = [r for r in this_week if d(r["due"]) == today]
    done_week = [r for r in done_rows if d(tm.done_date(r)) and d(tm.done_date(r)) >= week_start]
    recent = sorted((r for r in done_rows if d(tm.done_date(r)) and d(tm.done_date(r)) >= today - dt.timedelta(days=14)),
                    key=lambda r: tm.done_date(r), reverse=True)[:15]

    dups = set(tm.duplicate_ids(doc))

    def items(rows, kind):
        return [task_item(r, kind, today, week_end, r["id"] in dups) for r in rows]

    owners = {}
    for r in open_rows:
        owners.setdefault("" if tm.is_unassigned(r["owner"]) else r["owner"], []).append(r)
    groups = []
    for owner in sorted(owners, key=lambda o: (o != "", o.lower())):
        label = owner or "Unassigned"
        groups.append(f'<li class="group{" flag" if not owner else ""}">{esc(label)} ({len(owners[owner])})</li>')
        groups += items(owners[owner], "open")
    owner_panel = (f'<section id="panel-owner" class="panel wide"><h2>Open by owner <span class="n">{len(open_rows)}</span></h2>'
                   f'<ul class="tasks">{"".join(groups) or "<li class=empty>Nothing open.</li>"}</ul></section>')

    kpis = [("Open", len(open_rows), ""), ("Due today", len(due_today), "today" if due_today else ""),
            ("Overdue", len(overdue), "overdue" if overdue else ""),
            ("Proposed", len(proposed), "proposed" if proposed else ""), ("Done this week", len(done_week), "good")]
    kpi_html = "".join(f'<div class="kpi {c}"><div class="kv">{n}</div><div class="kl">{esc(label)}</div></div>'
                       for label, n, c in kpis)

    data = {
        "revision": rev, "today": today.isoformat(), "weekEnd": week_end.isoformat(),
        "statuses": tm.OPEN_STATUSES,
        "tasks": {r["id"]: {"section": kind, **{f: r[f] for f in tm.FIELDS[1:]}}
                  for kind, r in doc.all_rows() if r["id"] not in dups},
        "owners": sorted({r["owner"] for _, r in doc.all_rows() if not tm.is_unassigned(r["owner"])}),
    }

    proposed_intro = ('<p class="hint">These came from a sweep but need your input: check the owner and due date '
                      'against the source, then Approve, Edit or Reject. No tick boxes here on purpose.</p>')
    panels = "".join([
        panel("overdue", "Overdue", items(overdue, "open"), "Nothing overdue."),
        panel("week", f"Due today and this week (to {fmt_date(week_end)})", items(this_week, "open"), "Nothing due this week."),
        panel("proposed", "Proposed, needs your approval", items(proposed, "proposed"), "Nothing waiting for approval.",
              proposed_intro),
        owner_panel,
        panel("done", "Done recently (14 days)", items(recent, "done"), "Nothing marked done in the last 14 days."),
    ])
    page = fill(PAGE, {
        "TITLE": esc(title), "REV": esc(rev), "GENERATED": esc(generated), "TODAY": esc(fmt_date(today)),
        "LAST_SWEEP": esc(doc.last_sweep or "never"), "KPIS": kpi_html, "PANELS": panels,
        "DATA": inline_json(data), "CSS": CSS, "JS": EDIT_DIFF_JS + JS,
    })
    counts = {"open": len(open_rows), "due_today": len(due_today), "overdue": len(overdue),
              "due_this_week": len(this_week), "proposed": len(proposed), "done_this_week": len(done_week)}
    return page, rev, counts


PAGE = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="task-tracker-revision" content="{{REV}}">
<title>{{TITLE}}</title>
<style>{{CSS}}</style>
</head>
<body>
<header class="top">
  <div>
    <h1>{{TITLE}}</h1>
    <p class="sub">{{TODAY}} &middot; from TASKS.md, revision <code>{{REV}}</code> &middot; rendered {{GENERATED}} &middot; last sweep {{LAST_SWEEP}}</p>
  </div>
  <div class="tools no-print">
    <input id="tt-search" type="search" placeholder="Search tasks, owners, sources" aria-label="Search">
    <button type="button" id="tt-add-toggle">Add task</button>
  </div>
</header>
<p class="howto no-print">Tick a task when it's done, or use Edit to change the action, owner, due date or status.
Nothing changes in TASKS.md until you click <b>Copy changes</b> and paste the block to Claude
(or <b>Download changes</b> and put <code>tasks-changes.json</code> in your tracker folder).
<span id="tt-storage-note"></span></p>
<noscript><p class="howto">This page needs JavaScript for ticking and editing; without it, it is a read-only view.</p></noscript>
<form id="tt-add" class="addform no-print" hidden>
  <input name="action" placeholder="Action" required aria-label="Action">
  <input name="owner" placeholder="Owner" list="tt-owners" aria-label="Owner">
  <input name="due" type="date" aria-label="Due date">
  <button type="submit">Add to changes</button>
</form>
<section class="kpis">{{KPIS}}</section>
<main class="grid">{{PANELS}}</main>
<aside id="tt-tray" class="tray no-print" aria-live="polite">
  <div class="trayhead">
    <b>Changes (<span id="tt-count">0</span>)</b>
    <button type="button" id="tt-copy" disabled>Copy changes</button>
    <button type="button" id="tt-download" disabled>Download changes</button>
    <button type="button" id="tt-clear" disabled>Clear all</button>
    <button type="button" id="tt-toggle" aria-expanded="false">Show</button>
  </div>
  <div id="tt-traybody" hidden>
    <ul id="tt-ops"></ul>
    <p id="tt-msg" class="hint"></p>
    <textarea id="tt-out" readonly hidden rows="5" aria-label="Changes block"></textarea>
  </div>
</aside>
<datalist id="tt-owners"></datalist>
<footer>task-tracker by SI with Ben &middot; TASKS.md is the source of truth; this page never changes it by itself.</footer>
<script type="application/json" id="tt-data">{{DATA}}</script>
<script>{{JS}}</script>
</body>
</html>
"""

CSS = """
:root{--bg:#f5f6f8;--card:#fff;--ink:#1d2330;--muted:#6b7280;--line:#e3e6eb;--accent:#2f5bd3;--red:#c62828;--amber:#b26a00;--green:#2e7d32;--violet:#6a3fb5}
*{box-sizing:border-box}
body{margin:0;padding:20px 20px 110px;background:var(--bg);color:var(--ink);font:14px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
h1{margin:0;font-size:24px}h2{font-size:15px;margin:0 0 8px;display:flex;gap:8px;align-items:center}
.top{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap}
.sub{margin:4px 0 0;color:var(--muted)}code{font-size:12px;background:#eef0f4;padding:1px 4px;border-radius:4px}
.tools{display:flex;gap:8px}#tt-search{padding:7px 10px;border:1px solid var(--line);border-radius:8px;min-width:240px}
button{font:inherit;padding:5px 10px;border:1px solid var(--line);border-radius:7px;background:#fff;cursor:pointer}
button:hover{border-color:var(--accent)}button:disabled{opacity:.45;cursor:default}
button.ok{color:var(--green)}button.no{color:var(--red)}
.howto{background:#eef3ff;border:1px solid #d5e0ff;border-radius:10px;padding:8px 12px;margin:14px 0}
.addform{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}.addform input{padding:6px 8px;border:1px solid var(--line);border-radius:7px}
.addform input[name=action]{flex:1;min-width:220px}
.kpis{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:14px 0}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
.kv{font-size:28px;font-weight:700}.kl{color:var(--muted)}
.kpi.overdue .kv{color:var(--red)}.kpi.today .kv{color:var(--amber)}.kpi.proposed .kv{color:var(--violet)}.kpi.good .kv{color:var(--green)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;break-inside:avoid}
.panel.wide{grid-column:1/-1}.n{background:#eef0f4;border-radius:10px;padding:0 8px;font-size:12px;color:var(--muted)}
#panel-overdue{border-top:3px solid var(--red)}#panel-week{border-top:3px solid var(--amber)}#panel-proposed{border-top:3px solid var(--violet)}#panel-done{border-top:3px solid var(--green)}
.tasks{list-style:none;margin:0;padding:0}
.task{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-top:1px solid var(--line)}
.task:first-child{border-top:0}.task .body{flex:1;min-width:0}
.tick-wrap input{width:18px;height:18px;margin:2px 0 0;cursor:pointer}
.needs{display:inline-flex;width:18px;height:18px;border-radius:50%;background:var(--violet);color:#fff;font-weight:700;font-size:12px;align-items:center;justify-content:center;margin-top:2px}
.donemark{color:var(--green);font-weight:700;width:18px;text-align:center}
.tid{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}.action{font-weight:600}
.meta{display:flex;gap:10px;flex-wrap:wrap;font-size:13px;margin-top:2px}
.src,.notes{font-size:12px;color:var(--muted);overflow-wrap:anywhere}.src a{color:var(--accent)}
.flag{color:var(--red);font-weight:600}.overdue{color:var(--red);font-weight:600}.today{color:var(--amber);font-weight:600}.soon{color:var(--amber)}.muted{color:var(--muted)}
.status{background:#eef0f4;border-radius:6px;padding:0 6px}.st-blocked{background:#fde8e8;color:var(--red)}.st-waiting{background:#fff4e0;color:var(--amber)}.st-in-progress{background:#e8f0ff;color:var(--accent)}
.acts{display:flex;gap:6px;flex-wrap:wrap}
.group{font-weight:700;padding:10px 0 2px;border-top:1px solid var(--line)}.group:first-child{border-top:0}
.empty{color:var(--muted);padding:6px 0}.hint{color:var(--muted);font-size:12px;margin:0 0 6px}
.pending-label{font-size:12px;color:var(--accent);font-weight:600}
.pending-done .action{text-decoration:line-through;color:var(--muted)}
.pending-approve{background:#f0faf1}.pending-reject{background:#fdf0f0}.pending-reject .action{text-decoration:line-through}
.edited .action,.edited [data-f]{color:var(--accent)}
.editor{display:grid;grid-template-columns:2fr 1fr 1fr 1fr auto auto;gap:6px;margin-top:6px}
.editor input,.editor select{padding:5px 6px;border:1px solid var(--line);border-radius:6px;font:inherit;min-width:0}
.tray{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid var(--line);box-shadow:0 -4px 16px rgba(0,0,0,.06);padding:10px 20px;max-height:55vh;overflow:auto}
.trayhead{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.trayhead b{margin-right:auto}
#tt-ops{list-style:none;padding:0;margin:8px 0}#tt-ops li{display:flex;justify-content:space-between;gap:8px;padding:4px 0;border-top:1px solid var(--line)}
#tt-out{width:100%;font:12px ui-monospace,Menlo,Consolas,monospace}
footer{color:var(--muted);font-size:12px;margin-top:18px}
@media (max-width:900px){.grid{grid-template-columns:1fr}.kpis{grid-template-columns:repeat(2,1fr)}.editor{grid-template-columns:1fr 1fr}}
@media print{body{background:#fff;padding:0}.no-print{display:none!important}.panel{border-color:#999}.grid{grid-template-columns:1fr}.kpi{border-color:#999}}
"""

EDIT_DIFF_JS = r"""
function ttUnassigned(o) { return ['', 'unassigned', 'tbc', '?'].indexOf((o || '').trim().toLowerCase()) >= 0; }
function ttEditDiff(orig, shownDue, input) {
  var next = { action: input.action, owner: input.owner, due: input.dueTouched ? input.due : shownDue };
  if (input.status !== undefined) next.status = input.status;
  var diff = {}, n = 0;
  for (var f in next) {
    var was = orig[f] || '';
    if (f === 'owner' && ttUnassigned(was)) was = '';
    if (next[f] !== was) { diff[f] = next[f]; n++; }
  }
  return n ? diff : null;
}
"""

JS = r"""
(function () {
  'use strict';
  var D = JSON.parse(document.getElementById('tt-data').textContent);
  var T = D.tasks;
  var KEY = 'task-tracker:pending';
  var FIELDS = ['action', 'owner', 'source', 'raised', 'due', 'status', 'notes'];
  var S = { complete: {}, update: {}, decision: {}, adds: [] };
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var store = null;
  try {
    if (window.storage && typeof window.storage.get === 'function' && typeof window.storage.set === 'function') {
      store = window.storage;
    }
  } catch (e) { store = null; }

  function $(id) { return document.getElementById(id); }
  function isIso(s) { return /^\d{4}-\d{2}-\d{2}$/.test(s || ''); }
  function utc(s) { return Date.UTC(+s.slice(0, 4), +s.slice(5, 7) - 1, +s.slice(8, 10)); }
  function fmt(s) { var x = new Date(utc(s)); return DAYS[x.getUTCDay()] + ' ' + x.getUTCDate() + ' ' + MONTHS[x.getUTCMonth()]; }
  var unassigned = ttUnassigned;
  function snapshot(i) { var t = T[i], s = { section: t.section }; FIELDS.forEach(function (f) { s[f] = t[f]; }); return s; }
  function sameSnap(a, b) {
    if (!a || typeof a !== 'object') return false;
    for (var k in b) if (a[k] !== b[k]) return false;
    return true;
  }
  function val(id, f) { var u = S.update[id]; return (u && Object.prototype.hasOwnProperty.call(u, f)) ? u[f] : T[id][f]; }
  function dueInfo(s) {
    if (!s) return ['no due date', 'muted'];
    if (!isIso(s)) return [s, 'muted'];
    var n = Math.round((utc(s) - utc(D.today)) / 86400000);
    if (n < 0) return [fmt(s) + ' (' + (-n) + (n < -1 ? ' days' : ' day') + ' overdue)', 'overdue'];
    if (n === 0) return ['today', 'today'];
    return [fmt(s), utc(s) <= utc(D.weekEnd) ? 'soon' : ''];
  }
  function label(id) { return id + ' ' + val(id, 'action'); }

  function buildOps() {
    var ops = [], id;
    for (id in S.update) ops.push({ op: 'update', id: id, fields: S.update[id], before: snapshot(id) });
    for (id in S.complete) ops.push({ op: 'complete', id: id, before: snapshot(id) });
    for (id in S.decision) ops.push({ op: S.decision[id], id: id, before: snapshot(id) });
    S.adds.forEach(function (a) { ops.push({ op: 'add', fields: a }); });
    return ops;
  }
  function block() {
    return { base_revision: D.revision, generated: new Date().toISOString(), ops: buildOps() };
  }
  function describe(op) {
    if (op.op === 'add') return 'Add: ' + op.fields.action + (op.fields.owner ? ' (' + op.fields.owner + ')' : '');
    if (op.op === 'complete') return 'Mark done: ' + label(op.id);
    if (op.op === 'approve') return 'Approve: ' + label(op.id);
    if (op.op === 'reject') return 'Reject: ' + label(op.id);
    var parts = [];
    for (var f in op.fields) parts.push(f + ' ' + (T[op.id][f] || 'blank') + ' to ' + (op.fields[f] || 'blank'));
    return 'Edit ' + op.id + ': ' + parts.join('; ');
  }

  function save() {
    if (!store) return;
    try {
      var snap = {};
      ['complete', 'update', 'decision'].forEach(function (k) { for (var id in S[k]) snap[id] = snapshot(id); });
      var p = store.set(KEY, JSON.stringify({ complete: S.complete, update: S.update, decision: S.decision,
                                              adds: S.adds, snap: snap }));
      if (p && typeof p.catch === 'function') p.catch(function () {});
    } catch (e) { /* storage unavailable: keep changes in memory */ }
  }
  function load() {
    if (!store) return Promise.resolve();
    try {
      return Promise.resolve(store.get(KEY)).then(function (r) {
        var v = (r && typeof r === 'object') ? r.value : r;
        if (!v) return;
        var s = JSON.parse(v), snap = (s.snap && typeof s.snap === 'object') ? s.snap : {}, dropped = {};
        ['complete', 'update', 'decision'].forEach(function (k) {
          if (s[k] && typeof s[k] === 'object') for (var id in s[k]) {
            if (T[id] && sameSnap(snap[id], snapshot(id))) S[k][id] = s[k][id]; else dropped[id] = true;
          }
        });
        if (Array.isArray(s.adds)) S.adds = s.adds.filter(function (a) { return a && a.action; });
        var gone = Object.keys(dropped);
        if (gone.length) $('tt-storage-note').textContent += ' Dropped saved changes for ' + gone.join(', ') +
          ' because those tasks changed in TASKS.md since. Redo them if they still apply.';
      }).catch(function () {});
    } catch (e) { return Promise.resolve(); }
  }

  function setField(li, f, text, cls) {
    var el = li.querySelector('[data-f="' + f + '"]');
    if (!el) return;
    el.textContent = text;
    if (cls !== undefined) el.className = cls;
  }
  function refresh() {
    var items = document.querySelectorAll('li.task');
    for (var i = 0; i < items.length; i++) {
      var li = items[i], id = li.getAttribute('data-id');
      if (!T[id]) continue;
      var done = !!S.complete[id], dec = S.decision[id] || '', edited = !!S.update[id];
      li.classList.toggle('pending-done', done);
      li.classList.toggle('pending-approve', dec === 'approve');
      li.classList.toggle('pending-reject', dec === 'reject');
      li.classList.toggle('edited', edited);
      var cb = li.querySelector('input.tick');
      if (cb) cb.checked = done;
      setField(li, 'action', val(id, 'action'));
      var o = val(id, 'owner');
      setField(li, 'owner', unassigned(o) ? 'Unassigned' : o, 'owner' + (unassigned(o) ? ' flag' : ''));
      if (T[id].section !== 'done') {
        var di = dueInfo(val(id, 'due'));
        setField(li, 'due', di[0], 'due ' + di[1]);
        var st = val(id, 'status');
        setField(li, 'status', st, 'status st-' + st.toLowerCase().replace(/ /g, '-'));
      }
      var pl = li.querySelector('.pending-label');
      if (pl) pl.textContent = done ? 'will be marked done' : dec === 'approve' ? 'will be approved' :
        dec === 'reject' ? 'will be rejected' : edited ? 'edited' : '';
    }
    renderTray();
    save();
  }

  function renderTray() {
    var ops = buildOps(), list = $('tt-ops');
    list.innerHTML = '';
    ops.forEach(function (op, i) {
      var li = document.createElement('li'), span = document.createElement('span'), b = document.createElement('button');
      span.textContent = describe(op);
      b.type = 'button';
      b.textContent = 'Undo';
      b.setAttribute('data-undo', op.op === 'add' ? 'add:' + (i - (ops.length - S.adds.length)) : op.op + ':' + op.id);
      li.appendChild(span); li.appendChild(b); list.appendChild(li);
    });
    $('tt-count').textContent = ops.length;
    ['tt-copy', 'tt-download', 'tt-clear'].forEach(function (b) { $(b).disabled = !ops.length; });
    if (!ops.length) { $('tt-out').hidden = true; $('tt-msg').textContent = ''; }
  }
  function openTray(open) {
    $('tt-traybody').hidden = !open;
    $('tt-toggle').textContent = open ? 'Hide' : 'Show';
    $('tt-toggle').setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  function el(tag, attrs) {
    var e = document.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    return e;
  }
  function openEditor(li) {
    var id = li.getAttribute('data-id');
    if (li.querySelector('.editor')) return;
    var t = T[id], form = el('div', { 'class': 'editor no-print' });
    var a = el('input', { 'aria-label': 'Action' }); a.value = val(id, 'action');
    var o = el('input', { 'aria-label': 'Owner', list: 'tt-owners', placeholder: 'Owner' }); o.value = unassigned(val(id, 'owner')) ? '' : val(id, 'owner');
    var shownDue = val(id, 'due'), dueTouched = false;
    var due = el('input', { type: 'date', 'aria-label': 'Due date' }); due.value = isIso(shownDue) ? shownDue : '';
    if (shownDue && !due.value) due.title = 'Due is "' + shownDue + '" in TASKS.md; it stays unless you pick or clear a date';
    function touch() { dueTouched = true; }
    due.addEventListener('input', touch); due.addEventListener('change', touch);
    form.appendChild(a); form.appendChild(o); form.appendChild(due);
    var st = null;
    if (t.section === 'open') {
      st = el('select', { 'aria-label': 'Status' });
      var cur = val(id, 'status');
      if (D.statuses.indexOf(cur) < 0) {
        var keep = el('option', {}); keep.value = cur; keep.textContent = (cur || 'blank') + ' (keep)'; st.appendChild(keep);
      }
      D.statuses.forEach(function (s) { var op = el('option', {}); op.value = s; op.textContent = s; st.appendChild(op); });
      st.value = cur;
      form.appendChild(st);
    } else {
      form.appendChild(el('span', {}));
    }
    var ok = el('button', { type: 'button' }); ok.textContent = 'Save';
    var cancel = el('button', { type: 'button' }); cancel.textContent = 'Cancel';
    form.appendChild(ok); form.appendChild(cancel);
    li.querySelector('.body').appendChild(form);
    a.focus();
    cancel.onclick = function () { form.remove(); };
    ok.onclick = function () {
      if (!a.value.trim()) { a.focus(); return; }
      var diff = ttEditDiff(t, shownDue, { action: a.value.trim(), owner: o.value.trim(), due: due.value,
                                           dueTouched: dueTouched, status: st ? st.value : undefined });
      if (diff) S.update[id] = diff; else delete S.update[id];
      form.remove();
      refresh();
    };
  }

  document.addEventListener('change', function (e) {
    var t = e.target;
    if (t.classList && t.classList.contains('tick')) {
      var id = t.getAttribute('data-id');
      if (t.checked) S.complete[id] = true; else delete S.complete[id];
      refresh();
    }
  });
  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('button') : null;
    if (!b) return;
    var act = b.getAttribute('data-act'), id = b.getAttribute('data-id'), undo = b.getAttribute('data-undo');
    if (act === 'edit') openEditor(b.closest('li.task'));
    if (act === 'approve' || act === 'reject') {
      if (S.decision[id] === act) delete S.decision[id]; else S.decision[id] = act;
      refresh();
    }
    if (undo) {
      var k = undo.split(':')[0], v = undo.slice(k.length + 1);
      if (k === 'add') S.adds.splice(+v, 1);
      else if (k === 'update') delete S.update[v];
      else if (k === 'complete') delete S.complete[v];
      else delete S.decision[v];
      refresh();
    }
  });

  $('tt-toggle').onclick = function () { openTray($('tt-traybody').hidden); };
  $('tt-add-toggle').onclick = function () { $('tt-add').hidden = !$('tt-add').hidden; };
  $('tt-add').onsubmit = function (e) {
    e.preventDefault();
    var f = e.target, a = f.action.value.trim();
    if (!a) return;
    var add = { action: a };
    if (f.owner.value.trim()) add.owner = f.owner.value.trim();
    if (f.due.value) add.due = f.due.value;
    S.adds.push(add);
    f.reset();
    refresh();
    openTray(true);
  };
  $('tt-copy').onclick = function () {
    var text = '```task-tracker-changes\n' + JSON.stringify(block()) + '\n```';
    var out = $('tt-out'), msg = $('tt-msg');
    out.value = text; out.hidden = false; openTray(true);
    function manual() { out.focus(); out.select(); msg.textContent = 'Copying is blocked here: the block is selected, press Ctrl+C (Cmd+C on a Mac), then paste it to Claude.'; }
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          msg.textContent = 'Copied. Paste it to Claude, which checks it against TASKS.md and applies it after you confirm.';
        }, manual);
      } else { manual(); }
    } catch (err) { manual(); }
  };
  $('tt-download').onclick = function () {
    try {
      var blob = new Blob([JSON.stringify(block(), null, 2) + '\n'], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'tasks-changes.json';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
      $('tt-msg').textContent = 'Saved tasks-changes.json. Put it in your tracker folder and ask Claude to apply the dashboard changes.';
    } catch (err) {
      $('tt-msg').textContent = 'Downloads are not available here. Use Copy changes instead.';
    }
    openTray(true);
  };
  $('tt-clear').onclick = function () {
    S = { complete: {}, update: {}, decision: {}, adds: [] };
    refresh();
  };
  $('tt-search').oninput = function () {
    var q = this.value.trim().toLowerCase(), items = document.querySelectorAll('li.task');
    for (var i = 0; i < items.length; i++) items[i].hidden = q && items[i].textContent.toLowerCase().indexOf(q) < 0;
  };
  var dl = $('tt-owners');
  D.owners.forEach(function (o) { var op = document.createElement('option'); op.value = o; dl.appendChild(op); });
  $('tt-storage-note').textContent = store
    ? 'Unapplied changes are kept in this artifact\'s own storage until you apply them.'
    : 'Unapplied changes only live in this open page, so copy them before you close it.';
  load().then(refresh);
})();
"""


def main(argv=None):
    ap = argparse.ArgumentParser(description="Render TASKS.md as a self-contained dashboard.html")
    ap.add_argument("--tasks", default="TASKS.md")
    ap.add_argument("--out", help="default: dashboard.html next to TASKS.md")
    ap.add_argument("--today", help="YYYY-MM-DD, default today")
    ap.add_argument("--title", default="Tasks")
    args = ap.parse_args(argv)
    if args.today and not tm.is_date(args.today):
        print(json.dumps({"ok": False, "error": f"--today '{args.today}' is not a real YYYY-MM-DD date"}))
        return 1
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    try:
        doc = tm.load(args.tasks)
    except (OSError, UnicodeDecodeError, tm.ParseError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    errors, warnings = tm.validate(doc)
    page, rev, counts = build(doc, today, args.title)
    out = Path(args.out) if args.out else Path(args.tasks).with_name("dashboard.html")
    tm.write_atomic(out, page, backup=False)
    print(json.dumps({"ok": True, "out": str(out.resolve()), "revision": rev, "counts": counts,
                      "errors": errors, "warnings": warnings}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
