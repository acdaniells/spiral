"""
Spiral core machine learning module.
"""

from abc import abstractmethod

from cement.core.handler import Handler
from cement.core.interface import Interface
from cement.utils.misc import minimal_logger

LOG = minimal_logger(__name__)


class MLInterface(Interface):

    """
    Machine learning interface class.

    Handlers that implement this interface must provide the methods and
    attributes defined below. In general, most implementations should
    sub-class from the provided :class:`MLHandler` base class as a
    starting point.

    """

    class Meta:

        """
        Interface meta-data.
        """

        interface = "ml"
        """The string identifier of the interface."""

    @abstractmethod
    def random_forest(self, *args, **kwargs):
        """
        Random forest abstract method.
        """
        pass  # pragma: nocover


class MLHandler(MLInterface, Handler):

    """
    Machine learning handler implementation.
    """

    pass  # pragma: nocover
