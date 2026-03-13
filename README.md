# my-soc-ops-python

Starter SOC operations toolkit in Python.

## Quick start

1. Create and activate a virtual environment.
2. Install package in editable mode.
3. Run the CLI.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
socops health
```

## CLI examples

```bash
socops health
socops parse-ioc --text "Suspicious host 10.10.10.5 and example.com"
```

## Project layout

- `src/soc_ops/`: package source code
- `configs/default.yaml`: baseline configuration
- `tests/`: unit tests
