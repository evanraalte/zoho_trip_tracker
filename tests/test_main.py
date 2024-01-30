import datetime
from zoho.main import app, reset_app_state
from typer.testing import CliRunner

runner = CliRunner()

add_preset = lambda title,distance:  runner.invoke(
    app,
    args=["add-preset"],
    input=f"{title}\n{distance}\n",
)

def setup_function(function):
    reset_app_state()  # Reset the state before each test


def test_main_has_add_preset_command():
    result = runner.invoke(app, args=["add-preset"], input="My preset\n15\n")
    assert "Added preset: My preset (15km)" in result.output
    assert result.exit_code == 0

def test_main_add_preset_needs_unique_title():


    result = add_preset("My preset", 15)
    assert "Added preset: My preset (15km)" in result.output

    result = add_preset("My preset", 15)
    assert "Title already exists" in result.output
    assert result.exit_code == 1

    result = add_preset("My preset", 10)
    assert "Title already exists" in result.output
    assert result.exit_code == 1

    result = add_preset("My other preset", 10)
    assert "Added preset: My other preset (10km)" in result.output
    assert result.exit_code == 0


def test_shows_presets():
    for n in range(10):
        add_preset(f"preset {n}", n)
    result = runner.invoke(
        app,
        args=["presets"],
    )
    assert result.exit_code == 0
    assert len(result.output.splitlines()) == 10

def test_add_trip_needs_preset():
    result = runner.invoke(app, args=["add-trip"])
    assert "Error: Missing option '--preset'" in result.output
    assert result.exit_code == 2

def test_add_trip_needs_valid_preset():
    result = runner.invoke(app, args=["add-trip", "--preset", "invalid"])
    assert "Error: Invalid value for '--preset': invalid is not a valid preset." in result.output
    assert result.exit_code == 2

def test_add_trip_defaults_to_today():
    add_preset("My preset", 15)
    result = runner.invoke(app, args=["add-trip", "--preset", "My preset"])
    today = datetime.date.today().strftime("%Y-%m-%d")
    assert f"Added trip: My preset (15km) on {today}" in result.output
    assert result.exit_code == 0

def test_add_trip_can_take_date():
    add_preset("My preset", 15)
    result = runner.invoke(app, args=["add-trip", "--preset", "My preset", "--date", "2020-01-01"])
    assert "Added trip: My preset (15km) on 2020-01-01" in result.output
    assert result.exit_code == 0

def test_rm_trip_needs_id():
    pass

def test_show_trips():
    pass

def test_show_trips_can_filter_by_dates():
    pass
