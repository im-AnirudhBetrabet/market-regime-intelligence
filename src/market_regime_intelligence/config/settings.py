"""
Typed application settings.
"""

from __future__ import annotations
from datetime   import date
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

    history_years: int  = Field(default=10, ge=1)
    timeframe    : str  = Field(default="5m")
    start_date   : date = date(2011, 1, 1)
    end_date     : date = date(2026, 3, 31)

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

    app    : AppConfig     = Field(default_factory=AppConfig)
    data   : DataConfig    = Field(default_factory=DataConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    market : MarketConfig  = Field(default_factory=MarketConfig)

settings = AppSettings()