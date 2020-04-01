from pytest import raises

from {{label}}.main import {{ class_name }}Test


def test_{{ label }}():
    # test {{ label }} without any subcommands or arguments
    with {{ class_name }}Test() as app:
        app.run()
        assert app.exit_code == 0


def test_{{ label }}_debug():
    # test that debug mode is functional
    argv = ["--debug"]
    with {{ class_name }}Test(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command():
    # test command without arguments
    argv = ["command"]
    with {{ class_name }}Test(argv=argv) as app:
        app.run()
        data, output = app.last_rendered
        assert data["foo"] == "bar"
        assert output.find("Foo => bar")

    # test command with arguments
    argv = ["command", "--foo", "not-bar"]
    with {{ class_name }}Test(argv=argv) as app:
        app.run()
        data, output = app.last_rendered
        assert data["foo"] == "not-bar"
        assert output.find("Foo => not-bar")
