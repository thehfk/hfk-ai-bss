# presentation-ai-workshop-for-member-mobile.html
<!-- 이 파일의 각 블록 텍스트를 고치고 `python scripts/deck_content.py inject presentation-ai-workshop-for-member-mobile.html` 를 실행하면 발표 HTML에 반영됩니다. 슬롯 헤더(### sN-M)는 위치 키이니 지우지 마세요. -->

## slide 0 · Claude Code 활용 가이드
### s0-0  (h1)
Claude Code<br/>활용 가이드

### s0-1  (p)
커스텀 스킬로 만드는 나만의 AI 업무 자동화

### s0-2  (p)
실제 운영 사례와 함께 보는 100개 스킬

### s0-3  (p)
AI Workshop for Member, Seulki.log


## slide 1 · 오늘 다룰 내용 소개
### s1-0  (h2)
오늘 다룰 내용 소개

### s1-1  (p)
케이스 스터디로 시작해서, 도구를 익히고, 직접 스킬을 만들어 본 뒤, 실전 사례와 나만의 활용법까지 보는 시간입니다.

### s1-2  (h3)
Part 1: 왜, 그리고 무엇을

### s1-3  (li)
센스의 재발견: 많이 볼수록 센스가 생긴다

### s1-4  (li)
AI를 쓸수록 나는? 암묵지가 차별화를 만든다

### s1-5  (li)
이 시간이 끝나고 기억할 세 가지

### s1-6  (h3)
Part 2: Claude Code 이해하기

### s1-7  (li)
Claude Code란? / ChatGPT와 비교

### s1-8  (li)
기본 개념: Skill, Agent, API, MCP

### s1-9  (li)
더 알아둘 개념: RAG, 하니스, 아티팩트, 카오스 엔지니어링

### s1-10  (li)
어디서 쓸 수 있나? / 설치 / VS Code 시작

### s1-11  (h3)
Part 3: 직접 만들어 보기

### s1-12  (li)
스킬 워크숍: 크롤링·유튜브·캘린더·카드뉴스

### s1-13  (li)
핸즈온: 하루를 기록하는 /run-daily-note 스킬

### s1-14  (li)
보안 리스크 관리 / 토큰 절약

### s1-15  (h3)
Part 4: 실전 스킬 100개

### s1-16  (li)
HFK 커뮤니티 운영 자동화 사례

### s1-17  (li)
상품, 콘텐츠, 일정, 이미지, 에이전트

### s1-18  (li)
시즌 오픈 자동화 워크플로우

### s1-19  (li)
MCP 서버 연동

### s1-20  (h3)
Part 5: 나만의 활용법 + 마무리

### s1-21  (li)
두번째 지능 / STAR · BCG 프레임워크

### s1-22  (li)
커스텀 스킬 / 내 워크스페이스 만들기

### s1-23  (li)
AI = 기본기, 인사이트와 센스를 기르는 것


## slide 2 · AI, 함께 배우고 만들어 온 이야기
### s2-0  (h2)
AI, 함께 배우고 만들어 온 이야기

### s2-1  (p)
2023

### s2-2  (h3)
AI 스터디 기획

### s2-3  (p)
ChatGPT 등장 이후 AI를 실무에 어떻게 적용할지 함께 탐색

### s2-4  (p)
2023~현재

### s2-5  (h3)
AI부사수 팀 운영

### s2-6  (p)
시즌마다 AI 활용 팀 운영, Work Breakdown으로 실무 적용

### s2-7  (p)
2025

### s2-8  (h3)
AI 컨퍼런스 개최

### s2-9  (p)
&lt;AI에 대체되지 않는 사람들&gt; 비개발자 연사 3명의 케이스 스터디

### s2-10  (p)
2025~

### s2-11  (h3)
Claude Code 도입

### s2-12  (p)
커뮤니티 운영 업무를 100개 커스텀 스킬로 자동화

### s2-13  (p)
<span class="sub">'AI를 과소평가하지도, 과대평가하지도 말 것. 자신만의 베이스캠프를 정해 꾸준히 활용하는 것이 중요하다.'</span>


## slide 3 · 센스의 재발견: 미즈노 마나부
### s3-0  (h2)
센스의 재발견: 미즈노 마나부

### s3-1  (p)
'센스란 재능이 아니다. 좋은 것을 많이 보고, 많이 알수록 길러지는 것이다.'

### s3-2  (p)
: 미즈노 마나부 『センスは知識からはじまる』

### s3-3  (p)
'평균이 어디에 있는지 파악하는 것이 센스의 시작이다. 그러려면 많이 봐야 한다.'

### s3-4  (p)
: 미즈노 마나부

### s3-5  (h3)
AI 활용에도 같은 원칙

### s3-6  (li)
좋은 Use Case를 많이 보면 → AI 활용 센스가 생긴다

### s3-7  (li)
내 업무에 어디까지 쓸 수 있는지 → 많이 볼수록 발견한다

### s3-8  (li)
타인의 사례에서 '나라면 어떻게?'를 고민하는 것이 성장

### s3-9  (h3)
오늘의 목표

### s3-10  (p)
HFK Claude Code 100개 스킬 사례를 통해 '내가 할 수 있는 것'의 범위를 넓혀가는 시간


## slide 4 · AI를 쓸수록, 나는 도태되는 걸까?
### s4-0  (h2)
AI를 쓸수록, 나는 도태되는 걸까?

### s4-1  (p)
최근 한 멤버와 운영자가 나눈 대화입니다. AI를 쓸수록 내 실력은 어떻게 되는지에 대한 이야기였습니다.

### s4-2  (p)
대기업 20년차 마케터 멤버

### s4-3  (p)
요즘 에이전틱으로 24시간 일한다는 게, 정말 '나'의 능력이 좋아진 걸까요? 그냥 '에이전트'가 좋아진 거 아닐까. 나는 오히려 도태되는 거 아닐까 싶어요.

### s4-4  (p)
HFK

### s4-5  (p)
스킬을 고도화하는 건 내 업무를 아주 구체적으로 발견하고 다듬는 일이에요. 인풋을 잘 넣어야 아웃풋인 에이전트가 잘 나오니까, 인풋 넣는 일을 게을리할 수가 없어요. 오히려 머리가 단단해지는 기분이에요.

### s4-6  (p)
좋은 문장을 쓰려고 안 보던 소설까지 봐요. 그걸 에이전트로 만들려면 결국 글로 써내야 하고, 그 과정에서 지식이 내 것이 되더라고요. 클로드 코드가 저를 멱살 잡고 성장시키는 중이에요. 결국 암묵지가 차별화를 만듭니다.

### s4-7  (p)
<span style="color:var(--accent);font-weight:600;">좋은 인풋, 곧 내 암묵지를 넣어야 좋은 아웃풋이 나옵니다.</span>
<span class="sub"> 스킬을 다듬는 과정이 내 일을 다시 들여다보는 공부가 됩니다.</span>


## slide 5 · 이 시간이 끝나고 기억할 세 가지
### s5-0  (h2)
이 시간이 끝나고 기억할 세 가지

### s5-1  (h3)
다양한 케이스 보기

### s5-2  (p)
AI가 어디까지 하는지<br/>최대한 많은 사례를 보자

### s5-3  (h3)
하나를 제대로 쓰기

### s5-4  (p)
여러 도구를 얕게 쓰는 것보다<br/>하나를 깊이 쓰는 것이 낫다

### s5-5  (h3)
기록하기

### s5-6  (p)
결과물을 쌓아가는 것이 자산

### s5-7  (p)
<span style="color:var(--accent);font-weight:600;">Claude Code는 도구입니다.</span>
<span class="sub"> 많이 보고, 깊이 쓰고, 꾸준히 기록해야 실력이 됩니다.</span>


## slide 6 · Claude Code를 잘 쓰려면, 세 가지가 함께 있어야 합니다
### s6-0  (h2)
Claude Code를 잘 쓰려면, 세 가지가 함께 있어야 합니다

### s6-1  (p)
도구가 손에 있다고 결과가 자동으로 나오지 않습니다. 다음 세 가지가 같이 있어야 도구가 일이 됩니다.

### s6-2  (p)
01

### s6-3  (h3)
데이터 기반의 숙원 사업

### s6-4  (p)
'이거 좀 자동으로 처리됐으면' 하고 오래 미뤄둔 일이 머릿속에 있어야 합니다. 어떤 데이터가 있는지 알고, 어떤 결과를 보고 싶은지 그림이 잡혀 있는 일.

### s6-5  (p)
<span style="font-weight:600;">예)</span> 시즌 운영 대시보드, 멤버 마스터 테이블

### s6-6  (p)
02

### s6-7  (h3)
기술에 대한 호기심

### s6-8  (p)
'이게 뭐길래?'부터 시작하는 태도가 있어야 합니다. 새 모델, 새 기능이 나오면 일단 켜보고, 완전히 이해하지 못해도 손을 대보는 마음.

### s6-9  (p)
회사에서 Claude를 직접 쓰지 않더라도, 바이브 코딩이 무엇이고 어떤 문제를 어떻게 풀어주는지 개념은 알아둬야 합니다.

### s6-10  (p)
<span style="font-weight:600;">예)</span> Opus 4.8, Figma MCP, Skills

### s6-11  (p)
03

### s6-12  (h3)
업무에 대한 욕심

### s6-13  (p)
'이 정도면 됐다'가 아니라 '이번엔 이걸 해결하자'의 욕심이 있어야 합니다. 지표를 보고 다음 일을 잡는 자세.

### s6-14  (p)
<span style="font-weight:600;">예)</span> 재등록율 72% 목표, 상품 완성도 지표

### s6-15  (p)
<span class="sub">숙원 사업이 있어야 시작하고, 호기심이 있어야 새 도구를 켜고, 욕심이 있어야 끝까지 다듬습니다.</span>


## slide 7 · Claude Code란?
### s7-0  (h2)
Claude Code란?

### s7-1  (p)
터미널에서 동작하는 AI 코딩 에이전트

### s7-2  (p)
자연어로 지시하면 Claude가 직접 파일을 다루며 작업을 수행합니다.

### s7-3  (p)
주요 특징

### s7-4  (li)
파일 읽기, 수정, 생성을 직접 수행

### s7-5  (li)
터미널 명령어 실행

### s7-6  (li)
MCP 서버로 외부 API 연동

### s7-7  (li)
커스텀 스킬로 반복 업무 자동화

### s7-8  (li)
VS Code 확장 프로그램 지원


## slide 8 · Claude vs Claude Code
### s8-0  (h2)
Claude vs Claude Code

### s8-1  (p)
같은 Claude라도 대화창에서 쓰는 것과 코드를 직접 실행하는 것은 결과가 다릅니다.

### s8-2  (p)
Claude (대화형 AI)

### s8-3  (li)
생각하고 답을 만드는 엔진

### s8-4  (li)
파일 업로드 → 요약/분석 결과를 텍스트로 제공

### s8-5  (li)
데이터가 크면 샘플링하거나 잘림 발생

### s8-6  (li)
중간 과정을 검증하기 어려움 (블랙박스)

### s8-7  (li)
결과를 다시 수작업으로 옮겨야 함

### s8-8  (p)
Claude Code (코딩 에이전트)

### s8-9  (li)
Claude라는 엔진에 파일을 읽고 코드를 실행하는 손발을 달아준 도구

### s8-10  (li)
전체 데이터를 빠짐없이 처리 (샘플링 없음)

### s8-11  (li)
코드가 남아 검증/재현 가능 (투명한 과정)

### s8-12  (li)
결과를 파일 저장, API로 바로 반영

### s8-13  (li)
스킬로 저장해 다음에 한 번에 재실행

### s8-14  (p)
<span style="color:var(--accent);font-weight:600;">정확히는</span>: <span class="sub">같은 Claude 모델을 '채팅 인터페이스'로 쓰느냐, '코딩 에이전트(Claude Code)'로 쓰느냐의 차이입니다.</span>


## slide 9 · AI는 왜 틀릴까
### s9-0  (h2)
AI는 왜 틀릴까

### s9-1  (p)
둘 다 '다음에 올 말을 확률로 예측해' 글을 씁니다. 그래서 그럴듯하지만 틀린 답(할루시네이션)이 나옵니다. 뿌리는 같고, <span style="color:var(--accent);font-weight:600;">틀렸을 때 드러나는 방식</span>이 다릅니다.

### s9-2  (h3)
Claude (채팅)의 실수

### s9-3  (li)
무엇을 어떤 과정에서 틀렸는지 알 수 없다

### s9-4  (li)
숫자와 사실을 그럴듯하게 지어낸다

### s9-5  (li)
검증할 수단이 없어 교정 기회가 적다

### s9-6  (li)
위험: 그럴듯한 오답을 사실로 믿게 된다

### s9-7  (h3)
Claude Code (실행)의 실수

### s9-8  (li)
틀리면 에러와 실패 기록이 남는다

### s9-9  (li)
코딩 시행착오를 반복하며 코드를 고친다

### s9-10  (li)
위험: 통과는 하는데 틀린 미묘한 버그가 있을 수 있다

### s9-11  (p)
<span style="color:var(--accent);font-weight:600;">한두 번 물어가며 정답에 가까워지는 건</span> <span class="sub">시간 끌기가 아니라, 실행해보고 정보를 모아 추측을 교정하는 과정입니다. 검증 수단(테스트·에러·실제 파일)을 줄수록 빨라집니다.</span>


## slide 10 · 같은 데이터 분석을 맡기면: 두 사람 비유
### s10-0  (h2)
같은 데이터 분석을 맡기면: 두 사람 비유

### s10-1  (p)
같은 매출 표에 '지난달 대비 증감률 뽑아줘'라고 시켜봅니다. 둘은 <span style="color:var(--accent);font-weight:600;">서로 다른 종류의 실수</span>를 합니다.

### s10-2  (p)
Claude (채팅) = 암산 천재, 검산은 안 함

### s10-3  (li)
큰 표를 끝까지 안 보고 머릿속으로 어림한다

### s10-4  (li)
'약 12% 증가한 것 같아요' (실제로는 9%)

### s10-5  (li)
틀려도 자신 있게 말해 티가 안 난다

### s10-6  (p)
실수 유형: 맞는 질문에 틀린 답

### s10-7  (p)
Claude Code = 검산은 완벽, 가끔 엉뚱한 걸 계산

### s10-8  (li)
코드로 정확히 9.3% 산출 (다시 돌려도 같은 값)

### s10-9  (li)
단, '지난달'에 취소 주문을 넣었다면?

### s10-10  (li)
그 잘못된 전제로 정확한 9.3%를 낸다

### s10-11  (p)
실수 유형: 틀린 질문에 맞는 답

### s10-12  (p)
<span style="color:var(--accent);font-weight:600;">그래서 사람이 챙길 것이 다릅니다</span>: <span class="sub">채팅에는 검산(숫자가 맞는지)을, Claude Code에는 전제 확인(무엇을 계산할지)을 짚어줘야 합니다.</span>


## slide 11 · Claude Code를 이해하는 데 필요한 개념들
### s11-0  (h2)
Claude Code를 이해하는 데 필요한 개념들

### s11-1  (p)
Claude Code를 이해하려면 이 네 가지만 알면 됩니다. <span style="color:var(--accent);font-weight:600;">카페 운영</span>에 비유해봅시다.

### s11-2  (p)
Skill

### s11-3  (h3)
레시피

### s11-4  (p)
'아메리카노 만드는 법'처럼<br/>업무 절차를 적어둔 <span style="font-weight:600;">마크다운 파일</span>

### s11-5  (p)
<span style="color:var(--accent);font-weight:600;">실제 예)</span> /sync-products<br/>→ 노트 읽기 → HTML 변환 → 아임웹 반영

### s11-6  (p)
Agent

### s11-7  (h3)
매니저

### s11-8  (p)
레시피 여러 개를 조합해서<br/><span style="font-weight:600;">알바생들에게 순서대로 시키는 사람</span>

### s11-9  (p)
<span style="color:var(--accent2);font-weight:600;">실제 예)</span> /run-season-ops<br/>→ 일정 + 동기화 + 레터 + 슬랙 한 번에

### s11-10  (p)
API

### s11-11  (h3)
주문 창구

### s11-12  (p)
외부 서비스와 데이터를 주고받는<br/><span style="font-weight:600;">정해진 규격의 통로</span>

### s11-13  (p)
<span style="color:var(--accent3);font-weight:600;">실제 예)</span> 아임웹 API<br/>→ 상품 조회, 수정, 등록을 코드로 처리

### s11-14  (p)
MCP

### s11-15  (h3)
멀티탭

### s11-16  (p)
API라는 플러그를 Claude Code에<br/><span style="font-weight:600;">꽂을 수 있게 해주는 어댑터</span>

### s11-17  (p)
<span style="color:var(--accent4);font-weight:600;">실제 예)</span> Slack MCP 서버<br/>→ Claude가 직접 메시지 발송, 채널 생성


## slide 12 · 요즘 더 알아두면 좋은 개념
### s12-0  (h2)
요즘 더 알아두면 좋은 개념

### s12-1  (p)
스킬과 에이전트에 더해, 이 세 가지를 알아두면 AI 도구를 더 깊이 이해할 수 있습니다.

### s12-2  (p)
RAG

### s12-3  (h3)
검색 증강

### s12-4  (p)
답하기 전에 필요한 자료를 먼저 찾아 읽는 방식. 내 문서와 기록을 근거로 답하게 만듭니다.

### s12-5  (p)
비유) 매뉴얼을 펴놓고 답하기

### s12-6  (p)
Harness

### s12-7  (h3)
실행 골격

### s12-8  (p)
일일이 시키지 않아도 런타임이 훅, 설정, 스킬을 자동 실행하는 골격. Claude Code 자체가 하나의 하니스입니다.

### s12-9  (p)
비유) 자동으로 도는 주방 동선

### s12-10  (p)
Artifact

### s12-11  (h3)
결과물

### s12-12  (p)
Claude가 만들어내는 문서, 코드, 대시보드 같은 결과물. 따로 보관해두고 다음 작업의 재료로 씁니다.

### s12-13  (p)
비유) 만들어 쌓아두는 완성품


## slide 13 · 지금 HFK는 이렇게 쓰고 있습니다
### s13-0  (h2)
지금 HFK는 이렇게 쓰고 있습니다

### s13-1  (p)
셋 다 모델이 아니라 <span style="color:var(--accent);font-weight:600;">AI를 둘러싼 환경</span>을 짜는 이야기입니다.

### s13-2  (p)
RAG

### s13-3  (h3)
답하기 전에 내 자료부터

### s13-4  (p)
Claude가 답하기 전에 메모리와 옵시디언 노트, 후기 톤을 먼저 읽습니다. 기억이 아니라 내가 모은 자료에서 끌어옵니다.

### s13-5  (p)
<span style="color:var(--accent3);font-weight:600;">지금)</span> MEMORY.md, note/리뷰 톤, 녹취 먼저 읽기

### s13-6  (p)
카오스 엔지니어링

### s13-7  (h3)
깨질 때를 미리 설계

### s13-8  (p)
잘 돌 때를 믿지 않고, 끊기거나 두 번 실행되는 상황을 미리 막아둡니다. 사고를 한 번 겪으면 그 자리에 방어막을 답니다.

### s13-9  (p)
<span style="color:var(--accent5);font-weight:600;">지금)</span> 헬스체크 알림, 발송 로그, 멱등 가드

### s13-10  (p)
하네스

### s13-11  (h3)
AI에게 도구·규칙을 깔아주기

### s13-12  (p)
같은 AI라도 어떤 도구와 규칙을 주고, 얼마나 자주 피드백과 메모리를 남기느냐로 결과가 갈립니다. 이 워크스페이스 전체가 하나의 하네스입니다.

### s13-13  (p)
<span style="color:var(--accent);font-weight:600;">지금)</span> 스킬 100개, CLAUDE.md 규칙, 메모리

### s13-14  (p)
<span class="sub">개념으로 배워서 한 게 아니라, 운영하면서 필요해서 스스로 만들어 온 것들입니다.</span>


## slide 14 · Claude Code, 어디서 쓸 수 있나?
### s14-0  (h2)
Claude Code, 어디서 쓸 수 있나?

### s14-1  (h3)
가장 강력한 방식

### s14-2  (p)
스킬, 에이전트, 자동화 모두 가능

### s14-3  (p)
추천: 자동화가 많은 분

### s14-4  (h3)
에디터 안에서 바로

### s14-5  (p)
코드 변경 사항을 시각적으로 비교

### s14-6  (p)
추천: VS Code 사용자

### s14-7  (h3)
설치 없이 브라우저에서

### s14-8  (p)
클라우드 실행, 폰에서도 확인 가능

### s14-9  (p)
추천: 빠르게 써보고 싶은 분

### s14-10  (h3)
일반 앱처럼

### s14-11  (p)
터미널 없이 GUI로 사용

### s14-12  (p)
추천: 터미널이 부담스러운 분

### s14-13  (p)
<span style="color:var(--accent);font-weight:600;">Cowork 모드</span>: <span class="sub">한 세션을 여러 사람이 동시에 보며 협업. 화면 공유 없이 같은 작업을 실시간으로 함께 볼 수 있습니다.</span>

### s14-14  (p)
<a href="https://github.com/skaug12/hfk-presentations/blob/main/claude-code-platforms.md" style="color:var(--accent);text-decoration:underline;font-weight:600;" target="_blank">플랫폼별 권한, 기능 상세 비교 →</a>


## slide 15 · 스킬 워크숍: 직접 만들어 봅니다
### s15-0  (h2)
스킬 워크숍: 직접 만들어 봅니다

### s15-1  (p)
내 반복 업무를 스킬로 만들어 보는 시간입니다. 프롬프트는 이렇게 씁니다: <span style="color:var(--accent);font-weight:600;">① 내 상황을 최대한 구체적으로 → ② 원하는 결과물 → ③ '이 일을 다시 쓰게 스킬로 만들어줘'</span>

### s15-2  (p)
01

### s15-3  (h3)
웹 크롤링으로 기록 수집

### s15-4  (p)
Claude Code로 웹을 크롤링해 흩어진 기록을 한곳에 모읍니다.

### s15-5  (p)
02

### s15-6  (h3)
유튜브 브리핑 만들기

### s15-7  (p)
YouTube를 연결해 재생목록에 영상을 넣으면, 그 내용을 정리한 브리핑이 자동으로 만들어집니다.

### s15-8  (p)
03

### s15-9  (h3)
액션 플랜과 캘린더

### s15-10  (p)
쌓인 기록을 정리해 액션 플랜을 만들고, 그대로 캘린더에 일정으로 적습니다.

### s15-11  (p)
04

### s15-12  (h3)
인스타 카드뉴스

### s15-13  (p)
인스타그램 카드뉴스 콘텐츠를 만들고 포스팅까지 이어갑니다.


## slide 16 · 웹 크롤링으로 기록 모으기 API·MCP 없이
### s16-0  (h2)
웹 크롤링으로 기록 모으기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(91,123,94,0.12);color:var(--accent3);vertical-align:middle;white-space:nowrap;">API·MCP 없이</span>

### s16-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 흩어진 글과 자료를 Claude Code가 웹에서 가져와 한 폴더에 정리합니다.

### s16-2  (p)
준비물: 모으고 싶은 사이트 주소, 저장할 폴더 이름. 따라 입력만 하면 됩니다.

### s16-3  (p)
STEP 1

### s16-4  (h3)
목록부터 만들기

### s16-5  (p)
STEP 2

### s16-6  (h3)
본문 저장하기

### s16-7  (p)
STEP 3

### s16-8  (h3)
깔끔하게 정리

### s16-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 크롤링 폴더에 글마다 마크다운 파일과 목록 표가 생깁니다. <span class="dim">공개된 페이지만 가져오고, 사이트의 robots 규칙을 지키세요.</span>

### s16-10  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: Claude Code의 웹 가져오기 기능과 Playwright(브라우저 자동화)로 페이지를 열어, '본문만 추려서 마크다운으로 저장해줘' 프롬프트를 더해 만듭니다.


## slide 17 · 유튜브로 브리핑 노트 만들기 API 연결
### s17-0  (h2)
유튜브로 브리핑 노트 만들기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(61,90,128,0.12);color:var(--accent2);vertical-align:middle;white-space:nowrap;">API 연결</span>

### s17-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 재생목록에 영상을 넣으면, 그 영상 내용을 요약한 브리핑 노트가 자동으로 만들어집니다.

### s17-2  (p)
준비물: 유튜브 재생목록 하나, /analyze-youtube 스킬

### s17-3  (p)
STEP 1

### s17-4  (h3)
영상 담기

### s17-5  (p)
브리핑 받고 싶은 영상을 'AI브리핑' 재생목록에 추가합니다.

### s17-6  (p)
STEP 2

### s17-7  (h3)
브리핑 요청

### s17-8  (p)
STEP 3

### s17-9  (h3)
노트로 저장

### s17-10  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 영상마다 요점, 인용, 적용 아이디어가 담긴 브리핑 노트가 쌓입니다. <span class="dim">자막이 없는 영상은 음성에서 자동으로 받아씁니다.</span>

### s17-11  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: 유튜브 자막을 가져오는 기능에 '요점만 정리해줘' 프롬프트를 묶은 /analyze-youtube 스킬입니다.


## slide 18 · 기록을 액션 플랜으로, 캘린더까지 MCP 연결
### s18-0  (h2)
기록을 액션 플랜으로, 캘린더까지 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(123,107,138,0.12);color:var(--accent4);vertical-align:middle;white-space:nowrap;">MCP 연결</span>

### s18-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 쌓인 메모를 정리해 할 일 목록을 만들고, 그대로 캘린더에 일정으로 넣습니다.

### s18-2  (p)
준비물: 정리할 노트 폴더, Google Calendar 연결(MCP)

### s18-3  (p)
STEP 1

### s18-4  (h3)
할 일만 뽑기

### s18-5  (p)
STEP 2

### s18-6  (h3)
살 붙이기

### s18-7  (p)
STEP 3

### s18-8  (h3)
캘린더 등록

### s18-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 액션 플랜 문서가 생기고, 마감일 일정이 캘린더에 올라갑니다. <span class="dim">먼저 미리보기만 요청해 확인한 뒤 등록하세요.</span>

### s18-10  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: 노트를 읽는 파일 기능과 Google Calendar 연결(MCP)에 '할 일만 뽑아 일정으로 넣어줘' 프롬프트를 더해 만듭니다.


## slide 19 · 인스타그램 카드뉴스 만들어 올리기 API 연결
### s19-0  (h2)
인스타그램 카드뉴스 만들어 올리기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(61,90,128,0.12);color:var(--accent2);vertical-align:middle;white-space:nowrap;">API 연결</span>

### s19-1  (p)
<span style="color:var(--accent);font-weight:600;">목표:</span> 글 하나로 인스타그램 카드뉴스를 만들고 예약 발행까지 합니다.

### s19-2  (p)
준비물: 소재가 될 글이나 주제, /post-to-buffer 스킬(Buffer 연결)

### s19-3  (p)
STEP 1

### s19-4  (h3)
장면 쪼개기

### s19-5  (p)
STEP 2

### s19-6  (h3)
이미지로

### s19-7  (p)
STEP 3

### s19-8  (h3)
예약 발행

### s19-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 카드 이미지 세트와 예약된 인스타 포스팅이 만들어집니다. <span class="dim">첫 장 후킹 문구가 가장 중요합니다. 좌상단부터 읽히게 두세요.</span>

### s19-10  (p)
<span style="color:var(--accent);font-weight:600;">스킬 기반</span>: Playwright로 카드 HTML을 1080x1080 이미지로 렌더링하고, Buffer 예약 발행 API로 올리는 /post-to-buffer 스킬입니다.


## slide 20 · 직접 해보기: 하루를 자동 기록하는 /run-daily-note 스킬 만
### s20-0  (h2)
직접 해보기: 하루를 자동 기록하는 /run-daily-note 스킬 만들기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(91,123,94,0.12);color:var(--accent3);vertical-align:middle;white-space:nowrap;">API·MCP 없이</span>

### s20-1  (p)
<span style="color:var(--accent);font-weight:600;">미션:</span> 오늘 한 작업을, 어떤 프롬프트로 무슨 결과가 나왔는지까지 데일리 노트 한 장에 그대로 남기는 스킬을 만드세요.

### s20-2  (p)
준비물: Claude Code가 도는 작업 폴더. 프롬프트는 '상황 구체화 → 결과물 형식 → 스킬화' 순서로. <span style="color:var(--accent);">폼이 아니라 대화예요: 한 칸 친 뒤 Claude 답을 보고 다음 칸으로 (앞 내용은 기억하니 다시 안 써도 됨).</span>

### s20-3  (p)
STEP 1

### s20-4  (h3)
작업 내역 자동 수집

### s20-5  (p)
STEP 2

### s20-6  (h3)
프롬프트·답변·결정·결과 남기기

### s20-7  (p)
STEP 3

### s20-8  (h3)
스킬로 만들기

### s20-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> 부를 때마다 그날 작업이 <span style="font-weight:600;">① 내 프롬프트 → ② Claude 답변·처리 → ③ 의사결정 → ④ 결과</span> 순으로 그대로 남습니다. 나중에 펼치면 그날 작업이 재현됩니다.


## slide 21 · Gen AI 보안 리스크 관리
### s21-0  (h2)
Gen AI 보안 리스크 관리

### s21-1  (p)
AI를 업무에 활용할 때 반드시 알아야 할 보안 원칙입니다.

### s21-2  (p)
공유해도 되는 것

### s21-3  (li)
코드, 개발 관련 질문

### s21-4  (li)
일반적인 업무 내용, 기획 아이디어

### s21-5  (li)
마케팅 카피, 콘텐츠 초안

### s21-6  (p)
피해야 하는 것

### s21-7  (li)
비밀번호, API 키, 인증 토큰

### s21-8  (li)
주민등록번호, 계좌번호, 카드번호

### s21-9  (li)
고객 개인정보 (이름+연락처+주소 조합)

### s21-10  (li)
미발표 일정, 공개 전 내부 전략

### s21-11  (p)
1. 데이터 격리

### s21-12  (p)
민감 정보는 .env 파일로 분리, .gitignore로 업로드 차단

### s21-13  (p)
2. 대화는 휘발성

### s21-14  (p)
대화는 나와 Claude만 볼 수 있고, 끝나면 Claude도 잊어버림

### s21-15  (p)
3. 로컬 실행

### s21-16  (p)
Claude Code는 내 컴퓨터에서 실행. 파일 내용은 처리를 위해 Anthropic 서버로 전송되지만 저장되지 않음


## slide 22 · 토큰, 아껴 쓰는 법
### s22-0  (h2)
토큰, 아껴 쓰는 법

### s22-1  (p)
토큰 = Claude가 읽고 쓰는 글자 단위. 매 질문마다 지금까지의 대화 전체를 다시 읽습니다. 대화가 길어질수록 한 번 질문에 쓰는 토큰이 눈덩이처럼 불어납니다.

### s22-2  (h3)
1. 낡은 세션 정리: /compact

### s22-3  (p)
<code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/compact</code> = 지금까지의 대화 내용을 요약본으로 압축하는 명령어.

### s22-4  (li)
대화가 길어졌을 때 입력하면 과거 내용을 짧게 줄여줌

### s22-5  (li)
주제가 바뀔 때마다 한 번씩 실행하면 효과적

### s22-6  (li)
아예 새 대화를 시작하는 것도 방법

### s22-7  (p)
한 세션에서 모든 걸 하려 하지 마세요. 주제별로 나누는 게 낫습니다.

### s22-8  (h3)
2. Claude가 읽을 범위 좁히기

### s22-9  (p)
Claude는 '어디를 봐야 하는지' 모르면 폴더 전체를 탐색합니다. 파일 경로와 범위를 명확히 지정하세요.

### s22-10  (li)
<span style="color:var(--accent5);">✗</span> '이 프로젝트 개선해줘' → 수십 개 파일 탐색

### s22-11  (li)
<span style="color:var(--accent3);">✓</span> 'src/auth.ts 파일의 login 함수 수정해줘' → 파일 1-2개만 읽음

### s22-12  (p)
경로가 명확할수록 토큰이 줄고, 결과도 정확해집니다.

### s22-13  (h3)
3. 기본 모델 바꾸기

### s22-14  (p)
기본값은 Sonnet. 복잡한 작업에만 Opus로 전환해서 사용.

### s22-15  (p)
<code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/model sonnet</code> 으로 전환

### s22-16  (h3)
4. 작업 전: /status

### s22-17  (p)
큰 작업을 시작하기 전에 <code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/status</code>로 현재 세션 정보 확인. 대화가 길어졌다면 /compact 또는 새 세션.

### s22-18  (h3)
5. 작업 중: /cost

### s22-19  (p)
<code style="background:rgba(0,0,0,0.06);padding:2px 6px;border-radius:3px;">/cost</code>로 현재 세션에서 사용한 비용 확인. Pro/Max 구독이면 API 비용 없이 사용 가능.


## slide 23 · 내가 잘 쓰는 서비스
### s23-0  (h2)
내가 잘 쓰는 서비스

### s23-1  (p)
Claude Code

### s23-2  (h3)
AI 부사수 역할

### s23-3  (li)
자연어 명령으로 파일 관리 및 작업 실행

### s23-4  (li)
100개 커스텀 스킬로 반복 업무 자동화

### s23-5  (li)
7개 MCP 서버로 외부 서비스 연결

### s23-6  (li)
VS Code 통합으로 코드 작업도 함께

### s23-7  (p)
Obsidian

### s23-8  (h3)
지식 베이스 &amp; 작업 파일 관리

### s23-9  (li)
로컬 마크다운 기반 노트앱

### s23-10  (li)
모든 업무 문서와 아이디어를 여기서 관리

### s23-11  (li)
Claude Code가 직접 파일을 읽고 수정

### s23-12  (p)
함께 쓰는 서비스

### s23-13  (p)
<a href="https://github.com" style="color:inherit;text-decoration:underline;" target="_blank">GitHub</a>

### s23-14  (p)
스킬과 코드를 버전 관리하고 팀과 공유. GitHub Pages로 무료 배포

### s23-15  (p)
<a href="https://vercel.com" style="color:inherit;text-decoration:underline;" target="_blank">Vercel</a>

### s23-16  (p)
만든 웹앱과 대시보드를 빠르게 배포

### s23-17  (p)
<a href="https://www.anthropic.com/learn" style="color:inherit;text-decoration:underline;" target="_blank">Anthropic Academy</a>

### s23-18  (p)
Claude 활용법을 배우는 공식 학습 자료

### s23-19  (p)
<a href="https://crontab.guru" style="color:inherit;text-decoration:underline;" target="_blank">cron</a>

### s23-20  (p)
정해둔 시각에 스킬을 자동으로 실행

### s23-21  (p)
<a href="https://n8n.io" style="color:inherit;text-decoration:underline;" target="_blank">n8n</a>

### s23-22  (p)
노코드로 서비스를 연결하는 자동화 도구

### s23-23  (p)
<a href="https://www.make.com" style="color:inherit;text-decoration:underline;" target="_blank">Make</a>

### s23-24  (p)
노코드 자동화로 여러 앱을 잇기

### s23-25  (p)
<span style="color:var(--accent);font-weight:600;">요점</span>: <span class="sub">Obsidian에 저장된 콘텐츠를 Claude Code가 읽어서 처리하고, 결과를 다시 Obsidian에 저장하거나 외부 서비스로 보냅니다.</span>


## slide 24 · HFK 커뮤니티 운영 자동화
### s24-0  (h2)
HFK 커뮤니티 운영 자동화

### s24-1  (p)
오프라인 학습 커뮤니티의 운영 업무를 <span style="color:var(--accent);font-weight:600;">100개 스킬</span>로 자동화한 사례입니다.

### s24-2  (p)
Obsidian

### s24-3  (p)
콘텐츠

### s24-4  (p)
Claude Code

### s24-5  (p)
100개 스킬

### s24-6  (p)
아임웹

### s24-7  (p)
쇼핑몰

### s24-8  (p)
Slack / Cal

### s24-9  (p)
소통, 일정

### s24-10  (p)
sync-products, backup-products, evaluate-teams, expand-idea, set-presale, refresh-presale, convert-imweb 외 6개

### s24-11  (p)
letter, handout, event-review, team-review, certificate, card-news, post-linkedin 외 11개

### s24-12  (p)
schedule, notices, reminder, attendance, event-attendees, signup-thread, arrival-check 외 12개

### s24-13  (p)
add-contacts, manage-member, move-member, invite-new-members, extract-rereg, brief-event-speaker, send-partner-briefing 외 1개

### s24-14  (p)
hello-world, season-ops, product-ops, content-ops, image-ops, daily-note, wednesday 외 7개

### s24-15  (p)
categorize, analyze-slack, analyze-youtube, ga-report, update-dashboard, audit-security, apple-notes 외 21개


## slide 25 · 한 곳에 있는 파일을 여러 도구가 읽고 씁니다
### s25-0  (h2)
한 곳에 있는 파일을 여러 도구가 읽고 씁니다

### s25-1  (p)
파일은 보관함 한 자리에 있고, 도구들이 그걸 <span style="color:var(--accent);font-weight:600;">양방향으로 읽고 씁니다.</span> 노드를 눌러 각 도구가 파일을 어떻게 다루는지 보세요.

### s25-2  (p)
보관함 · 한 자리

### s25-3  (p)
모든 것이 한 자리에 있습니다

### s25-4  (p)
파일은 보관함(폴더)에 그대로 있고, 도구들이 그걸 읽고 씁니다. 파일이 도구 사이를 옮겨 다니는 게 아닙니다. 한 번 한 일은 노트로, 자주 쓰는 규칙은 메모리로, 반복 작업은 스킬로 여기에 쌓입니다.

### s25-5  (p)
<span class="accent bold">예)</span> Seulki.log 폴더 하나에 노트 · 메모리(MEMORY.md) · 스킬이 함께 있습니다.

### s25-6  (p)
Obsidian · 읽기 ↔ 쓰기 (사람)

### s25-7  (p)
사람이 보고 고치는 창입니다

### s25-8  (p)
보관함의 파일을 보기 좋게 보여주고, 사람이 직접 읽고 고쳐서 다시 저장합니다. VS Code와 같은 파일을 보는 두 창 가운데 하나라, 한쪽에서 고치면 다른 쪽에도 그대로 보입니다.

### s25-9  (p)
<span class="accent bold">예)</span> 노트를 열어 읽고, 손으로 메모를 더해 저장합니다.

### s25-10  (p)
VS Code · 읽기 ↔ 쓰기 (사람 · 확장)

### s25-11  (p)
같은 파일을 편집기로 엽니다

### s25-12  (p)
Obsidian과 똑같은 파일을 코드 편집기에서 봅니다. 여기에 Claude Code 확장이 붙어 있어, 무엇이 바뀌는지 변경 전과 후를 나란히(diff) 보여줍니다.

### s25-13  (p)
<span class="accent bold">예)</span> Claude가 고친 부분이 초록 · 빨강으로 표시돼 확인하고 저장합니다.

### s25-14  (p)
Claude Code · 읽기 ↔ 쓰기 (AI)

### s25-15  (p)
읽고, 판단하고, 다시 씁니다

### s25-16  (p)
파일을 직접 읽어 맥락을 파악하고, 같은 파일에 고쳐 씁니다. 작업 전 메모리 · 노트부터 먼저 읽어 근거로 삼습니다(되먹임). 반자동이라 단계마다 확인합니다.

### s25-17  (p)
<span class="accent bold">예)</span> /convert-to-imweb 이 노트를 읽어 발행용 HTML로 바꿔 같은 자리에 저장합니다.

### s25-18  (p)
결과물 · 내보내기 + 되돌아옴

### s25-19  (p)
발행되어 나가고, 다시 입력이 됩니다

### s25-20  (p)
보관함에 쌓인 파일이 실제 결과로 나갑니다. 아임웹 페이지 · Slack 공지 · 시즌레터로. 그 결과와 기록이 다시 보관함의 새 입력이 되어 고리가 이어집니다.

### s25-21  (p)
<span class="accent bold">예)</span> 노트 → 아임웹 · Slack · 레터 → 그 기록이 다음 작업의 자료로


## slide 26 · 하루가 이렇게 흐릅니다
### s26-0  (h2)
하루가 이렇게 흐릅니다

### s26-1  (p)
<span style="color:var(--accent);font-weight:600;">스페이스</span>를 누르면 한 단계씩 진행됩니다. 명령 하나가 어디로 이어지는지 따라가 봅니다.

### s26-2  (p)
캘린더와 할 일을 읽어 오늘 하루를 브리핑합니다.

### s26-3  (p)
반복하는 운영 업무를 반자동으로 처리합니다. 단계마다 확인하며 진행합니다.

### s26-4  (p)
한 주 슬랙을 분석하고, 핸드아웃과 할 일을 정리합니다.

### s26-5  (p)
오늘 한 일을 기록으로 남기면, 그것이 워크스페이스로 쌓입니다.

### s26-6  (p)
<span style="color:var(--accent);font-weight:600;">기록이 쌓일수록, 내일의 AI 부사수가 더 똑똑해집니다.</span> <span class="sub">AI는 일을 줄이려고 쓰는 것이 아니라, 내 일을 자세히 남기려고 쓰는 것입니다.</span>


## slide 27 · 스킬 106개로 운영합니다
### s27-0  (h2)
스킬 106개로 운영합니다

### s27-1  (p)
반복하는 일을 마크다운 한 장으로 적어두면 명령 한 번으로 돕니다. <span class="accent bold">멤버들이 가장 흥미로워한 것</span>부터 봅니다.

### s27-2  (h3)
오늘 점심 뭐 먹지?

### s27-3  (h3)
유튜브 영상 자동 요약

### s27-4  (h3)
스크린샷 정리해 메모로

### s27-5  (h3)
주간 가계부 자동 정리

### s27-6  (h3)
녹음 → 글 초안

### s27-7  (h3)
후기 자동 작성

### s27-8  (h3)
하루 시작 브리핑

### s27-9  (h3)
시즌 운영 한 번에

### s27-10  (p)
지금 쓰는 전체 스킬 106개

### s27-11  (p)
상품·콘텐츠 <span style="color:var(--text-dim);font-weight:500;">(23)</span>

### s27-12  (p)
/sync-products · /backup-products · /clone-and-move-product · /convert-to-imweb · /convert-review-to-html · /expand-idea · /expand-cover-concepts · /generate-product-content · /generate-letter · /generate-event-review · /generate-team-review · /generate-handout · /generate-certificate · /draft-from-recording · /make-review-cards · /link-product-references · /evaluate-teams · /audit-product-templates · /refresh-presale · /set-presale · /schedule-unhide-product · /update-card-news · /normalize-profile-gallery

### s27-13  (p)
멤버·팀 <span style="color:var(--text-dim);font-weight:500;">(20)</span>

### s27-14  (p)
/manage-member · /move-member · /manage-attendance · /manage-attendance-26summer · /manage-signup-thread · /invite-new-members · /create-slack-channels · /send-partner-briefing · /brief-event-speaker · /plan-teams · /rename-team · /swap-schedule · /confirm-deposit · /extract-reregistration-contacts · /run-member-roadmap · /send-member-roadmap · /session-dashboard · /audit-team-channels · /sync-slack-profiles · /add-contacts

### s27-15  (p)
일정·이벤트·공지 <span style="color:var(--text-dim);font-weight:500;">(14)</span>

### s27-16  (p)
/update-schedule · /schedule-notices · /schedule-4l-reminders · /seed-canvas-sessions · /add-reminder · /check-reactions · /check-event-arrivals · /post-arrival-check · /post-event-attendees · /post-adventure-attendees · /post-signup-attendees · /relay-form-response · /sync-event-attendance · /sync-adventure-attendance

### s27-17  (p)
분석·이미지 <span style="color:var(--text-dim);font-weight:500;">(10)</span>

### s27-18  (p)
/analyze-slack · /analyze-youtube · /view-slack-archive · /ga-report · /categorize-images-hfk · /categorize-images-imweb · /process-screenshots · /run-higgsfield-batch · /export-to-figma · /make-nametags

### s27-19  (p)
시스템·문서 <span style="color:var(--text-dim);font-weight:500;">(20)</span>

### s27-20  (p)
/edit-premiere-xml · /indd-outline-and-export · /print-interpro-indigo · /run-book-prep · /save-output · /save-conversation · /backup-notes · /rename-by-content · /import-apple-notes · /sync-diary · /update-dashboard · /update-presentations · /update-skill-guide · /color-guide · /cleanup-home · /audit-security · /audit-skills · /check-ai-not-to-do · /review-model-choices · /sync-season-data

### s27-21  (p)
일상 &amp; 에이전트(묶음) <span style="color:var(--text-dim);font-weight:500;">(19)</span>

### s27-22  (p)
/today-lunch · /when-to-leave · /when-to-leave-popup · /heypop-now · /expense-tracker · /ask-jaeyoon · /hello-world · /run-daily-note · /run-wednesday · /run-season-ops · /run-season-planning · /run-product-ops · /run-content-ops · /run-image-ops · /run-event-ops · /run-odc-ops · /run-crm-mailing · /post-linkedin · /post-to-buffer


## slide 28 · 시즌 오픈 자동화
### s28-0  (h2)
시즌 오픈 자동화

### s28-1  (p)
<span class="skill-tag">/run-season-ops</span>  하나로 시즌 오픈 전체 프로세스를 자동 실행합니다.

### s28-2  (p)
Step 1

### s28-3  (p)
일정 업데이트

### s28-4  (p)
Google Calendar에서 세션 날짜를 가져와 상품 노트에 반영

### s28-5  (p)
Step 2

### s28-6  (p)
아임웹 동기화

### s28-7  (p)
변경된 노트를 HTML로 변환하여 쇼핑몰에 업데이트

### s28-8  (p)
Step 3

### s28-9  (p)
시즌레터 생성

### s28-10  (p)
이번 시즌 안내 레터를 자동 작성 (선택)

### s28-11  (p)
Step 4

### s28-12  (p)
Slack 공지 예약

### s28-13  (p)
팀별 채널에 세션 공지 예약 발송 (선택)

### s28-14  (p)
Before: 수동 작업

### s28-15  (p)
캘린더 확인 → 엑셀 → HTML → 아임웹 → 레터 → 슬랙

### s28-16  (p)
약 3~4시간

### s28-17  (p)
After: /run-season-ops

### s28-18  (p)
Claude Code에서 스킬 실행 → 각 단계 확인만

### s28-19  (p)
약 10~15분


## slide 29 · MCP 서버 연동
### s29-0  (h2)
MCP 서버 연동

### s29-1  (p)
MCP(Model Context Protocol)로 외부 서비스를 연결하면 스킬의 가능성이 확장됩니다.

### s29-2  (p)
아임웹 API

### s29-3  (p)
상품 CRUD, 카테고리 관리, 쇼핑몰 데이터 직접 제어

### s29-4  (p)
Google Calendar

### s29-5  (p)
일정 조회, 검색, 세션 날짜 자동 매칭

### s29-6  (p)
Slack

### s29-7  (p)
메시지 발송, 채널 생성, 예약 발송, 멤버 관리

### s29-8  (p)
Apple Reminders

### s29-9  (p)
미리알림 추가, 조회, To-Do 관리 자동화

### s29-10  (p)
Google Sheets

### s29-11  (p)
시트 읽기, 쓰기, 수강확인증 생성

### s29-12  (p)
Google Analytics

### s29-13  (p)
페이지뷰, 방문자 통계, 월별 리포트 생성


## slide 30 · 두번째 지능이란?
### s30-0  (h2)
두번째 지능이란?

### s30-1  (h3)
첫번째 지능: 타고난 능력

### s30-2  (li)
학습, 분석, 판단 등 인지적 능력

### s30-3  (li)
경험과 훈련으로 향상되지만 한계 존재

### s30-4  (li)
AI가 빠르게 대체하기 시작한 영역

### s30-5  (h3)
두번째 지능: AI로 확장된 능력

### s30-6  (li)
AI를 통해 가능해지는 새로운 실행력

### s30-7  (li)
기획자도 개발자의 눈을 가질 수 있다

### s30-8  (li)
미뤄뒀던 일, 엄두 못 냈던 영역에 도전

### s30-9  (p)
<span style="color:var(--accent);font-weight:600;">HFK AI부사수 팀의 질문</span>: <span class="sub">'나에게 AI 부사수가 생긴다면, 지금 당장 무엇부터 시킬 것인가?'</span>


## slide 31 · STAR 프레임워크: 두번째 지능 활용법
### s31-0  (h2)
STAR 프레임워크: 두번째 지능 활용법

### s31-1  (h3)
Start

### s31-2  (p)
하고 싶었는데<br/>미뤄왔던 일

### s31-3  (p)
습관 형성

### s31-4  (h3)
Try

### s31-5  (p)
평소 잘 못한다고<br/>생각했던 것

### s31-6  (p)
도전과 성장

### s31-7  (h3)
Amplify

### s31-8  (p)
이미 잘하지만<br/>더 잘하고 싶은 것

### s31-9  (p)
차별화와 전문성

### s31-10  (h3)
Recover

### s31-11  (p)
반복적인 작업을<br/>효율화하는 것

### s31-12  (p)
효율과 재투자

### s31-13  (h3)
워크숍: 내 STAR 찾기

### s31-14  (p)
S: 무엇을 시작할까?

### s31-15  (p)
오랫동안 미뤄온 업무 자동화가 있나요?

### s31-16  (p)
T: 무엇에 도전할까?

### s31-17  (p)
개발자에게 맡겨야 한다고 생각했던 것은?

### s31-18  (p)
A: 무엇을 증폭할까?

### s31-19  (p)
내가 이미 잘하는 것 + AI = ?

### s31-20  (p)
R: 무엇을 효율화할까?

### s31-21  (p)
반복 업무 중 자동화할 수 있는 것은?


## slide 32 · STAR 2×2 매트릭스
### s32-0  (h2)
STAR 2×2 매트릭스

### s32-1  (p)
나의 우선순위는 어디에 있는지, 한 눈에 보기. <span class="dim" style="font-size:0.88em;">X축: 역량, 기반 (약함 → 강함)  ,   Y축: 지향 (효율 → 성장)</span>

### s32-2  (p)
S, Start

### s32-3  (p)
하고 싶었는데 미뤄왔던 일

### s32-4  (p)
습관 형성

### s32-5  (p)
A, Amplify

### s32-6  (p)
이미 잘하지만 더 잘하고 싶은 것

### s32-7  (p)
차별화와 전문성

### s32-8  (p)
T, Try

### s32-9  (p)
평소 잘 못한다고 생각했던 것

### s32-10  (p)
도전과 성장

### s32-11  (p)
R, Recover

### s32-12  (p)
반복적인 작업을 효율화하는 것

### s32-13  (p)
효율과 재투자

### s32-14  (p)
바쁜 직장인

### s32-15  (p)
Start + Recover: 미뤄둔 습관 만들고, 반복 업무 줄이기

### s32-16  (p)
균형 추구

### s32-17  (p)
Start + Try: 미뤄둔 것 시작하고, 못하던 것에 도전


## slide 33 · 강점차별화 2×2 매트릭스
### s33-0  (h2)
강점차별화 2×2 매트릭스

### s33-1  (p)
같은 축 맥락으로, 내가 하는 업무를 선호도와 인정도로 매핑. <span class="dim" style="font-size:0.88em;">X축: 선호도 (낮음 → 높음)  ,   Y축: 인정도 (낮음 → 높음)</span>

### s33-2  (p)
Q2, 전략적 업무

### s33-3  (p)
덜 좋아하지만 인정받는 업무

### s33-4  (p)
이벤트 기획(25명 이하), CS

### s33-5  (p)
→ <code>/analyze-slack</code>, <code>/view-slack-archive</code>: 구조를 대신 만들기

### s33-6  (p)
Q1, 주요 강점 ★

### s33-7  (p)
좋아하고 인정도 받는 업무

### s33-8  (p)
이벤트 기획, 운영, 진행(100명), 파트너 섭외, 팀 기획, 웹사이트 제작

### s33-9  (p)
→ <code>/generate-handout</code>, <code>/manage-attendance</code>, <code>/sync-products</code>: 반복 위임, 판단 집중

### s33-10  (p)
Q3, 축소 고려

### s33-11  (p)
덜 좋아하고 덜 인정받는 업무

### s33-12  (p)
SNS, 슬랙 운영, 영상, 매거진, TF

### s33-13  (p)
→ <code>/schedule-notices</code>, <code>/run-content-ops</code>, <code>/generate-letter</code>: 자동화 or 통합, 위임

### s33-14  (p)
Q4, 숨은 강점

### s33-15  (p)
좋아하지만 덜 인정받는 업무

### s33-16  (p)
중간 서베이, 상세페이지 제작

### s33-17  (p)
→ <code>/ga-report</code>, <code>/evaluate-notes</code>: 성과를 데이터로 가시화

### s33-18  (p)
<span style="color:var(--accent3);font-weight:600;">Q1은 A(Amplify)</span>, <span style="color:var(--accent2);font-weight:600;">Q2는 S/T</span>, <span style="color:var(--accent5);font-weight:600;">Q3는 R</span>, <span style="color:var(--accent4);font-weight:600;">Q4는 T</span>
<span class="sub">: STAR와 같은 축 위에서 사분면이 대응됩니다.</span>


## slide 34 · BCG 매트릭스: HFK 운영에 적용하면
### s34-0  (h2)
BCG 매트릭스: HFK 운영에 적용하면

### s34-1  (p)
같은 축 맥락으로, HFK 운영 영역을 점유율(현재 강점)과 성장률(미래 가치)로 매핑. <span class="dim" style="font-size:0.88em;">X축: 점유율 (낮음 → 높음)  ,   Y축: 성장률 (낮음 → 높음)</span>

### s34-2  (p)
Question Mark, 물음표

### s34-3  (p)
성장 잠재 있으나 포지션 약함: 투자 결정 필요

### s34-4  (p)
AI 컨퍼런스, Figma MCP 연동, 다중 컴퓨터 환경 동기화

### s34-5  (p)
→ <code>/export-to-figma</code>, <code>/audit-skills</code> <span class="dim">신규</span>: 실험으로 가능성 검증

### s34-6  (p)
Star, 스타 ★

### s34-7  (p)
성장하는 시장에서 강한 포지션: 계속 투자

### s34-8  (p)
AI부사수 팀, 강점차별화 팀, Claude Code 스킬 생태계, 100명 이벤트

### s34-9  (p)
→ <code>/run-season-ops</code>, <code>/update-dashboard</code>: 대표 제품으로 키우기

### s34-10  (p)
Dog, 개

### s34-11  (p)
성장도 포지션도 낮음: 철수, 축소

### s34-12  (p)
SNS 운영, 매거진, 소규모 TF

### s34-13  (p)
→ 자동화로 비용 최소화 or 시즌레터로 통합

### s34-14  (p)
Cash Cow, 캐시카우

### s34-15  (p)
성숙 시장에서 안정 수익: 효율화로 수확

### s34-16  (p)
정규 성장트랙 팀, 세션 핸드아웃, 상품 운영, 시즌레터

### s34-17  (p)
→ <code>/run-product-ops</code>, <code>/generate-letter</code>, <code>/sync-products</code>: 반복을 스킬로 수확

### s34-18  (p)
<span style="color:var(--accent3);font-weight:600;">Star ↔ Q1 주요 강점 ↔ Amplify</span>, <span style="color:var(--accent2);font-weight:600;">Question Mark ↔ Q2 ↔ Start</span>, <span style="color:var(--accent4);font-weight:600;">Cash Cow ↔ Q4 ↔ Recover</span>, <span style="color:var(--accent5);font-weight:600;">Dog ↔ Q3 ↔ Try</span>


## slide 35 · 가볍게 시작: STAR로 내 업무를 뜯어보고, 당장 쓸 스킬 만들기 AP
### s35-0  (h2)
가볍게 시작: STAR로 내 업무를 뜯어보고, 당장 쓸 스킬 만들기 <span style="font-size:0.4em;font-weight:600;padding:3px 9px;border-radius:5px;background:rgba(91,123,94,0.12);color:var(--accent3);vertical-align:middle;white-space:nowrap;">API·MCP 없이</span>

### s35-1  (p)
<span style="color:var(--accent);font-weight:600;">미션:</span> 자료가 없어도 괜찮다. STAR로 내가 하는 일을 세세하게 파악하고, 그중 하나를 당장 직장에서 쓸 스킬로 만든다.

### s35-2  (p)
준비물: 없음. STAR 프레임과 5분이면 됩니다. <span style="color:var(--accent);">STEP 1은 Claude가 질문을 하나씩 던지는 왕복 대화예요. 여러 번 주고받은 뒤 다음 칸으로.</span>

### s35-3  (p)
STEP 1

### s35-4  (h3)
STAR로 내 업무 파악

### s35-5  (p)
STEP 2

### s35-6  (h3)
당장 쓸 결과물 정하기

### s35-7  (p)
STEP 3

### s35-8  (h3)
스킬로 만들기

### s35-9  (p)
<span style="color:var(--accent);font-weight:600;">완성:</span> STAR로 파악한 내 업무가 당장 쓰는 스킬이 됩니다. 남의 사례가 아니라 내 일에서 출발한 첫 스킬.


## slide 36 · 커스텀 스킬
### s36-0  (h2)
커스텀 스킬

### s36-1  (p)
마크다운(.md) 파일 하나로 Claude에게 복잡한 업무 절차를 가르칠 수 있습니다.

### s36-2  (h3)
만드는 법

### s36-3  (li)
<code>.claude/commands</code> 폴더에 <code>.md</code> 파일 생성

### s36-4  (li)
파일 안에 업무 절차를 자연어로 작성

### s36-5  (li)
Claude Code에서 <code style="color:var(--accent);">/파일명</code> 으로 실행

### s36-6  (h3)
잘 만드는 팁

### s36-7  (li)
단계별로 명확하게 절차를 기술

### s36-8  (li)
입출력 형식과 예시를 포함

### s36-9  (li)
MCP 도구명을 명시하면 정확도 향상

### s36-10  (li)
에이전트 스킬로 여러 스킬을 연결 가능

### s36-11  (li)
GitHub에 올려 팀과 공유 가능


## slide 37 · 지금까지 본 것을 바탕으로: 내 워크스페이스 만들기
### s37-0  (h2)
지금까지 본 것을 바탕으로: 내 워크스페이스 만들기

### s37-1  (p)
다양한 케이스를 봤습니다. 앞으로 내 업무에 맞는 환경을 만들어봅시다.

### s37-2  (p)
Step 1

### s37-3  (h3)
반복 업무 목록화

### s37-4  (p)
매주/매달 반복하는 업무를 적어보기. 시간이 많이 드는 것부터 우선순위 결정

### s37-5  (p)
Step 2

### s37-6  (h3)
첫 번째 스킬 만들기

### s37-7  (p)
<code>.claude/commands</code> 에 <code>.md</code> 파일 하나 생성. 절차를 자연어로 작성

### s37-8  (p)
Step 3

### s37-9  (h3)
필요한 서비스 연결

### s37-10  (p)
내가 자주 쓰는 서비스를 MCP로 연결. Claude Code 공식 문서 참고

### s37-11  (p)
Step 4

### s37-12  (h3)
스킬을 조합해 에이전트로

### s37-13  (p)
개별 스킬이 쌓이면 여러 스킬을 묶어 에이전트 스킬로 확장

### s37-14  (p)
<span style="color:var(--accent);font-weight:600;">코딩을 몰라도 됩니다.</span>
<span class="sub"> 업무 절차를 자연어로 적으면 Claude가 이해합니다. 반복되는 업무가 있다면, 그것이 바로 첫 번째 스킬 후보입니다.</span>

### s37-15  (p)
<span style="color:var(--accent);font-weight:600;">가능한 모든 일을 VS Code 환경에서 처리해봅니다.</span>
<span class="sub"> 워크스페이스가 풍성해집니다.</span>


## slide 38 · 심플하게, 이것 하나만 제대로
### s38-0  (h2)
심플하게, 이것 하나만 제대로

### s38-1  (p)
AI 서비스가 넘쳐나는 시대

### s38-2  (p)
ChatGPT, Gemini, Copilot, Claude, Cursor, n8n, Make, Zapier... 매주 새로운 도구가 등장합니다.

### s38-3  (p)
타인의 템플릿이나 스킬을 받아도, 책을 사는 것만으로 내 지식이 되지 않듯, 실제로 실행해봐야 합니다.

### s38-4  (p)
'코드를 실행해보고, 왜 이 코드를 만들었을까? 그럼 나는 어떻게 해볼까? 까지 고민을 전개해보세요.'


## slide 39 · AI = 기본기 , HFK = 인사이트와 센스
### s39-0  (h2)
AI = 기본기  ,   HFK = 인사이트와 센스

### s39-1  (h3)
AI만 있으면?

### s39-2  (li)
누구나 빠르게 기본기를 갖추게 된다

### s39-3  (li)
평균의 아웃풋이 올라간다

### s39-4  (li)
차별화가 어려워진다

### s39-5  (li)
<span style="color:var(--accent5);font-weight:600;">AI = 평범함의 도구</span>가 될 수도 있다

### s39-6  (h3)
AI + 인사이트/센스가 있으면?

### s39-7  (li)
기본기를 AI로 빠르게 처리

### s39-8  (li)
남는 시간에 인사이트와 센스를 키운다

### s39-9  (li)
업계 지식 + AI 실행력 = 진짜 강점

### s39-10  (li)
HFK는 그 인사이트, 센스를 함께 키운다

### s39-11  (p)
<span style="color:var(--accent);font-weight:600;">기본기를 AI로 빠르게 마스터하고, 비즈니스 인사이트와 센스, 즉 자신만의 암묵지를 기르는 게 필요합니다.</span>


## slide 40 · 다시 한번, 세 가지
### s40-0  (h2)
다시 한번, 세 가지

### s40-1  (h3)
다양한 케이스 보기

### s40-2  (p)
많이 볼수록 센스가 생깁니다.<br/>Use Case를 계속 발견해가세요.

### s40-3  (h3)
하나를 제대로 쓰기

### s40-4  (p)
Claude Code 하나를 야무지게<br/>잘 쓰는 것이 더 강력합니다.

### s40-5  (h3)
기록하기

### s40-6  (p)
업무 기록과 스킬을 쌓아가면<br/>그것이 나만의 워크스페이스가 됩니다.

### s40-7  (p)
<span style="color:var(--accent);font-weight:600;">AI는 내 일을 줄이기 위해서 쓰는 것이 아닙니다. 내 일을 자세히 남기기 위해서 쓰는 것입니다. AI로 초안의 완성도를 높이고, 결과물을 고도화하는 데 사용하세요.</span>
