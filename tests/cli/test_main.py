import os

from spiral.cli.main import SpiralTestApp as App, main

from pytest import raises


def test_main(tmp):
    with raises(SystemExit):
        main()


def test_app():
    argv = []

    with App(argv=argv) as app:
        no_base_controller_retval = app.run()
        assert no_base_controller_retval is None


def test_generate(tmp):
    argv = ["generate", "project", tmp.dir, "--defaults"]

    with App(argv=argv) as app:
        app.run()

        assert os.path.exists(os.path.join(tmp.dir, "setup.py"))
