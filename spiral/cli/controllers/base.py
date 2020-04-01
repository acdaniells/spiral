"""
Spiral developer base controller.
"""

from spiral import Controller, get_version

from cement.utils.version import get_version_banner

VERSION_BANNER = f"""
Spiral Framework v{get_version()}
{get_version_banner()}
"""


class Base(Controller):
    class Meta:
        label = "base"
        description = "Spiral Framework Developer Tools"
        title = "commands"
        subparser_options = {"metavar": "<command>"}
        epilog = "Example: spiral generate project /path/to/myapp"
        arguments = [
            (["-v", "--version"], {"action": "version", "version": VERSION_BANNER})
        ]

    def _default(self):
        self.app.args.print_help()
