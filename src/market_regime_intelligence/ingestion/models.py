from __future__  import annotations
from dataclasses import dataclass
from datetime    import date

@dataclass(frozen=True)
class DownloadRequest:
    symbol    : str
    interval  : str
    start_date: date
    end_date  : date

@dataclass(frozen=True)
class DownloadResult:
    symbol     : str
    rows       : int
    output_path: str