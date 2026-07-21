from __future__                                      import annotations
from market_regime_intelligence.ingestion.datasource import DataSource
from market_regime_intelligence.ingestion.models     import DownloadRequest
import pandas as pd

class BSEDataSource(DataSource):
    def download(self, request: DownloadRequest) -> pd.DataFrame:
        raise NotImplementedError("BSE datasource not implemented.")