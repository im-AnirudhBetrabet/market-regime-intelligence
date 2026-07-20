"""
Configuration package.
"""

from pathlib import Path

from market_regime_intelligence.config.manager  import ConfigurationManager
from market_regime_intelligence.config.settings import AppSettings

def get_settings(environment: str = "dev") -> AppSettings:
    """
    Load application settings.
    Args:
        environment:
            Target environment

    Returns:
        Validated application settings.
    """
    config_dir = Path("configs")
    manager    = ConfigurationManager(config_dir)

    return manager.load(environment)