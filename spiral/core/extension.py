"""
Spiral core extensions module.
"""

import sys

from spiral.core.exc import SpiralError

from cement.core.extension import ExtensionInterface
from cement.core.handler import Handler
from cement.utils.misc import minimal_logger

LOG = minimal_logger(__name__)


class ExtensionHandler(ExtensionInterface, Handler):

    """
    Extension handler class.

    This handler implements the Extension Interface, which handles
    loading framework extensions. All extension handlers should sub-
    class from here, or ensure that their implementation meets the
    requirements of this base class.

    """

    class Meta:

        """
        Handler meta-data.
        """

        label = "spiral"
        """The string identifier of the handler."""

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = None
        self._loaded_extensions = []

    def get_loaded_extensions(self):
        """
        Get all loaded extensions.

        Returns
        -------
        list
            A list of loaded extensions.

        """
        return self._loaded_extensions

    def list(self):
        """
        Get all loaded extensions.

        Synonymous with ``get_loaded_extensions()``.

        Returns
        -------
        list
            A list of loaded extensions.

        """
        return self._loaded_extensions

    def load_extension(self, ext_module):
        """
        Load an extension.

        Parameters
        ----------
        ext_module : str
            The extension module name. For example: ``spiral.ext.ext_logging``.

        Raises
        ------
        SpiralError
            Raised if ``ext_module`` can not be loaded.

        """
        # If its not a full module path then prepend our default path
        if ext_module.find(".") == -1:
            ext_module = f"spiral.ext.ext_{ext_module}"

        if ext_module in self._loaded_extensions:
            LOG.debug(f"framework extension '{ext_module}' already loaded")
            return

        LOG.debug(f"loading the '{ext_module}' framework extension")

        # try loading the extension from Spiral
        try:
            self._load_extension(ext_module)
        except ImportError:
            # try loading the extension from Cement
            try:
                self._load_extension(ext_module.replace("spiral", "cement"))
            except ImportError as e:
                raise SpiralError(e.args[0])

    def _load_extension(self, ext_module):
        if ext_module not in sys.modules:
            __import__(ext_module, globals(), locals(), [], 0)

        if hasattr(sys.modules[ext_module], "load"):
            sys.modules[ext_module].load(self.app)

        if ext_module not in self._loaded_extensions:
            self._loaded_extensions.append(ext_module)

    def load_extensions(self, ext_list):
        """
        Load extensions.

        Iterates over the list of extension modules passing each to
        ``self.load_extension()``.

        Parameters
        ----------
        ext_list : list
            A list of extension module names.

        """
        for ext in ext_list:
            self.load_extension(ext)
