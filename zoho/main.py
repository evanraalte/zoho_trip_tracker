import contextlib
import datetime

from typing_extensions import Annotated
import typer
from sqlmodel import Session, create_engine
from sqlmodel import SQLModel, select
app = typer.Typer()

from zoho.models import Preset

sqllite_file = "zoho.db"
sqllite_url = f"sqlite:///{sqllite_file}"

engine = create_engine(sqllite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@contextlib.contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

stored_presets = {}

def reset_app_state() -> None:
    global stored_presets
    stored_presets = {}

@app.command(help="Add a preset")
def add_preset(
    title: Annotated[str, typer.Option(prompt=True)],
    distance: Annotated[int, typer.Option(prompt=True)],
) -> None:
    if title in stored_presets.keys():
        typer.echo("Title already exists")
        raise typer.Exit(1)
    stored_presets[title] = distance


    typer.echo(f"Added preset: {title} ({distance}km)")


@app.command(help="Show presets")
def show_presets():

    with get_session() as session:
        pass
    for title, distance in stored_presets.items():
        typer.echo(f"{title} ({distance}km)")
    return

@app.command(help="Add a trip")
def add_trip(preset: Annotated[str, typer.Option(help="the preset",autocompletion=stored_presets.keys())], date: Annotated[str, typer.Option(help="Y-m-d")] = None) -> None:
    date = date or datetime.date.today().strftime("%Y-%m-%d")

    if preset not in stored_presets.keys():
        typer.echo(f"Error: Invalid value for '--preset': {preset} is not a valid preset.")
        raise typer.Exit(2)
    pass
    typer.echo(f"Added trip: {preset} ({stored_presets[preset]}km) on {date}")



if __name__ == "__main__":
    create_db_and_tables()
    app()
