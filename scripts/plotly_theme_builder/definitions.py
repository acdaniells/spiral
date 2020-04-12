"""
Template definitions.
"""

import plotly.express as px

from .utils import initialize_template
from .utils.colors import colors

spiral_colors = {
    "blue": "#00338D",
    "medium-blue": "#005EB8",
    "light-blue": "#0091DA",
    "pale-blue": "#99BFE3",
    "violet": "#483698",
    "purple": "#470A68",
    "light-purple": "#6D2077",
    "green": "#00A3A1",
    "dark-green": "#009A44",
    "light-green": "#43B02A",
    "yellow": "#EAAA00",
    "orange": "#F68D2E",
    "red": "#BC204B",
    "pink": "#C6007E",
    "white": "#FFFFFF",
}

spiral_colorway = [
    spiral_colors["blue"],
    spiral_colors["red"],
    spiral_colors["green"],
    spiral_colors["light-purple"],
    spiral_colors["orange"],
    spiral_colors["light-blue"],
    spiral_colors["pink"],
    spiral_colors["light-green"],
    spiral_colors["yellow"],
    spiral_colors["pale-blue"],
    colors["gray60"],
]


def spiral():
    # common colorbar properties
    colorbar_common = {"outlinewidth": 0, "ticks": ""}

    # common axis properties
    axis_common = {
        "showgrid": True,
        "gridwidth": 1,
        "gridcolor": colors["gray94"],
        "showline": True,
        "linecolor": colors["gray20"],
        "ticks": "",
        "title": {"standoff": 15},
    }

    # semi-transparent black and no outline
    shape_defaults = {"fillcolor": "black", "line": {"width": 0}, "opacity": 0.3}

    # remove arrow head and make line thinner
    annotation_defaults = {
        "font": {"size": 16},
        "arrowcolor": colors["gray20"],
        "arrowhead": 0,
        "arrowwidth": 1,
    }

    template = initialize_template(
        paper_color="white",
        font_color=colors["gray20"],
        panel_background_color=spiral_colors["white"],
        panel_grid_color=spiral_colors["medium-blue"],
        axis_ticks_color=colors["gray20"],
        zerolinecolor_color=colors["gray40"],
        table_cell_color=spiral_colors["white"],
        table_header_color=spiral_colors["blue"],
        table_line_color=spiral_colors["blue"],
        colorway=spiral_colorway,
        colorbar_common=colorbar_common,
        colorscale=px.colors.sequential.Plasma,
        colorscale_diverging=px.colors.diverging.RdBu,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults,
    )

    # increase global font size by 1.5x (12->18)
    template.layout.font.size = 18
    template.layout.font.family = "Arial"

    # left align title
    template.layout.title.x = 0.05

    # title color
    template.layout.title.font.color = spiral_colors["blue"]

    # increase grid width for 3d plots
    opts = {"gridwidth": 2, "gridcolor": colors["gray94"], "zeroline": False}
    template.layout.scene.xaxis.update(opts)
    template.layout.scene.yaxis.update(opts)
    template.layout.scene.zaxis.update(opts)

    # darken ternary
    opts = {"linecolor": colors["gray20"], "gridcolor": colors["gray94"]}
    template.layout.ternary.aaxis.update(opts)
    template.layout.ternary.baxis.update(opts)
    template.layout.ternary.caxis.update(opts)

    # remove lines through the origin
    template.layout.xaxis.update(zeroline=False)
    template.layout.yaxis.update(zeroline=False)

    # title font color
    template.layout.xaxis.title.font.color = spiral_colors["blue"]
    template.layout.yaxis.title.font.color = spiral_colors["blue"]
    template.layout.legend.title.font.color = spiral_colors["blue"]
    template.layout.coloraxis.colorbar.title.font.color = spiral_colors["blue"]

    # mapbox light style
    template.layout.mapbox.style = "light"

    # automargin for pie chart
    template.data.pie = [{"automargin": True}]

    # increase scatter markers and lines by 1.5x
    opts = {"marker": {"size": 9, "line": {"width": 2}}}
    template.data.scatter = [opts]
    template.data.scattergl = [opts]
    template.data.scatter3d = [opts]
    template.data.scatterpolar = [opts]
    template.data.scatterpolargl = [opts]
    template.data.scatterternary = [opts]
    template.data.scattergeo = [opts]

    # set marker size ans line for strip plots
    opts = {"marker": {"size": 5, "line": {"width": 1}}}
    template.data.box = [opts]
    template.data.violin = [opts]

    # table font properties
    template.data.table[0].header.font.color = "white"
    template.data.table[0].header.font.size = 12

    return template


builders = {"spiral": spiral}
