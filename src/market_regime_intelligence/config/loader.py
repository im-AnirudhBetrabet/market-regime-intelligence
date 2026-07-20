"""
Configuration file loader.
"""

from __future__ import annotations
from pathlib    import Path
from typing     import Any

import yaml

from market_regime_intelligence.config.exceptions import ConfigurationFileNotFoundError, ConfigurationLoadError


def load_yaml(path: Path) -> dict[str, Any]:
    """
    Load a YAML file.
    Args:
        path:
            YAML file path

    Returns:
        Parsed YAML dictionary.

    Raises:
        ConfigurationFileNotFoundError:
            If the file does not exist.
        ConfigurationLoadError:
            If YAML cannot be parsed.
    """
    if not path.exists():
        raise ConfigurationFileNotFoundError(f"Configuration file not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file) or {}
    except yaml.YAMLError as exc:
        raise ConfigurationLoadError(f"Unable to parse configuration file: {path}") from exc