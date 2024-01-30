from zoho.main import app, reset_app_state
from typer.testing import CliRunner

runner = CliRunner()

def setup_function(function):
    reset_app_state()  # Reset the state before each test


def test_main_has_add_preset_command():
    result = runner.invoke(app, args=["add-preset"], input="My preset\n15\n")
    assert "Added preset: My preset (15km)" in result.output
    assert result.exit_code == 0

def test_main_add_preset_needs_unique_title():
    add_preset = lambda title,distance:  runner.invoke(
        app,
        args=["add-preset"],
        input=f"{title}\n{distance}\n",
    )

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

def test_add_trip_needs_preset():
    result = runner.invoke(app, args=["add-trip"])
    assert "Error: Missing option '--preset'" in result.output
    assert result.exit_code == 2

