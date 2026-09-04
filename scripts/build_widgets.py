#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""아임웹 코드위젯 조각 → iframe 으로 실을 수 있는 독립 페이지 + 붙여넣을 조각.

왜: 아임웹에 HTML 을 통째로 붙여넣으면, 고칠 때마다 다시 붙여넣어야 한다.
    공개 레포에 독립 페이지로 올리고 아임웹엔 iframe 16줄만 두면,
    이후 수정은 git push 만으로 라이브에 반영된다.

    조각 원본은 이 워크스페이스(비공개)에 남고, 결과 페이지만 공개 레포로 나간다.

사용:
    python3 scripts/build_imweb_embed.py <조각.html> <출력이름> [--copy]
    예) python3 scripts/build_imweb_embed.py work/상시/발행/season-alarm-form.html widget-season-alarm
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PUB = BASE   # 결과 페이지는 이 레포 루트에 만든다
PAGES = "https://thehfk.github.io/hfk-ai-bss/"

WRAP = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
  html,body{{margin:0;padding:0;background:#f0eae2;}}
  body{{padding:48px 20px 64px;font-family:'Pretendard',-apple-system,BlinkMacSystemFont,sans-serif;
        letter-spacing:-0.02em;word-break:keep-all;}}
  /* iframe 으로 실릴 때는 폭·여백을 아임웹 섹션이 정한다 */
  html.hfk-embed body{{padding:0;}}
  /* 위젯 카드의 둥근 모서리 뒤로 iframe 배경(크림)이 비쳐 아임웹의 어두운 칸에서
     모서리에 밝은 조각이 생긴다. 실릴 때는 맨 바깥 카드만 각지게 해 꽉 채운다. */
  html.hfk-embed body > div{{border-radius:0 !important;}}
</style>
</head>
<body>
<!-- 자동 생성물입니다. 고치지 마세요. 원본: {src} · 만든이: scripts/build_imweb_embed.py -->
{fragment}
<script>
(function () {{
  if (!/[?&]embed=1/.test(location.search)) return;
  document.documentElement.classList.add('hfk-embed');
  var last = 0;
  function tell() {{
    var r = document.body.getBoundingClientRect(), cs = getComputedStyle(document.body);
    var h = Math.ceil(r.height + (parseFloat(cs.marginTop) || 0) + (parseFloat(cs.marginBottom) || 0));
    if (h && Math.abs(h - last) > 1) {{ last = h; parent.postMessage({{ hfkEmbedHeight: h }}, '*'); }}
  }}
  new ResizeObserver(tell).observe(document.body);
  addEventListener('load', tell); addEventListener('resize', tell);
  setInterval(tell, 1000); tell();
}})();
</script>
</body>
</html>
"""

SNIPPET = """<!-- HFK {name}. 수정은 hfk-workspace 의 {src} 를 고치고
     python3 scripts/build_imweb_embed.py 로 다시 만든 뒤 push 하면 여기에 반영됩니다. -->
<iframe id="hfk-{fid}"
        src="{pages}{name}.html?embed=1"
        title="{title}"
        scrolling="no"
        style="width:100%;height:{h}px;border:0;display:block;overflow:hidden;background:#f0eae2"></iframe>
<script>
(function () {{
  var f = document.getElementById('hfk-{fid}');
  window.addEventListener('message', function (e) {{
    if (e.origin !== 'https://thehfk.github.io') return;
    if (e.source !== f.contentWindow) return;   // 한 페이지에 위젯이 여럿일 때 서로 높이를 뺏지 않도록
    var h = e.data && (e.data.hfkEmbedHeight || e.data.hfkGuideHeight);
    if (typeof h === 'number' && h > 120) f.style.height = h + 'px';
  }});
}})();
</script>"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("fragment", help="아임웹에 붙여넣던 조각 HTML")
    ap.add_argument("name", help="공개 페이지 파일명 (확장자 없이)")
    ap.add_argument("--title", default=None)
    ap.add_argument("--copy", action="store_true", help="붙여넣을 iframe 조각을 클립보드로")
    ap.add_argument("--height", type=int, default=1200,
                    help="초기 높이(px). 실측값을 넣으면 높이 알림이 막혀도 그대로 맞는다")
    a = ap.parse_args()

    src = Path(a.fragment)
    if not src.is_absolute():
        src = BASE / src
    frag = src.read_text("utf-8").strip()
    if "<html" in frag.lower():
        sys.exit(f"{src.name} 은 이미 독립 페이지입니다 — 조각(fragment)만 넣으세요")

    title = a.title or a.name
    rel = src.relative_to(BASE) if src.is_relative_to(BASE) else src
    out = PUB / f"{a.name}.html"
    out.write_text(WRAP.format(title=title, src=rel, fragment=frag), "utf-8")
    print(f"  페이지  {out}  ({out.stat().st_size:,}B)")
    print(f"  주소    {PAGES}{a.name}.html")

    snip = SNIPPET.format(name=a.name, fid=a.name.replace("widget-", ""),
                          title=title, src=rel, pages=PAGES, h=a.height)
    if a.copy:
        subprocess.run(["pbcopy"], input=snip.encode("utf-8"), check=True)
        print(f"  클립보드 {len(snip):,}자 · {len(snip.splitlines())}줄")
    else:
        print("\n" + snip)
    return 0


if __name__ == "__main__":
    sys.exit(main())
