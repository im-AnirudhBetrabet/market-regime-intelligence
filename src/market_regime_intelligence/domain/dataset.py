from market_regime_intelligence.domain.enums import DatasetCategory
from dataclasses                             import dataclass

@dataclass(frozen=True, slots=True)
class Dataset:
    category   : DatasetCategory
    name       : str
    symbol     : str
    description: str  = ""
    enabled    : bool = True
    interval   : str  = "1d"
    provider   : str  = "yahoo"