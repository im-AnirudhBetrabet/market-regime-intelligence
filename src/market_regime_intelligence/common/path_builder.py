from __future__                                import annotations
from market_regime_intelligence.domain.dataset import Dataset
from pathlib                                   import Path

class DatasetPathBuilder:
    """
    Builds standardized filesystem paths for datasets
    within the MRI data lake.
    """
    DATA_PATH = Path("data")
    DATA_LAKE = DATA_PATH / "lake"

    @classmethod
    def raw(cls, dataset: Dataset) -> Path:
        return (
            cls.DATA_LAKE
            / "raw"
            / dataset.category.value
            / f"{dataset.name}.csv"
        )

    @classmethod
    def validated(cls, dataset: Dataset) -> Path:
        return (
            cls.DATA_LAKE
            / "validated"
            / dataset.category.value
            / f"{dataset.name}.csv"
        )

    @classmethod
    def canonical(cls, dataset: Dataset) -> Path:
        return (
            cls.DATA_LAKE
            / "canonical"
            / dataset.category.value
            / f"{dataset.name}.csv"
        )

    @classmethod
    def archive(cls, dataset: Dataset) -> Path:
        return (
            cls.DATA_LAKE
            / "archive"
            / dataset.category.value
            / f"{dataset.name}.csv"
        )

    @classmethod
    def features(cls, dataset: Dataset) -> Path:
        return (
            cls.DATA_PATH
            / "features"
            / dataset.category.value
            / f"{dataset.name}.csv"
        )

    @classmethod
    def labels(cls, dataset: Dataset) -> Path:
        return (
            cls.DATA_PATH
            / "labels"
            / dataset.category.value
            / f"{dataset.name}.csv"
        )

    @classmethod
    def datasets(cls, dataset: Dataset) -> Path:
        return (
            cls.DATA_PATH
            / "datasets"
            / dataset.category.value
            / f"{dataset.name}.csv"
        )