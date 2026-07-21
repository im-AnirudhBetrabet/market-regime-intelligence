from market_regime_intelligence.cleaning.cleaner   import MarketDataCleaner
from market_regime_intelligence.cleaning.pipeline  import CleaningPipeline
from market_regime_intelligence.cleaning.writer    import CanonicalDataWriter
from market_regime_intelligence.common.file_reader import CSVReader
from pathlib                                       import Path
import typer

clean_app = typer.Typer(help="Clean validated market data.")

@clean_app.command("run")
def run() -> None:
    pipeline = CleaningPipeline(
        reader=CSVReader(),
        cleaner=MarketDataCleaner(),
        writer=CanonicalDataWriter()
    )

    result = pipeline.run(
        input_path=Path("data/lake/validated/nifty.csv"),
        output_path=Path("data/lake/canonical/nifty.csv")
    )

    typer.echo(f"Cleaning completed successfully..")
    typer.echo(f"Rows before : {result.rows_before}")
    typer.echo(f"Rows after  : {result.rows_after}")
    typer.echo(f"Duplicates  : {result.duplicates_removed}")
    typer.echo(f"Missing     : {result.missing_rows_removed}")
