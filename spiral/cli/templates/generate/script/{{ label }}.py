#!/usr/bin/env python3

"""
{{ label }} script.
"""

from spiral import App, CaughtSignal, Controller, ex, get_version

VERSION = (0, 0, 1, "alpha", 0)

VERSION_BANNER = f"""
{{ label }} v{get_version(VERSION)}
"""


class Base(Controller):
    class Meta:
        label = "base"

        # text displayed at the bottom of --help output
        epilog = "Usage: {{ label }} command --foo bar"

        arguments = [
            ### add a version banner
            (["-v", "--version"], {"action": "version", "version": VERSION_BANNER})
        ]

    def _default(self):
        """
        Default action if no sub-command is passed.
        """

        self.app.args.print_help()

    @ex(
        help="example sub-command",
        arguments=[
            ### add a sample foo option under sub-command namespace
            (
                ["-f", "--foo"],
                {"help": "notorious foo option", "action": "store", "dest": "foo"},
            )
        ],
    )
    def command(self):
        """
        Example sub-command.
        """

        ### do something with arguments
        if self.app.pargs.foo is not None:
            print(f"Foo Argument > {self.app.pargs.foo}")


class MyApp(App):
    class Meta:
        # application label
        label = "{{ label }}"

        # register handlers
        handlers = [Base]

        # call exit on close
        exit_on_close = True


def main():
    with MyApp() as app:
        try:
            app.run()
        except CaughtSignal as e:
            print(f"\n{e}")
            app.exit_code = 0


if __name__ == "__main__":
    main()
