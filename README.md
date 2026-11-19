# HFK 공개 페이지

HFK 멤버·파트너가 보는 공개 정적 페이지 모음입니다. GitHub Pages 로 배포됩니다.

> 레포 이름 `hfk-ai-bss` 는 초기 'AI 부사수' 프로젝트에서 온 것입니다.
> 지금은 HFK 공개 페이지 전반을 담고 있어 이름과 내용이 다릅니다.
> 이름을 바꾸면 이미 나간 링크(이벤트 신청·파트너 매뉴얼·아임웹 임베드 등)가
> 전부 죽기 때문에 그대로 둡니다.

## 들어 있는 것

| 갈래 | 예 |
|---|---|
| 멤버 안내 | `member-guide.html` (thehfk.org/guide 가 iframe 으로 싣는 본문), `26fall-teams.html`, `faq-ai-assistant.html` |
| 이벤트 | `event-signup.html` + `event-signup-data.json` |
| ODC | `odc-lookup*.html`, `odc-membership*.html` |
| 파트너 | `partner-manual-cp.html`, `partner-manual-op.html` |
| 발표 | `presentation-newmember-orientation.html` (뉴멤버 OT) |
| 시즌 기록 | `season-26spring.html`, `season-26summer.html`, `log-26summer-sun.html`, `trends.html` |

## 여기 없는 것

개인 콘텐츠는 2026-09-04 에 분리했습니다. 옛 주소는 `404.html` 이 새 주소로 넘깁니다.

- AI 부사수 발표 → <https://seulkilog.today/ai-bss/>
- AI 워크숍 발표·브리핑 → <https://seulkilog.today/ai-workshop/>

## 고치는 법

`member-guide.html` 은 손으로 고치지 않습니다. 문구는 비공개 레포
`thehfk/hfk-workspace` 의 `data/member_guide.yml` 이 정본이고,
`scripts/build_member_guide.py` 가 이 파일을 만들어 냅니다.

## 개인정보

이 레포는 **PUBLIC** 입니다. 멤버 이름·소속·연락처가 담긴 데이터를 두지 않습니다.
(2026-09-04 `data/26spring-member-network.json` 제거 — 멤버 138명 이름·소속이 공개돼 있었습니다.)
