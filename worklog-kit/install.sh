#!/bin/bash
# Claude Code 업무일지(worklog) + 내 규칙(memory) + 내 자료(자료) 키트 설치 · 맥용 (윈도우는 install.ps1)
#   프로젝트 폴더에서:  curl -fsSL https://thehfk.github.io/hfk-ai-bss/worklog-kit/install.sh | bash
#
# 하는 일
#   1) .claude/hooks/worklog/ 에 훅 파일 9개를 받는다
#   2) worklog/README.md · memory/README.md · 자료/README.md(작성 기준)를 둔다. 이미 있고 내용이 다르면 백업 후 교체
#      memory/MEMORY.md(내 규칙 목록)는 없을 때만 만든다
#   3) .claude/settings.json 에 훅 8개(업무일지 4 + 규칙 2 + 자료 2)를 합친다. 기존 설정은 백업하고, 내 다른 설정은 건드리지 않는다
#   2·3 은 kit_setup.py 가 한다(윈도우 설치와 같은 코드)
#   다시 실행하면 최신 키트로 업데이트된다(기록·규칙은 그대로)
#
# 정본: hfk-workspace scripts/worklog_kit/ (여기 배포본을 직접 고치지 말 것)
set -euo pipefail

BASE="${WORKLOG_KIT_BASE:-https://thehfk.github.io/hfk-ai-bss/worklog-kit}"
DIR="$(pwd)"
HOOKS=(worklog_common.py pre_edit_gate.py post_action_log.py stop_worklog.py session_start.py feedback_capture.py feedback_session.py reference_capture.py reference_session.py)

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
for f in worklog-README.md memory-README.md library-README.md kit_setup.py; do
  curl -fsSL "$BASE/$f" -o "$TMP/$f"
done
for f in "${HOOKS[@]}" kit_setup.py; do
  python3 -c "import sys; compile(open(sys.argv[1], encoding='utf-8').read(), sys.argv[1], 'exec')" "$TMP/${f}"
done

mkdir -p .claude/hooks/worklog
cp "${HOOKS[@]/#/$TMP/}" .claude/hooks/worklog/
rm -rf .claude/hooks/worklog/__pycache__

python3 "$TMP/kit_setup.py" "$TMP" --launcher python3

NAME="$(git config user.name 2>/dev/null || true)"
[ -z "$NAME" ] && NAME="$(id -F 2>/dev/null || true)"

say ""
say "설치 완료: $DIR"
say "  - 훅: .claude/hooks/worklog/"
say "  - 기록: worklog/날짜.md  (작성 기준: worklog/README.md)"
say "  - 규칙: memory/MEMORY.md  (작성 기준: memory/README.md)"
say "  - 자료: 자료/목록.md  (작성 기준: 자료/README.md)"
say "  - 기록에 쓰일 이름: ${NAME:-'(없음, 첫 수정 때 Claude 가 물어봅니다)'}"
say ""
say "다음 단계: 이 폴더에서 Claude Code 를 새로 열어 주세요(이미 열려 있으면 껐다 켜기)."
say "처음 열 때 이 폴더를 믿을지 묻는 창이 뜨면 동의를 눌러야 기록이 시작됩니다."
