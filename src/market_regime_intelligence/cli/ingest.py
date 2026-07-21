from __future__ import annotations


import typer
from datetime                                      import date
from pathlib                                       import Path
from market_regime_intelligence.ingestion.models   import DownloadRequest
from market_regime_intelligence.ingestion.pipeline import IngestionPipeline
from market_regime_intelligence.ingestion.yahoo    import YahooFinanceDataSource

ingest_app = typer.Typer()

@ingest_app.command("run")
def run() -> None:
    """
    Run the ingestion pipeline.
    """
    typer.echo("Running ingestion pipeline..")
    pipeline = IngestionPipeline(YahooFinanceDataSource())

    result   = pipeline.run(
        DownloadRequest(
            symbol="^NSEI",
            interval="1d",
            start_date=date(2010, 1, 1),
            end_date=date.today()
        ),
        raw_path=Path("data/lake/raw/nifty.csv"),
        validated_path=Path("data/lake/validated/nifty.csv")
    )

    typer.echo(result)