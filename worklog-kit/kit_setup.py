#!/usr/bin/env python3
"""키트 설치의 공통 단계: 안내 파일 두기 + .claude/settings.json 에 훅 합치기. install.sh(맥)·install.ps1(윈도우)가 부른다.

  python3 kit_setup.py <내려받은 폴더> --launcher python3                 # 맥
  py -3   kit_setup.py <내려받은 폴더> --launcher "py -3" --abs-path        # 윈도우

- 현재 폴더(프로젝트)에서 실행한다. 훅 파일 복사는 설치 스크립트가 먼저 끝내 둔다
- worklog/README.md, memory/README.md 는 내용이 다르면 백업 후 교체. memory/MEMORY.md 는 없을 때만 만든다(내 규칙 목록이라 덮지 않음)
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
    ("UserPromptSubmit", None, "feedback_capture.py"),
    ("PreToolUse", "Edit|Write|MultiEdit", "pre_edit_gate.py"),
    ("PostToolUse", "Edit|Write|MultiEdit|NotebookEdit|Bash|mcp__.*", "post_action_log.py"),
    ("Stop", None, "stop_worklog.py"),
]
INDEX_HEAD = ("# 내 규칙 목록\n\n"
              "Claude 가 내 피드백을 규칙 파일로 저장할 때마다 여기에 한 줄씩 붙습니다. 작성 기준은 README.md 를 보세요.\n\n")


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
    say(f"{p} 에 훅 {len(WANT)}개(업무일지 4 + 피드백 2)를 등록했습니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
