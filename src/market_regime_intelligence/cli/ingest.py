from __future__ import annotations

import typer
from datetime                                      import date
from pathlib                                       import Path
from market_regime_intelligence.domain.datasets    import datasets
from market_regime_intelligence.ingestion.factory import DataSourceFactory
from market_regime_intelligence.ingestion.pipeline import IngestionPipeline

ingest_app = typer.Typer()

@ingest_app.command("run")
def run() -> None:
    """
    Run the ingestion pipeline.
    """
    typer.echo("Running ingestion pipeline..")
    enabled_dataset   = datasets.enabled()
    typer.echo(f"Ingesting {len(enabled_dataset)} datasets..")

    for dataset in enabled_dataset:
        typer.echo(f"Ingesting data for {dataset.name} ..")
        try:
            pipeline = IngestionPipeline(
                datasource=DataSourceFactory.create(dataset.provider)
            )
            result = pipeline.run(dataset)
            typer.echo(result)
            typer.echo(f"Successfully ingested data for {dataset.name} ..")
        except NotImplementedError as exc:
            pass
        except Exception as exc:
            typer.echo(f"Failed due to error: {str(exc)}")
    typer.echo("Ingestion pipeline ran successfully.")