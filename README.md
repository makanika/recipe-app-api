# recipe-app-api
Recipe API Project

## Continuous Git Play-by-Play Teaching Book

This repository now includes automation that converts each commit into a teaching entry.

- Output file: `docs/PLAYBOOK.md`
- Tracking state: `.playbook-state` (ignored by git)
- Generator script: `scripts/update-playbook.ps1`
- Hook installer: `scripts/install-git-hooks.ps1`

### One-time setup

Run this once from the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-git-hooks.ps1
```

This does two things:

1. Configures `core.hooksPath` to `.githooks`
2. Generates/updates `docs/PLAYBOOK.md` from existing commit history

### Ongoing use

After setup, every `git commit` triggers `.githooks/post-commit`, which appends a new play-by-play section to `docs/PLAYBOOK.md`.

If you ever want to regenerate manually, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\update-playbook.ps1
```

To fully rebuild the teaching book from all commits (recommended after improving templates), run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\update-playbook.ps1 -Rebuild
```

Each commit entry now includes a richer teaching narrative:

1. Story context for the change
2. Why the change matters in real engineering practice
3. A teaching method you can use to coach someone else

The playbook also auto-organizes entries by theme and chapter tags:

1. Track headings (for example: CI pipeline reliability, Docker image design)
2. Chapter tags per commit (for example: CI/CD, Docker Compose, Troubleshooting)
