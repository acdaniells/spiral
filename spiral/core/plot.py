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
    The Plot Interface class.

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
    def make_figure(self, args, constructor):
        """
        Make figure abstract method.
        """
        pass  # pragma: nocover

    @abstractmethod
    def scatter(self, *args, **kwargs):
        """
        Scatter plot abstract method.
        """
        pass  # pragma: nocover

    @abstractmethod
    def bar(self, *args, **kwargs):
        """
        Bar chart abstract method.
        """
        pass  # pragma: nocover

    @abstractmethod
    def line(self, *args, **kwargs):
        """
        Line plot abstract method.
        """
        pass  # pragma: nocover

    @abstractmethod
    def box(self, *args, **kwargs):
        """
        Box plot abstract method.
        """
        pass  # pragma: nocover

    @abstractmethod
    def violin(self, *args, **kwargs):
        """
        Violin plot abstract method.
        """
        pass  # pragma: nocover

    @abstractmethod
    def pie(self, *args, **kwargs):
        """
        Pie chart abstract method.
        """
        pass  # pragma: nocover


class PlotHandler(PlotInterface, Handler):

    """
    Plot handler implementation.
    """

    pass  # pragma: nocover
