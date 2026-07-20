"""
Cust exceptions for the configuration module.
"""

from __future__ import annotations

class ConfigurationError(Exception):
    """
    Base exception for all configuration-related errors.
    """

class ConfigurationFileNotFoundError(ConfigurationError):
    """
    Raised when a configuration file cannot be found.
    """

class InvalidConfigurationError(ConfigurationError):
    """
    Raised when configuration validation fails.
    """

class ConfigurationLoadError(ConfigurationError):
    """
    Raised when a configuration file cannot be loaded
    """