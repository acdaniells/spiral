from spiral import TestApp, init_defaults
from spiral.data import load_dataset

CONFIG = init_defaults("plot.plotly")
CONFIG["plot.plotly"]["show_logo"] = True
CONFIG["plot.plotly"]["show_watermark"] = True


class PlotlyApp(TestApp):
    class Meta:
        config_defaults = CONFIG


def test_pie():
    with PlotlyApp() as app:
        app.plot.pie(
            data_frame=load_dataset("gapminder"),
            values="pop",
            names="country",
            title="title",
            subtitle="subtitle",
        )


def test_scatter():
    with PlotlyApp() as app:
        app.plot.scatter(
            data_frame=load_dataset("iris"),
            x="petal_length",
            y="petal_width",
            color="species",
            symbol="species",
            xunit="cm",
            yunit="cm",
            title="title",
        )


def test_choropleth_mapbox():
    with PlotlyApp() as app:
        app.plot.choropleth_mapbox(
            data_frame=load_dataset("election"),
            geojson=load_dataset("election_geojson"),
            color="winner",
            locations="district",
            featureidkey="properties.district",
            center={"lat": 45.5517, "lon": -73.7073},
            mapbox_style="carto-positron",
            zoom=9,
        )


def test_facet():
    with PlotlyApp() as app:
        app.plot.scatter(
            data_frame=load_dataset("iris"),
            x="petal_length",
            y="petal_width",
            facet_col="species",
            xunit="cm",
            yunit="cm",
            title="title",
        )
