"""
Spiral core plot module.
"""

from abc import abstractmethod

from cement.core.handler import Handler
from cement.core.interface import Interface
from cement.utils.misc import minimal_logger

LOG = minimal_logger(__name__)


class PlotInterface(Interface):

    """
    This class defines the Plot Interface.

    Handlers that implement this
    interface must provide the methods and attributes defined below. In
    general, most implementations should sub-class from the provided
    :class:`PlotHandler` base class as a starting point.

    """

    class Meta:

        """
        Interface meta-data.
        """

        interface = "plot"
        """The string identifier of the interface."""

    @abstractmethod
    def bar(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def scatter(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def line(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def heatmap(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def pie(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def box(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def violin(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def hist(self, *args, **kwargs):
        pass  # pragma: nocover

    @abstractmethod
    def hist2d(self, *args, **kwargs):
        pass  # pragma: nocover


class PlotHandler(PlotInterface, Handler):

    """
    Plot handler implementation.
    """

    pass  # pragma: nocover
