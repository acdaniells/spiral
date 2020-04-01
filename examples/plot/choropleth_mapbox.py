"""
Spiral chloropleth mapbox example.
"""

from spiral import App, init_defaults
from spiral.data import load_dataset

# configuration defaults
CONFIG = init_defaults("plot.plotly")
CONFIG["plot.plotly"]["show_logo"] = True


# app definition
class PlotApp(App):
    class Meta:
        label = "chloropleth_mapbox"
        config_defaults = CONFIG
        plot_handler = "plotly"


with PlotApp() as app:
    # load the election dataset
    df = load_dataset("election")
    geojson = load_dataset("election_geojson")

    # set the theme
    app.plot.set_theme("spiral")

    # create a choropleth mapbox
    fig = app.plot.choropleth_mapbox(
        data_frame=df,
        geojson=geojson,
        color="winner",
        locations="district",
        featureidkey="properties.district",
        center={"lat": 45.5517, "lon": -73.7073},
        mapbox_style="carto-positron",
        zoom=9,
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    fig.show()
