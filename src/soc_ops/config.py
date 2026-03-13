from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


DEFAULT_CONFIG_PATH = Path("configs/default.yaml")


def load_config(config_path: Path | None = None) -> dict[str, Any]:
    """Load YAML configuration from disk."""
    path = config_path or DEFAULT_CONFIG_PATH
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError("Configuration root must be a mapping")
    return data
