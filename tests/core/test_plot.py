from spiral.core.foundation import TestApp
from spiral.core.plot import PlotHandler, PlotInterface

from pytest import raises

# module tests


class TestPlotInterface:
    def test_interface(self):
        assert PlotInterface.Meta.interface == "plot"


class TestPlotHandler:
    def test_subclassing(self):
        class MyPlotHandler(PlotHandler):
            class Meta:
                label = "my_plot_handler"

            def bar(self, *args, **kwargs):
                pass

            def scatter(self, *args, **kwargs):
                pass

            def line(self, *args, **kwargs):
                pass

            def heatmap(self, *args, **kwargs):
                pass

            def pie(self, *args, **kwargs):
                pass

            def box(self, *args, **kwargs):
                pass

            def violin(self, *args, **kwargs):
                pass

            def hist(self, *args, **kwargs):
                pass

            def hist2d(self, *args, **kwargs):
                pass

        h = MyPlotHandler()
        assert h._meta.interface == "plot"
        assert h._meta.label == "my_plot_handler"


# app functionality and coverage tests


def test_unproviding_handler():
    class BogusHandler(PlotHandler):
        class Meta:
            label = "bogus"

    with TestApp() as app:
        msg = "Can't instantiate abstract class .* with abstract methods"
        with raises(TypeError, match=msg):
            app.handler.register(BogusHandler)
