# presentation-ai부사수-3.html
<!-- 이 파일의 각 블록 텍스트를 고치고 `python scripts/deck_content.py inject presentation-ai부사수-3.html` 를 실행하면 발표 HTML에 반영됩니다. 슬롯 헤더(### sN-M)는 위치 키이니 지우지 마세요. -->

## slide 0 · 2주간의 클로드 코드, 그리고 S 사분면 워크숍
### s0-0  (h1)
2주간의 클로드 코드,<br/><span class="accent">그리고 S 사분면 워크숍</span>

### s0-1  (p)
AI 트렌드 두 가지 · 2주간 작업 공유 · 미뤄둔 일을 시작하는 시간

### s0-2  (p)
AI부사수 세션 3회차 · 2026.06.26 · @Seulki.log


## slide 1 · 지난 시간에 다룬 것
### s1-0  (h2)
지난 시간에 다룬 것

### s1-1  (h3)
STAR 프레임워크

### s1-2  (p)
AI에게 뭘 시킬지 정리하는 4가지 관점.

### s1-3  (p)
<span class="bold">S</span>tart · <span class="bold">T</span>ry · <span class="bold">A</span>mplify · <span class="bold">R</span>ecover

### s1-4  (h3)
설치 단계

### s1-5  (p)
Claude Code 구독 → VS Code 설치 → 확장 연결.

### s1-6  (p)
모든 일의 시작과 끝이 되어야 기록이 축적되고 더 정교한 결과가 나옴.

### s1-7  (h3)
데일리 노트 스킬 제작

### s1-8  (p)
자연어로 말해서 하루를 정리하는 <span class="bold">데일리 노트 스킬</span>을 직접 만들어봤습니다.

### s1-9  (p)
여러 스킬을 연결해 트리거로 만들 수도 있음.

### s1-10  (p)
<span class="accent bold">오늘의 흐름</span> —
      <span class="sub">AI 트렌드 → 지난 2주 작업 공유 → S 사분면 자세히 → 연결 준비 → 워크숍 실습</span>


## slide 2 · 최근 몇 주, 무슨 일이 있었나
### s2-0  (h1)
최근 몇 주,<br/><span class="accent">무슨 일이 있었나</span>

### s2-1  (p)
슬랙에서 @Claude로 일을 맡기는 Claude Tag가 열리고,<br/>
      클로드 코드가 자기 코드를 스스로 보안 검수하는 플러그인이 나왔습니다.

### s2-2  (p)
두 가지 모두 비개발자에게 의미가 있는 변화입니다.


## slide 3 · "슬랙에서 @Claude로 일을 맡긴다"
### s3-0  (h2)
"슬랙에서 @Claude로 일을 맡긴다"

### s3-1  (p)
앤트로픽이 자사 제품팀 코드의 <span class="accent bold">65%를 만드는 방식</span>, Claude Tag를 공개. 슬랙에 Claude를 팀원처럼 들여 <span class="accent bold">@Claude</span>로 일을 넘기는 기능입니다.

### s3-2  (h3)
어떻게 동작하나

### s3-3  (li)
말로 일을 던지면 <span class="bold">스스로 단계를 쪼개</span> 처리

### s3-4  (li)
결과를 <span class="bold">슬랙 스레드에 올림</span>

### s3-5  (li)
채널 맥락을 기억해 <span class="bold">팀이 하나의 Claude</span>를 같이 씀

### s3-6  (li)
맡겨두면 며칠짜리 일도 자율로 진행

### s3-7  (h3)
채널에 연결해두는 것

### s3-8  (p)
도구·데이터·코드베이스를 채널에 연결해두면 <span class="bold">누구나 @Claude를 불러</span> 일을 맡깁니다.

### s3-9  (h3)
기존 'Claude in Slack'과 다른 점

### s3-10  (p)
질의응답에서 그치지 않고, <span class="bold">실제 작업을 끝까지 수행하고 결과를 스레드에 남깁니다.</span> 채팅 상대가 아니라 일하는 팀원에 가깝습니다.


## slide 4 · 왜 이게 의미 있을까
### s4-0  (h2)
왜 이게 의미 있을까

### s4-1  (h3)
AI를 '도구'가 아니라 '팀원'으로

### s4-2  (p)
채널에 들여두고 누구나 일을 맡김. <span class="bold">실제로 슬랙에 존재하는 매니저에게 일을 시키는 방식</span>으로 일합니다.

### s4-3  (h3)
비개발자도 같은 흐름

### s4-4  (p)
코드 한 줄 없이, 평소 쓰는 <span class="bold">슬랙에서 말로</span> 맡김. 결과는 스레드에 남아 같이 보고 추적할 수 있음.

### s4-5  (h3)
만든 회사가 먼저 씀

### s4-6  (p)
앤트로픽이 자사 제품팀 코드의 <span class="bold">65%</span>를 이 방식으로 생산. 시연용이 아니라 실제 업무 도구.


## slide 5 · 클로드 코드가 자기 코드를 스스로 보안 검수한다
### s5-0  (h2)
클로드 코드가 자기 코드를 스스로 보안 검수한다

### s5-1  (p)
앤트로픽이 클로드 코드용 <span class="accent bold">보안 가이드 플러그인(Security Guidance)</span>을 공개. 코딩하는 동안 위험한 패턴을 백그라운드에서 자동으로 잡아 수정 가이드를 띄웁니다.

### s5-2  (h3)
무엇을 잡아내나

### s5-3  (li)
명령어 주입(command injection), XSS 같은 <span class="bold">주요 보안 위험을 자동 감지</span>

### s5-4  (li)
위험한 패턴을 <span class="bold">백그라운드에서 검사</span>(코딩 흐름을 끊지 않음)

### s5-5  (li)
클로드 코드에서 <span class="accent">/plugins</span> 입력하면 플러그인 마켓에서 골라 설치

### s5-6  (p)
AI 코딩의 다음 라운드는 'AI 보안'.

### s5-7  (h3)
공식 데모

### s5-8  (p)
8초 만에 작성한 145줄 NodeJS 코드 직후 빨간 배너: <span class="bold">'Background security review found'</span>. Go와 Node가 같은 키를 다르게 읽는 틈으로 메시지가 새는 구멍을 발견.

### s5-9  (p)
진단에 그치지 않고 <span class="bold">허용 키 재구성·변형 키 차단·타입 검사까지 자동 적용</span>했습니다.

### s5-10  (p)
<span class="accent bold">생각해볼 점</span><br/>
          비개발자가 만든 결과물에도 점검은 필요합니다. 비개발자의 실수를 줄일 수 있도록 사람이 일일이 못 보던 위험을 <span class="bold">도구가 대신 잡아주는 방향</span>으로 개발되고 있습니다.


## slide 6 · 내가 클로드 코드를 어떻게 쓰는지 리포트로 받아본다
### s6-0  (h2)
내가 클로드 코드를 어떻게 쓰는지 리포트로 받아본다

### s6-1  (p)
채팅창에 <span class="accent bold">/insights</span> 한 줄이면, <span class="bold">최근 30일</span> 동안 내가 클로드 코드를 어떻게 써왔는지 정리한 리포트(HTML)를 만들어줍니다.

### s6-2  (h3)
무엇을 보여주나

### s6-3  (li)
주로 <span class="bold">어떤 일에 많이 썼는지</span> (작업 종류 분포)

### s6-4  (li)
세션이 얼마나 <span class="bold">효율적이었는지</span>, 토큰은 얼마나 썼는지

### s6-5  (li)
자주 <span class="bold">막히거나 되돌린 지점</span> (마찰 포인트)

### s6-6  (h3)
/usage와 뭐가 다른가

### s6-7  (p)
<code class="accent">/usage</code>는 <span class="bold">지금 이 순간</span>의 비용·사용량을 즉시 보여주고, <code class="accent">/insights</code>는 <span class="bold">한 달치 패턴</span>을 분석해 리포트로 묶어줍니다.

### s6-8  (p)
<span class="accent bold">왜 좋은가</span><br/>
          "내가 클로드를 어디에 쓰고, 어디서 자꾸 막히는지"를 눈으로 보면 <span class="bold">다음에 뭘 스킬로 만들지</span>가 보입니다.


## slide 7 · 6월 12일 ~ 6월 26일, 클로드 코드와 함께한 2주
### s7-0  (h1)
6월 12일 ~ 6월 26일,<br/><span class="accent">클로드 코드와 함께한 2주</span>

### s7-1  (p)
어떻게 시즌 운영의 모든 단계를 클로드 코드와 함께 처리하는지,<br/>
      실제 산출물 중심으로 보여드립니다.


## slide 8 · 2주간의 작업 한눈에 보기
### s8-0  (h2)
2주간의 작업 한눈에 보기

### s8-1  (p)
19

### s8-2  (p)
신규·수정 스킬

### s8-3  (p)
5

### s8-4  (p)
신규 멤버 운영 스킬

### s8-5  (p)
7

### s8-6  (p)
CLAUDE.md 고위험 규칙

### s8-7  (p)
3

### s8-8  (p)
매일 도는 자동화

### s8-9  (h3)
날짜별 큰 흐름

### s8-10  (li)
<span class="bold">6/12</span> 데일리 노트에 작업 흐름 기록, backup-notes 본문 복원

### s8-11  (li)
<span class="bold">6/14</span> 4L 리마인더 시즌 가드, 멤버 가이드 재디자인

### s8-12  (li)
<span class="bold">6/19~20</span> 멤버 AI 워크숍 인터랙티브 덱(v1.1)

### s8-13  (li)
<span class="bold">6/21</span> 고위험 규칙·사전점검·헬스체크, 실시간 신청 알림

### s8-14  (li)
<span class="bold">6/21</span> 회차 읽을거리 공지, 컨퍼런스콜 2회차 발송

### s8-15  (li)
<span class="bold">6/25</span> 신규 멤버 운영 스킬 묶음(CS·환영메일·이탈감지)

### s8-16  (li)
<span class="bold">6/26</span> 인스타 인바운드 리포트 자동화

### s8-17  (h3)
2주간의 패턴

### s8-18  (p)
전부 <span class="bold">"같은 작업이 반복될 때 스킬로 만들어두기"</span>의 결과물. 한 번 만든 흐름이 다음 주에 다시 굴러감.

### s8-19  (p)
이번 2주의 특징: 멤버가 들어오고 나가는 모든 단계를 자동으로 챙기고, 되돌릴 수 없는 작업 앞에 안전장치를 깔고, 발표·공지·리포트를 한 번의 명령으로 만들어 냄.


## slide 9 · 멤버가 들어오고 나가는 모든 단계를 자동으로
### s9-0  (h2)
멤버가 들어오고 나가는 모든 단계를 자동으로

### s9-1  (h3)
신규 멤버가 들어오면 (온보딩)

### s9-2  (li)
매일 09:30 새 멤버를 찾아 <span class="bold">운영자에게 슬랙 DM</span>으로 알림 (launchd)

### s9-3  (li)
환영 메일을 처리 흐름에 연결해 자동 발송

### s9-4  (li)
슬랙 초대·주소록 추가까지 이어짐

### s9-5  (p)
스킬: <code class="accent">/send-welcome-email</code>

### s9-6  (h3)
응대가 필요하면 (CS)

### s9-7  (p)
CS 응대 매뉴얼과 유지보수 스킬로 <span class="bold">자주 묻는 질문에 일관된 답</span>을 빠르게.

### s9-8  (p)
스킬: <code class="accent">/update-cs-doc</code>

### s9-9  (h3)
이탈 신호가 보이면

### s9-10  (p)
출석·참여 데이터로 <span class="bold">이탈 신호를 감지</span>해 케어 DM을 준비.

### s9-11  (p)
스킬: <code class="accent">/detect-churn-signals</code>

### s9-12  (h3)
데이터가 어긋나면 (정합성)

### s9-13  (p)
멤버십 시트·슬랙·아임웹 사이의 <span class="bold">불일치를 자동으로 감사</span>.

### s9-14  (p)
스킬: <code class="accent">/audit-membership-consistency</code>


## slide 10 · 멤버 AI 워크숍 덱을 인터랙티브 버전으로
### s10-0  (h2)
멤버 AI 워크숍 덱을 인터랙티브 버전으로

### s10-1  (h3)
무엇을 만들었나

### s10-2  (li)
멤버용 AI 워크숍 발표덱을 <span class="bold">v1.1로 갱신</span>

### s10-3  (li)
파일 하나가 거치는 <span class="bold">이동 경로를 따라가는</span> 트레이스 슬라이드

### s10-4  (li)
워크플로우를 일방향에서 <span class="bold">보관함 중심 양방향 허브</span>로 교정

### s10-5  (h3)
함께 한 것

### s10-6  (li)
모바일 버전도 같은 v1.1로 맞춤

### s10-7  (li)
멤버 AI 워크숍 브리핑 페이지 추가, 발표 목록·index 카드 연결


## slide 11 · 되돌릴 수 없는 작업 앞에 안전장치를 깔다
### s11-0  (h2)
되돌릴 수 없는 작업 앞에 안전장치를 깔다

### s11-1  (h3)
고위험 액션 체크 규칙 7개 신설

### s11-2  (li)
날짜·장소는 <span class="bold">구글 캘린더가 정본</span>, 추측 금지

### s11-3  (li)
멤버 발송 전 <span class="bold">dry-run으로 대상·내용 먼저 확인</span>

### s11-4  (li)
검증 안 한 일을 "완료"로 단정하지 않음

### s11-5  (p)
CLAUDE.md에 운영 규칙으로 박아둠.

### s11-6  (h3)
사전 점검(preflight)

### s11-7  (p)
슬랙 게시·출석 기록·예약 발송 직전에 <span class="bold">날짜·신원·내용을 정본과 교차 검증</span>.

### s11-8  (p)
스킬: <code class="accent">/preflight-verify</code>

### s11-9  (h3)
자동화는 조용히 실패하지 않게

### s11-10  (p)
cron·launchd 작업을 <span class="bold">네트워크 대기 + healthcheck</span>로 감쌈. 무음 네트워크 실패가 드러나게.

### s11-11  (h3)
라이브 반영은 검증까지

### s11-12  (p)
배포 후 <span class="bold">실제 URL을 다시 확인</span>하고 나서 "완료"를 보고.

### s11-13  (p)
스킬: <code class="accent">/deploy-and-verify</code>

### s11-14  (p)
<span class="accent bold">포인트:</span>
<span class="sub">News에서 본 "AI가 자기 코드를 스스로 검수한다"는 흐름을, 우리 운영에도 규칙으로 심었습니다.</span>


## slide 12 · 이벤트 신청을 자체 웹폼 + 실시간 알림으로
### s12-0  (h2)
이벤트 신청을 자체 웹폼 + 실시간 알림으로

### s12-1  (h3)
무엇이 바뀌었나

### s12-2  (li)
시즌레터의 신청 버튼을 <span class="bold">자체 웹폼</span>으로 교체

### s12-3  (li)
체크박스 복수선택 + 이벤트별 기대사항 칸 + 신청 마감

### s12-4  (li)
신청 현황 대시보드를 <span class="bold">매일 09:00 자동 갱신</span> (launchd + healthcheck)

### s12-5  (h3)
실시간 신청 알림

### s12-6  (p)
새 신청이 들어오면 <span class="bold">운영자에게 바로 알림</span>. 일시 네트워크 오류는 재시도로 흘려보냄.

### s12-7  (h3)
이벤트별 발송 자동화

### s12-8  (li)
신청자 파싱 → 슬랙 매칭 → 참석/대기 댓글 자동 발송

### s12-9  (li)
정원 초과 시 선착순 + 우선 선발(ODC·뉴멤버)

### s12-10  (p)
스킬: <code class="accent">/open-event-signup</code>, <code class="accent">/post-event-attendees</code>

### s12-11  (p)
<span class="accent bold">의미:</span>
          신청을 받고, 확인하고, 댓글 달고, 마감하는 일을 <span class="bold">한 줄로</span>. 최근 여름 캠핑·박찬용 북토크 신청에 그대로 적용.


## slide 13 · "매주 수요일, 저희도 클로드 코드 모임을 하고 있어요"
### s13-0  (h2)
"매주 수요일, 저희도 클로드 코드 모임을 하고 있어요"

### s13-1  (p)
"AI부사수에서 배웠던 내용을 토대로 복습 겸 업무 효율을 높이기 위해 <span class="accent bold">매주 수요일 레디투킥 팀에서도 클로드 코드 모임</span>을 갖고 있어요. 모두 흥미로워하며 매일 조금씩 친해지는 중입니다."

### s13-2  (p)
"S에 포함되는 업무와 반복 업무를 적용해 봤고, 그래픽 디자이너님은 어도비와 연동하여 <span class="accent bold">2주 걸리는 작업을 3시간 만에</span> 끝내기도 했어요."

### s13-3  (p)
"중간에 막히는 게 있어도 <span class="accent bold">클로드와 끝까지 해결한 경우</span>가 있어서 클로드에 대한 믿음이 생겼습니다."

### s13-4  (h3)
레디투킥 팀 Use Cases

### s13-5  (li)
<span class="bold">아침 뉴스레터 자동 발송</span> — 폴인/캐릿 뉴스레터를 Gmail API + 웹 크롤링으로 슬랙 채널에 매일/매주 자동 발송

### s13-6  (li)
<span class="bold">월 매출 요약 자동 전송</span> — 카페24/스마트스토어/29CM 채널별 순매출, 목표 달성률, YoY/MoM 자동 집계 → 슬랙 리포트

### s13-7  (li)
<span class="bold">META 광고 성과 자동 요약</span> — Meta Marketing API 연동, 소재별 ROAS/CPA 자동 집계 → 시트 입력 + 슬랙 발송

### s13-8  (li)
<span class="bold">일별 매출 현황 자동 발송</span> — 매일 출근 시 전날 채널별 매출 + 주문건수 자동 발송 (월요일엔 주말 3일치 합산)

### s13-9  (h3)
어도비 일러스트레이터 자동화

### s13-10  (p)
구글 시트 제품 데이터 → 일러스트레이터 자동 연동 → 제품별 스티커 일괄 생성

### s13-11  (p)
수작업 2주 → 3시간


## slide 14 · 오늘은 S부터 시작합니다
### s14-0  (h1)
오늘은 S부터<br/><span class="accent">시작합니다</span>

### s14-1  (p)
STAR 4개 다 할 필요 없습니다.<br/>
      오늘은 가장 가벼운 한 칸, <span class="accent bold">S = Start</span>만 깊게 다룹니다.


## slide 15 · S 사분면이 어디에 있는지 다시 보기
### s15-0  (h2)
S 사분면이 어디에 있는지 다시 보기

### s15-1  (h3)
S

### s15-2  (p)
Start

### s15-3  (p)
하고 싶었는데<br/>미뤄왔던 일

### s15-4  (p)
습관 형성

### s15-5  (p)
★ 오늘 다룸

### s15-6  (h3)
T

### s15-7  (p)
Try

### s15-8  (p)
평소 잘 못한다고<br/>생각했던 것

### s15-9  (p)
도전과 성장

### s15-10  (h3)
A

### s15-11  (p)
Amplify

### s15-12  (p)
이미 잘하지만<br/>더 잘하고 싶은 것

### s15-13  (p)
차별화

### s15-14  (h3)
R

### s15-15  (p)
Recover

### s15-16  (p)
반복 작업을<br/>효율화하는 것

### s15-17  (p)
시간 회수

### s15-18  (p)
<span class="accent bold">왜 S부터?</span>
<span class="sub">제일 부담 없는 칸이기 때문. "잘해야 한다"는 생각 없이 일단 시작하는 것이 중요.</span>


## slide 16 · S = Start — 미뤄왔던 일을 시작하는 칸
### s16-0  (h2)
S = Start — 미뤄왔던 일을 시작하는 칸

### s16-1  (p)
"매일 하면 좋은데 자꾸 미루는 것들" — AI에게 그 일을 매일 옆에서 도와달라고 부탁하는 영역.

### s16-2  (h3)
S 영역의 특징

### s16-3  (li)
<span class="bold">실패해도 부담이 적음</span> — 어차피 안 하던 일이니까

### s16-4  (li)
<span class="bold">성과보다 빈도가 중요</span> — 매일 짧게 하는 게 성공

### s16-5  (li)
<span class="bold">결과물보다 트리거가 먼저</span> — "AI가 먼저 말 걸어주는 구조"가 절반

### s16-6  (li)
<span class="bold">나를 위한 일</span> — 회사 KPI가 아니라 내 삶의 작은 루틴

### s16-7  (h3)
슬기의 S 영역 4개 (실제 운영 중)

### s16-8  (li)
<code class="accent">/hello-world</code> — 아침에 캘린더·미리알림·어제 잔여 작업을 한 화면에 띄워주는 브리핑

### s16-9  (li)
<code class="accent">/run-daily-note</code> — 하루 끝에 그날 작업을 자동으로 일지로 정리

### s16-10  (li)
<code class="accent">/cleanup-home</code> — 흩어진 다운로드 파일을 자동 분류

### s16-11  (li)
<code class="accent">/backup-notes</code> — 노트를 주기적으로 백업

### s16-12  (p)
공통점: 전부 <span class="bold">"매일 해야 하는 줄 아는데 자꾸 까먹는 것"</span>이었음.


## slide 17 · S 영역 스킬은 어떻게 작동하는가
### s17-0  (h2)
S 영역 스킬은 어떻게 작동하는가

### s17-1  (h3)
예시 1 — /hello-world

### s17-2  (p)
아침에 명령 한 줄 입력하면:

### s17-3  (li)
인증 파일이 제대로 있는지 확인

### s17-4  (li)
오늘의 캘린더 일정 가져옴

### s17-5  (li)
미리알림 앱에서 오늘/늦은 항목 가져옴

### s17-6  (li)
어제 작업 일지에서 미완료 항목 확인

### s17-7  (li)
한 화면에 정리해서 보여줌

### s17-8  (h3)
예시 2 — /cleanup-home

### s17-9  (p)
홈/다운로드 폴더를 훑고, 파일 종류·날짜로 자동 분류 폴더에 이동. <span class="bold">"이거 어디에 둘까"</span>를 매번 고민하지 않아도 됨.

### s17-10  (h3)
공통 구조

### s17-11  (li)
<span class="bold">트리거</span> — 언제 시작할지 (아침에, 하루 끝에, 매주 일요일에)

### s17-12  (li)
<span class="bold">데이터 소스</span> — 어디서 정보를 가져올지 (캘린더, 폴더, 슬랙)

### s17-13  (li)
<span class="bold">처리</span> — 어떻게 정리할지 (분류, 요약, 정렬)

### s17-14  (li)
<span class="bold">결과 형식</span> — 어디로 보여줄지 (화면, 파일, DM)

### s17-15  (p)
<span class="accent bold">기억할 것</span><br/>
          좋은 S 스킬은 <span class="bold">"내가 명령하지 않아도 알아서 말 걸어주는 구조"</span>까지 만드는 것. 일단 오늘은 그 직전 단계인 <span class="bold">"명령 한 줄로 시작되는 단계"</span>까지 가봅니다.


## slide 18 · 클로드 코드에 내 도구를 연결한다: 커넥터
### s18-0  (h2)
클로드 코드에 내 도구를 연결한다: 커넥터

### s18-1  (p)
커넥터는 클로드 코드를 <span class="accent bold">구글·슬랙·깃허브 같은 외부 서비스에 연결</span>하는 통로입니다. 한 번 연결해두면 클로드가 그 도구를 직접 불러서 일을 합니다.

### s18-2  (h3)
무엇을 연결하나

### s18-3  (li)
구글(캘린더·드라이브·지메일), 슬랙, 깃허브

### s18-4  (li)
직접 만든 도구(MCP 서버)까지

### s18-5  (h3)
어떻게 추가하나

### s18-6  (p)
claude.ai 왼쪽 상단 메뉴 → 왼쪽 탭 <span class="bold">[사용자 지정]</span> → 커넥터에서 원하는 서비스를 검색해 설치. <span class="bold">코드 없이</span> 됩니다.

### s18-7  (p)
연결해두면 "내 캘린더 일정 가져와", "이 슬랙 채널에 올려줘" 같은 말이 <span class="bold">바로 동작</span>합니다.


## slide 19 · 커넥터가 편한데도, 구글 키를 따로 받는 이유
### s19-0  (h2)
커넥터가 편한데도, 구글 키를 따로 받는 이유

### s19-1  (h3)
왜 필요한가

### s19-2  (p)
커넥터는 <span class="bold">클로드 코드 안에서 대화할 때만</span> 작동합니다. 매일 자동으로 도는 작업이나 내 컴퓨터에서 따로 도는 스크립트가 구글에 접근하려면 <span class="accent bold">내 OAuth Client ID &amp; Key</span>가 필요합니다.

### s19-3  (h3)
무엇을 받나

### s19-4  (li)
<span class="bold">Client ID</span>: ...apps.googleusercontent.com 형태

### s19-5  (li)
<span class="bold">Client Secret</span>: 긴 비밀 문자열 (외부 공유·깃 커밋 금지)

### s19-6  (h3)
받는 법 (구글 클라우드 콘솔)

### s19-7  (li)
<span class="bold">console.cloud.google.com</span> 접속 → 프로젝트 만들기

### s19-8  (li)
"API 및 서비스"에서 쓸 API <span class="bold">사용 설정</span> (캘린더·드라이브·지메일)

### s19-9  (li)
<span class="bold">OAuth 동의 화면</span> 설정 (외부, 앱 이름, 본인 이메일을 테스트 사용자로)

### s19-10  (li)
<span class="bold">사용자 인증 정보</span> → OAuth 클라이언트 ID 만들기 → <span class="bold">데스크톱 앱</span> 선택

### s19-11  (li)
나온 <span class="bold">Client ID·Secret</span>을 JSON으로 저장 → 내 <code class="accent">.env</code>에 보관


## slide 20 · 받은 키는 대화창에 적지 말고 .env에 넣는다
### s20-0  (h2)
받은 키는 대화창에 적지 말고 .env에 넣는다

### s20-1  (h3)
VS Code에서 바로 .env 열기

### s20-2  (p)
클로드에게 <span class="bold">".env에 ID·Secret 넣을 자리를 만들고 그 파일을 열어줘"</span>라고 하면, VS Code 창에 .env가 바로 열립니다. 만들어진 자리에 값을 <span class="bold">복사·붙여넣기</span>만 하면 됩니다.

### s20-3  (h3)
JSON 파일을 받았다면

### s20-4  (p)
"다운로드 폴더에 있는 그 JSON 파일을 보고 <span class="bold">.env에 기록해줘</span>"라고 시키면 클로드가 알아서 옮겨 적습니다.

### s20-5  (p)
<span class="accent bold">딱 하나만 지키기</span><br/>
          ID·Secret을 <span class="bold">대화창에 직접 적지 않기.</span> "파일을 열어줘 / 파일을 보고 기록해줘"라고 시키면, 비밀 값이 대화 기록에 남지 않습니다.


## slide 21 · 오늘 워크숍 흐름
### s21-0  (h2)
오늘 워크숍 흐름

### s21-1  (p)
STEP 1 · 5분

### s21-2  (h3)
미뤄둔 일 떠올리기

### s21-3  (p)
지금 머릿속에 떠오르는 "해야지 하면서 미뤘던 일" 3개를 적어봅니다.

### s21-4  (p)
STEP 2 · 5분

### s21-5  (h3)
하나만 고르기

### s21-6  (p)
3개 중 가장 가벼운 것 1개만. 거창한 것 금지.

### s21-7  (p)
STEP 3 · 10분

### s21-8  (h3)
명령 만들기

### s21-9  (p)
트리거 / 소스 / 처리 / 결과 4칸에 각각 한 줄씩 적어봅니다.

### s21-10  (p)
STEP 4 · 15분

### s21-11  (h3)
실제 실행

### s21-12  (p)
클로드 코드 창에 그대로 붙여 넣고 결과 확인. 막히면 같이 풀어봅니다.

### s21-13  (p)
<span class="accent bold">목표</span> —
      <span class="sub">완벽한 자동화 X. 오늘 안에 <span class="bold">한 번이라도 작동하는 S 명령</span> 만들기 O.</span>


## slide 22 · STEP 1 — 미뤄둔 일 떠올리기 (5분)
### s22-0  (h2)
STEP 1 — 미뤄둔 일 떠올리기 (5분)

### s22-1  (h3)
"미뤄둔 일"의 정의

### s22-2  (li)
"매일 하면 좋은데 안 하고 있는 것"

### s22-3  (li)
"한 번 시작하면 좋은데 시작이 안 되는 것"

### s22-4  (li)
"머릿속엔 있는데 손이 안 가는 것"

### s22-5  (p)
업무도 좋고, 개인 영역(독서·운동·가계부)도 좋음.

### s22-6  (h3)
예시 (참고용)

### s22-7  (li)
매일 아침 어제 한 일 한 줄로 정리하기

### s22-8  (li)
주말마다 다운로드 폴더 정리

### s22-9  (li)
읽고 싶은 기사 모아두고 매일 한 개씩 요약

### s22-10  (li)
매주 월요일 한 주 캘린더 미리 보기

### s22-11  (li)
가계부에 어제 결제 내역 기록

### s22-12  (li)
슬랙 중요 메시지 모아두기

### s22-13  (p)
<span class="accent bold">활동</span> — 노트를 펴고 <span class="bold">3개를 적어보세요.</span> 잘 안 떠오르면 위 예시에서 가장 비슷한 것을 골라도 됩니다.


## slide 23 · STEP 2 — 가장 가벼운 1개 고르기 (5분)
### s23-0  (h2)
STEP 2 — 가장 가벼운 1개 고르기 (5분)

### s23-1  (h3)
고르는 기준 3가지

### s23-2  (li)
<span class="bold">5분 안에 끝나는 것</span> — 거창한 건 금지

### s23-3  (li)
<span class="bold">결과를 누가 검사 안 하는 것</span> — 회사 KPI 말고 내 삶의 일

### s23-4  (li)
<span class="bold">매일 또는 매주 반복되는 것</span> — 일회성 작업은 R 영역으로

### s23-5  (h3)
하지 말 것

### s23-6  (li)
"내 인생을 바꿀 거대한 습관" 같은 거 고르지 마세요

### s23-7  (li)
"AI가 알아서 다 해주는" 같은 막연한 기대 금지

### s23-8  (li)
다른 사람과 협업이 필요한 것은 보류

### s23-9  (p)
<span class="accent bold">활동</span> — 3개 중 가장 작고 가벼운 것에 <span class="bold">동그라미 하나</span>. 그것이 오늘 우리가 만들 S 스킬의 주제입니다.


## slide 24 · STEP 3 — 4칸으로 명령 만들기 (10분)
### s24-0  (h2)
STEP 3 — 4칸으로 명령 만들기 (10분)

### s24-1  (h3)
4칸 양식

### s24-2  (li)
<span class="bold">트리거</span> — "언제 이 일을 할 것인가?"

### s24-3  (li)
<span class="bold">소스</span> — "어디서 정보를 가져올 것인가?"

### s24-4  (li)
<span class="bold">처리</span> — "어떻게 가공할 것인가?"

### s24-5  (li)
<span class="bold">결과</span> — "결과를 어디로 보내줄 것인가?"

### s24-6  (p)
한 칸당 한 줄이면 충분합니다. 완벽할 필요 없음.

### s24-7  (h3)
완성 예시 — "매일 캘린더 정리"

### s24-8  (p)
<span class="accent bold">활동</span> —
      <span class="sub">노트 한 장에 4칸을 그리고 각각 한 줄씩 채워보세요. 옆사람과 비교해도 좋습니다.</span>


## slide 25 · STEP 4 — 실제로 실행해보기 (15분)
### s25-0  (h2)
STEP 4 — 실제로 실행해보기 (15분)

### s25-1  (h3)
실행 방법

### s25-2  (li)
VS Code에서 클로드 코드 채팅창 열기

### s25-3  (li)
4칸 내용을 그대로 한국어 문장으로 풀어 입력

### s25-4  (li)
클로드가 묻는 질문에 한 줄씩 대답

### s25-5  (li)
결과 확인 — 잘 되면 다음 칸 추가, 안 되면 막힌 부분 같이 풀기

### s25-6  (h3)
자주 막히는 곳

### s25-7  (li)
"권한이 없다"는 메시지 → 캘린더/슬랙 등 인증 필요

### s25-8  (li)
"파일을 찾을 수 없다" → 정확한 폴더 경로 알려주기

### s25-9  (li)
너무 많은 걸 한 번에 시키기 → 한 단계씩 나누기

### s25-10  (p)
팁: 첫 스킬은 캘린더·슬랙처럼 로그인이 필요한 것보다 <span class="bold">내 컴퓨터 파일 정리</span>처럼 바로 되는 일로 시작하면 막힘이 적습니다.

### s25-11  (h3)
입력 예시 (그대로 써도 됨)

### s25-12  (p)
결과가 마음에 들면 저장해두기. 매일 자동으로 실행하는 건 다음 시간에 다룹니다.


## slide 26 · AI는 부사수입니다
### s26-0  (h1)
AI는<br/><span class="accent">부사수입니다</span>

### s26-1  (p)
바이브 코딩으로 하나의 업무를 완벽하게 하려면<br/>
<span class="bold">업무 프로세스를 쪼개어 생각하며, 스킬을 디벨롭</span>해가세요.

### s26-2  (p)
AI부사수 세션 3회차 · 2026.06.26 · @Seulki.log
