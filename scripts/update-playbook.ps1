param(
    [string]$RepoRoot = (Resolve-Path ".").Path,
    [switch]$Rebuild
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-UniqueLessons {
    param(
        [string[]]$Files,
        [string]$Subject,
        [string]$Body
    )

    $lessons = New-Object System.Collections.Generic.List[string]

    foreach ($file in $Files) {
        if ($file -match '^Dockerfile$') {
            $lessons.Add('Container image design: layer order controls build speed and reproducibility.')
        }
        elseif ($file -match '^docker-compose\.yml$') {
            $lessons.Add('Service orchestration: Compose defines the local runtime contract between code and infrastructure.')
        }
        elseif ($file -match '^\.github/workflows/') {
            $lessons.Add('CI discipline: every push should verify tests and linting before merge.')
        }
        elseif ($file -match '^requirements(\.dev)?\.txt$') {
            $lessons.Add('Dependency governance: version ranges communicate compatibility boundaries.')
        }
        elseif ($file -match '^\.dockerignore$') {
            $lessons.Add('Build context hygiene: excluding noise reduces build time and accidental secret leaks.')
        }
        elseif ($file -match '^app/') {
            $lessons.Add('Application evolution: Django code changes should be traced to behavior, tests, and API intent.')
        }
        elseif ($file -match '^(README\.md|index\.html|docs/)') {
            $lessons.Add('Documentation is architecture: clear explanations reduce onboarding and debugging time.')
        }
    }

    $combined = "$Subject $Body".ToLowerInvariant()
    if ($combined -match 'fix|bug|error|fail') {
        $lessons.Add('Failure-driven development: each fix should preserve the root cause as a reusable lesson.')
    }
    if ($combined -match 'add|create|introduce|initial') {
        $lessons.Add('Incremental delivery: each addition should map to a clear capability gain.')
    }
    if ($combined -match 'update|adjust|refactor') {
        $lessons.Add('Controlled change: updates should improve reliability, maintainability, or clarity.')
    }

    $seen = @{}
    $result = New-Object System.Collections.Generic.List[string]
    foreach ($lesson in $lessons) {
        if (-not $seen.ContainsKey($lesson)) {
            $seen[$lesson] = $true
            $result.Add($lesson)
        }
    }

    if ($result.Count -eq 0) {
        $result.Add('Track intent explicitly: explain what changed, why it changed, and how to verify it.')
    }

    return $result
}

function Get-CommitTheme {
    param(
        [string[]]$Files,
        [string]$Subject
    )

    if ($Files -match '^\.github/workflows/') {
        return 'CI pipeline reliability'
    }
    if ($Files -match '^Dockerfile$') {
        return 'Container image design'
    }
    if ($Files -match '^docker-compose\.yml$') {
        return 'Local orchestration flow'
    }
    if ($Files -match '^requirements(\.dev)?\.txt$') {
        return 'Dependency strategy'
    }
    if ($Files -match '^app/') {
        return 'Django application behavior'
    }
    if ($Files -match '^(README\.md|index\.html|docs/)') {
        return 'Developer education and documentation'
    }

    $lower = $Subject.ToLowerInvariant()
    if ($lower -match 'fix|bug|error|fail') {
        return 'Root-cause remediation'
    }
    if ($lower -match 'add|create|introduce|initial') {
        return 'Capability expansion'
    }

    return 'Engineering iteration'
}

function Get-ChapterTags {
    param(
        [string]$Theme,
        [string[]]$Files,
        [string]$Subject
    )

    $tags = New-Object System.Collections.Generic.List[string]

    switch ($Theme) {
        'CI pipeline reliability' {
            $tags.Add('CI/CD')
            $tags.Add('GitHub Actions')
        }
        'Container image design' {
            $tags.Add('Dockerfile')
            $tags.Add('Image Build')
        }
        'Local orchestration flow' {
            $tags.Add('Docker Compose')
            $tags.Add('Local Development')
        }
        'Dependency strategy' {
            $tags.Add('Dependencies')
            $tags.Add('Python Packaging')
        }
        'Django application behavior' {
            $tags.Add('Django')
            $tags.Add('Application Logic')
        }
        'Developer education and documentation' {
            $tags.Add('Documentation')
            $tags.Add('Teaching')
        }
        'Root-cause remediation' {
            $tags.Add('Troubleshooting')
            $tags.Add('Debugging')
        }
        'Capability expansion' {
            $tags.Add('Feature Delivery')
            $tags.Add('Project Growth')
        }
        default {
            $tags.Add('Engineering')
        }
    }

    if ($Files -match '^\.dockerignore$') {
        $tags.Add('Build Context')
    }
    if ($Files -match '^Dockerfile$') {
        $tags.Add('Container Security')
    }
    if ($Files -match '^app/') {
        $tags.Add('Backend API')
    }

    $lower = $Subject.ToLowerInvariant()
    if ($lower -match 'fix|bug|error|fail') {
        $tags.Add('Fix')
    }

    $seen = @{}
    $result = New-Object System.Collections.Generic.List[string]
    foreach ($tag in $tags) {
        if (-not $seen.ContainsKey($tag)) {
            $seen[$tag] = $true
            $result.Add($tag)
        }
    }

    return $result
}

function Get-NarrativeLines {
    param(
        [string]$Theme,
        [string]$Subject,
        [int]$Insertions,
        [int]$Deletions,
        [string[]]$Lessons
    )

    $changeSignal = if (($Insertions + $Deletions) -lt 10) {
        'small but high-signal'
    }
    elseif (($Insertions + $Deletions) -lt 80) {
        'moderate and visible'
    }
    else {
        'large and foundational'
    }

    $primaryLesson = $Lessons[0]

    return @(
        '- Teaching Narrative:',
        "  - Story: This commit advances $Theme through a $changeSignal delta and centers on '$Subject'.",
        "  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.",
        "  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.",
        "  - Anchor lesson: $primaryLesson"
    )
}

function Write-PlaybookHeader {
    param(
        [string]$Path
    )

    @(
        '# Git Play-by-Play Teaching Book',
        '',
        'This file is auto-appended from commit history by scripts/update-playbook.ps1.',
        'Each entry explains what changed and why it matters for Docker + Django engineering.',
        ''
    ) -join [Environment]::NewLine | Set-Content -Path $Path -Encoding UTF8
}

if (-not (Test-Path (Join-Path $RepoRoot '.git'))) {
    throw "No git repository found at $RepoRoot"
}

$playbookPath = Join-Path $RepoRoot 'docs/PLAYBOOK.md'
$statePath = Join-Path $RepoRoot '.playbook-state'

if (-not (Test-Path (Join-Path $RepoRoot 'docs'))) {
    New-Item -ItemType Directory -Path (Join-Path $RepoRoot 'docs') | Out-Null
}

if ($Rebuild) {
    Write-PlaybookHeader -Path $playbookPath
}
elseif (-not (Test-Path $playbookPath)) {
    Write-PlaybookHeader -Path $playbookPath
}

$lastProcessed = ''
if (-not $Rebuild -and (Test-Path $statePath)) {
    $lastProcessed = (Get-Content -Path $statePath -Raw).Trim()
}

$range = if ([string]::IsNullOrWhiteSpace($lastProcessed)) { 'HEAD' } else { "$lastProcessed..HEAD" }
$commitList = git -C $RepoRoot rev-list --reverse $range

if ($LASTEXITCODE -ne 0) {
    throw 'Unable to read git history.'
}

if ([string]::IsNullOrWhiteSpace(($commitList -join ''))) {
    Write-Host 'No new commits to append.'
    exit 0
}

$entries = New-Object System.Collections.Generic.List[string]
$finalSha = $null
$currentTheme = ''

foreach ($sha in $commitList) {
    if ([string]::IsNullOrWhiteSpace($sha)) {
        continue
    }

    $subject = git -C $RepoRoot show -s --format=%s $sha
    $body = git -C $RepoRoot show -s --format=%b $sha
    $author = git -C $RepoRoot show -s --format=%an $sha
    $date = git -C $RepoRoot show -s --date=iso-strict --format=%ad $sha

    $nameStatus = git -C $RepoRoot show --name-status --pretty=format: $sha
    $changed = @()
    foreach ($line in $nameStatus) {
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }
        $changed += $line
    }

    $filesOnly = @()
    foreach ($line in $changed) {
        $parts = $line -split "`t"
        if ($parts.Length -ge 2) {
            $filesOnly += $parts[$parts.Length - 1]
        }
    }

    $stats = git -C $RepoRoot show --numstat --pretty=format: $sha
    $insertions = 0
    $deletions = 0
    foreach ($row in $stats) {
        if ([string]::IsNullOrWhiteSpace($row)) {
            continue
        }
        $cols = $row -split "`t"
        if ($cols.Length -lt 2) {
            continue
        }
        if ($cols[0] -match '^\d+$') {
            $insertions += [int]$cols[0]
        }
        if ($cols[1] -match '^\d+$') {
            $deletions += [int]$cols[1]
        }
    }

    $lessons = Get-UniqueLessons -Files $filesOnly -Subject $subject -Body $body
    $theme = Get-CommitTheme -Files $filesOnly -Subject $subject
    $chapterTags = Get-ChapterTags -Theme $theme -Files $filesOnly -Subject $subject
    $narrativeLines = Get-NarrativeLines -Theme $theme -Subject $subject -Insertions $insertions -Deletions $deletions -Lessons $lessons
    $shortSha = $sha.Substring(0, 7)

    if ($theme -ne $currentTheme) {
        $entries.Add("### Track: $theme")
        $entries.Add('')
        $currentTheme = $theme
    }

    $entries.Add("## $(Get-Date $date -Format 'yyyy-MM-dd HH:mm') - $subject")
    $entries.Add("")
    $entries.Add("- Commit: $shortSha")
    $entries.Add("- Author: $author")
    $entries.Add("- Date: $date")
    $entries.Add("- Delta: +$insertions / -$deletions")
    $entries.Add("- Chapter Tags: $($chapterTags -join ', ')")

    if ($changed.Count -gt 0) {
        $entries.Add('- Changed Files:')
        foreach ($line in $changed) {
            $entries.Add("  - $line")
        }
    }

    $entries.Add('- Teaching Focus:')
    foreach ($lesson in $lessons) {
        $entries.Add("  - $lesson")
    }

    foreach ($line in $narrativeLines) {
        $entries.Add($line)
    }

    $entries.Add("- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.")
    $entries.Add('- Verification Prompt: Run the smallest command that proves this commit works as intended.')
    $entries.Add('')

    $finalSha = $sha
}

Add-Content -Path $playbookPath -Value (($entries -join [Environment]::NewLine) + [Environment]::NewLine) -Encoding UTF8
Set-Content -Path $statePath -Value $finalSha -Encoding UTF8

Write-Host "Appended $($entries.Count) lines to docs/PLAYBOOK.md"
Write-Host "Updated .playbook-state to $finalSha"
