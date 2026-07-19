# presentation-ai부사수-26여름-2-sun.html
<!-- 이 파일의 각 블록 텍스트를 고치고 `python scripts/deck_content.py inject presentation-ai부사수-26여름-2-sun.html` 를 실행하면 발표 HTML에 반영됩니다. 슬롯 헤더(### sN-M)는 위치 키이니 지우지 마세요. -->

## slide 0 · Claude Code 활용 가이드
### s0-0  (h1)
Claude Code<br/>활용 가이드

### s0-1  (p)
커스텀 스킬로 만드는 나만의 AI 업무 자동화

### s0-2  (p)
실제 운영 사례와 함께 보는 100개 스킬

### s0-3  (p)
26여름 AI부사수 2회차 · 7월 5일 (일) · @Seulki.log


## slide 1 · 지난 시간에 다룬 것
### s1-0  (h2)
지난 시간에 다룬 것

### s1-1  (h3)
클로드 코드란?

### s1-2  (p)
내 말을 이해하는 개발자. 한국어로 말하면 알아서 코드를 설계해 문제를 해결해주는 AI.

### s1-3  (p)
ChatGPT는 "알려주는" AI, 클로드 코드는 <span class="bold">"실행하는" AI</span>.

### s1-4  (h3)
스킬과 에이전트

### s1-5  (p)
<span class="bold">스킬 = 레시피</span><br/>정해진 순서대로 실행

### s1-6  (p)
<span class="bold">에이전트 = 요리사</span><br/>스스로 판단하며 여러 단계를 처리

### s1-7  (h3)
반자동화 vs 완전자동화

### s1-8  (p)
클로드 코드는 <span class="bold">반자동화</span> 방식. 중간중간 "이렇게 할까요?" 확인하며 진행.

### s1-9  (p)
매니저로서 프로세스를 직접 점검하고 주도.

### s1-10  (h3)
HFK 실전 사례

### s1-11  (p)
Obsidian → 클로드 코드(106개 스킬) → 아임웹 쇼핑몰 → Slack·캘린더. 반복되는 운영 업무를 반자동화.

### s1-12  (h3)
1회차 핵심 메시지

### s1-13  (p)
"코딩을 몰라도 됨. 중요한 건 <span class="accent bold">'이걸로 뭘 할 수 있을까?'</span>를 상상하는 것."

### s1-14  (p)
<span class="accent bold">오늘의 흐름</span> —
      <span class="sub">지난 시간 복습 → Claude Code 개념 → 직접 만들기 워크숍 → STAR → 마무리</span>


## slide 2 · 자주 묻는 질문
### s2-0  (h2)
자주 묻는 질문

### s2-1  (p)
Q. 계정 하나로 컴퓨터 몇 대까지 쓸 수 있나요?

### s2-2  (p)
본인이 쓰는 컴퓨터라면 여러 대도 괜찮습니다. "몇 대까지"라는 정해진 숫자는 없습니다. 회사 노트북과 집 데스크톱을 오가며 같은 계정으로 쓰는 건 문제없습니다. 단, 다른 사람과 계정을 나눠 쓰는 건 금지입니다. 그리고 여러 대에서 동시에 많이 돌려도 사용량 한도는 한 계정에서 함께 빠져나갑니다.


## slide 3 · 대화 기록은 컴퓨터마다 따로 저장됩니다
### s3-0  (h2)
대화 기록은 컴퓨터마다 따로 저장됩니다

### s3-1  (p)
클로드 코드의 대화 기록은 인터넷 계정이 아니라, 지금 쓰는 컴퓨터의 디스크에 파일로 쌓입니다. 그래서 A 컴퓨터에서 나눈 대화가 B 컴퓨터에 저절로 나타나지 않습니다.

### s3-2  (h3)
무슨 뜻이냐면

### s3-3  (li)
회사 컴퓨터에서 한 대화는 회사 컴퓨터에만 남습니다.

### s3-4  (li)
집 노트북을 켜면, 같은 계정이어도 그 대화는 안 보입니다.

### s3-5  (li)
계정은 클라우드, 대화 기록은 내 컴퓨터. 둘은 따로입니다.

### s3-6  (h3)
그래서 좋은 점

### s3-7  (p)
내 대화는 내 컴퓨터 안에 있는 <span class="bold">내 자산</span>입니다. 회사 계정을 반납하더라도, 파일만 미리 빼두면 다른 컴퓨터에서 그대로 열어볼 수 있습니다.


## slide 4 · 강의를 듣고 결정하기보다, 구독하며 공부하기
### s4-0  (h2)
강의를 듣고 결정하기보다, 구독하며 공부하기

### s4-1  (p)
AI 도구는 영상으로 미리 다 배운 뒤 시작하는 게 아닙니다. 직접 써보면서 익히는 게 훨씬 빠릅니다.

### s4-2  (li)
영상으로 개념만 익히고, 구독할지 말지 계속 고민합니다.

### s4-3  (li)
막상 손이 잘 안 갑니다.

### s4-4  (li)
배운 내용이 며칠 지나면 사라집니다.

### s4-5  (li)
월 27,000원으로 내 업무를 직접 시켜봅니다.

### s4-6  (li)
오늘 배운 걸 오늘 적용합니다.

### s4-7  (li)
손에 남는 실력이 쌓입니다.

### s4-8  (p)
<span class="accent bold">운전은 영상으로 못 배웁니다.</span>
<span class="sub">차에 앉아 핸들을 잡아야 늡니다. 클로드도 똑같습니다.</span>


## slide 5 · 같은 데이터 분석을 맡기면: 두 사람 비유
### s5-0  (h2)
같은 데이터 분석을 맡기면: 두 사람 비유

### s5-1  (p)
같은 매출 표에 '지난달 대비 증감률 뽑아줘'라고 시켜봅니다. 둘은 <span style="color:var(--accent);font-weight:600;">서로 다른 종류의 실수</span>를 합니다.

### s5-2  (p)
Claude (채팅) = 암산 천재, 검산은 안 함

### s5-3  (li)
큰 표를 끝까지 안 보고 머릿속으로 어림한다

### s5-4  (li)
'약 12% 증가한 것 같아요' (실제로는 9%)

### s5-5  (li)
틀려도 자신 있게 말해 티가 안 난다

### s5-6  (p)
실수 유형: 맞는 질문에 틀린 답

### s5-7  (p)
Claude Code = 검산은 완벽, 가끔 엉뚱한 걸 계산

### s5-8  (li)
코드로 정확히 9.3% 산출 (다시 돌려도 같은 값)

### s5-9  (li)
단, '지난달'에 취소 주문을 넣었다면?

### s5-10  (li)
그 잘못된 전제로 정확한 9.3%를 낸다

### s5-11  (p)
실수 유형: 틀린 질문에 맞는 답

### s5-12  (p)
<span style="color:var(--accent);font-weight:600;">그래서 사람이 챙길 것이 다릅니다</span>: <span class="sub">채팅에는 검산(숫자가 맞는지)을, Claude Code에는 전제 확인(무엇을 계산할지)을 짚어줘야 합니다.</span>


## slide 6 · Claude Code를 이해하는 데 필요한 개념들
### s6-0  (h2)
Claude Code를 이해하는 데 필요한 개념들

### s6-1  (p)
Claude Code를 이해하려면 이 네 가지만 알면 됩니다. <span style="color:var(--accent);font-weight:600;">카페 운영</span>에 비유해봅시다.

### s6-2  (p)
Skill

### s6-3  (h3)
레시피

### s6-4  (p)
'아메리카노 만드는 법'처럼<br/>업무 절차를 적어둔 <span style="font-weight:600;">마크다운 파일</span>

### s6-5  (p)
<span style="color:var(--accent);font-weight:600;">실제 예)</span> /sync-products<br/>→ 노트 읽기 → HTML 변환 → 아임웹 반영

### s6-6  (p)
Agent

### s6-7  (h3)
매니저

### s6-8  (p)
레시피 여러 개를 조합해서<br/><span style="font-weight:600;">알바생들에게 순서대로 시키는 사람</span>

### s6-9  (p)
<span style="color:var(--accent2);font-weight:600;">실제 예)</span> /run-season-ops<br/>→ 일정 + 동기화 + 레터 + 슬랙 한 번에

### s6-10  (p)
API

### s6-11  (h3)
주문 창구

### s6-12  (p)
외부 서비스와 데이터를 주고받는<br/><span style="font-weight:600;">정해진 규격의 통로</span>

### s6-13  (p)
<span style="color:var(--accent3);font-weight:600;">실제 예)</span> 아임웹 API<br/>→ 상품 조회, 수정, 등록을 코드로 처리

### s6-14  (p)
MCP

### s6-15  (h3)
멀티탭

### s6-16  (p)
API라는 플러그를 Claude Code에<br/><span style="font-weight:600;">꽂을 수 있게 해주는 어댑터</span>

### s6-17  (p)
<span style="color:var(--accent4);font-weight:600;">실제 예)</span> Slack MCP 서버<br/>→ Claude가 직접 메시지 발송, 채널 생성


## slide 7 · 요즘 더 알아두면 좋은 개념
### s7-0  (h2)
요즘 더 알아두면 좋은 개념

### s7-1  (p)
스킬과 에이전트에 더해, 이 세 가지를 알아두면 AI 도구를 더 깊이 이해할 수 있습니다.

### s7-2  (p)
RAG

### s7-3  (h3)
검색 증강

### s7-4  (p)
답하기 전에 필요한 자료를 먼저 찾아 읽는 방식. 내 문서와 기록을 근거로 답하게 만듭니다.

### s7-5  (p)
비유) 매뉴얼을 펴놓고 답하기

### s7-6  (p)
Harness

### s7-7  (h3)
실행 골격

### s7-8  (p)
일일이 시키지 않아도 런타임이 훅, 설정, 스킬을 자동 실행하는 골격. Claude Code 자체가 하나의 하니스입니다.

### s7-9  (p)
비유) 자동으로 도는 주방 동선

### s7-10  (p)
Artifact

### s7-11  (h3)
결과물

### s7-12  (p)
Claude가 만들어내는 문서, 코드, 대시보드 같은 결과물. 따로 보관해두고 다음 작업의 재료로 씁니다.

### s7-13  (p)
비유) 만들어 쌓아두는 완성품


## slide 8 · 지금 HFK는 이렇게 쓰고 있습니다
### s8-0  (h2)
지금 HFK는 이렇게 쓰고 있습니다

### s8-1  (p)
셋 다 모델이 아니라 <span style="color:var(--accent);font-weight:600;">AI를 둘러싼 환경</span>을 짜는 이야기입니다.

### s8-2  (p)
RAG

### s8-3  (h3)
답하기 전에 내 자료부터

### s8-4  (p)
Claude가 답하기 전에 메모리와 옵시디언 노트, 후기 톤을 먼저 읽습니다. 기억이 아니라 내가 모은 자료에서 끌어옵니다.

### s8-5  (p)
<span style="color:var(--accent3);font-weight:600;">지금)</span> MEMORY.md, note/리뷰 톤, 녹취 먼저 읽기

### s8-6  (p)
카오스 엔지니어링

### s8-7  (h3)
깨질 때를 미리 설계

### s8-8  (p)
잘 돌 때를 믿지 않고, 끊기거나 두 번 실행되는 상황을 미리 막아둡니다. 사고를 한 번 겪으면 그 자리에 방어막을 답니다.

### s8-9  (p)
<span style="color:var(--accent5);font-weight:600;">지금)</span> 헬스체크 알림, 발송 로그, 멱등 가드

### s8-10  (p)
하네스

### s8-11  (h3)
AI에게 도구·규칙을 깔아주기

### s8-12  (p)
같은 AI라도 어떤 도구와 규칙을 주고, 얼마나 자주 피드백과 메모리를 남기느냐로 결과가 갈립니다. 이 워크스페이스 전체가 하나의 하네스입니다.

### s8-13  (p)
<span style="color:var(--accent);font-weight:600;">지금)</span> 스킬 100개, CLAUDE.md 규칙, 메모리

### s8-14  (p)
<span class="sub">개념으로 배워서 한 게 아니라, 운영하면서 필요해서 스스로 만들어 온 것들입니다.</span>


## slide 9 · Claude Code, 어디서 쓸 수 있나?
### s9-0  (h2)
Claude Code, 어디서 쓸 수 있나?

### s9-1  (h3)
가장 강력한 방식

### s9-2  (p)
스킬, 에이전트, 자동화 모두 가능

### s9-3  (p)
추천: 자동화가 많은 분

### s9-4  (h3)
에디터 안에서 바로

### s9-5  (p)
코드 변경 사항을 시각적으로 비교

### s9-6  (p)
추천: VS Code 사용자

### s9-7  (h3)
설치 없이 브라우저에서

### s9-8  (p)
클라우드 실행, 폰에서도 확인 가능

### s9-9  (p)
추천: 빠르게 써보고 싶은 분

### s9-10  (h3)
일반 앱처럼

### s9-11  (p)
터미널 없이 GUI로 사용

### s9-12  (p)
추천: 터미널이 부담스러운 분

### s9-13  (p)
<span style="color:var(--accent);font-weight:600;">Cowork 모드</span>: <span class="sub">한 세션을 여러 사람이 동시에 보며 협업. 화면 공유 없이 같은 작업을 실시간으로 함께 볼 수 있습니다.</span>

### s9-14  (p)
<a href="https://github.com/skaug12/hfk-presentations/blob/main/claude-code-platforms.md" style="color:var(--accent);text-decoration:underline;font-weight:600;" target="_blank">플랫폼별 권한, 기능 상세 비교 →</a>


## slide 10 · 스킬 워크숍: 직접 만들어 봅니다
### s10-0  (h2)
스킬 워크숍: 직접 만들어 봅니다

### s10-1  (p)
내 반복 업무를 스킬로 만들어 보는 시간입니다. 프롬프트는 이렇게 씁니다: <span style="color:var(--accent);font-weight:600;">① 내 상황을 최대한 구체적으로 → ② 원하는 결과물 → ③ '이 일을 다시 쓰게 스킬로 만들어줘'</span>

### s10-2  (p)
01

### s10-3  (h3)
웹 크롤링으로 기록 수집

### s10-4  (p)
Claude Code로 웹을 크롤링해 흩어진 기록을 한곳에 모읍니다.

### s10-5  (p)
02

### s10-6  (h3)
유튜브 브리핑 만들기

### s10-7  (p)
YouTube를 연결해 재생목록에 영상을 넣으면, 그 내용을 정리한 브리핑이 자동으로 만들어집니다.

### s10-8  (p)
03

### s10-9  (h3)
액션 플랜과 캘린더

### s10-10  (p)
쌓인 기록을 정리해 액션 플랜을 만들고, 그대로 캘린더에 일정으로 적습니다.

### s10-11  (p)
04

### s10-12  (h3)
인스타 카드뉴스

### s10-13  (p)
인스타그램 카드뉴스 콘텐츠를 만들고 포스팅까지 이어갑니다.


## slide 11 · 웹 크롤링으로 기록 모으기 API·MCP 없이
### s11-0  (h2)
웹 크롤링으로 기록 모으기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(91,123,94,0.12);color:var(--accent3);vertical-align:middle;white-space:nowrap;">API·MCP 없이</span>

### s11-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 흩어진 글과 자료를 Claude Code가 웹에서 가져와 한 폴더에 정리합니다.

### s11-2  (p)
준비물: 모으고 싶은 사이트 주소, 저장할 폴더 이름. 따라 입력만 하면 됩니다.

### s11-3  (p)
STEP 1

### s11-4  (h3)
목록부터 만들기

### s11-5  (p)
STEP 2

### s11-6  (h3)
본문 저장하기

### s11-7  (p)
STEP 3

### s11-8  (h3)
깔끔하게 정리

### s11-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 크롤링 폴더에 글마다 마크다운 파일과 목록 표가 생깁니다. <span class="dim">공개된 페이지만 가져오고, 사이트의 robots 규칙을 지키세요.</span>

### s11-10  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: Claude Code의 웹 가져오기 기능과 Playwright(브라우저 자동화)로 페이지를 열어, '본문만 추려서 마크다운으로 저장해줘' 프롬프트를 더해 만듭니다.


## slide 12 · 유튜브로 브리핑 노트 만들기 API 연결
### s12-0  (h2)
유튜브로 브리핑 노트 만들기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(61,90,128,0.12);color:var(--accent2);vertical-align:middle;white-space:nowrap;">API 연결</span>

### s12-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 재생목록에 영상을 넣으면, 그 영상 내용을 요약한 브리핑 노트가 자동으로 만들어집니다.

### s12-2  (p)
준비물: 유튜브 재생목록 하나, /analyze-youtube 스킬

### s12-3  (p)
STEP 1

### s12-4  (h3)
영상 담기

### s12-5  (p)
브리핑 받고 싶은 영상을 'AI브리핑' 재생목록에 추가합니다.

### s12-6  (p)
STEP 2

### s12-7  (h3)
브리핑 요청

### s12-8  (p)
STEP 3

### s12-9  (h3)
노트로 저장

### s12-10  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 영상마다 요점, 인용, 적용 아이디어가 담긴 브리핑 노트가 쌓입니다. <span class="dim">자막이 없는 영상은 음성에서 자동으로 받아씁니다.</span>

### s12-11  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: 유튜브 자막을 가져오는 기능에 '요점만 정리해줘' 프롬프트를 묶은 /analyze-youtube 스킬입니다.


## slide 13 · 기록을 액션 플랜으로, 캘린더까지 MCP 연결
### s13-0  (h2)
기록을 액션 플랜으로, 캘린더까지 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(123,107,138,0.12);color:var(--accent4);vertical-align:middle;white-space:nowrap;">MCP 연결</span>

### s13-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 쌓인 메모를 정리해 할 일 목록을 만들고, 그대로 캘린더에 일정으로 넣습니다.

### s13-2  (p)
준비물: 정리할 노트 폴더, Google Calendar 연결(MCP)

### s13-3  (p)
STEP 1

### s13-4  (h3)
할 일만 뽑기

### s13-5  (p)
STEP 2

### s13-6  (h3)
살 붙이기

### s13-7  (p)
STEP 3

### s13-8  (h3)
캘린더 등록

### s13-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 액션 플랜 문서가 생기고, 마감일 일정이 캘린더에 올라갑니다. <span class="dim">먼저 미리보기만 요청해 확인한 뒤 등록하세요.</span>

### s13-10  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: 노트를 읽는 파일 기능과 Google Calendar 연결(MCP)에 '할 일만 뽑아 일정으로 넣어줘' 프롬프트를 더해 만듭니다.


## slide 14 · 인스타그램 카드뉴스 만들어 올리기 API 연결
### s14-0  (h2)
인스타그램 카드뉴스 만들어 올리기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(61,90,128,0.12);color:var(--accent2);vertical-align:middle;white-space:nowrap;">API 연결</span>

### s14-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 글 하나로 인스타그램 카드뉴스를 만들고 예약 발행까지 합니다.

### s14-2  (p)
준비물: 소재가 될 글이나 주제, /post-to-buffer 스킬(Buffer 연결)

### s14-3  (p)
STEP 1

### s14-4  (h3)
장면 쪼개기

### s14-5  (p)
STEP 2

### s14-6  (h3)
이미지로

### s14-7  (p)
STEP 3

### s14-8  (h3)
예약 발행

### s14-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 카드 이미지 세트와 예약된 인스타 포스팅이 만들어집니다. <span class="dim">첫 장 후킹 문구가 가장 중요합니다. 좌상단부터 읽히게 두세요.</span>

### s14-10  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: Playwright로 카드 HTML을 1080x1080 이미지로 렌더링하고, Buffer 예약 발행 API로 올리는 /post-to-buffer 스킬입니다.


## slide 15 · 직접 해보기: 하루를 자동 기록하는 /run-daily-note 스킬 만
### s15-0  (h2)
직접 해보기: 하루를 자동 기록하는 /run-daily-note 스킬 만들기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(91,123,94,0.12);color:var(--accent3);vertical-align:middle;white-space:nowrap;">API·MCP 없이</span>

### s15-1  (p)
<span style="color:var(--accent);font-weight:600;">미션:</span> 오늘 한 작업을, 어떤 프롬프트로 무슨 결과가 나왔는지까지 데일리 노트 한 장에 그대로 남기는 스킬을 만드세요.

### s15-2  (p)
준비물: Claude Code가 도는 작업 폴더. 프롬프트는 '상황 구체화 → 결과물 형식 → 스킬화' 순서로. <span style="color:var(--accent);">폼이 아니라 대화예요: 한 칸 친 뒤 Claude 답을 보고 다음 칸으로 (앞 내용은 기억하니 다시 안 써도 됨).</span>

### s15-3  (p)
STEP 1

### s15-4  (h3)
작업 내역 자동 수집

### s15-5  (p)
STEP 2

### s15-6  (h3)
프롬프트·답변·결정·결과 남기기

### s15-7  (p)
STEP 3

### s15-8  (h3)
스킬로 만들기

### s15-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 부를 때마다 그날 작업이 <span style="font-weight:600;">① 내 프롬프트 → ② Claude 답변·처리 → ③ 의사결정 → ④ 결과</span> 순으로 그대로 남습니다. 나중에 펼치면 그날 작업이 재현됩니다.


## slide 16 · Gen AI 보안 리스크 관리
### s16-0  (h2)
Gen AI 보안 리스크 관리

### s16-1  (p)
AI를 업무에 활용할 때 반드시 알아야 할 보안 원칙입니다.

### s16-2  (p)
공유해도 되는 것

### s16-3  (li)
코드, 개발 관련 질문

### s16-4  (li)
일반적인 업무 내용, 기획 아이디어

### s16-5  (li)
마케팅 카피, 콘텐츠 초안

### s16-6  (p)
피해야 하는 것

### s16-7  (li)
비밀번호, API 키, 인증 토큰

### s16-8  (li)
주민등록번호, 계좌번호, 카드번호

### s16-9  (li)
고객 개인정보 (이름+연락처+주소 조합)

### s16-10  (li)
미발표 일정, 공개 전 내부 전략

### s16-11  (p)
1. 데이터 격리

### s16-12  (p)
민감 정보는 .env 파일로 분리, .gitignore로 업로드 차단

### s16-13  (p)
2. 대화는 휘발성

### s16-14  (p)
대화는 나와 Claude만 볼 수 있고, 끝나면 Claude도 잊어버림

### s16-15  (p)
3. 로컬 실행

### s16-16  (p)
Claude Code는 내 컴퓨터에서 실행. 파일 내용은 처리를 위해 Anthropic 서버로 전송되지만 저장되지 않음


## slide 17 · 토큰, 아껴 쓰는 법
### s17-0  (h2)
토큰, 아껴 쓰는 법

### s17-1  (p)
토큰 = Claude가 읽고 쓰는 글자 단위. 매 질문마다 지금까지의 대화 전체를 다시 읽습니다. 대화가 길어질수록 한 번 질문에 쓰는 토큰이 눈덩이처럼 불어납니다.

### s17-2  (h3)
1. 낡은 세션 정리: /compact

### s17-3  (p)
<code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/compact</code> = 지금까지의 대화 내용을 요약본으로 압축하는 명령어.

### s17-4  (li)
대화가 길어졌을 때 입력하면 과거 내용을 짧게 줄여줌

### s17-5  (li)
주제가 바뀔 때마다 한 번씩 실행하면 효과적

### s17-6  (li)
아예 새 대화를 시작하는 것도 방법

### s17-7  (p)
한 세션에서 모든 걸 하려 하지 마세요. 주제별로 나누는 게 낫습니다.

### s17-8  (h3)
2. Claude가 읽을 범위 좁히기

### s17-9  (p)
Claude는 '어디를 봐야 하는지' 모르면 폴더 전체를 탐색합니다. 파일 경로와 범위를 명확히 지정하세요.

### s17-10  (li)
<span style="color:var(--accent5);">✗</span> '이 프로젝트 개선해줘' → 수십 개 파일 탐색

### s17-11  (li)
<span style="color:var(--accent3);">✓</span> 'src/auth.ts 파일의 login 함수 수정해줘' → 파일 1-2개만 읽음

### s17-12  (p)
경로가 명확할수록 토큰이 줄고, 결과도 정확해집니다.

### s17-13  (h3)
3. 기본 모델 바꾸기

### s17-14  (p)
기본값은 Sonnet. 복잡한 작업에만 Opus로 전환해서 사용.

### s17-15  (p)
<code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/model sonnet</code> 으로 전환

### s17-16  (h3)
4. 작업 전: /status

### s17-17  (p)
큰 작업을 시작하기 전에 <code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/status</code>로 현재 세션 정보 확인. 대화가 길어졌다면 /compact 또는 새 세션.

### s17-18  (h3)
5. 작업 중: /cost

### s17-19  (p)
<code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/cost</code>로 현재 세션에서 사용한 비용 확인. Pro/Max 구독이면 API 비용 없이 사용 가능.


## slide 18 · 두번째 지능이란?
### s18-0  (h2)
두번째 지능이란?

### s18-1  (h3)
첫번째 지능: 타고난 능력

### s18-2  (li)
학습, 분석, 판단 등 인지적 능력

### s18-3  (li)
경험과 훈련으로 향상되지만 한계 존재

### s18-4  (li)
AI가 빠르게 대체하기 시작한 영역

### s18-5  (h3)
두번째 지능: AI로 확장된 능력

### s18-6  (li)
AI를 통해 가능해지는 새로운 실행력

### s18-7  (li)
기획자도 개발자의 눈을 가질 수 있다

### s18-8  (li)
미뤄뒀던 일, 엄두 못 냈던 영역에 도전

### s18-9  (p)
<span style="color:var(--accent);font-weight:600;">HFK AI부사수 팀의 질문</span>: <span class="sub">'나에게 AI 부사수가 생긴다면, 지금 당장 무엇부터 시킬 것인가?'</span>


## slide 19 · STAR 프레임워크: 두번째 지능 활용법
### s19-0  (h2)
STAR 프레임워크: 두번째 지능 활용법

### s19-1  (h3)
Start

### s19-2  (p)
하고 싶었는데<br/>미뤄왔던 일

### s19-3  (p)
습관 형성

### s19-4  (h3)
Try

### s19-5  (p)
평소 잘 못한다고<br/>생각했던 것

### s19-6  (p)
도전과 성장

### s19-7  (h3)
Amplify

### s19-8  (p)
이미 잘하지만<br/>더 잘하고 싶은 것

### s19-9  (p)
차별화와 전문성

### s19-10  (h3)
Recover

### s19-11  (p)
반복적인 작업을<br/>효율화하는 것

### s19-12  (p)
효율과 재투자

### s19-13  (h3)
워크숍: 내 STAR 찾기

### s19-14  (p)
S: 무엇을 시작할까?

### s19-15  (p)
오랫동안 미뤄온 업무 자동화가 있나요?

### s19-16  (p)
T: 무엇에 도전할까?

### s19-17  (p)
개발자에게 맡겨야 한다고 생각했던 것은?

### s19-18  (p)
A: 무엇을 증폭할까?

### s19-19  (p)
내가 이미 잘하는 것 + AI = ?

### s19-20  (p)
R: 무엇을 효율화할까?

### s19-21  (p)
반복 업무 중 자동화할 수 있는 것은?


## slide 20 · STAR 2×2 매트릭스
### s20-0  (h2)
STAR 2×2 매트릭스

### s20-1  (p)
나의 우선순위는 어디에 있는지, 한 눈에 보기. <span class="dim" style="font-size:0.88em;">X축: 역량, 기반 (약함 → 강함)  ,   Y축: 지향 (효율 → 성장)</span>

### s20-2  (p)
S, Start

### s20-3  (p)
하고 싶었는데 미뤄왔던 일

### s20-4  (p)
습관 형성

### s20-5  (p)
A, Amplify

### s20-6  (p)
이미 잘하지만 더 잘하고 싶은 것

### s20-7  (p)
차별화와 전문성

### s20-8  (p)
T, Try

### s20-9  (p)
평소 잘 못한다고 생각했던 것

### s20-10  (p)
도전과 성장

### s20-11  (p)
R, Recover

### s20-12  (p)
반복적인 작업을 효율화하는 것

### s20-13  (p)
효율과 재투자

### s20-14  (p)
바쁜 직장인

### s20-15  (p)
Start + Recover: 미뤄둔 습관 만들고, 반복 업무 줄이기

### s20-16  (p)
균형 추구

### s20-17  (p)
Start + Try: 미뤄둔 것 시작하고, 못하던 것에 도전


## slide 21 · 강점차별화 2×2 매트릭스
### s21-0  (h2)
강점차별화 2×2 매트릭스

### s21-1  (p)
같은 축 맥락으로, 내가 하는 업무를 선호도와 인정도로 매핑. <span class="dim" style="font-size:0.88em;">X축: 선호도 (낮음 → 높음)  ,   Y축: 인정도 (낮음 → 높음)</span>

### s21-2  (p)
Q2, 전략적 업무

### s21-3  (p)
덜 좋아하지만 인정받는 업무

### s21-4  (p)
이벤트 기획(25명 이하), CS

### s21-5  (p)
→ <code>/analyze-slack</code>, <code>/view-slack-archive</code>: 구조를 대신 만들기

### s21-6  (p)
Q1, 주요 강점 ★

### s21-7  (p)
좋아하고 인정도 받는 업무

### s21-8  (p)
이벤트 기획, 운영, 진행(100명), 파트너 섭외, 팀 기획, 웹사이트 제작

### s21-9  (p)
→ <code>/generate-handout</code>, <code>/manage-attendance</code>, <code>/sync-products</code>: 반복 위임, 판단 집중

### s21-10  (p)
Q3, 축소 고려

### s21-11  (p)
덜 좋아하고 덜 인정받는 업무

### s21-12  (p)
SNS, 슬랙 운영, 영상, 매거진, TF

### s21-13  (p)
→ <code>/schedule-notices</code>, <code>/run-content-ops</code>, <code>/generate-letter</code>: 자동화 or 통합, 위임

### s21-14  (p)
Q4, 숨은 강점

### s21-15  (p)
좋아하지만 덜 인정받는 업무

### s21-16  (p)
중간 서베이, 상세페이지 제작

### s21-17  (p)
→ <code>/ga-report</code>, <code>/evaluate-notes</code>: 성과를 데이터로 가시화

### s21-18  (p)
<span style="color:var(--accent3);font-weight:600;">Q1은 A(Amplify)</span>, <span style="color:var(--accent2);font-weight:600;">Q2는 S/T</span>, <span style="color:var(--accent5);font-weight:600;">Q3는 R</span>, <span style="color:var(--accent4);font-weight:600;">Q4는 T</span>
<span class="sub">: STAR와 같은 축 위에서 사분면이 대응됩니다.</span>


## slide 22 · BCG 매트릭스: HFK 운영에 적용하면
### s22-0  (h2)
BCG 매트릭스: HFK 운영에 적용하면

### s22-1  (p)
같은 축 맥락으로, HFK 운영 영역을 점유율(현재 강점)과 성장률(미래 가치)로 매핑. <span class="dim" style="font-size:0.88em;">X축: 점유율 (낮음 → 높음)  ,   Y축: 성장률 (낮음 → 높음)</span>

### s22-2  (p)
Question Mark, 물음표

### s22-3  (p)
성장 잠재 있으나 포지션 약함: 투자 결정 필요

### s22-4  (p)
AI 컨퍼런스, Figma MCP 연동, 다중 컴퓨터 환경 동기화

### s22-5  (p)
→ <code>/export-to-figma</code>, <code>/audit-skills</code> <span class="dim">신규</span>: 실험으로 가능성 검증

### s22-6  (p)
Star, 스타 ★

### s22-7  (p)
성장하는 시장에서 강한 포지션: 계속 투자

### s22-8  (p)
AI부사수 팀, 강점차별화 팀, Claude Code 스킬 생태계, 100명 이벤트

### s22-9  (p)
→ <code>/run-season-ops</code>, <code>/update-dashboard</code>: 대표 제품으로 키우기

### s22-10  (p)
Dog, 개

### s22-11  (p)
성장도 포지션도 낮음: 철수, 축소

### s22-12  (p)
SNS 운영, 매거진, 소규모 TF

### s22-13  (p)
→ 자동화로 비용 최소화 or 시즌레터로 통합

### s22-14  (p)
Cash Cow, 캐시카우

### s22-15  (p)
성숙 시장에서 안정 수익: 효율화로 수확

### s22-16  (p)
정규 성장트랙 팀, 세션 핸드아웃, 상품 운영, 시즌레터

### s22-17  (p)
→ <code>/run-product-ops</code>, <code>/generate-letter</code>, <code>/sync-products</code>: 반복을 스킬로 수확

### s22-18  (p)
<span style="color:var(--accent3);font-weight:600;">Star ↔ Q1 주요 강점 ↔ Amplify</span>, <span style="color:var(--accent2);font-weight:600;">Question Mark ↔ Q2 ↔ Start</span>, <span style="color:var(--accent4);font-weight:600;">Cash Cow ↔ Q4 ↔ Recover</span>, <span style="color:var(--accent5);font-weight:600;">Dog ↔ Q3 ↔ Try</span>


## slide 23 · 가볍게 시작: STAR로 내 업무를 뜯어보고, 당장 쓸 스킬 만들기 AP
### s23-0  (h2)
가볍게 시작: STAR로 내 업무를 뜯어보고, 당장 쓸 스킬 만들기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(91,123,94,0.12);color:var(--accent3);vertical-align:middle;white-space:nowrap;">API·MCP 없이</span>

### s23-1  (p)
<span style="color:var(--accent);font-weight:600;">미션:</span> 자료가 없어도 괜찮다. STAR로 내가 하는 일을 세세하게 파악하고, 그중 하나를 당장 직장에서 쓸 스킬로 만든다.

### s23-2  (p)
준비물: 없음. STAR 프레임과 5분이면 됩니다. <span style="color:var(--accent);">STEP 1은 Claude가 질문을 하나씩 던지는 왕복 대화예요. 여러 번 주고받은 뒤 다음 칸으로.</span>

### s23-3  (p)
STEP 1

### s23-4  (h3)
STAR로 내 업무 파악

### s23-5  (p)
STEP 2

### s23-6  (h3)
당장 쓸 결과물 정하기

### s23-7  (p)
STEP 3

### s23-8  (h3)
스킬로 만들기

### s23-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> STAR로 파악한 내 업무가 당장 쓰는 스킬이 됩니다. 남의 사례가 아니라 내 일에서 출발한 첫 스킬.


## slide 24 · 커스텀 스킬
### s24-0  (h2)
커스텀 스킬

### s24-1  (p)
마크다운(.md) 파일 하나로 Claude에게 복잡한 업무 절차를 가르칠 수 있습니다.

### s24-2  (h3)
만드는 법

### s24-3  (li)
<code>.claude/commands</code> 폴더에 <code>.md</code> 파일 생성

### s24-4  (li)
파일 안에 업무 절차를 자연어로 작성

### s24-5  (li)
Claude Code에서 <code style="color:var(--accent);">/파일명</code> 으로 실행

### s24-6  (h3)
잘 만드는 팁

### s24-7  (li)
단계별로 명확하게 절차를 기술

### s24-8  (li)
입출력 형식과 예시를 포함

### s24-9  (li)
MCP 도구명을 명시하면 정확도 향상

### s24-10  (li)
에이전트 스킬로 여러 스킬을 연결 가능

### s24-11  (li)
GitHub에 올려 팀과 공유 가능


## slide 25 · 지금까지 본 것을 바탕으로: 내 워크스페이스 만들기
### s25-0  (h2)
지금까지 본 것을 바탕으로: 내 워크스페이스 만들기

### s25-1  (p)
다양한 케이스를 봤습니다. 앞으로 내 업무에 맞는 환경을 만들어봅시다.

### s25-2  (p)
Step 1

### s25-3  (h3)
반복 업무 목록화

### s25-4  (p)
매주/매달 반복하는 업무를 적어보기. 시간이 많이 드는 것부터 우선순위 결정

### s25-5  (p)
Step 2

### s25-6  (h3)
첫 번째 스킬 만들기

### s25-7  (p)
<code>.claude/commands</code> 에 <code>.md</code> 파일 하나 생성. 절차를 자연어로 작성

### s25-8  (p)
Step 3

### s25-9  (h3)
필요한 서비스 연결

### s25-10  (p)
내가 자주 쓰는 서비스를 MCP로 연결. Claude Code 공식 문서 참고

### s25-11  (p)
Step 4

### s25-12  (h3)
스킬을 조합해 에이전트로

### s25-13  (p)
개별 스킬이 쌓이면 여러 스킬을 묶어 에이전트 스킬로 확장

### s25-14  (p)
<span style="color:var(--accent);font-weight:600;">코딩을 몰라도 됩니다.</span>
<span class="sub"> 업무 절차를 자연어로 적으면 Claude가 이해합니다. 반복되는 업무가 있다면, 그것이 바로 첫 번째 스킬 후보입니다.</span>

### s25-15  (p)
<span style="color:var(--accent);font-weight:600;">가능한 모든 일을 VS Code 환경에서 처리해봅니다.</span>
<span class="sub"> 워크스페이스가 풍성해집니다.</span>


## slide 26 · AI = 기본기 , HFK = 인사이트와 센스
### s26-0  (h2)
AI = 기본기  ,   HFK = 인사이트와 센스

### s26-1  (h3)
AI만 있으면?

### s26-2  (li)
누구나 빠르게 기본기를 갖추게 된다

### s26-3  (li)
평균의 아웃풋이 올라간다

### s26-4  (li)
차별화가 어려워진다

### s26-5  (li)
<span style="color:var(--accent5);font-weight:600;">AI = 평범함의 도구</span>가 될 수도 있다

### s26-6  (h3)
AI + 인사이트/센스가 있으면?

### s26-7  (li)
기본기를 AI로 빠르게 처리

### s26-8  (li)
남는 시간에 인사이트와 센스를 키운다

### s26-9  (li)
업계 지식 + AI 실행력 = 진짜 강점

### s26-10  (li)
HFK는 그 인사이트, 센스를 함께 키운다

### s26-11  (p)
<span style="color:var(--accent);font-weight:600;">기본기를 AI로 빠르게 마스터하고, 비즈니스 인사이트와 센스, 즉 자신만의 암묵지를 기르는 게 필요합니다.</span>


## slide 27 · 다시 한번, 세 가지
### s27-0  (h2)
다시 한번, 세 가지

### s27-1  (h3)
다양한 케이스 보기

### s27-2  (p)
많이 볼수록 센스가 생깁니다.<br/>Use Case를 계속 발견해가세요.

### s27-3  (h3)
하나를 제대로 쓰기

### s27-4  (p)
Claude Code 하나를 야무지게<br/>잘 쓰는 것이 더 강력합니다.

### s27-5  (h3)
기록하기

### s27-6  (p)
업무 기록과 스킬을 쌓아가면<br/>그것이 나만의 워크스페이스가 됩니다.

### s27-7  (p)
<span style="color:var(--accent);font-weight:600;">AI는 내 일을 줄이기 위해서 쓰는 것이 아닙니다. 내 일을 자세히 남기기 위해서 쓰는 것입니다. AI로 초안의 완성도를 높이고, 결과물을 고도화하는 데 사용하세요.</span>
