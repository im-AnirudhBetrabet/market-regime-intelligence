"""
Data ingestion pipeline
"""
from __future__ import annotations
from pathlib    import Path

from market_regime_intelligence.ingestion.models     import DownloadResult, DownloadRequest
from market_regime_intelligence.validation.validator import DatasetValidator
from market_regime_intelligence.common.file_reader   import CSVReader
from market_regime_intelligence.common.file_writer   import CSVWriter
class IngestionPipeline:
    """
    Market data ingestion pipeline
    """
    def __init__(self, datasource):
        self.datasource = datasource
        self.reader     = CSVReader()
        self.writer     = CSVWriter()
        self.validator  = DatasetValidator()

    def run(self, request: DownloadRequest, raw_path: Path, validated_path: Path) -> DownloadResult:
        dataframe  = self.datasource.download(request)
        self.writer.write(dataframe, raw_path)

        dataframe  = self.reader.read(raw_path)
        result     = self.validator.validate(dataframe)

        if not result.passed:
            raise ValueError("\n".join(result.errors))

        self.writer.write(dataframe, validated_path)

        return DownloadResult(
            symbol=request.symbol,
            rows=len(dataframe),
            output_path=str(validated_path)
        )