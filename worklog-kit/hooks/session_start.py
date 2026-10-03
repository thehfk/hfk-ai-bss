#!/usr/bin/env python3
"""세션 시작 시 업무일지 규칙(세션 ID·작업자 포함) + 오늘 업무일지 + 진척도(PROGRESS.md 가 있으면)를 보여준다."""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import read_hook_input, project_dir, short_sid, read, worker_name, header_template


def main():
    data = read_hook_input()
    proj = project_dir(data)
    sid = short_sid(data)
    today = datetime.date.today().isoformat()
    name = worker_name(proj)
    parts = [f"[업무일지 규칙] 파일 편집 전, worklog/{today}.md 끝에 이 세션 헤더를 먼저 붙이세요"
             " (기준: worklog/README.md). 헤더가 없으면 편집이 차단되고, 편집·실행 뒤 결과 줄이 없으면 턴 종료가 한 번 막힙니다.\n"
             + header_template(sid or "<세션ID 앞8자>", name)
             + ("" if name else "작업자 이름을 모르니 첫 편집 전에 사용자에게 물어보세요.\n")]
    wl = os.path.join(proj, "worklog", today + ".md")
    if os.path.exists(wl):
        parts.append("── 오늘 업무일지 ──\n" + read(wl)[-1000:])
    pg = os.path.join(proj, "PROGRESS.md")
    if os.path.exists(pg):
        parts.append("── 진척도(PROGRESS.md) ──\n" + read(pg)[:800])
    print("\n\n".join(parts))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
