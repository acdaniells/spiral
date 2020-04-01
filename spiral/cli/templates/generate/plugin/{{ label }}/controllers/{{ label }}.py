"""
{{ label }} plug-in controller.
"""

from spiral import Controller, ex


class {{ class_name }}(Controller):
    class Meta:
        label = "{{ label }}"
        stacked_on = "base"
        stacked_type = "nested"

    def _default(self):
        self._parser.print_help()

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

        data = {"foo": "bar"}

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data["foo"] = self.app.pargs.foo

        self.app.render(data, "plugins/{{ label }}/command.jinja2")
