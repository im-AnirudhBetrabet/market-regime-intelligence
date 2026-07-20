from __future__ import annotations

import typer

train_app = typer.Typer()

@train_app.command("run")
def run() -> None:
    """
    Run model training.
    """
    typer.echo("Running training...")