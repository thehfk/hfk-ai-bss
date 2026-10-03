#!/usr/bin/env python3
"""턴을 끝내기 전에 이 세션의 worklog 결과 줄을 요구한다 (Stop 훅).

- 이 세션에 자동 기록(편집·실행)이 있는데, 그 뒤에 `- 결과(<ID>):` 또는 `- 중간(<ID>):` 줄이 없으면
  한 번 막고 Claude 에게 결과를 쓰게 한다. 조회·대화만 한 턴은 그냥 통과
- 헤더 없이 실행 기록만 있는 세션(Bash·MCP 로만 일한 경우)은 헤더도 함께 요구
- 자정을 넘긴 세션: 어제 파일 + 오늘 파일을 이어서 본다(23:59 기록을 00:01 Stop 이 놓치지 않게)
- stop_hook_active 면 통과(같은 턴에 두 번 막지 않는다 = 무한 반복 방지)
- 어떤 예외든 통과(fail-safe)
"""
import sys, os, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import (read_hook_input, project_dir, short_sid, worklog_path, read, worker_name,
                             has_header, header_template, needs_result, CHECKLIST)


def main():
    data = read_hook_input()
    if data.get("stop_hook_active"):
        return
    sid = short_sid(data)
    if not sid:
        return
    proj = project_dir(data)
    today = datetime.date.today()
    text = read(worklog_path(proj, today - datetime.timedelta(days=1))) + "\n" + read(worklog_path(proj, today))
    if not needs_result(text, sid):
        return
    reason = [f"[업무일지] 이 세션(session:{sid})에서 파일 편집이나 실행이 있었는데 결과 기록이 없습니다.",
              f"턴을 마치기 전에 worklog/{today.isoformat()}.md 끝에 아래 형식으로 한 줄 덧붙이세요."]
    if not has_header(text, sid):
        reason.append("이 세션 헤더도 없으니 헤더부터 붙이세요(목적이 불분명하면 대화 내용 기준으로 쓰고 '추정'이라고 표시):\n"
                      + header_template(sid, worker_name(proj)))
    reason += [f"- 결과({sid}): ...   ← 이번 작업이 끝났을 때",
               f"- 중간({sid}): ...   ← 사용자 답을 기다리는 등 아직 진행 중일 때(지금까지 한 것 + 남은 것)",
               "", CHECKLIST,
               "기록은 Bash heredoc(cat >> worklog/…) 이나 Edit 로 붙이면 됩니다. 이미 이 턴 앞에서 쓴 내용과 겹치면 바뀐 것만 짧게."]
    print(json.dumps({"decision": "block", "reason": "\n".join(reason)}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
