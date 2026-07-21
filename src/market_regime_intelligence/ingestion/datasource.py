from __future__                                  import annotations
from abc                                         import ABC, abstractmethod
from market_regime_intelligence.ingestion.models import DownloadRequest
import pandas as pd

class DataSource(ABC):
    """
    Abstract market data source.
    """
    @abstractmethod
    def download(self, request: DownloadRequest) -> pd.DataFrame:
        """
        Download market data.
        """
