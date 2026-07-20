from __future__ import annotations
import typer

characterize_app = typer.Typer()

@characterize_app.command("run")
def run() -> None:
    """
    Run market characterization.
    """
    typer.echo("Running market characterization...")