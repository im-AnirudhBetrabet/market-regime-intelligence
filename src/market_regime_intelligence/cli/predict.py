from __future__ import annotations
import typer

predict_app = typer.Typer()

@predict_app.command("run")
def run() -> None:
    """
    Run inference.
    """
    typer.echo("Running prediction...")