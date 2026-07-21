from market_regime_intelligence.cleaning.cleaner   import MarketDataCleaner
from market_regime_intelligence.cleaning.pipeline  import CleaningPipeline
from market_regime_intelligence.cleaning.writer    import CanonicalDataWriter
from market_regime_intelligence.common.file_reader import CSVReader
from market_regime_intelligence.domain.datasets    import datasets
from pathlib                                       import Path

import typer

clean_app = typer.Typer(help="Clean validated market data.")

@clean_app.command("run")
def run() -> None:
    typer.echo("Cleaning validated dataset..")
    pipeline = CleaningPipeline(
        reader=CSVReader(),
        cleaner=MarketDataCleaner(),
        writer=CanonicalDataWriter()
    )

    enabled_data = datasets.enabled()
    for dataset in enabled_data:
        result = pipeline.run(dataset)
        typer.echo(f"Cleaned {dataset.name} successfully..")
        typer.echo(f"Rows before : {result.rows_before}")
        typer.echo(f"Rows after  : {result.rows_after}")
        typer.echo(f"Duplicates  : {result.duplicates_removed}")
        typer.echo(f"Missing     : {result.missing_rows_removed}")