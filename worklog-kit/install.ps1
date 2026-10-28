# Claude Code 업무일지(worklog) + 내 규칙(memory) + 내 자료(자료) 키트 설치 · 윈도우용 (맥은 install.sh)
#   PowerShell 을 열고 프로젝트 폴더로 이동(cd)한 뒤 아래 한 줄을 붙여넣는다:
#   [Net.ServicePointManager]::SecurityProtocol='Tls12'; iwr -useb https://thehfk.github.io/hfk-ai-bss/worklog-kit/install.ps1 -OutFile "$env:TEMP\hfk-kit.ps1"; powershell -NoProfile -ExecutionPolicy Bypass -File "$env:TEMP\hfk-kit.ps1" -ProjectDir "$PWD"
#
# 하는 일은 맥판과 같다(훅 파일 9개 받기 → 안내 파일 → settings.json 합치기, 2·3 은 kit_setup.py).
# 다른 점 두 가지
#   - 파이썬 이름: 윈도우는 python3 가 없거나 마이크로소프트 스토어 안내로 연결되는 일이 많아 py -3 → python → python3 순서로 실제로 돌아가는 것을 고른다
#   - 훅 명령에 이 폴더의 절대경로를 적는다(--abs-path). 훅이 Git Bash 가 아니라 PowerShell 로 돌 때도 같은 뜻이 되게. 폴더를 옮기면 다시 설치
# 이 파일은 UTF-8(BOM 포함)으로 저장한다. BOM 이 없으면 윈도우 PowerShell 5.1 이 한글을 깨뜨린다.
#
# 정본: hfk-workspace scripts/worklog_kit/ (여기 배포본을 직접 고치지 말 것)
param(
  [string]$ProjectDir = (Get-Location).Path,
  [string]$Base = $(if ($env:WORKLOG_KIT_BASE) { $env:WORKLOG_KIT_BASE } else { 'https://thehfk.github.io/hfk-ai-bss/worklog-kit' })
)
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
try { [Console]::OutputEncoding = [Text.Encoding]::UTF8 } catch {}

$Hooks = @('worklog_common.py','pre_edit_gate.py','post_action_log.py','stop_worklog.py','session_start.py','feedback_capture.py','feedback_session.py','reference_capture.py','reference_session.py')

$dir = (Resolve-Path $ProjectDir).Path.TrimEnd('\')
if ($dir -eq $HOME.TrimEnd('\') -or $dir -match '^[A-Za-z]:$') {
  Write-Host '홈 폴더가 아니라 작업하는 프로젝트 폴더 안에서 실행해 주세요.'
  Write-Host "예: cd $HOME\Documents\내프로젝트 후 다시 실행"
  exit 1
}
Set-Location $dir

# 실제로 돌아가는 파이썬 고르기
$py = $null
foreach ($cand in @(@('py','-3'), @('python'), @('python3'))) {
  try {
    $exe = $cand[0]; $rest = @($cand | Select-Object -Skip 1)
    & $exe @rest -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) { $py = $cand; break }
  } catch {}
}
if (-not $py) {
  Write-Host '파이썬 3.8 이상이 필요합니다. https://www.python.org/downloads/ 에서 설치하고,'
  Write-Host "설치 첫 화면에서 'Add python.exe to PATH' 에 체크한 뒤 PowerShell 을 새로 열어 다시 실행해 주세요."
  exit 1
}
$launcher = ($py -join ' ')
$pyExe = $py[0]; $pyArgs = @($py | Select-Object -Skip 1)

$tmp = Join-Path ([IO.Path]::GetTempPath()) ('hfk-kit-' + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
  Write-Host "키트 내려받는 중… ($Base)"
  foreach ($f in $Hooks) { Invoke-WebRequest -UseBasicParsing "$Base/hooks/$f" -OutFile (Join-Path $tmp $f) }
  foreach ($f in @('worklog-README.md','memory-README.md','library-README.md','kit_setup.py')) { Invoke-WebRequest -UseBasicParsing "$Base/$f" -OutFile (Join-Path $tmp $f) }
  foreach ($f in $Hooks + @('kit_setup.py')) {
    & $pyExe @pyArgs -c "import sys; compile(open(sys.argv[1], encoding='utf-8').read(), sys.argv[1], 'exec')" (Join-Path $tmp $f)
    if ($LASTEXITCODE -ne 0) { throw "내려받은 파일이 깨졌습니다: $f" }
  }

  $hookDir = Join-Path $dir '.claude\hooks\worklog'
  New-Item -ItemType Directory -Force -Path $hookDir | Out-Null
  foreach ($f in $Hooks) { Copy-Item (Join-Path $tmp $f) $hookDir -Force }
  Remove-Item (Join-Path $hookDir '__pycache__') -Recurse -Force -ErrorAction SilentlyContinue

  & $pyExe @pyArgs (Join-Path $tmp 'kit_setup.py') $tmp --launcher $launcher --abs-path
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} finally {
  Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
}

$name = ''
try { $name = (git config user.name 2>$null) } catch {}
if (-not $name) { $name = $env:USERNAME }

Write-Host ''
Write-Host "설치 완료: $dir"
Write-Host '  - 훅: .claude\hooks\worklog\'
Write-Host '  - 기록: worklog\날짜.md  (작성 기준: worklog\README.md)'
Write-Host '  - 규칙: memory\MEMORY.md  (작성 기준: memory\README.md)'
Write-Host '  - 자료: 자료\목록.md  (작성 기준: 자료\README.md)'
Write-Host "  - 기록에 쓰일 이름: $name"
Write-Host "  - 파이썬: $launcher"
Write-Host ''
Write-Host '다음 단계: 이 폴더에서 Claude Code 를 새로 열어 주세요(이미 열려 있으면 껐다 켜기).'
Write-Host '처음 열 때 이 폴더를 믿을지 묻는 창이 뜨면 동의를 눌러야 기록이 시작됩니다.'
Write-Host '폴더를 다른 곳으로 옮기면 그 폴더에서 이 설치를 한 번 더 실행해 주세요.'
