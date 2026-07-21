"""
Raw data writer.
"""

from __future__ import annotations
from pathlib    import Path

import pandas as pd

from market_regime_intelligence.ingestion.exceptions import DataWriteError
from market_regime_intelligence.logging              import get_logger

logger = get_logger(__name__)

class RawDataWriter:
    """
    Writes raw datasets.
    """

    def write(self, dataframe: pd.DataFrame, output_path: Path) -> None:
        """
        Save dataframe
        Args:
            dataframe:
                DataFrame
            output_path:
                Destination path
        """

        try:
            output_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            dataframe.to_csv(
                output_path,
                index=False
            )
            logger.info(
                "Saved dataset to %s", output_path
            )

        except Exception as exc:
            raise DataWriteError(f"Unable to write {output_path}") from exc