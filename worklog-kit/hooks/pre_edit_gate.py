#!/usr/bin/env python3
"""업무일지 게이트(PreToolUse: Edit|Write|MultiEdit): 편집 전 이 세션의 목적이 worklog에 있는지 검사.
- worklog/ 자체 편집은 항상 허용(목적을 적어야 하니까)
- 오늘 worklog에 이 세션의 `## session:<ID>` 헤더가 없으면 편집 차단(exit 2)
  (다른 사람·다른 세션 헤더에 묻어 통과하지 않도록 세션 ID로 본다)
- 자정을 넘긴 세션은 어제 파일 헤더도 인정하고, 오늘 파일에 이어짐 헤더를 자동으로 단다
- 편집 기록 자체는 성공한 편집만 남도록 PostToolUse(post_action_log.py)가 맡는다
- 어떤 예외든 발생하면 '허용'으로 폴백(fail-safe, 사고 방지)
"""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import (read_hook_input, project_dir, short_sid, worklog_path, read, locked,
                             worker_name, has_header, header_template, CHECKLIST)


def main():
    data = read_hook_input()
    ti = data.get("tool_input", {}) or {}
    proj = project_dir(data)
    sid = short_sid(data)
    path = ti.get("file_path") or ti.get("path") or ""
    if path:
        path = os.path.abspath(os.path.join(data.get("cwd") or proj, os.path.expanduser(path)))
        try:
            if os.path.commonpath([path, os.path.join(os.path.abspath(proj), "worklog")]) == os.path.join(os.path.abspath(proj), "worklog"):
                return 0
        except ValueError:
            pass
    today = datetime.date.today()
    wl = worklog_path(proj, today)
    if not sid:
        # 세션 ID를 못 받은 예외 상황: 옛 방식(오늘 파일에 '목적'이 있는지)으로 판정
        if "목적" in read(wl):
            return 0
        sys.stderr.write(f"[업무일지] worklog/{today.isoformat()}.md 에 작업 목적을 먼저 적어 주세요.\n")
        return 2
    with locked(wl) as f:
        f.seek(0)
        if has_header(f.read(), sid):
            return 0
        yday = today - datetime.timedelta(days=1)
        if has_header(read(worklog_path(proj, yday)), sid):
            f.write(f"\n## session:{sid} — {worker_name(proj) or '?'} (어제에서 이어짐)\n"
                    f"- 목적/왜: worklog/{yday.isoformat()}.md 같은 세션 참고\n")
            return 0
    name = worker_name(proj)
    msg = ("[업무일지] 편집 전 이 세션의 '작업 목적'을 먼저 업무일지에 적어야 합니다.\n"
           f"→ worklog/{today.isoformat()}.md 끝에 아래 헤더를 붙인 뒤 다시 시도하세요.\n"
           "  목적이 대화에서 분명하지 않으면 지어내지 말고 사용자에게 먼저 물어보세요.\n\n"
           + header_template(sid, name) + "\n" + CHECKLIST + "\n")
    if not name:
        msg += "\n작업자 이름을 모르면 사용자에게 물어보세요(~/.claude/settings.json env 의 WORKLOG_AUTHOR 로 고정 가능).\n"
    sys.stderr.write(msg)
    return 2  # block


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail-safe: 절대 락아웃 안 함
