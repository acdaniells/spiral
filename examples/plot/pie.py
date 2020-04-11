"""
Spiral pie chart example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class PlotApp(App):
    class Meta:
        label = "pie"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the gapminder dataset
    data = load_dataset("gapminder")

    # filter dataset
    data = data.query("year == 2007").query("continent == 'Americas'")

    # set the theme
    app.plot.set_theme("spiral")

    # create a pie chart with hover additional data
    fig = app.plot.pie(
        data,
        values="pop",
        names="country",
        title="Population of American continent (2007)",
        hover_data=["lifeExp"],
        labels={"lifeExp": "Life Expectancy"},
        hole=0.3,
        patches={"traces": {"textposition": "inside", "textinfo": "percent+label"}},
    )

    fig.show()
