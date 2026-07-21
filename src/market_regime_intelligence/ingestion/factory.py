from __future__ import annotations
from market_regime_intelligence.domain.providers           import DataProvider
from market_regime_intelligence.ingestion.datasource       import DataSource
from market_regime_intelligence.ingestion.providers.manual import ManualDataSource
from market_regime_intelligence.ingestion.providers.nse    import NSEDataSource
from market_regime_intelligence.ingestion.providers.bse    import BSEDataSource
from market_regime_intelligence.ingestion.providers.rbi    import RBIDataSource
from market_regime_intelligence.ingestion.providers.yahoo  import YahooFinanceDataSource

class DataSourceFactory:
    """
    Creates datasource implementations
    """

    _REGISTRY: dict[DataProvider, type[DataSource]] = {
        DataProvider.YAHOO : YahooFinanceDataSource,
        DataProvider.NSE   : NSEDataSource,
        DataProvider.RBI   : RBIDataSource,
        DataProvider.MANUAL: ManualDataSource
    }
    @classmethod
    def create(cls, provider: DataProvider) -> DataSource:
        try:
            datasource_cls = cls._REGISTRY[provider]
        except KeyError as exc:
            raise ValueError(
                f"Unsupported provider: {provider}"
            ) from exc

        return datasource_cls()