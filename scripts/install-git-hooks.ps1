param(
    [string]$RepoRoot = (Resolve-Path ".").Path
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path (Join-Path $RepoRoot '.git'))) {
    throw "No git repository found at $RepoRoot"
}

Write-Host "Configuring repo hooks path to .githooks"
git -C $RepoRoot config core.hooksPath .githooks
if ($LASTEXITCODE -ne 0) {
    throw 'Failed to set core.hooksPath.'
}

$updateScript = Join-Path $RepoRoot 'scripts/update-playbook.ps1'
if (-not (Test-Path $updateScript)) {
    throw 'Missing scripts/update-playbook.ps1'
}

Write-Host 'Generating/refreshing initial playbook from git history...'
& $updateScript -RepoRoot $RepoRoot

Write-Host ''
Write-Host 'Playbook automation enabled.'
Write-Host 'Every new commit will append a teaching entry to docs/PLAYBOOK.md via .githooks/post-commit.'
