from __future__                                     import annotations
from dataclasses                                    import dataclass
from market_regime_intelligence.cleaning.exceptions import InvalidOHLCError, InvalidSchemaError
from market_regime_intelligence.cleaning.models     import CleaningResult

import pandas as pd

_REQUIRED_COLUMNS = (
    "timestamp",
    "open",
    "high",
    "low",
    "close",
    "volume"
)

@dataclass(slots=True)
class MarketDataCleaner:
    """
    Transforms validated market data into canonical market data.
    """
    def clean(self, dataframe: pd.DataFrame) -> tuple[pd.DataFrame, CleaningResult]:
        df          = dataframe.copy(deep=True)
        rows_before = len(df)

        self._validate_schema(df)

        # ----------- timestamp -----------
        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            errors="coerce",
            utc=False
        )
        invalid_timestamp_rows = df["timestamp"].isna().sum()
        df                     = df.dropna(subset=["timestamp"])

        # ----------- numeric -----------
        numeric_columns = (
            "open",
            "high",
            "low",
            "close",
            "volume"
        )

        for column in numeric_columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )
        missing_before = len(df)
        df             = df.dropna(subset=numeric_columns)

        missing_rows_removed = missing_before - len(df)

        # ----------- sort -----------
        df = df.sort_values(
            "timestamp",
            kind="mergesort"
        )

        # ----------- duplicates -----------
        duplicate_rows = df.duplicated(
            subset="timestamp",
            keep="last"
        ).sum()

        # ----------- ohlc -----------
        self._validate_ohlc(df)

        df = df.reset_index(drop=True)

        return (
            df,
            CleaningResult(
                rows_before=rows_before,
                rows_after=len(df),
                duplicates_removed=int(duplicate_rows),
                missing_rows_removed=missing_rows_removed + int(invalid_timestamp_rows),
                output_path=None,
            )
        )

    @staticmethod
    def _validate_ohlc(dataframe: pd.DataFrame) -> None:
        invalid = (
              (dataframe["high"] < dataframe["low"]  )
            | (dataframe["high"] < dataframe["open"] )
            | (dataframe["high"] < dataframe["close"])
            | (dataframe["low"]  > dataframe["open"] )
            | (dataframe["low"]  > dataframe["close"])
        )
        if invalid.any():
            raise InvalidOHLCError(
                f"{invalid.sum()} rows contain invalid OHLC values."
            )

    @staticmethod
    def _validate_schema(dataframe: pd.DataFrame) -> None:
        missing = [ column for column in _REQUIRED_COLUMNS if column not in dataframe.columns ]

        if missing:
            raise InvalidSchemaError(f"Missing columns: {','.join(missing)}")