#!/usr/bin/env python3
"""키트 설치의 공통 단계: 안내 파일 두기 + .claude/settings.json 에 훅 합치기. install.sh(맥)·install.ps1(윈도우)가 부른다.

  python3 kit_setup.py <내려받은 폴더> --launcher python3                 # 맥
  py -3   kit_setup.py <내려받은 폴더> --launcher "py -3" --abs-path        # 윈도우

- 현재 폴더(프로젝트)에서 실행한다. 훅 파일 복사는 설치 스크립트가 먼저 끝내 둔다
- CLAUDE.md 끝에 키트 칸(BLOCK)을 넣거나 새 내용으로 바꾼다. 표시줄 사이만 고치고 내가 쓴 줄은 건드리지 않는다.
  코워크는 폴더 훅을 돌리지 않으므로(2026-10-28 시험) 훅이 하던 일을 이 칸에 글로 적어 둔다.
  코워크 프로젝트 지침에 'CLAUDE.md 를 먼저 읽어 줘' 한 줄만 넣으면 같은 방식으로 쌓인다. 클로드 코드에서는 훅과 겹쳐도 해가 없다
- worklog/README.md, memory/README.md, 자료/README.md 는 내용이 다르면 백업 후 교체. memory/MEMORY.md 는 없을 때만 만든다(내 규칙 목록이라 덮지 않음)
- settings.json: 기존 파일은 백업하고, .claude/hooks/worklog/ 가 들어간 예전 키트 항목만 지운 뒤 새로 넣는다(재실행 = 업데이트, 중복 없음)
- --abs-path: 훅 명령에 $CLAUDE_PROJECT_DIR 대신 이 폴더의 절대경로(슬래시)를 적는다.
  윈도우는 Git Bash 가 없으면 훅을 PowerShell 로 돌리는데, 거기선 $CLAUDE_PROJECT_DIR 가 풀린다는 보장이 없다.
  그래서 '파이썬이름 "절대경로"' 꼴로 bash·PowerShell 양쪽에서 같은 뜻이 되게 한다. 폴더를 옮기면 다시 설치

정본: hfk-workspace scripts/worklog_kit/ (배포본을 직접 고치지 말 것)
"""
import argparse, filecmp, json, os, shutil, sys, time

HOOK_DIR = ".claude/hooks/worklog"
WANT = [  # (이벤트, matcher, 훅 파일) — 같은 이벤트에 여럿이면 적힌 순서대로 돈다
    ("SessionStart", None, "session_start.py"),
    ("SessionStart", None, "feedback_session.py"),
    ("SessionStart", None, "reference_session.py"),
    ("UserPromptSubmit", None, "feedback_capture.py"),
    ("UserPromptSubmit", None, "reference_capture.py"),
    ("PreToolUse", "Edit|Write|MultiEdit", "pre_edit_gate.py"),
    ("PostToolUse", "Edit|Write|MultiEdit|NotebookEdit|Bash|mcp__.*", "post_action_log.py"),
    ("Stop", None, "stop_worklog.py"),
]
INDEX_HEAD = ("# 내 규칙 목록\n\n"
              "Claude 가 내 피드백을 규칙 파일로 저장할 때마다 여기에 한 줄씩 붙습니다. 작성 기준은 README.md 를 보세요.\n\n")
BLOCK_START = "<!-- hfk-kit:start (설치 키트가 관리하는 칸입니다. 고치려면 키트를 다시 설치하세요) -->"
BLOCK_END = "<!-- hfk-kit:end -->"
BLOCK = [
    "## 기록·규칙·자료 남기기",
    "클로드 코드에서는 훅이 자동으로 하고, 코워크에서는 아래대로 직접 합니다. 이미 적혀 있으면 겹쳐 쓰지 않습니다.",
    "- 일을 시작하면 `memory/MEMORY.md`(내 규칙)와 `자료/목록.md`(내 자료)를 먼저 읽고 따릅니다",
    "- 내가 '다음부터·하지 마·기억해'처럼 고쳐 주면, 다음에도 지킬 규칙일 때만 `memory/feedback_주제.md` 로 저장하고 목록에 한 줄 붙입니다(형식은 `memory/README.md`)",
    "- 내가 링크나 파일을 건네면 `자료/목록.md` 에 없을 때 한 줄 붙이고, 열어 본 뒤 '무엇·언제' 칸을 채웁니다(형식은 `자료/README.md`)",
    "- 파일을 고치기 전에 `worklog/오늘날짜.md` 에 목적을 적고, 끝나면 결과를 적습니다(형식은 `worklog/README.md`)",
]


def ensure_claude_md(stamp, say):
    """CLAUDE.md 의 키트 칸을 넣거나 바꾼다. 원래 줄바꿈(CRLF/LF)을 따른다. 바뀐 게 없으면 손대지 않는다."""
    p = "CLAUDE.md"
    old = open(p, encoding="utf-8-sig", newline="").read() if os.path.exists(p) else ""
    nl = "\r\n" if "\r\n" in old else "\n"
    block = nl.join([BLOCK_START] + BLOCK + [BLOCK_END])
    i, j = old.find(BLOCK_START.split(" (")[0]), old.find(BLOCK_END)
    if i != -1 and j != -1 and j > i:
        new = old[:i] + block + old[j + len(BLOCK_END):]
    else:
        new = (old.rstrip("\r\n") + nl + nl if old.strip() else "") + block + nl
    if new == old:
        return
    if old:
        shutil.copy(p, f"{p}.bak-{stamp}")
        say(f"기존 {p} 를 {p}.bak-{stamp} 로 백업하고 끝에 키트 칸을 넣었습니다.")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(new)


def place(src, dst, stamp, say):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst) and not filecmp.cmp(src, dst, shallow=False):
        shutil.copy(dst, f"{dst}.bak-{stamp}")
        say(f"기존 {dst} 를 {dst}.bak-{stamp} 로 백업했습니다.")
    shutil.copy(src, dst)


def hook_command(launcher, name, abs_path):
    if abs_path:
        root = os.path.abspath(os.getcwd()).replace("\\", "/")
        return f'{launcher} "{root}/{HOOK_DIR}/{name}"'
    return f'{launcher} "$CLAUDE_PROJECT_DIR/{HOOK_DIR}/{name}"'


def merge_settings(s, launcher, abs_path):
    hooks = s.setdefault("hooks", {})
    events = dict.fromkeys(e for e, _, _ in WANT)
    for event in events:
        kept = []
        for e in hooks.get(event, []):
            hs = [h for h in e.get("hooks", []) if f"{HOOK_DIR}/" not in h.get("command", "").replace("\\", "/")]
            if hs:
                e["hooks"] = hs
                kept.append(e)
        for ev, matcher, name in WANT:
            if ev != event:
                continue
            entry = {"hooks": [{"type": "command", "command": hook_command(launcher, name, abs_path)}]}
            if matcher:
                entry = {"matcher": matcher, **entry}
            kept.append(entry)
        hooks[event] = kept
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--launcher", default="python3")
    ap.add_argument("--abs-path", action="store_true")
    args = ap.parse_args()
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    say = print
    stamp = time.strftime("%Y%m%d-%H%M%S")

    place(os.path.join(args.src, "worklog-README.md"), os.path.join("worklog", "README.md"), stamp, say)
    place(os.path.join(args.src, "memory-README.md"), os.path.join("memory", "README.md"), stamp, say)
    place(os.path.join(args.src, "library-README.md"), os.path.join("자료", "README.md"), stamp, say)
    ensure_claude_md(stamp, say)
    index = os.path.join("memory", "MEMORY.md")
    if not os.path.exists(index):
        with open(index, "w", encoding="utf-8", newline="\n") as f:
            f.write(INDEX_HEAD)

    p = os.path.join(".claude", "settings.json")
    s = {}
    if os.path.exists(p):
        raw = open(p, encoding="utf-8-sig").read()
        if raw.strip():
            try:
                s = json.loads(raw)
            except Exception:
                say(f"{p} 가 올바른 JSON 이 아니라 손대지 않았습니다. 고친 뒤 다시 실행해 주세요.")
                return 1
        shutil.copy(p, f"{p}.bak-{stamp}")
        say(f"기존 설정을 {p}.bak-{stamp} 로 백업했습니다.")
    merge_settings(s, args.launcher, args.abs_path)
    os.makedirs(".claude", exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(s, f, ensure_ascii=False, indent=2)
        f.write("\n")
    say(f"{p} 에 훅 {len(WANT)}개(업무일지 4 + 규칙 2 + 자료 2)를 등록했습니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
