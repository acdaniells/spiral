from spiral.core.foundation import TestApp
from spiral.core.ml import MLHandler, MLInterface

from pytest import raises

# module tests


class TestMLInterface:
    def test_interface(self):
        assert MLInterface.Meta.interface == "ml"


class TestMLHandler:
    def test_subclassing(self):
        class MyMLHandler(MLHandler):
            class Meta:
                label = "my_ml_handler"

            def random_forest(self):
                pass

        h = MyMLHandler()
        assert h._meta.interface == "ml"
        assert h._meta.label == "my_ml_handler"


# app functionality and coverage tests


def test_unproviding_handler():
    class BogusHandler(MLHandler):
        class Meta:
            label = "bogus"

    with TestApp() as app:
        msg = "Can't instantiate abstract class .* with abstract methods"
        with raises(TypeError, match=msg):
            app.handler.register(BogusHandler)
