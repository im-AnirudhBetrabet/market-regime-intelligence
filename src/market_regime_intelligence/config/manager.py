"""
Application configuration manager
"""

from __future__ import annotations
from pathlib    import Path
from pydantic   import ValidationError

from market_regime_intelligence.config.exceptions import InvalidConfigurationError
from market_regime_intelligence.config.loader     import load_yaml
from market_regime_intelligence.config.settings   import AppSettings

class ConfigurationManager:
    """
    Loads and validation application configuration
    """
    def __init__(self, config_directory: Path) -> None:
        self._config_directory = config_directory

    def load(self, environment: str = "dev") -> AppSettings:
        """
        Load application configuration.
        Args:
            environment:
                Configuration environment
        Returns:
            Validated application settings.
        """
        base = load_yaml(self._config_directory / "base.yaml")
        env  = load_yaml(self._config_directory / f"{environment}.yaml")

        merged = self._merge(base, env)

        try:
            return AppSettings.model_validate(merged)
        except ValidationError as exc:
            raise InvalidConfigurationError(str(exc)) from exc

    @staticmethod
    def _merge(base: dict, override: dict) -> dict:
        """
        Recursively merge dictionaries.
        """
        result = base.copy()

        for key, value in override.items():
            if key in result and isinstance(result[key], dict):
                result[key] = ConfigurationManager._merge(result[key], value)
            else:
                result[key] = value
        return result