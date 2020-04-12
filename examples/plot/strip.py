"""
Spiral strip plot example.
"""

from spiral import App
from spiral.data import load_dataset

import pandas as pd


# app definition
class PlotApp(App):
    class Meta:
        label = "strip"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the iris dataset
    data = load_dataset("iris")

    # "Melt" the dataset to "long-form" or "tidy" representation
    data = pd.melt(data, "species", var_name="measurement")
    data = data.loc[data.measurement != "species_id"]

    # create a strip plot
    fig = app.plot.strip(
        data,
        x="value",
        y="measurement",
        color="species",
        orientation="h",
        title="Iris observations",
        patches={"traces": {"jitter": 0.75}},
    )

    fig.show()
