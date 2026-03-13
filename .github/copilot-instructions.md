# Project Guidelines

## Mandatory Development Checklist
- Lint: `ruff check .`
- Build: `python -m build`
- Test: `pytest`

## Core Rules
- Target Python 3.10+ and preserve the `src/` layout.
- Keep CLI output deterministic JSON for automation.
- Prefer explicit typing and small helper functions.
- Avoid heavy dependencies; runtime dependency is `PyYAML`.

## Architecture
- Console entrypoint: `socops` -> `soc_ops.cli:main` (in `pyproject.toml`).
- Source code: `src/soc_ops/`; tests: `tests/`.
- Config loader: `src/soc_ops/config.py`, default path `configs/default.yaml`.

## Conventions
- Keep imports compatible with pytest `pythonpath = ["src"]`.
- New CLI commands must be added in `_build_parser()` and dispatched from `main()`.
- Validate IP addresses with `ipaddress`, not regex-only checks.
- For extraction features, return sorted, deduplicated lists.

## Pitfalls
- `src` layout requires editable install for reliable imports.
- Missing `configs/default.yaml` must not crash startup; return `{}`.
- Keep output shape stable to avoid breaking tests and downstream tooling.
