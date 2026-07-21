from __future__ import annotations

import typer
from datetime                                      import date
from pathlib                                       import Path
from market_regime_intelligence.domain.datasets    import datasets
from market_regime_intelligence.ingestion.pipeline import IngestionPipeline
from market_regime_intelligence.ingestion.yahoo    import YahooFinanceDataSource

ingest_app = typer.Typer()

@ingest_app.command("run")
def run() -> None:
    """
    Run the ingestion pipeline.
    """
    typer.echo("Running ingestion pipeline..")
    yfinance_pipeline = IngestionPipeline(YahooFinanceDataSource())
    yf_dataset        = datasets.by_provider("yahoo")
    typer.echo(f"Ingesting {len(yf_dataset)} datasets from yfinance..")
    for dataset in yf_dataset:
        typer.echo(f"Ingesting data for {dataset.name} ..")
        result = yfinance_pipeline.run(dataset)
        typer.echo(result)
        typer.echo(f"Successfully ingested data for {dataset.name} ..")
    typer.echo("Ingestion pipeline ran successfully.")