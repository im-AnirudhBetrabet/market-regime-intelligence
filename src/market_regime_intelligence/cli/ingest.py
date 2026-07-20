from __future__ import annotations

import typer

ingest_app = typer.Typer()

@ingest_app.command("run")
def run() -> None:
    """
    Run the ingestion pipeline.
    """
    typer.echo("Running ingestion pipeline..")