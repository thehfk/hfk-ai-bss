#!/bin/bash
# Claude Code 업무일지(worklog) 키트 설치
#   프로젝트 폴더에서:  curl -fsSL https://thehfk.github.io/hfk-ai-bss/worklog-kit/install.sh | bash
#
# 하는 일
#   1) .claude/hooks/worklog/ 에 훅 5개를 받는다
#   2) worklog/README.md(작성 기준)를 둔다. 이미 있고 내용이 다르면 백업 후 교체
#   3) .claude/settings.json 에 훅 4개를 합친다. 기존 설정은 백업하고, 내 다른 설정은 건드리지 않는다
#   다시 실행하면 최신 키트로 업데이트된다(기록은 그대로)
#
# 정본: hfk-workspace scripts/worklog_kit/ (여기 배포본을 직접 고치지 말 것)
set -euo pipefail

BASE="${WORKLOG_KIT_BASE:-https://thehfk.github.io/hfk-ai-bss/worklog-kit}"
DIR="$(pwd)"
HOOKS=(worklog_common.py pre_edit_gate.py post_action_log.py stop_worklog.py session_start.py)

say() { printf '%s\n' "$*"; }

if [ "$DIR" = "$HOME" ] || [ "$DIR" = "/" ]; then
  say "홈 폴더가 아니라 작업하는 프로젝트 폴더 안에서 실행해 주세요."
  say "예: cd ~/Documents/내프로젝트 후 다시 실행"
  exit 1
fi

if ! python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' >/dev/null 2>&1; then
  say "python3 가 필요합니다. 터미널에서 아래를 실행해 설치한 뒤 다시 실행해 주세요."
  say "  xcode-select --install"
  exit 1
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

say "키트 내려받는 중… ($BASE)"
for f in "${HOOKS[@]}"; do
  curl -fsSL "$BASE/hooks/$f" -o "$TMP/$f"
done
curl -fsSL "$BASE/worklog-README.md" -o "$TMP/README.md"
for f in "${HOOKS[@]}"; do
  python3 -c "import sys; compile(open(sys.argv[1], encoding='utf-8').read(), sys.argv[1], 'exec')" "$TMP/$f"
done

mkdir -p .claude/hooks/worklog worklog
cp "${HOOKS[@]/#/$TMP/}" .claude/hooks/worklog/
rm -rf .claude/hooks/worklog/__pycache__

STAMP="$(date +%Y%m%d-%H%M%S)"
if [ -f worklog/README.md ] && ! cmp -s worklog/README.md "$TMP/README.md"; then
  cp worklog/README.md "worklog/README.md.bak-$STAMP"
  say "기존 worklog/README.md 를 worklog/README.md.bak-$STAMP 로 백업했습니다."
fi
cp "$TMP/README.md" worklog/README.md

python3 - "$STAMP" <<'PY'
import json, os, shutil, sys
stamp = sys.argv[1]
p = ".claude/settings.json"
s = {}
if os.path.exists(p):
    raw = open(p, encoding="utf-8").read()
    if raw.strip():
        try:
            s = json.loads(raw)
        except Exception:
            print(f"{p} 가 올바른 JSON 이 아니라 손대지 않았습니다. 고친 뒤 다시 실행해 주세요.")
            sys.exit(1)
    shutil.copy(p, f"{p}.bak-{stamp}")
    print(f"기존 설정을 {p}.bak-{stamp} 로 백업했습니다.")

def cmd(name):
    return f'python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/worklog/{name}"'

WANT = {
    "SessionStart": (None, "session_start.py"),
    "PreToolUse": ("Edit|Write|MultiEdit", "pre_edit_gate.py"),
    "PostToolUse": ("Edit|Write|MultiEdit|NotebookEdit|Bash|mcp__.*", "post_action_log.py"),
    "Stop": (None, "stop_worklog.py"),
}
hooks = s.setdefault("hooks", {})
for event, (matcher, name) in WANT.items():
    entries = hooks.setdefault(event, [])
    # 예전 키트 항목은 지우고 새로 넣는다(재실행 = 업데이트, 중복 없음)
    kept = []
    for e in entries:
        hs = [h for h in e.get("hooks", []) if ".claude/hooks/worklog/" not in h.get("command", "")]
        if hs:
            e["hooks"] = hs
            kept.append(e)
    entry = {"hooks": [{"type": "command", "command": cmd(name)}]}
    if matcher:
        entry = {"matcher": matcher, **entry}
    kept.append(entry)
    hooks[event] = kept

os.makedirs(".claude", exist_ok=True)
with open(p, "w", encoding="utf-8") as f:
    json.dump(s, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"{p} 에 업무일지 훅 4개를 등록했습니다.")
PY

NAME="$(git config user.name 2>/dev/null || true)"
[ -z "$NAME" ] && NAME="$(id -F 2>/dev/null || true)"

say ""
say "설치 완료: $DIR"
say "  - 훅: .claude/hooks/worklog/"
say "  - 기록: worklog/날짜.md  (작성 기준: worklog/README.md)"
say "  - 기록에 쓰일 이름: ${NAME:-'(없음, 첫 수정 때 Claude 가 물어봅니다)'}"
say ""
say "다음 단계: 이 폴더에서 Claude Code 를 새로 열어 주세요(이미 열려 있으면 껐다 켜기)."
say "처음 열 때 이 폴더를 믿을지 묻는 창이 뜨면 동의를 눌러야 기록이 시작됩니다."
