#!/usr/bin/env python3
"""고쳐 달라는 말을 규칙 파일로 남기게 한다 (UserPromptSubmit).

- 사용자 입력에 교정 신호('다음부터'·'하지 마'·'그게 아니라'·'기억해' 등)가 보이면 Claude 에게
  '요청을 처리한 뒤, 다음에도 지킬 규칙이면 memory/feedback_*.md 로 저장' 지시를 짧게 붙인다
- 저장할지는 Claude 가 판단한다(이번 한 번만의 지시면 저장하지 않음). 그래서 신호는 넓게 잡는다
- 긴 붙여넣기 안의 문장에 걸리지 않게, 긴 입력은 앞뒤 400자만 본다
- 규칙 목록을 세션마다 다시 읽히는 일은 feedback_session.py(SessionStart) 가 맡는다
- 작성 기준 정본은 memory/README.md. 여기 문구는 그 요약만 담는다
- 어떤 예외든 조용히 통과(fail-safe: 입력을 막지 않는다)

정본은 hfk-workspace scripts/hooks/, 부사수 멤버용 키트는 scripts/build_worklog_kit.py 가 복사한다.
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import read_hook_input, project_dir

# '기억해' 류는 명시적 저장 요청. 나머지는 교정 신호(저장 여부는 Claude 판단)
EXPLICIT = re.compile(r"기억해|기억해\s?줘|기억하고|명심|메모리에|규칙으로\s?(저장|남겨)")
SIGNAL = re.compile(
    r"다음부터|다음에는|다음엔|앞으로는|앞으로\s|"
    r"[가-힣]지\s?(마|말아|말고)(?![련음])|"  # 하지 마·지어내지 마·넣지 말고 (마련·마음 제외)
    r"말고\s|그게\s?아니|아니(야|라|고)\b|아니요?[,.\s]|"
    r"틀렸|잘못\s?(했|됐|썼|넣었|만들었|알|이야|이에요)|또\s?(그러|이러|틀)|왜\s?또|"
    r"매번|항상|절대|(^|\s)늘\s|"  # '오늘 '의 늘은 제외
    r"어색|(^|\s)별로|싫어|이상해")  # '지역별로'의 별로는 제외
WINDOW = 400


def scan_text(prompt):
    if len(prompt) <= WINDOW * 2:
        return prompt
    return prompt[:WINDOW] + "\n" + prompt[-WINDOW:]


def main():
    data = read_hook_input()
    prompt = data.get("prompt") or data.get("user_prompt") or ""
    if not prompt.strip() or prompt.lstrip().startswith("/"):
        return  # 빈 입력·슬래시 명령은 건너뜀
    text = scan_text(prompt)
    explicit = EXPLICIT.search(text)
    m = explicit or SIGNAL.search(text)
    if not m:
        return
    proj = project_dir(data)
    has_index = os.path.exists(os.path.join(proj, "memory", "MEMORY.md"))
    head = ("[피드백 기록] 사용자가 기억해 달라고 했습니다. 요청을 처리한 뒤 규칙으로 저장하세요."
            if explicit else
            f"[피드백 기록] 방금 말에 고쳐 달라는 신호('{m.group(0).strip()}')가 있습니다. 요청을 처리한 뒤,"
            " 다음에도 지켜야 할 규칙이면 저장하세요. 이번 한 번만의 지시거나 이미 저장된 규칙이면 저장하지 않습니다.")
    lines = [
        head,
        "- 저장 위치: 이 프로젝트 폴더의 memory/ (~/.claude 쪽 자동 메모리가 아님). 한 파일에 규칙 하나",
        "- 파일: memory/feedback_<주제>.md. 같은 주제 파일이 이미 있으면 새로 만들지 말고 그 파일을 고친다",
        "- 내용: 규칙 · 이유(사용자가 말한 그대로, 없으면 '이유 미확인') · 언제 적용하나. 형식은 memory/README.md",
        "- memory/MEMORY.md 에 한 줄: - [제목](feedback_<주제>.md) — 언제: …"
        + ("" if has_index else " (파일이 없으면 만든다)"),
        "- 저장했으면 답 끝에 '규칙으로 저장: memory/…' 한 줄로 알린다",
    ]
    print("\n".join(lines))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
