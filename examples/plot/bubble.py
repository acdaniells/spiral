"""
Spiral bubble plot example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class PlotApp(App):
    class Meta:
        label = "bubble"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the iris dataset
    data = load_dataset("gapminder")

    # filter data for 1982
    data = data.loc[data.year == 1982]

    # create a bubble plot (scatter+size)
    fig = app.plot.scatter(
        data,
        x="lifeExp",
        y="gdpPercap",
        color="continent",
        size="pop",
        hover_data=["country"],
        labels={
            "lifeExp": "Life Expectancy",
            "gdpPercap": "GDP per capita",
            "pop": "Population",
        },
        log_y=True,
        title="Life Expectancy and GDP per capita (1982)",
        units={"x": "Years"},
        patches={
            "markers": {"marker_sizemode": "area", "marker_sizeref": 200000},
            "layout": {"yaxis_tickprefix": "$"},
        },
    )

    fig.show()
