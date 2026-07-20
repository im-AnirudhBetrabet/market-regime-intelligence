from __future__ import annotations

import typer

validate_app = typer.Typer()

@validate_app.command("run")
def run() -> None:
    """
    Run validation.
    """
    typer.echo("Running validation...")