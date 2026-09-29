# qa-toolkit

A small Python library for validating bug reports and checking requirements.

## Workflows

| Workflow | Trigger | Jobs |
|---|---|---|
| CI | push / PR to `main` | lint → test (3.11, 3.12, 3.13) |
| Release | tag `v*.*.*` | lint → test → build → GitHub Release |
| Webhook | `repository_dispatch` / manual | test |

## Setup

```bash
bash scripts/setup_env.sh
```

## Running tests

```bash
pytest
```

## Release

Tag a commit to trigger the release workflow:

```bash
git tag v0.1.0
git push origin v0.1.0
```

## Webhook

```bash
export GITHUB_TOKEN=<your_token>
python scripts/send_webhook.py
```
