"""
Data ingestion pipeline
"""
from __future__                                      import annotations
from datetime                                        import date
from market_regime_intelligence.ingestion.models     import DownloadResult, DownloadRequest
from market_regime_intelligence.validation.validator import DatasetValidator
from market_regime_intelligence.common.file_reader   import CSVReader
from market_regime_intelligence.common.file_writer   import CSVWriter
from market_regime_intelligence.common.path_builder  import DatasetPathBuilder
from market_regime_intelligence.config.settings      import settings
from market_regime_intelligence.domain.dataset       import Dataset

class IngestionPipeline:
    """
    Downloads, validates and stores market datasets.
    """
    def __init__(self, datasource):
        self._datasource = datasource
        self._reader     = CSVReader()
        self._writer     = CSVWriter()
        self._validator  = DatasetValidator()

    def run(self, dataset: Dataset) -> DownloadResult:
        """
        Download and validate a dataset.

        Args:
             dataset:
                Dataset defined from the registry.

        Returns:
            DownloadResult
        """
        request = DownloadRequest(
            symbol=dataset.symbol,
            interval=dataset.interval,
            start_date=settings.data.start_date,
            end_date=settings.data.end_date
        )

        raw_path       = DatasetPathBuilder.raw(dataset)
        validated_path = DatasetPathBuilder.validated(dataset)

        dataframe      = self._datasource.download(request)

        self._writer.write(dataframe, raw_path)

        dataframe  = self._reader.read(raw_path)
        validation = self._validator.validate(dataframe)

        if not validation.passed:
            raise ValueError("\n".join(validation.errors))

        self._writer.write(dataframe, validated_path)

        return DownloadResult(
            symbol=dataset.symbol,
            rows=len(dataframe),
            output_path=validated_path
        )