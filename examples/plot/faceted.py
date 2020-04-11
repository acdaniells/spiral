"""
Spiral faceted plot example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class PlotApp(App):
    class Meta:
        label = "facet"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the tips dataset
    data = load_dataset("tips")

    # create grouped+faceted histogram
    fig = app.plot.histogram(
        data,
        x="sex",
        y="total_bill",
        color="smoker",
        barmode="group",
        facet_row="time",
        facet_col="day",
        histfunc="sum",
        title="Total bill for different meal times",
        subtitle="By sex and smoking status",
        patches={"layout": {"yaxis_tickprefix": "$", "yaxis5_tickprefix": "$"}},
    )

    fig.show()
