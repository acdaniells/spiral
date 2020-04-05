"""
Spiral generate extension module.
"""

import inspect
import os
import re
import shutil

from spiral import Controller
from spiral.core.version import VERSION, get_version

import yaml

from cement import minimal_logger, shell

LOG = minimal_logger(__name__)


class GenerateTemplateAbstractBase(Controller):

    """
    Generate template abstract base controller.
    """

    class Meta:

        """
        Controller meta-data.
        """

        pass

    def _generate(self, source, dest):  # noqa: C901
        self.app.log.info(
            f"Generating {self.app._meta.label} {self._meta.label} in {dest}"
        )

        data = {}

        # built-in variables
        maj_min = float("{}.{}".format(VERSION[0], VERSION[1]))
        data["spiral"] = {}
        data["spiral"]["version"] = get_version()
        data["spiral"]["major_version"] = VERSION[0]
        data["spiral"]["minor_version"] = VERSION[1]
        data["spiral"]["major_minor_version"] = maj_min

        fp = open(os.path.join(source, ".generate.yml"))
        yaml_load = yaml.full_load if hasattr(yaml, "full_load") else yaml.load
        g_config = yaml_load(fp)
        fp.close()

        variable_definitions = g_config.get("variables", {})
        excludes = g_config.get("exclude", [])
        ignores = g_config.get("ignore", [])

        # default ignore the .generate.yml config
        g_config_yml = r"^(.*)[\/\\\\]%s[\/\\\\]\.generate\.yml$" % self._meta.label
        ignores.append(g_config_yml)

        var_defaults = {
            "name": None,
            "prompt": None,
            "validate": None,
            "case": None,
            "default": None,
        }

        for var_def in variable_definitions:
            defs = var_defaults.copy()
            defs.update(var_def)

            for key in ["name", "prompt"]:
                assert (
                    defs[key] is not None
                ), f"Required generate config key missing: {key}"

            value = None
            if defs["default"] is not None and self.app.pargs.defaults:
                value = defs["default"]

            elif defs["default"] is not None:
                default_text = f" [{defs['default']}]"

            else:
                default_text = ""  # pragma: nocover

            if value is None:

                class MyPrompt(shell.Prompt):
                    class Meta:
                        text = f"{defs['prompt']}{default_text}:"
                        default = defs.get("default", None)

                prompt = MyPrompt()
                value = prompt.prompt()  # pragma: nocover

            if defs["case"] in ["lower", "upper", "title"]:
                value = getattr(value, defs["case"])()
            elif defs["case"] is not None:
                self.app.log.warning(
                    f"Invalid configuration for variable '{defs['name']}': "
                    + "case must be one of lower, upper, or title."
                )

            if defs["validate"] is not None:
                assert re.match(
                    defs["validate"], value
                ), f"Invalid Response (must match: '{defs['validate']}')"

            data[defs["name"]] = value

        try:
            self.app.template.copy(
                source,
                dest,
                data,
                force=self.app.pargs.force,
                ignore=ignores,
                exclude=excludes,
            )
        except AssertionError as e:
            if re.match("(.*)already exists(.*)", e.args[0]):
                raise AssertionError(e.args[0] + " (try: --force)")
            else:
                raise  # pragma: nocover

    def _clone(self, source, dest):
        self.app.log.info(
            f"Cloning {self.app._meta.label} {self._meta.label} template to {dest}"
        )

        if os.path.exists(dest) and self.app.pargs.force is True:
            shutil.rmtree(dest)
        elif os.path.exists(dest):
            msg = f"Destination path already exists: {dest} (try: --force)"
            raise AssertionError(msg)

        shutil.copytree(source, dest)

    def _default(self):
        source = self._meta.source_path
        dest = self.app.pargs.dest

        if self.app.pargs.clone is True:
            self._clone(source, dest)
        else:
            self._generate(source, dest)


def setup_template_items(app):
    """
    Add template controllers to the application.
    """
    template_dirs = []
    template_items = []

    # look in app template dirs
    for path in app._meta.template_dirs:
        subpath = os.path.join(path, "generate")
        if os.path.exists(subpath) and subpath not in template_dirs:
            template_dirs.append(subpath)

    # use app template module, find it's path on filesystem
    if app._meta.template_module is not None:
        mod_parts = app._meta.template_module.split(".")
        mod = mod_parts.pop()
        try:
            mod = app.__import__(mod, from_module=".".join(mod_parts))
            mod_path = os.path.dirname(inspect.getfile(mod))
            subpath = os.path.join(mod_path, "generate")

            if os.path.exists(subpath) and subpath not in template_dirs:
                template_dirs.append(subpath)

        # FIXME: not exactly sure how to test for this so not covering
        except AttributeError:  # pragma: nocover
            msg = "unable to load template module" + "{} from {}".format(
                mod, ".".join(mod_parts)
            )  # pragma: nocover
            app.log.debug(msg)  # pragma: nocover

    for path in template_dirs:
        for item in os.listdir(path):
            if item not in template_items:
                template_items.append(item)

            class GenerateTemplate(GenerateTemplateAbstractBase):
                class Meta:
                    label = item
                    stacked_on = "generate"
                    stacked_type = "nested"
                    help = f"generate {item} from template"  # noqa: VNE003
                    arguments = [
                        (["dest"], {"help": "destination directory path"}),
                        (
                            ["-f", "--force"],
                            {
                                "help": "force operation if destination exists",
                                "dest": "force",
                                "action": "store_true",
                            },
                        ),
                        (
                            ["-D", "--defaults"],
                            {
                                "help": "use all default variable values",
                                "dest": "defaults",
                                "action": "store_true",
                            },
                        ),
                        (
                            ["--clone"],
                            {
                                "help": "clone this template to destination path",
                                "dest": "clone",
                                "action": "store_true",
                            },
                        ),
                    ]
                    source_path = os.path.join(path, item)

            app.handler.register(GenerateTemplate)


class Generate(Controller):

    """
    Generate controller.
    """

    class Meta:

        """
        Controller meta-data.
        """

        label = "generate"
        stacked_on = "base"
        stacked_type = "nested"
        config_section = "generate"
        subparser_options = {"metavar": "<sub-command>"}

    def _setup(self, app):
        super()._setup(app)

    def _default(self):
        self._parser.print_help()


def load(app):
    """
    Extension loader function.
    """
    app.handler.register(Generate)
    app.hook.register("pre_run", setup_template_items)
