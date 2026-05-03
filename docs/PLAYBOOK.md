# Git Play-by-Play Teaching Book

This file is auto-appended from commit history by scripts/update-playbook.ps1.
Each entry explains what changed and why it matters for Docker + Django engineering.

### Track: Developer education and documentation

## 2026-05-02 10:38 - Initial commit

- Commit: 177d852
- Author: makanika
- Date: 2026-05-02T10:38:24+03:00
- Delta: +220 / -0
- Chapter Tags: Documentation, Teaching
- Changed Files:
  - A	.gitignore
  - A	README.md
- Teaching Focus:
  - Documentation is architecture: clear explanations reduce onboarding and debugging time.
  - Incremental delivery: each addition should map to a clear capability gain.
- Teaching Narrative:
  - Story: This commit advances Developer education and documentation through a large and foundational delta and centers on 'Initial commit'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: Documentation is architecture: clear explanations reduce onboarding and debugging time.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.

### Track: CI pipeline reliability

## 2026-05-02 16:02 - Added Github Actions

- Commit: f482f18
- Author: makanika
- Date: 2026-05-02T16:02:34+03:00
- Delta: +277 / -0
- Chapter Tags: CI/CD, GitHub Actions, Build Context, Container Security, Backend API
- Changed Files:
  - A	.dockerignore
  - A	.github/workflows/checks.yml
  - A	Dockerfile
  - A	app/.flake8
  - A	app/app/__init__.py
  - A	app/app/asgi.py
  - A	app/app/settings.py
  - A	app/app/urls.py
  - A	app/app/wsgi.py
  - A	app/manage.py
  - A	docker-compose.yml
  - A	dockerignore
  - A	requirements.dev.txt
  - A	requirements.txt
- Teaching Focus:
  - Build context hygiene: excluding noise reduces build time and accidental secret leaks.
  - CI discipline: every push should verify tests and linting before merge.
  - Container image design: layer order controls build speed and reproducibility.
  - Application evolution: Django code changes should be traced to behavior, tests, and API intent.
  - Service orchestration: Compose defines the local runtime contract between code and infrastructure.
  - Dependency governance: version ranges communicate compatibility boundaries.
  - Incremental delivery: each addition should map to a clear capability gain.
- Teaching Narrative:
  - Story: This commit advances CI pipeline reliability through a large and foundational delta and centers on 'Added Github Actions'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: Build context hygiene: excluding noise reduces build time and accidental secret leaks.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.

## 2026-05-02 16:07 - adjusted_GitHubActions

- Commit: 20b5d66
- Author: makanika
- Date: 2026-05-02T16:07:40+03:00
- Delta: +2 / -2
- Chapter Tags: CI/CD, GitHub Actions
- Changed Files:
  - M	.github/workflows/checks.yml
- Teaching Focus:
  - CI discipline: every push should verify tests and linting before merge.
  - Controlled change: updates should improve reliability, maintainability, or clarity.
- Teaching Narrative:
  - Story: This commit advances CI pipeline reliability through a small but high-signal delta and centers on 'adjusted_GitHubActions'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: CI discipline: every push should verify tests and linting before merge.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.

## 2026-05-02 16:08 - adjusted_docker_password

- Commit: 878671a
- Author: makanika
- Date: 2026-05-02T16:08:23+03:00
- Delta: +1 / -1
- Chapter Tags: CI/CD, GitHub Actions
- Changed Files:
  - M	.github/workflows/checks.yml
- Teaching Focus:
  - CI discipline: every push should verify tests and linting before merge.
  - Controlled change: updates should improve reliability, maintainability, or clarity.
- Teaching Narrative:
  - Story: This commit advances CI pipeline reliability through a small but high-signal delta and centers on 'adjusted_docker_password'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: CI discipline: every push should verify tests and linting before merge.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.

## 2026-05-02 16:12 - fixed_docker-compose

- Commit: a3c619d
- Author: makanika
- Date: 2026-05-02T16:12:21+03:00
- Delta: +2 / -2
- Chapter Tags: CI/CD, GitHub Actions, Fix
- Changed Files:
  - M	.github/workflows/checks.yml
- Teaching Focus:
  - CI discipline: every push should verify tests and linting before merge.
  - Failure-driven development: each fix should preserve the root cause as a reusable lesson.
- Teaching Narrative:
  - Story: This commit advances CI pipeline reliability through a small but high-signal delta and centers on 'fixed_docker-compose'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: CI discipline: every push should verify tests and linting before merge.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.

## 2026-05-02 16:16 - Adjusted_docker_login_action

- Commit: d68bc9d
- Author: makanika
- Date: 2026-05-02T16:16:17+03:00
- Delta: +2 / -2
- Chapter Tags: CI/CD, GitHub Actions
- Changed Files:
  - M	.github/workflows/checks.yml
- Teaching Focus:
  - CI discipline: every push should verify tests and linting before merge.
  - Controlled change: updates should improve reliability, maintainability, or clarity.
- Teaching Narrative:
  - Story: This commit advances CI pipeline reliability through a small but high-signal delta and centers on 'Adjusted_docker_login_action'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: CI discipline: every push should verify tests and linting before merge.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.


### Track: Container image design

## 2026-05-03 10:21 - added_postgres

- Commit: 6239b56
- Author: makanika
- Date: 2026-05-03T10:21:31+03:00
- Delta: +3926 / -2
- Chapter Tags: Dockerfile, Image Build, Container Security, Backend API
- Changed Files:
  - A	.githooks/post-commit
  - M	.gitignore
  - M	Dockerfile
  - M	README.md
  - A	app/app/calc.py
  - A	app/app/tests.py
  - A	compile-learn.html
  - M	docker-compose.yml
  - A	docs/PLAYBOOK.md
  - A	index.html
  - M	requirements.txt
  - A	scripts/install-git-hooks.ps1
  - A	scripts/update-playbook.ps1
- Teaching Focus:
  - Container image design: layer order controls build speed and reproducibility.
  - Documentation is architecture: clear explanations reduce onboarding and debugging time.
  - Application evolution: Django code changes should be traced to behavior, tests, and API intent.
  - Service orchestration: Compose defines the local runtime contract between code and infrastructure.
  - Dependency governance: version ranges communicate compatibility boundaries.
  - Incremental delivery: each addition should map to a clear capability gain.
- Teaching Narrative:
  - Story: This commit advances Container image design through a large and foundational delta and centers on 'added_postgres'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: Container image design: layer order controls build speed and reproducibility.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.


### Track: Developer education and documentation

## 2026-05-03 10:21 - added_postgresql_dependency

- Commit: 2eb69ed
- Author: makanika
- Date: 2026-05-03T10:21:40+03:00
- Delta: +39 / -0
- Chapter Tags: Documentation, Teaching
- Changed Files:
  - M	docs/PLAYBOOK.md
- Teaching Focus:
  - Documentation is architecture: clear explanations reduce onboarding and debugging time.
  - Incremental delivery: each addition should map to a clear capability gain.
- Teaching Narrative:
  - Story: This commit advances Developer education and documentation through a moderate and visible delta and centers on 'added_postgresql_dependency'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: Documentation is architecture: clear explanations reduce onboarding and debugging time.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.


### Track: Developer education and documentation

## 2026-05-03 10:22 - updated_playbook

- Commit: 319f5fb
- Author: makanika
- Date: 2026-05-03T10:22:23+03:00
- Delta: +23 / -0
- Chapter Tags: Documentation, Teaching
- Changed Files:
  - M	docs/PLAYBOOK.md
- Teaching Focus:
  - Documentation is architecture: clear explanations reduce onboarding and debugging time.
  - Controlled change: updates should improve reliability, maintainability, or clarity.
- Teaching Narrative:
  - Story: This commit advances Developer education and documentation through a moderate and visible delta and centers on 'updated_playbook'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: Documentation is architecture: clear explanations reduce onboarding and debugging time.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.


### Track: Django application behavior

## 2026-05-03 12:13 - added_unit_testing_for_DB

- Commit: 7c2d521
- Author: makanika
- Date: 2026-05-03T12:13:44+03:00
- Delta: +3335 / -2
- Chapter Tags: Django, Application Logic, Backend API
- Changed Files:
  - M	app/app/settings.py
  - A	app/core/__init__.py
  - A	app/core/admin.py
  - A	app/core/apps.py
  - A	app/core/management/__init__.py
  - A	app/core/management/commands/__init__.py
  - A	app/core/management/commands/wait_db.py
  - A	app/core/migrations/__init__.py
  - A	app/core/models.py
  - A	app/core/tests/__init__.py
  - A	app/core/tests/tests_commands.py
  - M	docs/PLAYBOOK.md
  - A	emiru.html
  - A	mqtt-book.html
- Teaching Focus:
  - Application evolution: Django code changes should be traced to behavior, tests, and API intent.
  - Documentation is architecture: clear explanations reduce onboarding and debugging time.
  - Incremental delivery: each addition should map to a clear capability gain.
- Teaching Narrative:
  - Story: This commit advances Django application behavior through a large and foundational delta and centers on 'added_unit_testing_for_DB'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: Application evolution: Django code changes should be traced to behavior, tests, and API intent.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.


### Track: Developer education and documentation

## 2026-05-03 12:14 - improved_pay_book

- Commit: eb505eb
- Author: makanika
- Date: 2026-05-03T12:14:01+03:00
- Delta: +37 / -0
- Chapter Tags: Documentation, Teaching
- Changed Files:
  - M	docs/PLAYBOOK.md
- Teaching Focus:
  - Documentation is architecture: clear explanations reduce onboarding and debugging time.
- Teaching Narrative:
  - Story: This commit advances Developer education and documentation through a moderate and visible delta and centers on 'improved_pay_book'.
  - Why this matters: Production quality improves when teams turn each change into a reusable operating principle.
  - Teach it this way: Start with the problem, show the exact file changes, then validate behavior with one concrete command.
  - Anchor lesson: Documentation is architecture: clear explanations reduce onboarding and debugging time.
- Hands-on Prompt: Explain this commit to a junior engineer in 3 sentences, then pair it with one local verification command.
- Verification Prompt: Run the smallest command that proves this commit works as intended.


