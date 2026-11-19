#!/usr/bin/env python3
"""세션 시작 때 memory/MEMORY.md(내가 정한 규칙 목록)를 Claude 에게 보여준다 (SessionStart).

- 목록만 보여주고, 각 규칙 파일은 관련 작업을 할 때 Claude 가 열어 읽는다(목록이 길어져도 가볍게)
- 목록이 없으면 아무것도 출력하지 않는다
- 규칙을 쌓는 쪽은 feedback_capture.py(UserPromptSubmit)
- 어떤 예외든 조용히 통과(fail-safe)
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import read_hook_input, project_dir, read

LIMIT = 4000  # 목록이 이보다 길면 앞부분만(정리할 때가 됐다는 신호도 같이)


def main():
    data = read_hook_input()
    index = read(os.path.join(project_dir(data), "memory", "MEMORY.md")).strip()
    entries = [l for l in index.splitlines() if re.match(r"\s*[-*]\s*\[", l)]
    if not entries:
        return
    body = "\n".join(entries)
    note = ""
    if len(body) > LIMIT:
        body = body[:LIMIT].rsplit("\n", 1)[0]
        note = "\n(목록이 길어 앞부분만 보입니다. 사용자에게 겹치는 규칙을 합치자고 한 번 제안하세요.)"
    print(f"── 내 규칙 (memory/MEMORY.md, {len(entries)}개) ──\n"
          "사용자가 이 프로젝트에서 정한 규칙입니다. 관련 작업을 시작하기 전에 해당 파일을 열어 따르세요."
          " 규칙과 다르게 해야 하면 먼저 묻습니다.\n" + body + note)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
