#!/usr/bin/env python3
"""세션 시작 시 업무일지 규칙(세션 ID·작업자 포함) + 오늘 업무일지 + 진척도(PROGRESS.md 가 있으면)
+ 최근 24시간 Aside 업무 세션(있으면)을 보여준다."""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import read_hook_input, project_dir, short_sid, read, worker_name, header_template


def aside_recent(proj, days=1, limit=8):
    """Aside 브라우저 에이전트가 최근에 한 업무 세션. VSCode 쪽 훅은 Aside 작업을 못 보니 여기서 보여준다.
    판정은 export_aside_sessions.recent_work 와 같다(개인·루틴·CLI 임시 세션 제외). 읽기 전용."""
    import glob
    if not os.path.isdir(os.path.expanduser("~/.aside/u/0/sessions")):
        return ""
    sys.path.insert(0, os.path.join(proj, "scripts"))
    from export_aside_sessions import recent_work
    rows = recent_work(days)
    if not rows:
        return ""
    logged = "".join(read(f) for f in sorted(glob.glob(os.path.join(proj, "worklog", "*.md")))[-2:])
    rows = rows[::-1]
    lines = []
    for s in rows[:limit]:
        mark = "기록됨" if f"aside:{s['sid'][:8]}" in logged else "업무일지 미기록"
        lines.append(f"- {datetime.datetime.fromtimestamp(s['mtime']):%m-%d %H:%M} {s['title'][:50]} [{mark}] (aside:{s['sid'][:8]})")
    more = f"\n  …외 {len(rows) - limit}건" if len(rows) > limit else ""
    return ("── Aside 최근 24시간 (업무 추정) ──\n" + "\n".join(lines) + more
            + "\n  주간 점검: python3 scripts/export_aside_sessions.py --unlogged 7 · 이어가기: aside session resume <ID>")


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
    try:
        ar = aside_recent(proj)
        if ar:
            parts.append(ar)
    except Exception:
        pass
    print("\n\n".join(parts))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
