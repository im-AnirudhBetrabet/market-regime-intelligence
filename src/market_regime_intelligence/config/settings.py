"""
Typed application settings.
"""

from __future__ import annotations

from email.policy import default

from pydantic   import BaseModel, ConfigDict, Field

class AppConfig(BaseModel):
    """
    Application configuration.
    """
    model_config = ConfigDict(frozen=True)

    environment: str = Field(default="dev")
    timezone   : str = Field(default="Asia/Kolkata")

class MarketConfig(BaseModel):
    """
    Market configuration.
    """
    model_config = ConfigDict(frozen=True)
    symbol: str  = Field(default="^NSEI")

class DataConfig(BaseModel):
    """
    Data configuration
    """
    model_config = ConfigDict(frozen=True)

    history_years: int = Field(default=10, ge=1)
    timeframe    : str = Field(default="5m")

class LoggingConfig(BaseModel):
    """
    Logging configuration.
    """
    model_config  = ConfigDict(frozen=True)
    level  : str  = Field(default="INFO")
    console: bool = Field(default=True)

class AppSettings(BaseModel):
    """
    Root application settings.
    """
    model_config = ConfigDict(frozen=True, extra="forbid")

    app    : AppConfig
    data   : DataConfig
    logging: LoggingConfig
    market : MarketConfig