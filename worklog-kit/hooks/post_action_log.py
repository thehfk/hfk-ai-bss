#!/usr/bin/env python3
"""무언가를 바꾼 실행을 worklog에 한 줄 남긴다 (PostToolUse: Edit|Write|MultiEdit|NotebookEdit|Bash|mcp__.*).

PostToolUse 는 성공한 호출에만 돈다. 그래서 실패한 편집은 기록되지 않는다.
- Edit/Write: 파일 경로(worklog/ 자체는 제외)
- Bash: 명령을 ; && || | 줄바꿈으로 나눠 조각마다 판정. 쓰기 조각만 남긴다
    git commit/push 등 · 스크립트(.py/.sh) 실행 · launchctl · crontab · curl 쓰기 요청 ·
    rm/mv/cp/mkdir/chmod/tee/sed -i · 파일로 리다이렉트(>)
  조회성 스크립트(fetch_·audit_·check_ …)는 --send/--apply/--fix 같은 쓰기 옵션이 있을 때만,
  --dry-run 이 붙은 조각은 그 조각만 뺀다. /tmp 같은 임시 경로만 건드리면 뺀다.
  heredoc 본문과 따옴표 문자열은 판정에서 빼고(결과 줄에 적힌 글자를 실행으로 오인하지 않게),
  bash -c '…' 안쪽은 따로 판정한다
- MCP: 도구 이름을 _ 로 나눈 단어 중 쓰기 동사가 있을 때만(get_updates 같은 조회는 제외)
- 명령 원문은 남기지 않는다. 프로그램·하위명령·스크립트 경로·옵션 이름만 남긴다(값은 버림).
  worklog 는 레포에 커밋되고, 그 레포가 공개일 수도 있다
- 같은 명령이 결과(<ID>)/중간(<ID>) 줄도 썼으면 [결과 함께] 표시를 붙여 Stop 훅이 다시 막지 않게 한다
- 어떤 예외든 조용히 통과(fail-safe)
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worklog_common import (read_hook_input, project_dir, short_sid, worklog_path, append,
                             log_line, WITH_RESULT)

HEREDOC = re.compile(r"<<-?\s*['\"]?(\w+)['\"]?[^\n]*\n.*?\n\s*\1\b", re.S)
QUOTED = re.compile(r"'[^']*'|\"(?:[^\"\\]|\\.)*\"")
NESTED_SH = re.compile(r"\b(?:ba|z)?sh\s+-c\s+('([^']*)'|\"((?:[^\"\\]|\\.)*)\")")
SPLIT = re.compile(r"&&|\|\||[;|\n]")
PY_PATH = re.compile(r"['\"]?[\w/.$~{}-]+\.py['\"]?")

PREFIXES = {"sudo", "time", "nohup", "command", "exec", "env", "caffeinate"}
GIT_WRITE = {"commit", "push", "reset", "revert", "rm", "mv", "merge", "rebase", "cherry-pick",
             "clean", "restore", "stash", "tag", "am", "apply"}
FILE_WRITE = {"rm", "mv", "cp", "mkdir", "rmdir", "chmod", "chown", "ln", "touch", "tee", "rsync", "unlink", "trash"}
LAUNCHCTL_WRITE = {"load", "unload", "bootstrap", "bootout", "kickstart", "enable", "disable", "remove", "submit"}
READONLY_SCRIPT = re.compile(r"(^|/)(fetch|audit|check|list|show|read|get|preview|find|search|lookup|count|diff|verify|parse|dump|inspect)_[\w-]*\.(py|sh)$")
WRITE_FLAG = re.compile(r"^--?(send|apply|fix|write|commit|execute|post|update|delete|publish|deploy|force|yes|confirm)\b")
TMP_PATH = re.compile(r"^(/tmp/|/private/tmp/|/private/var/folders/|/var/folders/|/dev/)")
SECRETISH = re.compile(r"(xox[a-z]-|sk-|ghp_|github_pat_|AIza|Bearer|Basic|://|@|[A-Za-z0-9+/_-]{32,})")
SENSITIVE_OPT = re.compile(r"^--?(password|passwd|pass|token|secret|key|api-key|apikey|auth|cookie|header|user|u|H|b|d|data[\w-]*|F|form)$", re.I)
MCP_WRITE = {"post", "reply", "send", "create", "update", "delete", "trash", "untrash", "add", "apply",
             "publish", "deploy", "share", "forward", "respond", "write", "edit", "set", "upload",
             "archive", "remove", "invite", "label", "unlabel", "mark", "unmark", "move", "copy",
             "cancel", "rename", "submit", "schedule", "pin", "unpin", "import", "connect", "batch"}


def code_only(cmd):
    cmd = HEREDOC.sub("<<EOF", cmd)
    # 따옴표로 감싼 .py 경로는 실행 대상이라 남긴다
    return QUOTED.sub(lambda m: m.group(0).strip("'\"") if PY_PATH.fullmatch(m.group(0)) else "''", cmd)


def is_tmp(p):
    p = os.path.expanduser(p)
    return bool(TMP_PATH.match(p)) or "/scratchpad/" in p


def safe_token(t):
    """경로·하위명령처럼 남겨도 되는 토큰만. 값·URL·비밀처럼 보이면 버린다."""
    if "=" in t or SECRETISH.search(t):
        return None
    return t


def flag_names(tokens):
    out, skip = [], False
    for t in tokens:
        if skip:
            skip = False
            continue
        if t.startswith("-"):
            name = t.split("=", 1)[0]
            out.append(name)
            if SENSITIVE_OPT.match(name) and "=" not in t:
                skip = True  # 다음 토큰은 값
    return out


def classify(seg):
    """쓰기 조각이면 안전한 요약 문자열, 아니면 None."""
    toks = seg.split()
    # 리다이렉트 대상(파일로 쓰기)을 먼저 떼어 둔다
    redirects = []
    i = 0
    rest = []
    while i < len(toks):
        t = toks[i]
        m = re.match(r"^\d?(>>?)(.*)$", t)
        if m and not t.startswith(">&") and not re.match(r"^\d?>&", t):
            target = m.group(2) or (toks[i + 1] if i + 1 < len(toks) else "")
            if not m.group(2):
                i += 1
            if target and not is_tmp(target) and target != "''" and "worklog/" not in target:
                redirects.append(target)
        else:
            rest.append(t)
        i += 1
    toks = rest
    while toks and (re.match(r"^\w+=", toks[0]) or toks[0] in PREFIXES):
        toks = toks[1:]
    if not toks:
        return None
    prog = os.path.basename(toks[0])
    args = toks[1:]
    summary = None

    if re.search(r"--dry[-_]?run\b", " ".join(args)):
        return None
    if prog == "git":
        j = 0
        while j < len(args) and args[j].startswith("-"):
            j += 2 if args[j] in ("-C", "-c") else 1
        sub = args[j] if j < len(args) else ""
        if sub in GIT_WRITE and "--dry-run" not in args:
            summary = f"git {sub}"
    elif prog == "launchctl":
        if args and args[0] in LAUNCHCTL_WRITE:
            label = next((os.path.basename(a) for a in args[1:] if not a.startswith("-") and safe_token(a)), "")
            summary = f"launchctl {args[0]} {label}".strip()
    elif prog == "crontab":
        if args and args[0] not in ("-l",):
            summary = "crontab (설치)"
    elif prog == "curl":
        joined = " ".join(args)
        m = re.search(r"(?:-X|--request)\s*=?\s*(\w+)", joined, re.I)
        method = (m.group(1).upper() if m else "")
        if not method and re.search(r"(^|\s)(-d|--data[\w-]*|-F|--form|-T|--upload-file)\b", joined):
            method = "POST"
        if method in ("POST", "PUT", "PATCH", "DELETE"):
            host = next((re.sub(r"^\w+://([^/:@]+).*$", r"\1", a) for a in args if "://" in a), "?")
            summary = f"curl {method} {host}"
    elif prog in FILE_WRITE or (prog in ("sed", "perl") and any(a.startswith("-i") for a in args)):
        paths = [a for a in args if not a.startswith("-") and a != "''"]
        if prog in ("sed", "perl"):
            # 따옴표 없이 쓴 치환식(s/a/b/ 등)은 경로가 아니다. 따옴표 친 식은 code_only 가 이미 지웠다
            paths = [p for p in paths if not re.match(r"^[sy]([^\w\s]).*\1", p) and not p.startswith("-e")]
        if paths and all(is_tmp(p) for p in paths):
            return None
        shown = [p for p in (safe_token(p) for p in paths[:4]) if p]
        summary = " ".join([prog] + shown)
    else:
        # 스크립트 실행: python3 x.py / bash x.sh / ./x.py / ~/venv/bin/python3 x.py
        script = None
        if re.match(r"^(python[\d.]*|bash|sh|zsh|node|uv|ruby)$", prog):
            cand = [a for a in args if not a.startswith("-")]
            if prog == "uv" and cand[:1] == ["run"]:
                cand = cand[1:]
            script = next((a for a in cand if re.search(r"\.(py|sh|js|rb)$", a)), None)
        elif re.search(r"\.(py|sh)$", toks[0]):
            script = toks[0]
        if script and not is_tmp(script):
            flags = flag_names(args)
            if READONLY_SCRIPT.search(script) and not any(WRITE_FLAG.match(f) for f in flags):
                script = None
            if script:
                rel = re.sub(r"^.*?/((scripts|\.claude)/)", r"\1", os.path.expanduser(script))
                summary = " ".join([os.path.basename(toks[0]), rel] + flags[:6])

    if redirects:
        tgt = " ".join(t for t in (safe_token(r) for r in redirects) if t)
        summary = f"{summary} > {tgt}" if summary else (f"> {tgt}" if tgt else None)
    return summary


INLINE_PY = re.compile(r"\bpython[\d.]*\s+(-\s*<<-?\s*['\"]?(\w+)['\"]?[^\n]*\n(.*?)\n\s*\2\b|-c\s+('[^']*'|\"(?:[^\"\\\\]|\\\\.)*\"))", re.S)
INLINE_WRITE = re.compile(
    r"open\([^)]*,\s*(mode\s*=\s*)?['\"](w|a|x|r\+)b?\+?['\"]|\.write_(text|bytes)\(|json\.dump\(|os\.(remove|unlink|rename|replace|makedirs)\("
    r"|shutil\.(copy|move|rmtree)|requests\.(post|put|patch|delete)\(|\.(post|put|patch|delete)\(|chat_(postMessage|update|delete|scheduleMessage)"
    r"|\bsubprocess\.|\.to_csv\(|\.save\(|smtplib|send_message\(")


def inline_python(cmd):
    """python3 - <<'PY' … PY / python3 -c '…' 안에 파일 쓰기·전송 코드가 보이면 요약 한 줄."""
    for m in INLINE_PY.finditer(cmd):
        body = m.group(3) if m.group(3) is not None else (m.group(4) or "")
        if INLINE_WRITE.search(body):
            return "python3 (인라인 코드: 파일 쓰기·전송)"
    return None


def bash_summary(cmd, depth=0):
    parts = []
    s = inline_python(cmd)
    if s:
        parts.append(s)
    if depth < 2:
        for m in NESTED_SH.finditer(cmd):
            inner = m.group(2) if m.group(2) is not None else m.group(3)
            s = bash_summary(inner, depth + 1)
            if s:
                parts.append(s)
    for seg in SPLIT.split(code_only(cmd)):
        if seg.strip():
            s = classify(seg)
            if s:
                parts.append(s)
    if not parts:
        return None
    one = " ; ".join(dict.fromkeys(parts))
    return one[:200] + ("…" if len(one) > 200 else "")


def mcp_is_write(tool):
    words = set(re.split(r"[_\W]+", tool.split("__")[-1].lower()))
    return bool(words & MCP_WRITE)


def main():
    data = read_hook_input()
    tool = data.get("tool_name", "") or ""
    ti = data.get("tool_input", {}) or {}
    sid = short_sid(data)
    proj = project_dir(data)
    tag = ""
    if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = ti.get("file_path") or ti.get("notebook_path") or ti.get("path") or ""
        if not path:
            return
        path = os.path.abspath(os.path.join(data.get("cwd") or proj, os.path.expanduser(path)))
        wl_dir = os.path.join(os.path.abspath(proj), "worklog")
        if path == wl_dir or path.startswith(wl_dir + os.sep):
            return
        what = os.path.relpath(path, proj) if path.startswith(os.path.abspath(proj) + os.sep) else path
    elif tool == "Bash":
        cmd = ti.get("command", "") or ""
        what = bash_summary(cmd)
        if not what:
            return
        what = f"`{what}`"
        if sid and re.search(rf"(결과|중간)\({re.escape(sid)}\)", cmd):
            tag = " " + WITH_RESULT
    elif tool.startswith("mcp__"):
        if not mcp_is_write(tool):
            return
        what = tool.replace("mcp__", "", 1)
        tool = "MCP"
    else:
        return
    append(worklog_path(proj), log_line(tool, what + tag, sid))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
