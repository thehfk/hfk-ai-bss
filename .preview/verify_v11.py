#!/usr/bin/env python3
"""v1.1 인터랙티브 슬라이드 동작 검증 (클릭형 맵 + 단계별 흐름)."""
import sys, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
DECK = HERE.parent / "presentation-ai-workshop-for-member-v1.1.html"
OUT = HERE
URL = DECK.as_uri()

NODES = ["claude", "obsidian", "imweb", "external"]

def main():
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        console_errs = []
        page.on("console", lambda m: console_errs.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: console_errs.append(str(e)))

        # 슬라이드 A (idx 25)
        page.goto(URL + "#/25")
        page.wait_for_timeout(700)

        # 기본 선택 = claude 패널 보임
        assert page.locator('[data-panel="claude"]').is_visible(), "claude 패널 기본 표시 실패"
        for hidden in ["obsidian", "imweb", "external"]:
            assert page.locator(f'[data-panel="{hidden}"]').is_hidden(), f"{hidden} 패널이 기본에 보임"
        page.screenshot(path=str(OUT / "A-0-default-claude.png"))

        # 각 노드 클릭 → 해당 패널만 보이고 다른 건 숨김
        for key in NODES:
            page.locator(f'.wnode[data-node="{key}"]').click()
            page.wait_for_timeout(350)
            if not page.locator(f'[data-panel="{key}"]').is_visible():
                errors.append(f"{key} 클릭 후 패널 미표시")
            others = [k for k in NODES if k != key]
            for o in others:
                if page.locator(f'[data-panel="{o}"]').is_visible():
                    errors.append(f"{key} 선택인데 {o} 패널이 보임")
            sel = page.locator(f'.wnode[data-node="{key}"]').get_attribute("class") or ""
            if "sel" not in sel:
                errors.append(f"{key} 노드에 sel 강조 미적용")
            page.screenshot(path=str(OUT / f"A-{key}.png"))

        # 슬라이드 B (idx 26) — fragment 단계별 진행
        page.goto(URL + "#/26")
        page.wait_for_timeout(600)
        frag_total = page.locator("#/26 .fragment").count() if False else page.evaluate(
            "() => Reveal.getSlide(26,0).querySelectorAll('.fragment').length")
        page.screenshot(path=str(OUT / "B-0-start.png"))
        for i in range(6):
            page.keyboard.press("Space")
            page.wait_for_timeout(280)
        visible_frags = page.evaluate(
            "() => Array.from(Reveal.getSlide(26,0).querySelectorAll('.fragment')).filter(f => f.classList.contains('visible')).length")
        page.screenshot(path=str(OUT / "B-1-all-steps.png"))
        if visible_frags < 4:
            errors.append(f"fragment {visible_frags}/{frag_total}개만 노출 (4+ 기대)")

        # 진행바 점프 정상 동작 (Yours 세그먼트 31-40 → 31로 이동)
        page.locator('#custom-progress .seg[data-range="31-40"]').click()
        page.wait_for_timeout(400)
        cur = page.evaluate("() => Reveal.getIndices().h")
        if cur != 31:
            errors.append(f"진행바 'Yours' 클릭 시 idx {cur} (31 기대)")

        if console_errs:
            errors.append("콘솔/페이지 에러: " + " | ".join(console_errs[:5]))

        browser.close()

    print(f"fragment total = {frag_total}, visible after spaces = {visible_frags}")
    if errors:
        print("\n검증 실패:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("\n모든 검증 통과. 스크린샷:", OUT)

if __name__ == "__main__":
    main()
