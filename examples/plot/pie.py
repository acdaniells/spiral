"""
Spiral pie plot example.
"""

from spiral import App, init_defaults
from spiral.data import load_dataset

# configuration defaults
CONFIG = init_defaults("plot.plotly")
CONFIG["plot.plotly"]["show_logo"] = True


# app definition
class PlotApp(App):
    class Meta:
        label = "pie"
        config_defaults = CONFIG
        plot_handler = "plotly"


with PlotApp() as app:
    # load the gapminder dataset
    gapminder = load_dataset("gapminder")

    df = gapminder.query("year == 2007").query("continent == 'Americas'")

    # set the theme
    app.plot.set_theme("spiral")

    # create a pie chart
    fig = app.plot.pie(
        data_frame=df,
        values="pop",
        names="country",
        title="Population of American continent",
        # hover_data=["lifeExp"],
        labels={"lifeExp": "life expectancy"},
        hole=0.3,
    )

    fig.update_layout(margin={"l": 30, "b": 30})
    fig.update_traces(textposition="inside", textinfo="percent+label")

    fig.show()
