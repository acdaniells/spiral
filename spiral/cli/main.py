#!/usr/bin/env python3

"""
Spiral developer application main module.
"""

from spiral import App, CaughtSignal
from spiral.cli.controllers.base import Base


class SpiralApp(App):

    """
    Spiral developer application.
    """

    class Meta:
        label = "spiral"
        controller = "base"
        template_module = "spiral.cli.templates"
        template_handler = "jinja2"
        config_handler = "yaml"
        config_file_suffix = ".yml"
        extensions = ["generate", "yaml", "jinja2"]
        handlers = [Base]


class SpiralTestApp(SpiralApp):

    """
    Spiral testing application.
    """

    class Meta:
        argv = []
        config_files = []
        exit_on_close = False


def main(argv=None):
    with SpiralApp() as app:
        try:
            app.run()
        except AssertionError as e:  # pragma: nocover
            print(f"AssertionError > {e.args[0]}")  # pragma: nocover
            app.exit_code = 1  # pragma: nocover
        except CaughtSignal as e:  # pragma: nocover
            print(f"\n{e}")  # pragma: nocover
            app.exit_code = 0  # pragma: nocover


if __name__ == "__main__":
    main()  # pragma: nocover
