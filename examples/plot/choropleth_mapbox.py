"""
Spiral choropleth mapbox example.
"""

from spiral import App
from spiral.data import load_dataset


# app definition
class PlotApp(App):
    class Meta:
        label = "choropleth_mapbox"
        plot_handler = "plotly"


with PlotApp() as app:
    # load the election datasets
    data = load_dataset("election")
    geojson = load_dataset("election_geojson")

    # create choropleth mapbox plot
    fig = app.plot.choropleth_mapbox(
        data_frame=data,
        geojson=geojson,
        color="winner",
        locations="district",
        featureidkey="properties.district",
        center={"lat": 45.5517, "lon": -73.7073},
        mapbox_style="carto-positron",
        zoom=9,
        title="Montreal mayoral election (2013)",
    )

    fig.show()
