from __future__                                     import annotations
from pathlib                                        import Path
from market_regime_intelligence.cleaning.exceptions import CleaningWriteError

import pandas as pd

class CanonicalDataWriter:
    """
    Writes cleaned market data to the canonical data lake.
    """

    def write(self, dataframe: pd.DataFrame, output_path: Path) -> None:
        try:
            output_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )
            dataframe.to_csv(output_path, index=False)
        except Exception as exc:
            raise CleaningWriteError(f"Failed to write canonical dataset to '{output_path}'.") from exc