from market_regime_intelligence.cleaning.cleaner    import MarketDataCleaner
from market_regime_intelligence.cleaning.models     import CleaningResult
from market_regime_intelligence.cleaning.writer     import CanonicalDataWriter
from market_regime_intelligence.common.file_reader  import CSVReader
from market_regime_intelligence.domain.dataset      import Dataset
from market_regime_intelligence.common.path_builder import DatasetPathBuilder
from pathlib                                        import Path

class CleaningPipeline:
    def __init__(self, reader: CSVReader, cleaner: MarketDataCleaner, writer: CanonicalDataWriter):
        self._reader  = reader
        self._writer  = writer
        self._cleaner = cleaner

    def run(self, dataset: Dataset) -> CleaningResult:
        input_path         = DatasetPathBuilder.validated(dataset)
        output_path        = DatasetPathBuilder.canonical(dataset)
        df                 = self._reader.read(input_path)
        cleaned_df, result = self._cleaner.clean(df)
        self._writer.write(cleaned_df, output_path)
        result.output_path = output_path

        return result