from __future__ import annotations
from datetime   import date
import pandas as pd
import requests

class NSECLIENT:
    BASE_URL    = "https://www.nseindia.com"
    HISTORY_URL = (
        "https://www.nseindia.com/api/historical/indicesHistory"
    )

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/",
    }

    def __init__(self) -> None:
        self._session = requests.Session()
        self._session.headers.update(self.HEADERS)
        self._initialize_session()

    def _initialize_session(self) -> None:
        response = self._session.get(
            self.BASE_URL,
            timeout=30,
        )
        response.raise_for_status()

    def fetch_historical_index(
            self,
            index: str,
            start_date: date,
            end_date: date,
    ) -> pd.DataFrame:
        params = {
            "indexType": index,
            "from": start_date.strftime("%d-%m-%Y"),
            "to": end_date.strftime("%d-%m-%Y"),
        }

        response = self._session.get(
            self.HISTORY_URL,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        payload = response.json()

        data = payload["data"]["indexCloseOnlineRecords"]

        df = pd.DataFrame(data)

        df = df.rename(
            columns={
                "EOD_TIMESTAMP": "Date",
                "OPEN_INDEX_VAL": "Open",
                "HIGH_INDEX_VAL": "High",
                "LOW_INDEX_VAL": "Low",
                "CLOSE_INDEX_VAL": "Close",
            }
        )

        df["Adj Close"] = df["Close"]
        df["Volume"] = 0

        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True,
        )

        numeric_columns = [
            "Open",
            "High",
            "Low",
            "Close",
            "Adj Close",
        ]

        for column in numeric_columns:
            df[column] = (
                df[column]
                .astype(str)
                .str.replace(",", "", regex=False)
                .astype(float)
            )

        return df[
            [
                "Date",
                "Open",
                "High",
                "Low",
                "Close",
                "Adj Close",
                "Volume",
            ]
        ].sort_values("Date").reset_index(drop=True)