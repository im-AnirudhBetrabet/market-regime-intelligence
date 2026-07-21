from __future__ import annotations

from market_regime_intelligence.cli.characterize import characterize_app
from market_regime_intelligence.cli.ingest       import ingest_app
from market_regime_intelligence.cli.predict      import predict_app
from market_regime_intelligence.cli.train        import train_app
from market_regime_intelligence.cli.validate     import validate_app
from market_regime_intelligence.cli.clean        import clean_app
from market_regime_intelligence.config           import get_settings
from market_regime_intelligence.logging          import configure_logging
import typer

settings = get_settings()

configure_logging(settings.logging.level)

app = typer.Typer(
    help="Market Regime Intelligence CLI",
    no_args_is_help=True,
)

app.add_typer(ingest_app      , name="ingest"      )
app.add_typer(validate_app    , name="validate"    )
app.add_typer(characterize_app, name="characterize")
app.add_typer(train_app       , name="train"       )
app.add_typer(predict_app     , name="predict"     )
app.add_typer(clean_app       , name="clean"       )
@app.command()
def version() -> None:
    """
    Display application version.
    """
    typer.echo("Market Regime Intelligence v0.1.0")