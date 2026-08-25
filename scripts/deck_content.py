#!/usr/bin/env python3
"""HFK 발표 덱 콘텐츠 파이프라인 (콘텐츠 .md + 주입 방식).

리치한 reveal.js HTML 디자인은 그대로 두고, 편집 가능한 '텍스트 블록'만
content/<덱이름>.md 로 빼낸다. .md 를 고치고 inject 하면 HTML 본문에 반영된다.

슬롯 키는 '슬라이드 순서 + 블록 순서'로 정한다(위치 기반). 즉 슬라이드 구조를
바꾸지 않고 '텍스트만' 편집하는 워크플로우를 전제로 한다.

명령:
  extract <deck.html> [md]   # 리프 텍스트 블록(h1~h4,p,li)의 innerHTML 을 content/<name>.md 로 추출
  inject  <deck.html> [md]   # content/<name>.md 를 읽어 HTML 본문에 반영(같은 위치의 블록 innerHTML 치환)
  check   <deck.html>        # extract→inject 왕복 후 '보이는 텍스트/슬라이드 수'가 원본과 동일한지 검증
  extract-all <deck.html...> # 여러 덱을 한 번에 추출

워크플로우:
  (수시) content/<name>.md 편집 → `python scripts/deck_content.py inject <deck>` → git push → GitHub Pages 반영
"""
import sys, os, re, html
from bs4 import BeautifulSoup

BLOCK = ["h1", "h2", "h3", "h4", "p", "li"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(ROOT, "content")
# 발표 텍스트 원본(.md)은 개인 자료라 Memo 보관함이 정본이다. 이 레포에는 배포용 HTML 만 둔다.
# 레포 content/ 는 아직 안 옮긴 덱을 위한 폴백일 뿐이다.
MEMO_CONTENT_DIR = os.path.expanduser(
    "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Memo/3 콘텐츠/발표/AI부사수/_content"
)


def md_path(deck, md=None):
    """<덱이름>.md 경로. Memo(정본) 우선, 없으면 레포 content/ 폴백."""
    if md:
        return md
    base = os.path.splitext(os.path.basename(deck))[0]
    memo = os.path.join(MEMO_CONTENT_DIR, base + ".md")
    if os.path.exists(memo):
        return memo
    repo = os.path.join(CONTENT_DIR, base + ".md")
    if os.path.exists(repo):
        return repo
    return memo  # 새로 추출하는 덱은 Memo 에 쓴다


def soup_of(deck):
    with open(deck, encoding="utf-8") as f:
        return BeautifulSoup(f.read(), "html.parser")


def slides_of(soup):
    slides = soup.select(".slides > section")
    return slides if slides else soup.find_all("section")


def is_leaf_block(el):
    """다른 블록을 품지 않는 '잎' 블록만 편집 단위로 삼는다(중첩 충돌 방지)."""
    return el.name in BLOCK and el.find(BLOCK) is None


def leaf_blocks(section):
    return [el for el in section.find_all(BLOCK) if is_leaf_block(el)]


def inner_html(el):
    # decode_contents(): 텍스트 노드의 <, >, & 를 엔티티로 이스케이프하며 innerHTML 직렬화
    # (책 제목 <...> 같은 리터럴 꺾쇠가 주입 때 태그로 오인돼 유실되는 것을 방지)
    return el.decode_contents()


def extract(deck, md=None):
    soup = soup_of(deck)
    out = [f"# {os.path.basename(deck)}",
           "<!-- 이 파일의 각 블록 텍스트를 고치고 `python scripts/deck_content.py inject "
           f"{os.path.basename(deck)}` 를 실행하면 발표 HTML에 반영됩니다. 슬롯 헤더(### sN-M)는 위치 키이니 지우지 마세요. -->",
           ""]
    for si, sec in enumerate(slides_of(soup)):
        label = ""
        h = sec.find(["h1", "h2"])
        if h:
            label = " · " + re.sub(r"\s+", " ", h.get_text(" ", strip=True))[:40]
        out.append(f"## slide {si}{label}")
        for n, el in enumerate(leaf_blocks(sec)):
            out.append(f"### s{si}-{n}  ({el.name})")
            out.append(inner_html(el).strip())
            out.append("")
        out.append("")
    dst = md_path(deck, md)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")
    return dst


SLOT_RE = re.compile(r"^### (s\d+-\d+)\b", re.M)


def parse_md(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    slots = {}
    parts = SLOT_RE.split(text)
    # parts: [preamble, key1, body1, key2, body2, ...]
    for i in range(1, len(parts), 2):
        key = parts[i].strip()
        body = parts[i + 1]
        # 슬롯 헤더 줄의 나머지(" (p)") 제거 후, 다음 '## '/'### ' 전까지가 본문
        body = re.split(r"\n#{2,3} ", body, maxsplit=1)[0]
        body = body.split("\n", 1)[1] if "\n" in body else ""
        slots[key] = body.strip()
    return slots


def inject(deck, md=None, write=True):
    src = md_path(deck, md)
    slots = parse_md(src)
    soup = soup_of(deck)
    applied = 0
    for si, sec in enumerate(slides_of(soup)):
        for n, el in enumerate(leaf_blocks(sec)):
            key = f"s{si}-{n}"
            if key in slots:
                new = BeautifulSoup(slots[key], "html.parser")
                el.clear()
                for c in list(new.contents):
                    el.append(c)
                applied += 1
    result = str(soup)
    if write:
        with open(deck, "w", encoding="utf-8") as f:
            f.write(result)
    return applied, result


def visible_text(s):
    soup = s if isinstance(s, BeautifulSoup) else BeautifulSoup(s, "html.parser")
    for t in soup(["script", "style"]):
        t.extract()
    return re.sub(r"\s+", " ", soup.get_text(" ", strip=True))


def check(deck):
    """extract→inject 왕복 후 보이는 텍스트와 슬라이드 수가 원본과 같은지 검증."""
    with open(deck, encoding="utf-8") as f:
        original = f.read()
    orig_soup = BeautifulSoup(original, "html.parser")
    n_orig = len(slides_of(orig_soup))
    vt_orig = visible_text(orig_soup)
    tmp = md_path(deck, os.path.join(os.path.dirname(md_path(deck)), "_check_tmp.md"))
    extract(deck, tmp)
    _, injected = inject(deck, tmp, write=False)
    os.remove(tmp)
    inj_soup = BeautifulSoup(injected, "html.parser")
    n_inj = len(slides_of(inj_soup))
    vt_inj = visible_text(inj_soup)
    ok = (n_orig == n_inj) and (vt_orig == vt_inj)
    print(f"  slides: {n_orig} -> {n_inj}  {'OK' if n_orig==n_inj else 'MISMATCH'}")
    print(f"  visible-text identical: {vt_orig == vt_inj}")
    if not ok and vt_orig != vt_inj:
        # 첫 차이 위치 보고
        for i, (a, b) in enumerate(zip(vt_orig, vt_inj)):
            if a != b:
                print(f"  first diff @ char {i}: ...{vt_orig[max(0,i-30):i+30]!r} vs {vt_inj[max(0,i-30):i+30]!r}")
                break
    return ok


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "extract":
        dst = extract(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        print(f"extracted -> {dst}")
    elif cmd == "extract-all":
        for deck in sys.argv[2:]:
            dst = extract(deck)
            print(f"extracted -> {dst}")
    elif cmd == "inject":
        applied, _ = inject(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        print(f"injected {applied} slots -> {sys.argv[2]}")
    elif cmd == "check":
        ok = check(sys.argv[2])
        print("CHECK", "PASS" if ok else "FAIL")
        return 0 if ok else 1
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
