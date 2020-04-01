"""
Spiral core ml module.
"""

from abc import abstractmethod

from cement.core.handler import Handler
from cement.core.interface import Interface
from cement.utils.misc import minimal_logger

LOG = minimal_logger(__name__)


class MLInterface(Interface):

    """
    This class defines the ML Interface.

    Handlers that implement this
    interface must provide the methods and attributes defined below. In
    general, most implementations should sub-class from the provided
    :class:`MLHandler` base class as a starting point.

    """

    class Meta:

        """
        Interface meta-data.
        """

        interface = "ml"
        """The string identifier of the interface."""

    @abstractmethod
    def random_forest(self, *args, **kwargs):
        pass  # pragma: nocover


class MLHandler(MLInterface, Handler):

    """
    ML handler implementation.
    """

    pass  # pragma: nocover
