# 발표 덱 콘텐츠 파이프라인 (콘텐츠 .md + 주입)

리치한 reveal.js HTML 디자인은 그대로 두고, **편집 가능한 텍스트 블록만** 이 폴더의
`*.md` 로 빼놓은 것입니다. `.md` 를 고치고 주입(inject)하면 발표 HTML 본문에 반영되고,
git push 하면 `skaug12.github.io/hfk-ai-bss/` 에 배포됩니다.

## 워크플로우

```bash
# 1) content/<덱이름>.md 에서 원하는 블록 텍스트를 수정
#    - '### s3-2  (p)' 같은 슬롯 헤더는 위치 키이니 지우지 말 것
#    - 슬라이드 순서를 바꾸지 말 것(텍스트만 편집). 순서를 바꾸면 슬롯이 어긋남
#    - <, > 는 &lt; &gt; 로. 책 제목은 《제목》 권장

# 2) 주입 (HTML 본문 갱신)
python3 scripts/deck_content.py inject presentation-ai부사수-26여름-3-sun.html

# 3) 검증 (보이는 텍스트·슬라이드 수가 보존되는지)
python3 scripts/deck_content.py check presentation-ai부사수-26여름-3-sun.html

# 4) 배포
git add -A && git commit -m "content: 3-sun 문구 수정" && git push
```

## 명령

| 명령 | 설명 |
|---|---|
| `extract <deck.html>` | 덱의 텍스트 블록(h1~h4·p·li)을 `content/<name>.md` 로 추출 |
| `inject  <deck.html>` | `content/<name>.md` 를 읽어 HTML 본문에 반영 |
| `check   <deck.html>` | extract→inject 왕복 후 '보이는 텍스트/슬라이드 수'가 원본과 동일한지 검증 |
| `extract-all <deck.html...>` | 여러 덱 일괄 추출 |

## 동작 방식 / 주의

- 슬롯 키 `sN-M` 은 **N번째 슬라이드의 M번째 잎 텍스트 블록**(위치 기반)입니다.
  텍스트만 고치는 한 안전합니다. 슬라이드를 추가/삭제/재정렬하면 그 덱을 다시 `extract` 하세요.
- 디자인(카드·그리드·색·스크립트)은 건드리지 않습니다. `.md` 에는 각 블록의 innerHTML
  (인라인 `<span class="bold">` 등 포함)이 들어갑니다.
- **첫 inject** 때는 HTML이 파서 기준으로 한 번 정규화되어 포맷 diff가 크게 잡힐 수 있습니다.
  내용(보이는 텍스트)은 보존됩니다(아래 검증 완료).

## 커버된 덱 (전부 `check PASS`)

- `presentation-ai부사수-26여름-1-fri.html`, `-1-sun.html`
- `presentation-ai부사수-26여름-2-fri.html`, `-2-sun.html`
- `presentation-ai부사수-3.html` (3회차 주중), `presentation-ai부사수-26여름-3-sun.html` (3회차 주말)
- `presentation-ai부사수-26여름-4-fri.html`, `-4-sun.html`
- `presentation-ai-workshop-for-member-mobile.html` (멤버 워크숍)

> 검증: 위 8개 모두 extract→inject 왕복 후 보이는 텍스트·슬라이드 수 100% 일치.
