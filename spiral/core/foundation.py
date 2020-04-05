"""
Spiral core foundation module.
"""

import logging
import os
import signal
import sys

from importlib import reload as reload_module

from spiral.core import extension, ml, plot
from spiral.ext.ext_argparse import ArgparseController as Controller

from cement.core import (
    arg,
    cache,
    config,
    controller,
    log,
    mail,
    output,
    plugin,
    template,
)
from cement.core.foundation import (
    App as CementApp,
    add_handler_override_options,
    handler_override,
)
from cement.core.handler import HandlerManager
from cement.core.hook import HookManager
from cement.core.interface import InterfaceManager
from cement.utils import misc
from cement.utils.misc import minimal_logger

join = os.path.join

LOG = minimal_logger(__name__)

SIGNALS = [signal.SIGTERM, signal.SIGINT, signal.SIGHUP]


class App(CementApp):

    """
    Primary application object class.
    """

    class Meta:

        """
        Application meta-data.
        """

        extension_handler = "spiral"
        """
        Handler class that implements the Extension interface.
        """

        plot_handler = "plotly"
        """
        Handler class that implements the Plot interface.
        """

        core_extensions = [
            "cement.ext.ext_dummy",
            "cement.ext.ext_plugin",
            "cement.ext.ext_configparser",
            "spiral.ext.ext_argparse",
            "spiral.ext.ext_logging",
            "spiral.ext.ext_plotly",
        ]
        """
        List of Spiral core extensions. These are generally required by
        Spiral and should only be modified if you know what you're
        doing. Use ``App.Meta.extensions`` to add to this list, rather than
        overriding core extensions. That said if you want to prune down
        your application, you can remove core extensions if they are
        not necessary (for example if using your own log handler
        extension you might not need/want ``LoggingLogHandler`` to be
        registered).
        """

        core_meta_override = [
            "debug",
            "plugin_dir",
            "ignore_deprecation_warnings",
            "template_dir",
            "mail_handler",
            "cache_handler",
            "log_handler",
            "output_handler",
            "template_handler",
            "plot_handler",
        ]
        """
        List of meta options that can/will be overridden by config options
        of the ``base`` config section (where ``base`` is the base
        configuration section of the application which is determined by
        ``App.Meta.config_section`` but defaults to ``App.Meta.label``). These
        overrides are required by the framework to function properly and should
        not be used by end-user (developers) unless you really know what
        you're doing. To add your own extended meta overrides you should use
        ``App.Meta.meta_override``.
        """

        core_interfaces = [
            extension.ExtensionInterface,
            log.LogInterface,
            config.ConfigInterface,
            mail.MailInterface,
            plugin.PluginInterface,
            output.OutputInterface,
            template.TemplateInterface,
            arg.ArgumentInterface,
            controller.ControllerInterface,
            cache.CacheInterface,
            plot.PlotInterface,
            ml.MLInterface,
        ]
        """
        List of core interfaces to be defined (by the framework). You should
        not modify this unless you really know what you're doing... instead,
        you probably want to add your own interfaces to
        ``App.Meta.interfaces``.
        """

    def __init__(self, label=None, **kw):
        self._loaded_bootstrap = None
        self.interface = None
        self.handler = None
        self.hook = None
        self.controller = None
        self.plot = None

        self._suppress_loggers()

        super().__init__(label, **kw)

    @staticmethod
    def _suppress_loggers():
        """
        Set logging level of non-application loggers to ERROR.
        """
        for name in logging.root.manager.loggerDict:
            logger = logging.getLogger(name)

            if "cement" not in name and "spiral" not in name:
                LOG.debug(f"Setting log level for '{name}' to ERROR")
                logger.setLevel(logging.ERROR)

    def _lay_cement(self):
        """
        Initialize the framework.
        """
        LOG.debug(f"laying cement for the '{self._meta.label}' application")

        self.interface = InterfaceManager(self)
        self.handler = HandlerManager(self)
        self.hook = HookManager(self)

        # define framework hooks
        self.hook.define("pre_setup")
        self.hook.define("post_setup")
        self.hook.define("pre_run")
        self.hook.define("post_run")
        self.hook.define("pre_argument_parsing")
        self.hook.define("post_argument_parsing")
        self.hook.define("pre_close")
        self.hook.define("post_close")
        self.hook.define("signal")
        self.hook.define("pre_render")
        self.hook.define("post_render")

        # define application hooks from meta
        for label in self._meta.define_hooks:
            self.hook.define(label)

        # register some built-in framework hooks
        self.hook.register("post_setup", add_handler_override_options, weight=-99)
        self.hook.register("post_argument_parsing", handler_override, weight=-99)

        # register application hooks from meta. the hooks listed in
        # App.Meta.hooks are registered here, so obviously can not be
        # for any hooks other than the builtin framework hooks that we just
        # defined here (above). Anything that we couldn't register here
        # will be retried after setup
        self.__retry_hooks__ = []
        for hook_spec in self._meta.hooks:
            if not self.hook.defined(hook_spec[0]):
                LOG.debug(f"hook {hook_spec[0]} not defined, will retry after setup")
                self.__retry_hooks__.append(hook_spec)
            else:
                self.hook.register(*hook_spec)

        # define interfaces
        for i in self._meta.core_interfaces:
            self.interface.define(i)

        for i in self._meta.interfaces:
            self.interface.define(i)

        # extension handler is the only thing that can't be loaded... as,
        # well, an extension. ;)
        self.handler.register(extension.ExtensionHandler)

        # register application handlers
        for handler_class in self._meta.handlers:
            self.handler.register(handler_class)

    def setup(self):
        """
        Application setup method.

        This method wraps all ``_setup`` actons in one call. It is called
        before ``self.run()``, allowing the application to be setup but not
        executed (possibly letting the developer perform other actions before
        full execution).

        All handlers should be instantiated and callable after setup is
        complete.

        """
        LOG.debug(f"now setting up the '{self._meta.label}' application")

        if self._meta.bootstrap is not None:
            LOG.debug(f"importing bootstrap code from {self._meta.bootstrap}")

            if (
                self._meta.bootstrap not in sys.modules
                or self._loaded_bootstrap is None
            ):
                __import__(self._meta.bootstrap, globals(), locals(), [], 0)
                if hasattr(sys.modules[self._meta.bootstrap], "load"):
                    sys.modules[self._meta.bootstrap].load(self)

                self._loaded_bootstrap = sys.modules[self._meta.bootstrap]
            else:
                reload_module(self._loaded_bootstrap)

        for _result in self.hook.run("pre_setup", self):
            pass  # pragma: nocover

        self._setup_extension_handler()
        self._setup_signals()
        self._setup_config_handler()
        self._setup_mail_handler()
        self._setup_cache_handler()
        self._setup_log_handler()
        self._setup_plugin_handler()
        self._setup_arg_handler()
        self._setup_output_handler()
        self._setup_template_handler()
        self._setup_controllers()
        self._setup_plot_handler()

        for hook_spec in self.__retry_hooks__:
            self.hook.register(*hook_spec)

        for _result in self.hook.run("post_setup", self):
            pass

    def _setup_controllers(self):
        LOG.debug("setting up application controllers")

        if self.handler.registered("controller", "base"):
            self.controller = self._resolve_handler("controller", "base")
        else:

            class DefaultBaseController(Controller):
                class Meta:
                    label = "base"

                def _default(self):
                    # don't enforce anything cause developer might not be
                    # using controllers... if they are, they should define
                    # a base controller.
                    pass

            self.handler.register(DefaultBaseController)
            self.controller = self._resolve_handler("controller", "base")

    def _setup_plot_handler(self):
        self.plot = self._resolve_handler("plot", self._meta.plot_handler)


class TestApp(App):

    """
    Testing application.
    """

    # tells pytest to not consider this a class for testing
    __test__ = False

    class Meta:

        """
        Test application meta-data.
        """

        label = f"app-{misc.rando()[:12]}"
        argv = []
        core_system_config_files = []
        core_user_config_files = []
        config_files = []
        core_system_config_dirs = []
        core_user_config_dirs = []
        config_dirs = []
        core_system_template_dirs = []
        core_user_template_dirs = []
        core_system_plugin_dirs = []
        core_user_plugin_dirs = []
        plugin_dirs = []
        exit_on_close = False
