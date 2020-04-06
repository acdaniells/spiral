"""
Spiral scikit-learn extension module.
"""

from spiral.core.ml import MLHandler

from cement.utils.misc import minimal_logger

LOG = minimal_logger(__name__)


class SklearnMLHandler(MLHandler):

    """
    Scikit-learn handler class.

    This class is an implementation of the :ref:`Plot <spiral.core.ml>`
    interface using the scikit-learn machine learning library.

    """

    class Meta:

        """
        Handler meta-data.
        """

        label = "sklearn"
        """The string identifier for this handler."""

        config_defaults = {}
        """Configuration default values."""

    def random_forest(self):
        """
        Random forest model builder.
        """


def extend_app(app):
    """
    Extend the application object.
    """
    app.extend("sklearn", app.handler.resolve("ml", "sklearn"))


def load(app):
    """
    Extension loader function.
    """
    app.handler.register(SklearnMLHandler)
    app.hook.register("post_setup", extend_app)
