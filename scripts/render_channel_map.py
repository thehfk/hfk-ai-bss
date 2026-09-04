#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""멤버 가이드·뉴멤버 OT 가 같이 쓰는 채널 구조 캡처(assets/shots/shot-channels.jpg)를 만든다.

원본 이미지는 생성 소스가 남아 있지 않아 26여름 채널 + 아카이브된 FAQ 채널이
계속 찍혀 나갔다. 이 스크립트가 그 캡처의 정본이다. 시즌이 바뀌면 GROUPS 만 고친다.

    ~/hfk-slack-venv/bin/python3 scripts/render_channel_map.py
"""
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "assets" / "shots" / "shot-channels.jpg"

# (그룹 라벨, [(종류, 이름), ...])  종류: sec=사이드바 섹션(번호 배지) / ch=채널
LEFT = [
    ("0 · 전체 멤버", [
        ("sec", "0", "전체-멤버"),
        ("ch", None, "0--공지-확인"),
        ("ch", None, "0--교류-게시판"),
    ]),
    ("1 · 26가을 멤버", [
        ("sec", "1", "26가을-멤버"),
        ("ch", None, "1--26가을-공지-확인"),
        ("ch", None, "1--26가을-어드벤처-신청"),
        ("ch", None, "1--ai부사수-주중"),
        ("ch", None, "1--강점차별화"),
    ]),
]
RIGHT = [
    ("1 · 26가을 팀 (예시)", [
        ("ch", None, "1--리더의서재"),
        ("ch", None, "1--중간리더십"),
        ("ch", None, "1--글쓰는oo"),
        ("ch", None, "1--관찰과발견"),
        ("ch", None, "1--투자의기준"),
    ]),
    ("2 · 이벤트", [
        ("sec", "2", "26가을-이벤트"),
        ("ch", None, "2--aar밋업"),
        ("ch", None, "2--hbr포럼"),
        ("ch", None, "2--pest브리핑"),
        ("ch", None, "2--저자북토크"),
    ]),
]

CSS = """
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
*{box-sizing:border-box;margin:0;padding:0}
body{width:1280px;height:720px;background:#fff;
     font-family:Pretendard,-apple-system,sans-serif;letter-spacing:-0.02em;
     -webkit-font-smoothing:antialiased}
.bar{height:52px;border-bottom:1px solid #ececec;display:flex;align-items:center;
     gap:10px;padding:0 20px}
.logo{font-size:15px;font-weight:800;color:#1a1a1a}
.bt{font-size:11px;color:#8a8a8a}
.cols{display:flex;padding:50px 55px 0}
.col{width:615px}
.grp{font-size:10px;color:#9a9a9a;margin-bottom:11px}
.grp+.grp,.g:not(:first-child) .grp{margin-top:0}
.g:not(:first-child){margin-top:39px}
.row{display:flex;align-items:center;height:36.5px}
.badge{width:20px;height:18px;border-radius:4px;background:#e9ebee;color:#4a4a4a;
       font-size:11px;font-weight:700;display:flex;align-items:center;
       justify-content:center;margin-right:9px}
.hash{width:12px;text-align:center;color:#b3b3b3;font-size:15px;margin-right:5px}
.secname{font-size:15px;color:#1f1f1f;font-weight:500}
.chname{font-size:14px;color:#4a4a4a}
"""


def render_group(label, items):
    rows = []
    for kind, num, name in items:
        if kind == "sec":
            rows.append(f'<div class="row"><span class="badge">{num}</span>'
                        f'<span class="secname">{name}</span></div>')
        else:
            rows.append(f'<div class="row"><span class="hash">#</span>'
                        f'<span class="chname">{name}</span></div>')
    return f'<div class="g"><p class="grp">{label}</p>{"".join(rows)}</div>'


def build_html():
    left = "".join(render_group(l, it) for l, it in LEFT)
    right = "".join(render_group(l, it) for l, it in RIGHT)
    return (f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>'
            f'<div class="bar"><span class="logo">thehfk</span>'
            f'<span class="bt">HFK · 채널 구조</span></div>'
            f'<div class="cols"><div class="col">{left}</div>'
            f'<div class="col">{right}</div></div>')


def main():
    from playwright.sync_api import sync_playwright
    html = build_html()
    tmp = BASE / "assets" / "shots" / "_channel-map.html"
    tmp.write_text(html, "utf-8")
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1280, "height": 720},
                         device_scale_factor=1)
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(1200)          # 웹폰트 로드 대기
        pg.screenshot(path=str(OUT), type="jpeg", quality=92)
        br.close()
    tmp.unlink()
    print(f"  {OUT.relative_to(BASE)}  ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
