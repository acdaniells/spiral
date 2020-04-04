"""
Spiral scatter plot example.
"""

from spiral import App, init_defaults
from spiral.data import load_dataset

# configuration defaults
CONFIG = init_defaults("scatter", "plot.plotly")
CONFIG["plot.plotly"]["show_logo"] = True


# app definition
class PlotApp(App):
    class Meta:
        label = "scatter"
        config_defaults = CONFIG
        plot_handler = "plotly"


with PlotApp() as app:
    # load the iris dataset
    iris = load_dataset("iris")

    # set the theme
    app.plot.set_theme("spiral")

    app.log.info("Plotting")

    # create a scatter plot
    fig = app.plot.scatter(
        data_frame=iris,
        x="petal_length",
        y="petal_width",
        color="species",
        symbol="species",
        units={"x": "cm", "y": "cm"},
        title="title",
    )

    fig.show()
