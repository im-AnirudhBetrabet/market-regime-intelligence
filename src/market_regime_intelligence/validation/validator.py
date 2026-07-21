from __future__ import annotations

import pandas
import pandas as pd
from mypyc.irbuild.util import dataclass_decorator_type

from market_regime_intelligence.validation.models import ValidationResult
from market_regime_intelligence.validation.rules  import REQUIRED_COLUMNS

class DatasetValidator:
    """
    Validate raw market datasets.
    """

    def validate(self, dataframe: pd.DataFrame) -> ValidationResult:
        errors  : list[str] = []
        warnings: list[str] = []

        missing = [ col for col in REQUIRED_COLUMNS if col not in dataframe.columns ]

        if missing:
            errors.append(
                f"Missing columns: {', '.join(missing)}"
            )

        if dataframe.empty:
            errors.append("Dataset is empty.")

        if dataframe["timestamp"].duplicated().any():
            errors.append("Duplicate timestamps detected.")

        if dataframe.isna().sum().sum() > 0:
            warnings.append("Dataset contains missing values.")

        if (dataframe["high"] < dataframe["low"]).any():
            errors.append("Found rows where high < low.")

        return ValidationResult(
            passed=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )