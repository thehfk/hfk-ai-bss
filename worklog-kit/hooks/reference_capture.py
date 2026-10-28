#!/usr/bin/env python3
"""사용자가 건넨 링크·파일을 자료/목록.md 에 쌓는다 (UserPromptSubmit).

- 입력에 링크(http·https)나 파일 경로가 보이면, 목록에 없는 것만 한 줄씩 바로 적는다(Claude 가 잊어도 빠지지 않게)
- 그 줄의 '무엇'·'언제' 칸은 비워 두고, Claude 에게 '이 자료를 쓴 뒤 그 칸을 채우라'고 짧게 안내한다
- 긴 붙여넣기 안의 링크까지 줍지 않게, 긴 입력은 앞뒤 400자만 보고 한 번에 5개까지만
- 링크 뒤 물음표 부분에 token·key·sig 같은 말이 있으면 물음표부터 잘라 낸다(비밀값이 목록에 남지 않게)
- 세션 시작 때 목록을 보여주는 일은 reference_session.py 가 맡는다. 작성 기준 정본은 자료/README.md
- 어떤 예외든 조용히 통과(fail-safe: 입력을 막지 않는다)

정본은 hfk-workspace scripts/hooks/, 부사수 멤버용 키트는 scripts/build_worklog_kit.py 가 복사한다.
"""
import sys, os, re, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import read_hook_input, project_dir, read, append

URL = re.compile(r"https?://[^\s<>()'\"`，。]+")
PATH = re.compile(r"(?:~|/Users|/home|[A-Za-z]:\\)[^\s'\"`<>|]*\.[A-Za-z0-9]{2,5}\b")
SECRET_QUERY = re.compile(r"(token|key|sig|signature|secret|auth|password|passwd|code|credential)", re.I)
WINDOW, MAX_ITEMS = 400, 5
HEAD = "# 자료 목록\n\n내가 Claude 에게 건넨 링크와 파일이 한 줄씩 쌓입니다. 작성 기준은 README.md 를 보세요.\n\n"
BLANK = "무엇: ? · 언제: ?"


def clean(u):
    u = u.rstrip(".,;:!?)]}>'\"")
    if "?" in u and SECRET_QUERY.search(u.split("?", 1)[1]):
        u = u.split("?", 1)[0]
    return u


def found(prompt):
    text = prompt if len(prompt) <= WINDOW * 2 else prompt[:WINDOW] + "\n" + prompt[-WINDOW:]
    items = [clean(u) for u in URL.findall(text)] + [p.rstrip(".,;:!?)") for p in PATH.findall(text)]
    return list(dict.fromkeys(i for i in items if len(i) > 8))[:MAX_ITEMS]


def main():
    data = read_hook_input()
    prompt = data.get("prompt") or data.get("user_prompt") or ""
    if not prompt.strip() or prompt.lstrip().startswith("/"):
        return
    items = found(prompt)
    if not items:
        return
    proj = project_dir(data)
    path = os.path.join(proj, "자료", "목록.md")
    have = read(path)
    new = [i for i in items if f" · {i} · " not in have]
    if not new:
        return
    today = datetime.date.today().isoformat()
    append(path, ("" if have.strip() else HEAD) + "".join(f"- {today} · {i} · {BLANK}\n" for i in new))
    print("\n".join([
        f"[자료 기록] 사용자가 건넨 자료 {len(new)}개를 자료/목록.md 에 적었습니다: " + ", ".join(new),
        f"- 요청을 처리하며 이 자료를 열어 봤다면, 그 줄의 '{BLANK}' 를 채우세요."
        " 무엇 = 어떤 자료인지 한 줄(제목·작성처·날짜), 언제 = 어떤 작업을 할 때 다시 열면 되는지",
        "- 열어 보지 못했으면 '?' 는 그대로 둡니다. 지어내지 않습니다",
        "- 비밀번호·개인 연락처가 담긴 자료면 그 줄을 지우고 사용자에게 알립니다",
    ]))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
