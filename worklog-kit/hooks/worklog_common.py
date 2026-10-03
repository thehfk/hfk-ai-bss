"""worklog 훅 공통: 경로·작업자 이름·세션 기록 판정·잠금 쓰기.

훅들은 `python3 <훅폴더>/xxx.py` 로 실행되므로 같은 폴더의 이 모듈을 바로 import 한다.
품질 기준 정본은 worklog/README.md 다. 여기 문구는 그 요약만 담는다.

이 파일들은 hfk-workspace(scripts/hooks/)와 부사수 멤버용 키트(hfk-ai-bss worklog-kit/)가 함께 쓴다.
정본은 hfk-workspace 쪽이고(파일명에 _ 를 붙이지 않는 건 GitHub Pages Jekyll 이 _ 파일을 배포하지 않아서), 키트는 scripts/build_worklog_kit.py 가 복사한다. 키트에서 직접 고치지 말 것.
"""
import os, re, json, datetime, subprocess
from contextlib import contextmanager

try:
    import fcntl
except ImportError:  # 윈도우 등: 잠금 없이 동작
    fcntl = None

CHECKLIST = (
    "작성 기준(정본 worklog/README.md):\n"
    "- 목적/왜: 계기(누가 요청했나·무슨 문제였나) + 이유\n"
    "- 무엇을: 고칠 범위 + 손대지 않는 것\n"
    "- 결과: ① 실제로 바뀐 것과 식별자(파일 경로·커밋·메시지 링크·문서 행 등)"
    " ② 어떻게 확인했나(다시 열어봄·실행해봄·미리보기 등, 확인 못 했으면 '미확인'이라고)"
    " ③ 못 한 것·남은 수동 작업. 숫자는 출처와 대조한 것만"
)
WITH_RESULT = "[결과 함께]"  # 같은 명령이 결과 줄도 썼다는 표시. needs_result 가 이 줄은 건너뛴다


def read_hook_input():
    import sys
    raw = sys.stdin.read()
    return json.loads(raw) if raw.strip() else {}


def project_dir(data):
    # CLAUDE_PROJECT_DIR 우선. cwd 는 편집 대상 위치로 잡힐 수 있어 폴백으로만.
    return os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()


def short_sid(data):
    return (data.get("session_id", "") or "")[:8]


def worklog_path(proj, day=None):
    day = day or datetime.date.today()
    return os.path.join(proj, "worklog", day.isoformat() + ".md")


def read(path):
    return open(path, encoding="utf-8").read() if os.path.exists(path) else ""


@contextmanager
def locked(path):
    """같은 worklog 에 여러 세션이 동시에 쓰므로 읽고-판단하고-쓰기를 파일 잠금으로 묶는다.
    yield 하는 핸들은 a+ 모드: read 전 seek(0), write 는 항상 끝에 붙는다."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a+", encoding="utf-8") as f:
        if fcntl:
            fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield f
        finally:
            f.flush()
            if fcntl:
                fcntl.flock(f, fcntl.LOCK_UN)


def append(path, text):
    with locked(path) as f:
        f.write(text)


def worker_name(proj):
    """WORKLOG_AUTHOR / HFK_WORKER(각자 ~/.claude/settings.json env) → git user.name → 맥 사용자 전체 이름."""
    for key in ("WORKLOG_AUTHOR", "HFK_WORKER"):
        name = (os.environ.get(key) or "").strip()
        if name:
            return name
    for cmd in (["git", "-C", proj, "config", "user.name"], ["id", "-F"]):
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=3).stdout.strip()
            if out:
                return out
        except Exception:
            pass
    return ""


def has_header(text, sid):
    return bool(sid) and re.search(rf"^## session:{re.escape(sid)}\b", text, re.M) is not None


def header_template(sid, name):
    return (f"## session:{sid} — {name or '<작업자 이름>'}\n"
            "- 목적/왜: ...\n- 무엇을: ...\n")


def log_line(tool, what, sid):
    now = datetime.datetime.now().strftime("%H:%M")
    return f"- {now} [{tool}] {what}  (session:{sid})\n"


def needs_result(text, sid):
    """이 세션의 마지막 자동 기록이 마지막 결과(sid)/중간(sid) 줄보다 뒤에 있으면 True.
    자정을 넘긴 세션은 호출하는 쪽에서 어제+오늘 파일을 이어 붙여 넘긴다."""
    if not sid:
        return False
    last_log = last_result = -1
    for i, line in enumerate(text.splitlines()):
        if re.match(rf"- \d\d:\d\d \[.+\(session:{re.escape(sid)}\)\s*$", line):
            if WITH_RESULT not in line:
                last_log = i
        elif re.match(rf"- (결과|중간)\({re.escape(sid)}\)\s*:", line):
            last_result = i
    return last_log > last_result
