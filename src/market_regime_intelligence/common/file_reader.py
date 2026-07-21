from __future__ import annotations
from pathlib    import Path
import pandas as pd

class CSVReader:
    """
    Read CSV datasets.
    """
    def read(self, path: Path) -> pd.DataFrame:
        return pd.read_csv(path)