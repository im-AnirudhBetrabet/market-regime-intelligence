from __future__                                import annotations
from market_regime_intelligence.domain.dataset import Dataset
from market_regime_intelligence.domain.enums   import DatasetCategory
from collections.abc                           import Iterable

class DatasetRegistry:
    """
    Registry for all supported datasets.
    """
    def __init__(self, datasets: Iterable[Dataset]) -> None:
        self._datasets = list(datasets)
        self._validate()

    def all(self) -> list[Dataset]:
        return self._datasets.copy()

    def enabled(self) -> list[Dataset]:
        return [d for d in self._datasets if d.enabled]

    def by_name(self, name: str) -> Dataset:
        for dataset in self._datasets:
            if dataset.name == name:
                return dataset

        raise ValueError(f"Unknown dataset: {name}")

    def by_category(self, category: DatasetCategory) -> list[Dataset]:
        return [
            dataset
            for dataset in self._datasets
            if dataset.category == category
        ]

    def by_provider(self, provider: str) -> list[Dataset]:
        return [
            dataset
            for dataset in self._datasets
            if dataset.provider == provider
        ]

    def _validate(self) -> None:
        names   = set()
        symbols = set()

        for dataset in self._datasets:
            if dataset.name in names:
                raise ValueError(f"Duplicate dataset name '{dataset.name}'")

            if dataset.symbol in symbols:
                raise ValueError(f"Duplicate dataset symbol '{dataset.symbol}'")

            names.add(dataset.name)
            symbols.add(dataset.symbol)