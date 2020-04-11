"""
Spiral advanced violin plot example.
"""

from spiral import App, init_defaults
from spiral.data import load_dataset

# configuration defaults
CONFIG = init_defaults("plot.plotly")
CONFIG["plot.plotly"]["plot_width"] = 800


# app definition
class PlotApp(App):
    class Meta:
        label = "violin"
        config_defaults = CONFIG
        plot_handler = "plotly"


with PlotApp() as app:
    # load the tips dataset
    data = load_dataset("tips")

    # create a grouped+split violin plot with scaling
    fig = app.plot.violin(
        data,
        x="day",
        y="total_bill",
        color="sex",
        violinmode="overlay",
        title="Total bill distribution",
        subtitle="Scaled by number of bills per gender",
        patches={
            "data": [
                {"side": "negative", "pointpos": -1},
                {"side": "positive", "pointpos": 1},
            ],
            "traces": {
                "meanline_visible": True,
                "points": "all",
                "jitter": 0.1,
                "scalemode": "count",
            },
            "layout": {"violingap": 0, "yaxis_tickprefix": "$"},
        },
    )

    fig.show()
