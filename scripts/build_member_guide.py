#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""멤버 가이드 두 벌을 문구 한 파일에서 만든다.

입력: data/member_guide.yml (문구만)
출력:
  1) ~/Projects/hfk-presentations/member-guide.html   — thehfk.github.io 미리보기
  2) work/상시/발행/멤버가이드_아임웹위젯_전문.html      — thehfk.org/guide 코드위젯 붙여넣기용

디자인 값은 아래 T(토큰)에 모여 있다. 문구는 yml, 모양은 여기.
레이아웃은 '시안 A' — 왼쪽 라벨 칸(번호·제목) + 오른쪽 본문 칸.

    python3 scripts/build_member_guide.py            # 두 벌 생성
    python3 scripts/build_member_guide.py --copy     # + 위젯 전문을 클립보드로
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "content" / "member-guide.yml"
OUT_PREVIEW = BASE / "member-guide.html"
OUT_WIDGET = None   # 아임웹은 iframe 임베드로 바뀌어 전문 붙여넣기가 필요 없다
SHOT = "https://thehfk.github.io/hfk-ai-bss/assets/shots/"
PHOTO = "https://thehfk.github.io/hfk-ai-bss/assets/photos/"

# ── 디자인 토큰 (시안 A) ───────────────────────────────────────
T = {
    "ink": "#2d2523", "body": "#3d3733", "dim": "#7a6a60",
    "red": "#980000", "line": "#e3d8c9", "rule": "#ece3d7",
    "paper": "#f0eae2", "card": "#ffffff", "soft": "#faf6f0",
    "ls": "-0.02em",
    "body_size": "17px", "body_lh": "1.78", "measure": "660px",
    "step_title": "20px", "h2": "30px", "sub": "16px",
    "label_col": "248px", "col_gap": "48px",
    "sec_gap": "80px", "step_pad": "36px", "card_pad": "44px 48px",
}

# (미디어쿼리 | None, 셀렉터, 선언)  — 셀렉터의 & 는 루트로 치환된다
CSS = [
    (None, "&", f"color:{T['ink']};letter-spacing:{T['ls']};word-break:keep-all;"
                f"font-family:'Pretendard Variable','Pretendard',-apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo',sans-serif"),
    (None, "& *", "box-sizing:border-box;font-family:inherit"),
    (None, "& p,& h1,& h2,& h3,& h4,& ul,& ol,& li", "margin:0;padding:0;text-indent:0"),
    (None, "& img", "max-width:100%;height:auto;border-radius:10px;display:block"),
    (None, "& a", f"color:{T['red']};font-weight:700;text-decoration:underline"),

    (None, "& .eyebrow", f"font-size:13px;font-weight:700;letter-spacing:0.14em;color:{T['red']};margin:0 0 12px"),
    (None, "& .h1", f"font-size:{T['h2']};font-weight:700;line-height:1.28;margin:0 0 16px"),
    (None, "& .lead", f"font-size:{T['sub']};line-height:1.75;color:{T['dim']};margin:0 0 64px"),

    (None, "& .sec", f"margin:0 0 {T['sec_gap']}"),
    (None, "& .sec:last-child", "margin:0"),
    (None, "& .h2", f"font-size:{T['h2']};font-weight:700;color:{T['ink']};line-height:1.28;margin:0 0 10px"),
    (None, "& .sub", f"font-size:{T['sub']};line-height:1.7;color:{T['dim']};margin:0 0 40px"),

    (None, "& .card", f"background:{T['card']};border:1px solid {T['line']};border-radius:14px;padding:{T['card_pad']}"),
    (None, "& .duo", "display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:0 0 16px"),
    (None, "& .duo .card", "margin:0"),
    (None, "& .label", f"font-size:13px;font-weight:700;letter-spacing:0.08em;color:{T['red']};margin:0 0 12px"),
    (None, "& .h3", f"font-size:19px;font-weight:700;color:{T['ink']};line-height:1.45;margin:0 0 12px"),
    (None, "& .b", f"font-size:{T['body_size']};line-height:{T['body_lh']};color:{T['body']}"),
    (None, "& .b+.b", "margin-top:14px"),
    (None, "& .b b", f"font-weight:700;color:{T['ink']}"),

    # 좌 라벨 / 우 본문 — 항목·About·멤버십 구성·공지 예시가 모두 같은 격자를 쓴다
    (None, "& .r2", f"display:grid;grid-template-columns:{T['label_col']} 1fr;gap:{T['col_gap']}"),
    (None, "& .step", f"padding:{T['step_pad']} 0;border-top:1px solid {T['rule']}"),
    (None, "& .step:first-child", "border-top:0;padding-top:0"),
    (None, "& .step:last-child", "padding-bottom:0"),
    (None, "& .st", f"font-size:{T['step_title']};font-weight:700;color:{T['ink']};line-height:1.4"),
    (None, "& .num", f"display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;"
                     f"border-radius:50%;background:{T['red']};color:#fff;font-size:12px;font-weight:700;"
                     f"margin-right:10px;vertical-align:2px"),
    (None, "& .slab", f"font-size:14px;font-weight:700;color:{T['red']};margin:22px 0 6px"),
    (None, "& .note", f"font-size:14px;line-height:1.7;color:{T['dim']};margin:12px 0 0"),
    (None, "& .shotset", "margin-top:26px"),
    (None, "& .fig", "margin:0 0 22px"),
    (None, "& .fig:last-child", "margin-bottom:0"),
    (None, "& .fig img", f"border:1px solid {T['line']}"),
    (None, "& .figcap", f"font-size:14px;line-height:1.65;color:{T['dim']};margin:10px 0 0"),
    (None, "& .figcap .tag", f"font-size:11px;font-weight:700;letter-spacing:0.04em;color:{T['red']};"
                             f"background:{T['soft']};border:1px solid {T['rule']};border-radius:4px;"
                             "padding:3px 7px;margin-right:8px;white-space:nowrap"),

    (None, "& .kv", f"font-size:{T['body_size']};line-height:{T['body_lh']};color:{T['body']};margin:0 0 4px"),
    (None, "& .kv b", f"font-weight:700;color:{T['ink']}"),
    (None, "& .kv b.n", f"color:{T['red']}"),

    (None, "& .hist", "margin:0 0 10px"),
    (None, "& .hist:last-of-type", "margin:0"),
    (None, "& .hist .y", f"font-size:15px;font-weight:700;color:{T['red']};display:inline-block;width:72px"),
    (None, "& .hist .t", f"font-size:15px;color:{T['body']}"),
    (None, "& .links", f"font-size:15px;line-height:1.8;color:{T['body']};margin:22px 0 0"),

    (None, "& .prog", "margin:0 0 44px"),
    (None, "& .prog:last-child", "margin:0"),
    (None, "& .kicker", f"font-size:13px;font-weight:700;color:{T['red']};margin:0 0 4px"),
    (None, "& .grid2", "display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px"),

    (None, "& .chgrid", f"display:grid;grid-template-columns:1fr 1fr;gap:22px 28px;background:{T['soft']};"
                        f"border:1px solid {T['rule']};border-radius:10px;padding:24px;margin-top:18px"),
    (None, "& .chg", f"font-size:12px;font-weight:700;letter-spacing:0.06em;color:{T['dim']};margin:0 0 8px"),
    (None, "& .chl", f"font-size:15px;line-height:1.85;color:{T['body']};margin:0"),

    (None, "& .rule", f"padding:14px 0;border-bottom:1px solid {T['rule']};display:grid;"
                      "grid-template-columns:76px 1fr;gap:14px;align-items:baseline"),
    (None, "& .rule:last-child", "border-bottom:0;padding-bottom:0"),
    (None, "& .rule .k", f"font-size:16px;font-weight:700;color:{T['red']}"),
    (None, "& .rule .v", f"font-size:16px;line-height:1.7;color:{T['body']}"),

    (None, "& .ben", "display:grid;grid-template-columns:1fr 1fr;gap:26px 24px;margin-top:18px"),
    (None, "& .ben .n", f"font-size:13px;font-weight:700;color:{T['red']};margin:0"),
    (None, "& .ben .h", f"font-size:17px;font-weight:700;color:{T['ink']};line-height:1.4;margin:8px 0 14px"),
    (None, "& .ben img", "height:150px;object-fit:cover;width:100%;margin:0 0 14px"),
    (None, "& .ben .t", f"font-size:15px;line-height:1.75;color:{T['body']};margin:0"),

    (None, "& .end", f"background:{T['ink']};border-radius:14px;padding:40px 32px;text-align:center"),
    (None, "& .end .e", "font-size:13px;font-weight:700;letter-spacing:0.12em;color:#F5EBE0;margin:0 0 14px"),
    (None, "& .end .h", "font-size:21px;font-weight:700;color:#fff;margin:0 0 8px"),
    (None, "& .end .p", "font-size:15px;line-height:1.7;color:#cbbfb7;margin:0"),

    ("(max-width:860px)", "& .r2", "grid-template-columns:1fr;gap:14px"),
    ("(max-width:860px)", "& .card", "padding:28px 22px"),
    ("(max-width:860px)", "& .chgrid,& .ben,& .duo", "grid-template-columns:1fr"),
    ("(max-width:860px)", "& .sec", "margin-bottom:56px"),
    ("(max-width:860px)", "& .b,& .kv", "font-size:16px"),
]


def css(root: str, important: bool) -> str:
    out, cur = [], object()
    for media, sel, decls in CSS:
        if media != cur:
            if cur is not None and not isinstance(cur, object.__class__) and cur != object():
                pass
            cur = media
        d = "; ".join(x.strip() + (" !important" if important else "")
                      for x in decls.split(";") if x.strip())
        line = f"{sel.replace('&', root)} {{ {d}; }}"
        out.append(f"@media {media} {{ {line} }}" if media else line)
    return "\n".join(out)


# ── 마크업 ────────────────────────────────────────────────────
def esc(s) -> str:
    return str(s)


def photos(names, alt):
    cells = "".join(f'<img src="{PHOTO}{n}.jpg" alt="{alt}">' for n in names)
    return f'<div class="grid2">{cells}</div>'


def step_html(i, s):
    r = [f'<p class="b">{s["lead"]}</p>'] if s.get("lead") else []
    if s.get("label"):
        r.append(f'<p class="slab">{s["label"]}</p>')
    for k, v in s.get("kv", []):
        cls = ' class="n"' if s.get("kv_accent") else ""
        r.append(f'<p class="kv"><b{cls}>{k}</b>&nbsp;&nbsp;{v}</p>')
    for blk in s.get("blocks", []):
        r.append(f'<p class="slab">{blk["label"]}</p><p class="b">{blk["text"]}</p>')
    if s.get("channels"):
        g = "".join(f'<div><p class="chg">{c["group"]}</p>'
                    f'<p class="chl">{"<br>".join(c["list"])}</p></div>' for c in s["channels"])
        r.append(f'<div class="chgrid">{g}</div>')
    if s.get("rules"):
        rows = "".join(f'<div class="rule"><span class="k">{k}</span><span class="v">{v}</span></div>'
                       for k, v in s["rules"])
        r.append(f'<div style="margin-top:8px">{rows}</div>')
    if s.get("benefits"):
        cells = "".join(
            f'<div><p class="n">{b["num"]}</p><h3 class="h">{b["heading"]}</h3>'
            f'<img src="{b["img"].replace("PHOTO/", PHOTO)}" alt="{b["alt"]}">'
            f'<p class="t">{b["text"]}</p></div>' for b in s["benefits"])
        r.append(f'<div class="ben">{cells}</div>')
    if s.get("note"):
        r.append(f'<p class="note">{s["note"]}</p>')
    if s.get("shots"):
        figs = "".join(
            f'<figure class="fig"><img src="{SHOT}{f}" alt="{alt}">'
            f'<figcaption class="figcap"><span class="tag">{tag}</span>{cap}</figcaption></figure>'
            for f, tag, cap, alt in s["shots"])
        r.append(f'<div class="shotset">{figs}</div>')
    return (f'<div class="step r2"><div class="st"><span class="num">{i}</span>{s["title"]}</div>'
            f'<div>{"".join(r)}</div></div>')


def body_html(d) -> str:
    h, a, pg, st, c = (d["hero"], d["about"], d["program"], d["steps"], d["closing"])

    cards = "".join(
        f'<div class="card"><p class="label">{x["label"]}</p><h3 class="h3">{x["heading"]}</h3>'
        + "".join(f'<p class="b">{p}</p>' for p in x["paras"]) + "</div>" for x in a["cards"])
    cards = f'<div class="duo">{cards}</div>'
    hist = "".join(f'<div class="hist"><span class="y">{y}</span><span class="t">{t}</span></div>'
                   for y, t in a["history"]["rows"])
    links = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in a["history"]["links"])
    about = (f'<section class="sec"><h2 class="h2">{a["title"]}</h2><p class="sub">{a["sub"]}</p>'
             f'{cards}<div class="card r2"><div><p class="label">{a["history"]["label"]}</p></div>'
             f'<div>{hist}<p class="links">{links} {a["history"]["links_tail"]}</p></div></div></section>')

    progs = "".join(
        f'<div class="prog r2"><div><p class="kicker">{x["kicker"]}</p>'
        f'<h3 class="h3">{x["heading"]}</h3></div>'
        f'<div><p class="b">{x["text"]}</p>{photos(x["photos"], x["alt"])}</div></div>' for x in pg["items"])
    program = (f'<section class="sec"><h2 class="h2">{pg["title"]}</h2>'
               f'<p class="sub">{pg["sub"]}</p>{progs}</section>')

    steps = "".join(step_html(i, s) for i, s in enumerate(st["items"], 1))
    steps_sec = (f'<section class="sec"><h2 class="h2">{st["title"]}</h2><p class="sub">{st["sub"]}</p>'
                 f'<div class="card">{steps}</div></section>')

    closing = (f'<section class="sec"><div class="end"><p class="e">{c["eyebrow"]}</p>'
               f'<p class="h">{c["title"]}</p><p class="p">{c["text"]}</p></div></section>')

    hero = (f'<p class="eyebrow">{h["eyebrow"]}</p><h1 class="h1">{h["title"]}</h1>'
            f'<p class="lead">{h["lead"]}</p>')
    return hero + about + program + steps_sec + closing


def build_preview(d) -> str:
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HFK 멤버 가이드</title>
<meta name="description" content="HFK에 처음 오신 멤버를 위한 안내서: 멤버십 구성, 슬랙, 팀 어드벤처, 이벤트 신청, 자기소개, 그라운드룰, 4L 리뷰, 멤버 베네핏.">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
html,body{{margin:0;padding:0;background:{T['paper']};}}
body{{padding:56px 20px 72px;}}
.g{{max-width:1240px;margin:0 auto;}}
@media (max-width:860px){{ body{{padding:28px 14px 48px;}} }}
/* ?embed=1 로 열리면(아임웹 iframe) 바깥 여백·폭 제한을 뺀다. 폭은 아임웹 섹션이 정한다 */
html.embed body{{padding:0;}}
html.embed .g{{max-width:none;}}
{css('.g', False)}
</style>
</head>
<body>
<div class="g">
{body_html(d)}
</div>
<script>
// 아임웹 코드위젯이 이 페이지를 iframe 으로 싣는 경우: 여백을 빼고 높이를 부모에게 알린다.
(function () {{
  var embed = /[?&]embed=1/.test(location.search);
  if (!embed) return;
  document.documentElement.classList.add('embed');
  var last = 0;
  function tell() {{
    var r = document.body.getBoundingClientRect(), cs = getComputedStyle(document.body);
    var h = Math.ceil(r.height + (parseFloat(cs.marginTop) || 0) + (parseFloat(cs.marginBottom) || 0));
    if (h && Math.abs(h - last) > 1) {{
      last = h;
      parent.postMessage({{ hfkGuideHeight: h }}, '*');
    }}
  }}
  new ResizeObserver(tell).observe(document.body);
  addEventListener('load', tell);
  addEventListener('resize', tell);
  setInterval(tell, 1000);   // 이미지가 늦게 뜰 때 대비
  tell();
}})();
</script>
</body>
</html>
"""


def build_widget(d) -> str:
    return f"""<!--
  ============================================================
  HFK 멤버 가이드 — 아임웹 코드 위젯 전문
  ============================================================
  자동 생성 파일입니다. 직접 고치지 마세요.
    문구 → data/member_guide.yml
    모양 → scripts/build_member_guide.py 의 T(토큰)
    생성 → python3 scripts/build_member_guide.py [--copy]

  ※ 2026-09-04 부터 thehfk.org/guide 는 iframe 임베드로 바뀌었습니다
     (work/상시/발행/멤버가이드_아임웹_iframe조각.html 을 코드위젯에 한 번 넣어둠).
     그래서 이 전문은 평소에 붙여넣을 필요가 없습니다. iframe 이 막혔을 때 쓰는 대비본입니다.

  붙여넣는 곳(대비용): 아임웹 빌더 > 해당 페이지 > 「코드/HTML」 위젯.
  아래 <style> 부터 끝까지 전부. 일반 텍스트 편집기(froala)에 넣으면
  <style> 이 통째로 지워지므로 반드시 코드 위젯이어야 합니다.

  레이아웃: 시안 A — 왼쪽 라벨 칸(번호·제목) + 오른쪽 본문 칸.
  폭·정렬은 아임웹 섹션이 담당하므로 여기에 max-width 컨테이너를 두지 않습니다.
  ============================================================
-->
<style>
{css('#hfkg#hfkg', True)}
</style>

<div id="hfkg">
{body_html(d)}
</div>
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copy", action="store_true", help="위젯 전문을 클립보드에 복사")
    args = ap.parse_args()

    d = yaml.safe_load(SRC.read_text("utf-8"))
    prev = build_preview(d)
    OUT_PREVIEW.write_text(prev, "utf-8")
    print(f"  {OUT_PREVIEW.name}  ({len(prev):,}자)")
    print("  → 커밋·푸시하면 thehfk.org/guide 에 저절로 반영됩니다 (iframe 임베드)")


if __name__ == "__main__":
    sys.exit(main())
