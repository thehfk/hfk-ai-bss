#!/usr/bin/env python3
"""세션 시작 때 자료/목록.md(내가 건넨 링크·파일)의 최근 줄을 Claude 에게 보여준다 (SessionStart).

- 최근 15줄만 보여주고, 나머지는 필요할 때 Claude 가 목록 파일을 검색하게 한다(목록이 길어져도 가볍게)
- '무엇' 칸이 빈 줄이 있으면 그 수를 알려 채울 기회를 준다
- 목록이 없으면 아무것도 출력하지 않는다. 쌓는 쪽은 reference_capture.py(UserPromptSubmit)
- 어떤 예외든 조용히 통과(fail-safe)
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import read_hook_input, project_dir, read

RECENT = 15


def main():
    data = read_hook_input()
    rows = [l for l in read(os.path.join(project_dir(data), "자료", "목록.md")).splitlines() if re.match(r"\s*-\s", l)]
    if not rows:
        return
    blank = sum("무엇: ?" in r for r in rows)
    print(f"── 내 자료 (자료/목록.md, {len(rows)}개 중 최근 {min(RECENT, len(rows))}개) ──\n"
          "사용자가 지금까지 건넨 링크·파일입니다. 관련 작업이면 답하기 전에 이 목록부터 찾아보세요"
          "(전체는 자료/목록.md 를 검색).\n" + "\n".join(rows[-RECENT:])
          + (f"\n('무엇' 칸이 빈 자료 {blank}개. 그 자료를 열어 보게 되면 채우세요.)" if blank else ""))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
