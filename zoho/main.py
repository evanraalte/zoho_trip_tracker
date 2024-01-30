import datetime
from typing_extensions import Annotated
import typer

app = typer.Typer()


presets = {}

def reset_app_state() -> None:
    global presets
    presets = {}

@app.command()
def add_preset(
    title: Annotated[str, typer.Option(prompt=True)],
    distance: Annotated[int, typer.Option(prompt=True)],
) -> None:
    if title in presets.keys():
        typer.echo("Title already exists")
        raise typer.Exit(1)
    presets[title] = distance
    typer.echo(f"Added preset: {title} ({distance}km)")


@app.command()
def presets():
    for title, distance in presets.items():
        typer.echo(f"{title} ({distance}km)")
    return

@app.command()
def add_trip(preset: Annotated[str, typer.Option(help="the preset")]) -> None:
    date = datetime.date.today().strftime("%Y-%m-%d")

    if preset not in presets.keys():
        typer.echo(f"Error: Invalid value for '--preset': {preset} is not a valid preset.")
        raise typer.Exit(2)
    pass
    typer.echo(f"Added trip: {preset} ({presets[preset]}km) on {date}")

if __name__ == "__main__":
    app()
