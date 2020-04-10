"""
Spiral plotly express module.
"""

from spiral.plotly._doc import make_docstring

import plotly.express as px  # noqa: F401


class PlotlyExpress:

    """
    Plotly express class.

    This class includes all the plots available in plotly express.

    """

    def scatter(
        self,
        data_frame=None,
        x=None,
        y=None,
        color=None,
        symbol=None,
        size=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        text=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        error_x=None,
        error_x_minus=None,
        error_y=None,
        error_y_minus=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        symbol_sequence=None,
        symbol_map={},
        opacity=None,
        size_max=None,
        marginal_x=None,
        marginal_y=None,
        trendline=None,
        trendline_color_override=None,
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        render_mode="auto",
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Scatter plot.

        Each row of `data_frame` is represented by a symbol mark in 2D
        space.

        """
        return self.make_figure(args=locals(), constructor=px.scatter)

    def density_contour(
        self,
        data_frame=None,
        x=None,
        y=None,
        z=None,
        color=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        marginal_x=None,
        marginal_y=None,
        trendline=None,
        trendline_color_override=None,
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        histfunc=None,
        histnorm=None,
        nbinsx=None,
        nbinsy=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Density contour plot.

        Rows of `data_frame` are grouped together into contour marks to
        visualize the 2D distribution of an aggregate function
        `histfunc` (e.g. the count or sum) of the value `z`.

        """
        return self.make_figure(args=locals(), constructor=px.density_contour)

    def density_heatmap(
        self,
        data_frame=None,
        x=None,
        y=None,
        z=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        marginal_x=None,
        marginal_y=None,
        opacity=None,
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        histfunc=None,
        histnorm=None,
        nbinsx=None,
        nbinsy=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Density heatmap.

        Rows of `data_frame` are grouped together into colored
        rectangular tiles to visualize the 2D distribution of an
        aggregate function `histfunc` (e.g. the count or sum) of the
        value `z`.

        """
        return self.make_figure(args=locals(), constructor=px.density_heatmap)

    def line(
        self,
        data_frame=None,
        x=None,
        y=None,
        line_group=None,
        color=None,
        line_dash=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        text=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        error_x=None,
        error_x_minus=None,
        error_y=None,
        error_y_minus=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        line_dash_sequence=None,
        line_dash_map={},
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        line_shape=None,
        render_mode="auto",
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Line plot.

        Each row of `data_frame` is represented as vertex of a polyline
        mark in 2D space.

        """
        return self.make_figure(args=locals(), constructor=px.line)

    def area(
        self,
        data_frame=None,
        x=None,
        y=None,
        line_group=None,
        color=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        text=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        orientation="v",
        groupnorm=None,
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        line_shape=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Area plot.

        Each row of `data_frame` is represented as vertex of a polyline
        mark in 2D space. The area between successive polylines is
        filled.

        """
        return self.make_figure(args=locals(), constructor=px.area)

    def bar(
        self,
        data_frame=None,
        x=None,
        y=None,
        color=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        text=None,
        error_x=None,
        error_x_minus=None,
        error_y=None,
        error_y_minus=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        opacity=None,
        orientation="v",
        barmode="relative",
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Bar chart.

        Each row of `data_frame` is represented as a rectangular mark.

        """
        return self.make_figure(args=locals(), constructor=px.bar)

    def histogram(
        self,
        data_frame=None,
        x=None,
        y=None,
        color=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        marginal=None,
        opacity=None,
        orientation="v",
        barmode="relative",
        barnorm=None,
        histnorm=None,
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        histfunc=None,
        cumulative=None,
        nbins=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Histogram.

        Rows of `data_frame` are grouped together into a rectangular
        mark to visualize the 1D distribution of an aggregate function
        `histfunc` (e.g. the count or sum) of the value `y` (or `x` if
        `orientation` is `'h'`).

        """
        return self.make_figure(args=locals(), constructor=px.histogram)

    def violin(
        self,
        data_frame=None,
        x=None,
        y=None,
        color=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        orientation="v",
        violinmode="group",
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        points=None,
        box=False,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Violin plot.

        Rows of `data_frame` are grouped together into a curved mark to
        visualize their distribution.

        """
        return self.make_figure(args=locals(), constructor=px.violin)

    def box(
        self,
        data_frame=None,
        x=None,
        y=None,
        color=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        orientation="v",
        boxmode="group",
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        points=None,
        notched=False,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Box plot.

        Rows of `data_frame` are grouped together into a box-and-whisker
        mark to visualize their distribution. Each box spans from
        quartile 1 (Q1) to quartile 3 (Q3). The second quartile (Q2) is
        marked by a line inside the box. By default, the whiskers
        correspond to the box' edges +/- 1.5 times the interquartile
        range (IQR: Q3-Q1), see "points" for other options.

        """
        return self.make_figure(args=locals(), constructor=px.box)

    def strip(
        self,
        data_frame=None,
        x=None,
        y=None,
        color=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        orientation="v",
        stripmode="group",
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Strip plot.

        Each row of `data_frame` is represented as a jittered mark
        within categories.

        """
        return self.make_figure(args=locals(), constructor=px.strip)

    def scatter_3d(
        self,
        data_frame=None,
        x=None,
        y=None,
        z=None,
        color=None,
        symbol=None,
        size=None,
        text=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        error_x=None,
        error_x_minus=None,
        error_y=None,
        error_y_minus=None,
        error_z=None,
        error_z_minus=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        size_max=None,
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        symbol_sequence=None,
        symbol_map={},
        opacity=None,
        log_x=False,
        log_y=False,
        log_z=False,
        range_x=None,
        range_y=None,
        range_z=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        3D scatter plot.

        Each row of `data_frame` is represented by a symbol mark in 3D
        space.

        """
        return self.make_figure(args=locals(), constructor=px.scatter_3d)

    def line_3d(
        self,
        data_frame=None,
        x=None,
        y=None,
        z=None,
        color=None,
        line_dash=None,
        text=None,
        line_group=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        error_x=None,
        error_x_minus=None,
        error_y=None,
        error_y_minus=None,
        error_z=None,
        error_z_minus=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        line_dash_sequence=None,
        line_dash_map={},
        log_x=False,
        log_y=False,
        log_z=False,
        range_x=None,
        range_y=None,
        range_z=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        3D line plot.

        Each row of `data_frame` is represented as vertex of a polyline
        mark in 3D space.

        """
        return self.make_figure(args=locals(), constructor=px.line_3d)

    def scatter_ternary(
        self,
        data_frame=None,
        a=None,
        b=None,
        c=None,
        color=None,
        symbol=None,
        size=None,
        text=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        symbol_sequence=None,
        symbol_map={},
        opacity=None,
        size_max=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Ternary plot.

        Each row of `data_frame` is represented by a symbol mark in
        ternary coordinates.

        """
        return self.make_figure(args=locals(), constructor=px.scatter_ternary)

    def line_ternary(
        self,
        data_frame=None,
        a=None,
        b=None,
        c=None,
        color=None,
        line_dash=None,
        line_group=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        text=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        line_dash_sequence=None,
        line_dash_map={},
        line_shape=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Ternary line plot.

        Each row of `data_frame` is represented as vertex of a polyline
        mark in ternary coordinates.

        """
        return self.make_figure(args=locals(), constructor=px.line_ternary)

    def scatter_polar(
        self,
        data_frame=None,
        r=None,
        theta=None,
        color=None,
        symbol=None,
        size=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        text=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        symbol_sequence=None,
        symbol_map={},
        opacity=None,
        direction="clockwise",
        start_angle=90,
        size_max=None,
        range_r=None,
        range_theta=None,
        log_r=False,
        render_mode="auto",
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        note=None,
        patches={},
    ):
        """
        Polar scatter plot.

        Each row of `data_frame` is represented by a symbol mark in
        polar coordinates.

        """
        return self.make_figure(args=locals(), constructor=px.scatter_polar)

    def line_polar(
        self,
        data_frame=None,
        r=None,
        theta=None,
        color=None,
        line_dash=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        line_group=None,
        text=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        line_dash_sequence=None,
        line_dash_map={},
        direction="clockwise",
        start_angle=90,
        line_close=False,
        line_shape=None,
        render_mode="auto",
        range_r=None,
        range_theta=None,
        log_r=False,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        note=None,
        patches={},
    ):
        """
        Polar line plot.

        Each row of `data_frame` is represented as vertex of a polyline
        mark in polar coordinates.

        """
        return self.make_figure(args=locals(), constructor=px.line_polar)

    def bar_polar(
        self,
        data_frame=None,
        r=None,
        theta=None,
        color=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        barnorm=None,
        barmode="relative",
        direction="clockwise",
        start_angle=90,
        range_r=None,
        range_theta=None,
        log_r=False,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        note=None,
        patches={},
    ):
        """
        Polar bar plot.

        Each row of `data_frame` is represented as a wedge mark in polar
        coordinates.

        """
        return self.make_figure(args=locals(), constructor=px.bar_polar)

    def choropleth(
        self,
        data_frame=None,
        lat=None,
        lon=None,
        locations=None,
        locationmode=None,
        geojson=None,
        featureidkey=None,
        color=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        projection=None,
        scope=None,
        center=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Choropleth map.

        Each row of `data_frame` is represented by a colored region mark
        on a map.

        """
        return self.make_figure(args=locals(), constructor=px.choropleth)

    def scatter_geo(
        self,
        data_frame=None,
        lat=None,
        lon=None,
        locations=None,
        locationmode=None,
        color=None,
        text=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        size=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        opacity=None,
        size_max=None,
        projection=None,
        scope=None,
        center=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Geographic scatter plot.

        Each row of `data_frame` is represented by a symbol mark on a
        map.

        """
        return self.make_figure(args=locals(), constructor=px.scatter_geo)

    def line_geo(
        self,
        data_frame=None,
        lat=None,
        lon=None,
        locations=None,
        locationmode=None,
        color=None,
        line_dash=None,
        text=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        line_group=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        line_dash_sequence=None,
        line_dash_map={},
        projection=None,
        scope=None,
        center=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Geographic line plot.

        Each row of `data_frame` is represented as vertex of a polyline
        mark on a map.

        """
        return self.make_figure(args=locals(), constructor=px.line_geo)

    def scatter_mapbox(
        self,
        data_frame=None,
        lat=None,
        lon=None,
        color=None,
        text=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        size=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        opacity=None,
        size_max=None,
        zoom=8,
        center=None,
        mapbox_style=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Mapbox scatter plot.

        Each row of `data_frame` is represented by a symbol mark on a
        Mapbox map.

        """
        return self.make_figure(args=locals(), constructor=px.scatter_mapbox)

    def choropleth_mapbox(
        self,
        data_frame=None,
        geojson=None,
        featureidkey=None,
        locations=None,
        color=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        opacity=None,
        zoom=8,
        center=None,
        mapbox_style=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Mapbox choropleth map.

        Each row of `data_frame` is represented by a colored region on a
        Mapbox map.

        """
        return self.make_figure(args=locals(), constructor=px.choropleth_mapbox)

    def density_mapbox(
        self,
        data_frame=None,
        lat=None,
        lon=None,
        z=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        opacity=None,
        zoom=8,
        center=None,
        mapbox_style=None,
        radius=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Mapbox density map.

        Each row of `data_frame` contributes to the intensity of the
        color of the region around the corresponding point on the map

        """
        return self.make_figure(args=locals(), constructor=px.density_mapbox)

    def line_mapbox(
        self,
        data_frame=None,
        lat=None,
        lon=None,
        color=None,
        text=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        line_group=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        zoom=8,
        center=None,
        mapbox_style=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Mapbox line plot.

        Each row of `data_frame` is represented as vertex of a polyline
        mark on a Mapbox map.

        """
        return self.make_figure(args=locals(), constructor=px.line_mapbox)

    def scatter_matrix(
        self,
        data_frame=None,
        dimensions=None,
        color=None,
        symbol=None,
        size=None,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        symbol_sequence=None,
        symbol_map={},
        opacity=None,
        size_max=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Scatter plot matrix (or SPLOM).

        Each row of `data_frame` is represented by a multiple symbol
        marks, one in each cell of a grid of 2D scatter plots, which
        plot each pair of `dimensions` against each other.

        """
        return self.make_figure(args=locals(), constructor=px.scatter_matrix)

    def parallel_coordinates(
        self,
        data_frame=None,
        dimensions=None,
        color=None,
        labels={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Parallel coordinates plot.

        Each row of `data_frame` is represented by a polyline mark which
        traverses a set of parallel axes, one for each of the
        `dimensions`.

        """
        return self.make_figure(args=locals(), constructor=px.parallel_coordinates)

    def parallel_categories(
        self,
        data_frame=None,
        dimensions=None,
        color=None,
        labels={},
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        dimensions_max_cardinality=50,
        units={},
        note=None,
        patches={},
    ):
        """
        Parallel categories plot.

        Each row of `data_frame` is grouped with other rows that share
        the same values of `dimensions` and then plotted as a polyline
        mark through a set of parallel axes, one for each of the
        `dimensions`.

        """
        return self.make_figure(args=locals(), constructor=px.parallel_categories)

    def pie(
        self,
        data_frame=None,
        names=None,
        values=None,
        color=None,
        color_discrete_sequence=None,
        color_discrete_map={},
        hover_name=None,
        hover_data=None,
        custom_data=None,
        labels={},
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        opacity=None,
        hole=0.3,
        units={},
        note=None,
        patches={},
    ):
        """
        Pie chart.

        Each row of `data_frame` is represented as a sector of a pie.

        """
        return self.make_figure(args=locals(), constructor=px.pie)

    def sunburst(
        self,
        data_frame=None,
        names=None,
        values=None,
        parents=None,
        path=None,
        ids=None,
        color=None,
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        color_discrete_sequence=None,
        color_discrete_map={},
        hover_name=None,
        hover_data=None,
        custom_data=None,
        labels={},
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        branchvalues=None,
        maxdepth=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Sunburst plot.

        Represents hierarchical data as sectors laid out over several
        levels of concentric rings.

        """
        return self.make_figure(args=locals(), constructor=px.sunburst)

    def treemap(
        self,
        data_frame=None,
        names=None,
        values=None,
        parents=None,
        ids=None,
        path=None,
        color=None,
        color_continuous_scale=None,
        range_color=None,
        color_continuous_midpoint=None,
        color_discrete_sequence=None,
        color_discrete_map={},
        hover_name=None,
        hover_data=None,
        custom_data=None,
        labels={},
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        branchvalues=None,
        maxdepth=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Treemap plot.

        Represents hierarchical data as nested rectangular sectors.

        """
        return self.make_figure(args=locals(), constructor=px.treemap)

    def funnel(
        self,
        data_frame=None,
        x=None,
        y=None,
        color=None,
        facet_row=None,
        facet_col=None,
        facet_col_wrap=0,
        hover_name=None,
        hover_data=None,
        custom_data=None,
        text=None,
        animation_frame=None,
        animation_group=None,
        category_orders={},
        labels={},
        color_discrete_sequence=None,
        color_discrete_map={},
        opacity=None,
        orientation="h",
        log_x=False,
        log_y=False,
        range_x=None,
        range_y=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Funnel plot.

        Each row of `data_frame` is represented as a rectangular sector
        of a funnel.

        """
        return self.make_figure(args=locals(), constructor=px.funnel)

    def funnel_area(
        self,
        data_frame=None,
        names=None,
        values=None,
        color=None,
        color_discrete_sequence=None,
        color_discrete_map={},
        hover_name=None,
        hover_data=None,
        custom_data=None,
        labels={},
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        opacity=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Funnel area plot.

        Each row of `data_frame` is represented as a trapezoidal sector
        of a funnel.

        """
        return self.make_figure(args=locals(), constructor=px.funnel_area)

    def imshow(
        self,
        img,
        zmin=None,
        zmax=None,
        origin=None,
        labels={},
        x=None,
        y=None,
        color_continuous_scale=None,
        color_continuous_midpoint=None,
        range_color=None,
        title=None,
        subtitle=None,
        template=None,
        width=None,
        height=None,
        aspect=None,
        units={},
        note=None,
        patches={},
    ):
        """
        Display an image, i.e. data on a 2D regular raster.

        Parameters
        ----------
        img: array-like image, or xarray
            The image data. Supported array shapes are:

            - (M, N): an image with scalar data. The data is visualized
              using a colormap.
            - (M, N, 3): an image with RGB values.
            - (M, N, 4): an image with RGBA values, i.e. including
              transparency.
        zmin, zmax : scalar or iterable, optional
            zmin and zmax define the scalar range that the colormap
            covers. By default, zmin and zmax correspond to the min and
            max values of the datatype for integer datatypes (ie [0-255]
            for uint8 images, [0, 65535] for uint16 images, etc.). For a
            multichannel image of floats, the max of the image is
            computed and zmax is the smallest power of 256 (1, 255,
            65535) greater than this max value, with a 5% tolerance. For
            a single-channel image, the max of the image is used.
            Overridden by range_color.
        origin : str, 'upper' or 'lower' (default 'upper')
            Position of the [0, 0] pixel of the image array, in the
            upper left or lower left corner. The convention 'upper' is
            typically used for matrices and images.
        labels : dict with str keys and str values (default `{}`)
            Sets names used in the figure for axis titles (keys ``x``
            and ``y``), colorbar title and hoverlabel (key ``color``).
            The values should correspond to the desired label to be
            displayed. If ``img`` is an xarray, dimension names are used
            for axis titles, and long name for the colorbar title
            (unless overridden in ``labels``). Possible keys are: x, y,
            and color.
        x, y: list-like, optional
            x and y are used to label the axes of single-channel heatmap
            visualizations and their lengths must match the lengths of
            the second and first dimensions of the img argument. They
            are auto-populated if the input is an xarray.
        color_continuous_scale : str or list of str
            Colormap used to map scalar data to colors (for a 2D image).
            This parameter is not used for RGB or RGBA images. If a
            string is provided, it should be the name of a known color
            scale, and if a list is provided, it should be a list of
            CSS- compatible colors.
        color_continuous_midpoint : number
            If set, computes the bounds of the continuous color scale to
            have the desired midpoint. Overridden by range_color or zmin
            and zmax.
        range_color : list of two numbers
            If provided, overrides auto-scaling on the continuous color
            scale, including overriding `color_continuous_midpoint`.
            Also overrides zmin and zmax. Used only for single-channel
            images.
        title : str
            The figure title.
        subtitle : str
            The figure subtitle.
        template : str or dict or plotly.graph_objects.layout.Template
            The figure template name or definition.
        width : number
            The figure width in pixels.
        height: number
            The figure height in pixels.
        aspect: 'equal', 'auto', or None
          - 'equal': Ensures an aspect ratio of 1 or pixels (square
            pixels)
          - 'auto': The axes is kept fixed and the aspect ratio of
            pixels is adjusted so that the data fit in the axes. In
            general, this will result in non-square pixels.
          - if None, 'equal' is used for numpy arrays and 'auto' for
            xarrays (which have typically heterogeneous coordinates)
        units: dict with str keys and str values (default `{}`)
            The axis units.
        note: str
            Figure note text.
        patches: nested dict with str keys and any value (default `{}`)
            Can contain patches to 'data', 'traces', 'markers',
            'annotations', 'xaxis', 'yaxis' or 'layout'.

        Returns
        -------
        fig : plotly.graph_objects.Figure
            Plotly figure object containing the displayed image.

        See Also
        --------
        plotly.graph_objects.Image : image trace
        plotly.graph_objects.Heatmap : heatmap trace

        Notes
        -----
        In order to update and customize the returned figure, use
        `go.Figure.update_traces` or `go.Figure.update_layout`. If an
        xarray is passed, dimensions names and coordinates are used for
        axes labels and ticks.

        """
        return self.make_figure(args=locals(), constructor=px.imshow)


spx = PlotlyExpress
spx.scatter.__doc__ = make_docstring(spx.scatter)
spx.scatter_3d.__doc__ = make_docstring(spx.scatter_3d)
spx.scatter_geo.__doc__ = make_docstring(spx.scatter_geo)
spx.scatter_mapbox.__doc__ = make_docstring(spx.scatter_mapbox)
spx.scatter_matrix.__doc__ = make_docstring(spx.scatter_matrix)
spx.scatter_polar.__doc__ = make_docstring(spx.scatter_polar)
spx.scatter_ternary.__doc__ = make_docstring(spx.scatter_ternary)
spx.line.__doc__ = make_docstring(spx.line)
spx.line_3d.__doc__ = make_docstring(spx.line_3d)
spx.line_geo.__doc__ = make_docstring(spx.line_geo)
spx.line_mapbox.__doc__ = make_docstring(spx.line_mapbox)
spx.line_polar.__doc__ = make_docstring(spx.line_polar)
spx.line_ternary.__doc__ = make_docstring(spx.line_ternary)
spx.area.__doc__ = make_docstring(spx.area)
spx.bar.__doc__ = make_docstring(spx.bar)
spx.bar_polar.__doc__ = make_docstring(spx.bar_polar)
spx.box.__doc__ = make_docstring(spx.box)
spx.violin.__doc__ = make_docstring(spx.violin)
spx.strip.__doc__ = make_docstring(spx.strip)
spx.histogram.__doc__ = make_docstring(spx.histogram)
spx.parallel_categories.__doc__ = make_docstring(spx.parallel_categories)
spx.parallel_coordinates.__doc__ = make_docstring(spx.parallel_coordinates)
spx.choropleth.__doc__ = make_docstring(spx.choropleth)
spx.choropleth_mapbox.__doc__ = make_docstring(spx.choropleth_mapbox)
spx.density_contour.__doc__ = make_docstring(spx.density_contour)
spx.density_heatmap.__doc__ = make_docstring(spx.density_heatmap)
spx.density_mapbox.__doc__ = make_docstring(spx.density_mapbox)
spx.pie.__doc__ = make_docstring(spx.pie)
spx.sunburst.__doc__ = make_docstring(spx.sunburst)
spx.treemap.__doc__ = make_docstring(spx.treemap)
spx.funnel.__doc__ = make_docstring(spx.funnel)
spx.funnel_area.__doc__ = make_docstring(spx.funnel_area)
