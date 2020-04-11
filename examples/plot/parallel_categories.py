"""
Spiral parallel categories plot example.
"""

from spiral import App
from spiral.data import load_dataset

import plotly.express as px


# app definition
class PlotApp(App):
    class Meta:
        label = "parallel_categories"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the tips dataset
    data = load_dataset("tips")

    # create a parallel categories plot
    fig = app.plot.parallel_categories(
        data,
        dimensions=["sex", "smoker", "day"],
        color="size",
        color_continuous_scale=px.colors.sequential.Inferno,
    )

    fig.show()
