from plotly import graph_objs as go

colorscale_parent_paths = [
    ("histogram2dcontour",),
    ("choropleth",),
    ("histogram2d",),
    ("heatmap",),
    ("heatmapgl",),
    ("contourcarpet",),
    ("contour",),
    ("surface",),
    ("mesh3d",),
    ("scatter", "marker"),
    ("parcoords", "line"),
    ("scatterpolargl", "marker"),
    ("bar", "marker"),
    ("scattergeo", "marker"),
    ("scatterpolar", "marker"),
    ("histogram", "marker"),
    ("scattergl", "marker"),
    ("scatter3d", "line"),
    ("scatter3d", "marker"),
    ("scattermapbox", "marker"),
    ("scatterternary", "marker"),
    ("scattercarpet", "marker"),
    ("scatter", "marker", "line"),
    ("scatterpolargl", "marker", "line"),
    ("bar", "marker", "line"),
]


def set_all_colorbars(template, colorbar):
    for parent_path in colorscale_parent_paths:
        if not template.data[parent_path[0]]:
            template.data[parent_path[0]] = [{}]

        for trace in template.data[parent_path[0]]:
            parent = trace[parent_path[1:]]

            if "colorbar" in parent:
                parent.colorbar = colorbar


def initialize_template(
    annotation_defaults,
    axis_common,
    axis_ticks_color,
    colorbar_common,
    colorscale,
    colorway,
    font_color,
    panel_background_color,
    panel_grid_color,
    paper_color,
    shape_defaults,
    table_cell_color,
    table_header_color,
    table_line_color,
    zerolinecolor_color,
    colorscale_minus=None,
    colorscale_diverging=None,
):
    # Initialize template
    template = go.layout.Template()

    # trace cycle color
    template.layout.colorway = colorway

    # Set global font color
    template.layout.font.color = font_color

    # hovermode
    template.layout.hovermode = "closest"

    # right-align hoverlabels
    template.layout.hoverlabel.align = "left"

    # Set background colors
    template.layout.paper_bgcolor = paper_color
    template.layout.plot_bgcolor = panel_background_color
    template.layout.polar.bgcolor = panel_background_color
    template.layout.ternary.bgcolor = panel_background_color

    cartesian_axis = dict(axis_common, zerolinecolor=zerolinecolor_color)

    # Colorbars
    set_all_colorbars(template, colorbar_common)
    template.layout.coloraxis.colorbar = colorbar_common

    # Colorscales
    template.layout.colorscale.sequential = colorscale
    if colorscale_minus is not None:
        template.layout.colorscale.sequentialminus = colorscale_minus
    else:
        template.layout.colorscale.sequentialminus = colorscale

    if colorscale_diverging is not None:
        template.layout.colorscale.diverging = colorscale_diverging

    template.data.heatmap[0].colorscale = colorscale
    template.data.histogram2d[0].colorscale = colorscale
    template.data.histogram2dcontour[0].colorscale = colorscale
    template.data.contour[0].colorscale = colorscale
    template.data.surface[0].colorscale = colorscale
    template.data.heatmapgl[0].colorscale = colorscale

    # Cartesian
    template.layout.xaxis = cartesian_axis
    template.layout.yaxis = cartesian_axis

    # Set automargin to true in case we need to adjust margins for
    # larger font size
    template.layout.xaxis.automargin = True
    template.layout.yaxis.automargin = True

    # 3D
    axis_3d = dict(cartesian_axis)
    if axis_3d.get("title"):
        _ = axis_3d["title"].pop("standoff")
    if panel_background_color:
        axis_3d["backgroundcolor"] = panel_background_color
        axis_3d["showbackground"] = True
    template.layout.scene.xaxis = axis_3d
    template.layout.scene.yaxis = axis_3d
    template.layout.scene.zaxis = axis_3d

    # Ternary
    template.layout.ternary.aaxis = axis_common
    template.layout.ternary.baxis = axis_common
    template.layout.ternary.caxis = axis_common

    # Polar
    if axis_common.get("title") or axis_common.get("title") == {}:
        _ = axis_common.pop("title")
    template.layout.polar.angularaxis = axis_common
    template.layout.polar.radialaxis = axis_common

    # Carpet
    carpet_axis = {
        "gridcolor": panel_grid_color,
        "linecolor": panel_grid_color,
        "startlinecolor": axis_ticks_color,
        "endlinecolor": axis_ticks_color,
        "minorgridcolor": panel_grid_color,
    }
    template.data.carpet = [{"aaxis": carpet_axis, "baxis": carpet_axis}]

    # Shape defaults
    template.layout.shapedefaults = shape_defaults

    # Annotation defaults
    template.layout.annotationdefaults = annotation_defaults

    # Geo
    template.layout.geo.bgcolor = paper_color
    template.layout.geo.landcolor = panel_background_color
    template.layout.geo.subunitcolor = panel_grid_color
    template.layout.geo.showland = True
    template.layout.geo.showlakes = True
    template.layout.geo.lakecolor = paper_color

    # Table
    template.data.table = [
        {
            "header": {
                "fill": {"color": table_header_color},
                "line": {"color": table_line_color},
            },
            "cells": {
                "fill": {"color": table_cell_color},
                "line": {"color": table_line_color},
            },
        }
    ]

    # Bar outline
    # Changing marker line color also affects error color,
    # so reset default error colors
    template.data.bar = [
        {
            "marker": {"line": {"width": 0.5, "color": panel_background_color}},
            "error_x": {"color": font_color},
            "error_y": {"color": font_color},
        }
    ]
    template.data.barpolar = [
        {"marker": {"line": {"width": 0.5, "color": panel_background_color}}}
    ]

    return template
