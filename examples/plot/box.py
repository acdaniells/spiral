"""
Spiral box plot example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class PlotApp(App):
    class Meta:
        label = "box"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the tips dataset
    data = load_dataset("tips")

    # create plot
    fig = app.plot.box(
        data_frame=data,
        x="day",
        y="total_bill",
        color="smoker",
        patches={"layout": {"yaxis_tickprefix": "$"}},
    )

    fig.show()
