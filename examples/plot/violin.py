"""
Spiral violin plot example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class PlotApp(App):
    class Meta:
        label = "violin"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the tips dataset
    data = load_dataset("tips")

    # create a grouped violin plot
    fig = app.plot.violin(
        data,
        x="day",
        y="total_bill",
        color="smoker",
        box=True,
        patches={"layout": {"yaxis_tickprefix": "$"}},
    )

    fig.show()
