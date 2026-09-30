# Changelog

## [Unreleased]

## [0.1.0] - 2024-01-01
### Added
- `BugReport` dataclass and `validate_bug_report()` with severity, title, steps, and expected/actual checks.
- Flag bug report titles that end with a period.
- `check_requirements()` for running named rule functions against a value.
- CI workflow (lint + test matrix on Python 3.11/3.12/3.13).
- Release workflow (lint → test → build → GitHub Release on `v*.*.*` tags).
- Webhook workflow (`repository_dispatch` / manual dispatch).
