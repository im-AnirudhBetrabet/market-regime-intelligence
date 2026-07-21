"""
Yahoo Finance data source implementation
"""

from __future__ import annotations
from time       import sleep

import pandas   as pd
import yfinance as yf

from market_regime_intelligence.ingestion.datasource import DataSource
from market_regime_intelligence.ingestion.exceptions import DataDownloadError
from market_regime_intelligence.ingestion.models     import DownloadRequest
from market_regime_intelligence.logging              import get_logger

logger = get_logger(__name__)

class YahooFinanceDataSource(DataSource):
    """
    Yahoo Finance implementation.
    """

    RETRY_DELAY_SECONDS = 2
    MAX_RETRIES         = 3

    def download(self, request: DownloadRequest) -> pd.DataFrame:
        """
        Download market data from Yahoo Finance
        Args:
            request:
                Download request
        Returns:
            Standardized market data.
        """
        logger.info("Downloading %s (%s)", request.symbol, request.interval)

        last_exception: Exception | None = None

        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                df = yf.download(
                    tickers=request.symbol,
                    start=request.start_date,
                    end=request.end_date,
                    interval=request.interval,
                    auto_adjust=False,
                    progress=False,
                    threads=False,
                )
                if df.empty:
                    raise DataDownloadError(f"No data returned for {request.symbol}")

                df = self._normalize(df)

                logger.info("Downloaded %d rows.", len(df))

                return df
            except Exception as exc:
                last_exception = exc
                logger.warning("Attempt %d/%d failed.", attempt, self.MAX_RETRIES)

                if attempt < self.MAX_RETRIES:
                    sleep(self.RETRY_DELAY_SECONDS)

        raise DataDownloadError(f"Failed downloading {request.symbol}") from last_exception

    @staticmethod
    def _normalize(df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize Yahoo Finance dataframe.
        Args:
            df:
                Raw dataframe downloaded from yfinance.
        Returns:
            Standard dataframe
        """
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.rename(
            columns={
                "Open"     : "open",
                "High"     : "high",
                "Low"      : "low" ,
                "Close"    : "close",
                "Adj Close": "adj_close",
                "Volume"   : "volume"
            }
        )

        df.index.name = "timestamp"
        df            = df.reset_index()
        return df