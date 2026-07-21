from __future__ import annotations
from enum       import StrEnum

class DataProvider(StrEnum):
    """
    Supported market data providers.
    """
    YAHOO  = "yahoo"
    NSE    = "nse"
    RBI    = "rbi"
    MANUAL = "manual"
    BSE    = "bse"