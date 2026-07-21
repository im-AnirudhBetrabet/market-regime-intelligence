from __future__  import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ValidationResult:
    passed  : bool
    errors  : list[str]
    warnings: list[str]