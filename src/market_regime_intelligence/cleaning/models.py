from dataclasses import dataclass
from pathlib     import Path

@dataclass(slots=True)
class CleaningResult:
    duplicates_removed  : int
    missing_rows_removed: int
    output_path         : Path | None
    rows_before         : int
    rows_after          : int