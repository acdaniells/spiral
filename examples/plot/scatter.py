"""
Spiral scatter plot example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class PlotApp(App):
    class Meta:
        label = "scatter"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the iris dataset
    data = load_dataset("iris")

    # create a scatter plot
    fig = app.plot.scatter(
        data,
        x="petal_length",
        y="petal_width",
        color="species",
        symbol="species",
        units={"x": "cm", "y": "cm"},
        title="Petal length vs width",
    )

    fig.show()
