"""
Spiral polar bar chart example.
"""

from spiral import App
from spiral.data import load_dataset

import plotly.express as px


# app definition
class PlotApp(App):
    class Meta:
        label = "bar_polar"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the wind dataset
    data = load_dataset("wind")

    # set dark theme
    app.plot.set_theme("plotly_dark")

    # create polar bar chart
    fig = app.plot.bar_polar(
        data,
        r="frequency",
        theta="direction",
        color="strength",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
        title="Wind direction frequency",
        subtitle="Categorised by strength",
    )

    fig.show()
