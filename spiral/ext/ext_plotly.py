"""
Spiral plotly extension module.
"""

import os

from spiral.core.exc import SpiralError
from spiral.core.plot import PlotHandler
from spiral.plotly import PlotlyExpress
from spiral.utils.io import read_json, resource_exists, resource_filename

import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

from cement.utils.misc import minimal_logger
from titlecase import titlecase

LOG = minimal_logger(__name__)


def load_theme(name):
    """
    Load a plotly template from package data.

    Parameters
    ----------
    name : str
        The theme name.

    Returns
    -------
    plotly.graph_objs.layout.Template
        A Plotly template object.

    """
    filename = os.path.join("data", "plotly_themes", f"{name}.json")

    if not resource_exists(filename):
        raise SpiralError(f"The plotly theme file '{name}.json' does not exist")

    filename = resource_filename(filename)

    return go.layout.Template(read_json(filename))


def load_logo(name):
    """
    Load a logo from package data.

    Parameters
    ----------
    name : str
        The theme name.

    Returns
    -------
    datauri.DataURI
        A str based object for the data URI.

    """
    filename = os.path.join("data", "logos", f"{name}.svg")

    if not resource_exists(filename):
        LOG.debug(f"A logo for the theme '{name}' was not found")
        return None

    filename = resource_filename(filename)

    from datauri import DataURI

    return DataURI.from_file(filename)


def color_to_rgb(color):
    """
    Convert color string to rgb tuple.

    Parameters
    ----------
    color : str
        The color string.

    Raises
    ------
    SpiralError
        If color string type is not recognised.

    Returns
    -------
    tuple
        A tuple of the form (r, g, b).

    """
    from plotly.colors import color_parser, unlabel_rgb, hex_to_rgb

    if color.startswith("rgb"):
        color = color_parser(color, unlabel_rgb)
    elif color.startswith("#"):
        color = color_parser(color, hex_to_rgb)
    else:
        raise SpiralError(f"Unrecognised color string '{color}'")

    return color


class PlotlyPlotHandler(PlotlyExpress, PlotHandler):

    """
    Plotly handler class.

    This class is an implementation of the :ref:`Plot
    <spiral.core.plot>` interface using the plotly visualisation
    library.

    """

    class Meta:

        """
        Handler meta-data.
        """

        label = "plotly"
        """The string identifier for this handler."""

        custom_themes = ["spiral"]
        """The list of available custom themes."""

        data_attributes = (
            ["x", "y", "z", "a", "b", "c", "r", "theta", "size"]
            + ["custom_data", "hover_name", "hover_data", "text"]
            + ["names", "values", "parents", "ids"]
            + ["error_x", "error_y", "error_z"]
            + ["error_x_minus", "error_y_minus", "error_z_minus"]
            + ["lat", "lon", "locations", "animation_group", "path"]
            + ["animation_frame", "facet_row", "facet_col", "line_group"]
            + ["color", "symbol", "line_dash"]
        )

        axes = ["x", "y", "z", "a", "b", "c"]
        """A list of axes names."""

        default_font_size = 12
        """Default font size."""

        config_defaults = {
            "sizing": "plot",
            "figure_width": 600,
            "figure_height": 600,
            "plot_width": 470,
            "plot_height": 470,
            "facet_scale": 0.5,
            "axis_margin": 100,
            "border_margin": 30,
            "legend_margin": 200,
            "symbol_sequence": [
                "circle",
                "square",
                "diamond",
                "x",
                "hexagon",
                "star-square",
                "star-diamond",
                "star-triangle-up",
            ],
            "line_dash_sequence": [
                "solid",
                "dot",
                "dash",
                "longdash",
                "dashdot",
                "longdashdot",
            ],
            "marker_color_alpha": 0.5,
            "show_logo": False,
            "show_watermark": False,
            "generate_title": False,
        }
        """Configuration default values."""

    def __init__(self, **kw):
        super().__init__(**kw)

        self.figure = None
        self.left_margin = None
        self.right_margin = None
        self.top_margin = None
        self.bottom_margin = None
        self.logo_source = None
        self.facet_ncols = None
        self.figure_ncols = None
        self.figure_nrows = None

    def _setup(self, app_obj):
        super()._setup(app_obj)

        self.figure = go.Figure()

        self.set_theme()

    def _validate(self):
        if self._get_config("sizing") not in ["figure", "plot"]:
            raise SpiralError(
                "Configuration parameter 'sizing' must be either 'figure' or 'plot'"
            )

    def set_theme(self, name="spiral"):
        """
        Set the theme used for creating figures.
        """
        if name == pio.templates.default:
            return

        theme_names = name.split("+")

        for theme_name in theme_names:
            if theme_name not in self._meta.custom_themes:
                continue

            pio.templates[theme_name] = load_theme(theme_name)
            self.logo_source = load_logo(theme_name)

        pio.templates.default = name

    @property
    def figure_width(self):
        """
        Get the figure width in pixels from the configuration.
        """
        return self._get_config("figure_width")

    @property
    def figure_height(self):
        """
        Get the figure height in pixels from the configuration.
        """
        return self._get_config("figure_height")

    @property
    def plot_width(self):
        """
        Get the plot width in pixels from the configuration.
        """
        return self._get_config("plot_width")

    @property
    def plot_height(self):
        """
        Get the plot width in pixels from the configuration.
        """
        return self._get_config("plot_height")

    @figure_width.setter
    def figure_width(self, width):
        """
        Set the figure width in pixels in the configuration.
        """
        self._set_config("figure_width", width)

    @figure_height.setter
    def figure_height(self, height):
        """
        Set the figure height in pixels in the configuration.
        """
        self._set_config("figure_height", height)

    @plot_width.setter
    def plot_width(self, width):
        """
        Set the plot width in pixels in the configuration.
        """
        self._set_config("plot_width", width)

    @plot_height.setter
    def plot_height(self, height):
        """
        Set the plot height in pixels in the configuration.
        """
        self._set_config("plot_height", height)

    def figure_x(self, start, distance):
        """
        Get an x coordinate in the figure system for a distance in pixels.
        """
        return start + distance / self.figure_width

    def figure_y(self, start, distance):
        """
        Get a y coordinate in the figure system for a distance in pixels.
        """
        return start + distance / self.figure_height

    def plot_x(self, start, distance):
        """
        Get an x coordinate in the plot system for a distance in pixels.
        """
        return start + distance / self.plot_width

    def plot_y(self, start, distance):
        """
        Get an y coordinate in the plot system for a distance in pixels.
        """
        return start + distance / self.plot_height

    @property
    def font_size(self):
        """
        Return the font size.
        """
        font_size = pio.templates[pio.templates.default].layout.font.size

        if font_size is None:
            font_size = self._meta.default_font_size

        return font_size

    @property
    def font_size_px(self):
        """
        Return the font size in pixels.
        """
        return self.font_size * 1.28

    @property
    def subfont_size_px(self):
        """
        Return the subtitle font size in pixels.
        """
        return self.font_size * 0.9

    def _get_config(self, key):
        return self.app.config.get(self._meta.config_section, key)

    def _set_config(self, key, value):
        return self.app.config.set(self._meta.config_section, key, value)

    @staticmethod
    def _clean_text(text):
        return text.replace("_", " ")

    @staticmethod
    def _title_case(text):
        def skip_words(word, **kwargs):
            # skip non-lower case words
            if word != word.lower():
                return word

        return titlecase(text, callback=skip_words)

    def prepare_args(self, kwargs):
        """
        Prepare plotting arguments.
        """
        # remove self from keyword args
        kwargs.pop("self")

        kwargs = self._prepare_data(kwargs)
        kwargs = self._prepare_title(kwargs)
        kwargs = self._prepare_grid(kwargs)
        kwargs = self._prepare_sizes(kwargs)
        kwargs = self._prepare_labels(kwargs)
        kwargs = self._prepare_category_orders(kwargs)
        kwargs = self._prepare_patches(kwargs)

        return kwargs

    def _prepare_data(self, kwargs):
        # initialise data frame
        data = kwargs["data_frame"]

        if data is None:
            data = pd.DataFrame()

        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)

        for key, arg in kwargs.items():
            # consider only data attributes
            if key not in self._meta.data_attributes or arg is None:
                continue

            # get column name
            if isinstance(arg, pd.Series):
                column = arg.name
            elif isinstance(arg, str):
                column = arg
            else:
                column = key

            # column already exists
            if column not in data.columns:
                # add column data
                if hasattr(arg, "values"):
                    data[column] = arg.array
                else:
                    data[column] = np.array(arg)

            # update argument with column name
            kwargs[key] = column

        # update data frame
        kwargs["data_frame"] = data

        return kwargs

    def _prepare_title(self, kwargs):
        # remove subtitle from keyword args
        subtitle = kwargs.pop("subtitle")

        title = kwargs["title"]

        if title is not None:
            title = self._title_case(self._clean_text(title))

            if subtitle is not None:
                title += f"<br><sup>{self._clean_text(subtitle)}</sup>"

            # update title
            kwargs["title"] = title
        elif self._get_config("generate_title"):
            x = kwargs.get("x")
            y = kwargs.get("y")

            subitems = [
                kwargs.get("facet_col"),
                kwargs.get("facet_row"),
                kwargs.get("color"),
            ]

            if x is not None and y is not None:
                title = self._title_case(self._clean_text(f"{x} vs {y}"))
                subtitle = ", ".join([x for x in subitems if x is not None])

                if subtitle != "":
                    subtitle = f"Per {subtitle}"
                    title += f"<br><sup>{self._clean_text(subtitle)}</sup>"

            # update title
            kwargs["title"] = title

        return kwargs

    def _prepare_grid(self, kwargs):
        # determine number of facet columns and rows
        facet_ncols = 1
        facet_nrows = 1
        figure_ncols = 1
        figure_nrows = 1

        data = kwargs["data_frame"]
        facet_col = kwargs.get("facet_col")
        facet_row = kwargs.get("facet_row")

        if facet_col is not None:
            facet_ncols = data[facet_col].nunique()
            figure_ncols = facet_ncols

        if facet_row is not None:
            facet_nrows = data[facet_row].nunique()
            figure_nrows = facet_nrows

        # determine facet column wrapping
        facet_col_wrap = None

        if facet_ncols > 1 and facet_nrows == 1:
            self.facet_ncols = facet_ncols
            facet_col_wrap = kwargs.get("facet_col_wrap") or None

            # column wrapping defined by user
            if facet_col_wrap is not None:
                figure_ncols = facet_col_wrap
                figure_nrows = np.ceil(facet_ncols / facet_col_wrap)

            # automatically determine wrapping
            best_remainder_frac = 0
            if facet_col_wrap is None:
                for nrows in range(1, facet_ncols + 1):
                    ncols = int(np.ceil(facet_ncols / nrows))
                    if ncols >= nrows and ncols / nrows <= 3:
                        remainder_frac = (facet_ncols % ncols) / ncols or 1
                        if remainder_frac >= best_remainder_frac:
                            best_remainder_frac = remainder_frac
                            facet_col_wrap = ncols
                            figure_ncols = ncols
                            figure_nrows = nrows

        self.figure_ncols = figure_ncols
        self.figure_nrows = figure_nrows
        self.facet_ncols = facet_ncols

        if "facet_col_wrap" in kwargs:
            kwargs["facet_col_wrap"] = facet_col_wrap

        return kwargs

    def _prepare_sizes(self, kwargs):
        # calculate figure width, height and margins
        left_margin = self._get_config("axis_margin")
        right_margin = self._get_config("border_margin")
        top_margin = self._get_config("border_margin")
        bottom_margin = self._get_config("axis_margin")

        title_margin = top_margin + self.font_size_px
        if kwargs["title"] is not None and "<br><sup>" in kwargs["title"]:
            spacing = 0.236 * self.font_size
            title_margin += self.subfont_size_px + spacing
        title_margin = round(title_margin)

        note_margin = round(self.font_size_px * 2 / 3 + 10)

        if self._get_config("sizing") == "plot":
            # apply facet plot scaling
            if self.figure_ncols > 1 or self.figure_nrows > 1:
                self.plot_width *= self._get_config("facet_scale")
                self.plot_height *= self._get_config("facet_scale")

            figure_width = (
                left_margin + self.plot_width * self.figure_ncols + right_margin
            )
            figure_height = (
                top_margin + self.plot_height * self.figure_nrows + bottom_margin
            )
            plot_width = self.plot_width
            plot_height = self.plot_height

            if kwargs["title"] is not None:
                figure_height += title_margin
                top_margin += title_margin

            if kwargs["note"] is not None:
                figure_height += note_margin
                bottom_margin += note_margin

            if kwargs["color"] is not None:  # color axis?
                figure_width += self._get_config("legend_margin")
                right_margin += self._get_config("legend_margin")
        else:
            figure_width = self.figure_width
            figure_height = self.figure_height
            plot_width = self.figure_width - (left_margin + right_margin)
            plot_height = self.figure_height - (top_margin + bottom_margin)

            if kwargs["title"] is not None:
                plot_height -= title_margin
                top_margin += title_margin

            if kwargs["note"] is not None:
                plot_height -= note_margin
                bottom_margin += note_margin

            if kwargs["color"] is not None:  # color axis?
                plot_width -= self._get_config("legend_margin")
                right_margin += self._get_config("legend_margin")

        kwargs["width"] = figure_width
        kwargs["height"] = figure_height

        self.figure_width = figure_width
        self.figure_height = figure_height
        self.plot_width = plot_width
        self.plot_height = plot_height

        self.left_margin = left_margin
        self.right_margin = right_margin
        self.top_margin = top_margin
        self.bottom_margin = bottom_margin

        print(left_margin, right_margin, top_margin, bottom_margin)

        return kwargs

    def _prepare_labels(self, kwargs):
        # default labels
        columns = kwargs["data_frame"].columns.tolist()
        labels = {x: self._title_case(self._clean_text(x)) for x in columns}

        # add units to axis labels
        if "units" in kwargs:
            units = kwargs.pop("units")

            for axis, unit in units.items():
                key = kwargs[axis]
                label = self._title_case(self._clean_text(key))
                labels[key] = f"{label} [{unit}]"

        kwargs["labels"] = labels

        return kwargs

    @staticmethod
    def _prepare_category_orders(kwargs):
        if "category_orders" in kwargs:
            data = kwargs["data_frame"]
            category_orders = kwargs["category_orders"]

            if category_orders is None:
                category_orders = {}

                # attempt to order possible category columns
                for column in data:
                    series = data[column]

                    if hasattr(series, "cat"):
                        category_orders[column] = series.cat.categories.tolist()
                    elif str(series.dtype) in ("object", "int", "bool"):
                        if series.nunique() / len(series) < 0.5:
                            categories = series.unique()
                            categories.sort()
                            category_orders[column] = categories.tolist()

                kwargs["category_orders"] = category_orders

        return kwargs

    def _prepare_patches(self, kwargs):  # noqa: C901
        if "patches" not in kwargs or not isinstance(kwargs["patches"], dict):
            kwargs["patches"] = {}

        config_override = kwargs["patches"].copy()

        def rangemode(series):
            try:
                if series.array.min() / series.array.max() < 1 / 3:
                    return "tozero"
            except TypeError:
                pass
            return "normal"

        def is_not_cat(series):
            if str(series.dtype) in ("category", "object", "int", "bool"):
                if series.nunique() / len(series) < 0.5:
                    return False
            return True

        data = kwargs["data_frame"]

        config = {}
        for axis in self._meta.axes:
            column = kwargs.get(axis)
            if column is not None:
                config[f"{axis}axis"] = {}
                config[f"{axis}axis"]["rangemode"] = rangemode(data[column])
                config[f"{axis}axis"]["showgrid"] = is_not_cat(data[column])

        kwargs["patches"].update(config)
        kwargs["patches"].update(config_override)

        return kwargs

    def make_figure(self, args, constructor):
        """
        Make a figure object.
        """
        args = self.prepare_args(args)

        note = args.pop("note")
        patches = args.pop("patches")

        print(args)
        print(patches)

        self.figure = constructor(**args)

        self._update_layout(patches)
        self._update_axes(patches, args)
        self._update_markers(patches)
        self._update_annotations(patches)
        self._add_logo(patches)
        self._add_watermark(patches)
        self._add_note(note, patches)

        return self.figure

    def _update_layout(self, patches):
        border_margin = self._get_config("border_margin")

        defaults = {
            "margin_l": self.left_margin,
            "margin_r": self.right_margin,
            "margin_t": self.top_margin,
            "margin_b": self.bottom_margin,
            "title_x": self.figure_x(0, border_margin),
            "title_y": self.figure_y(1, -(border_margin + self.font_size)),
            "title_xref": "container",
            "title_yref": "container",
            "title_xanchor": "left",
            "title_yanchor": "bottom",
            "legend_x": self.plot_x(1, border_margin),
            "legend_y": self.plot_y(1, 0),
            "legend_xanchor": "left",
            "legend_yanchor": "top",
            "coloraxis_colorbar_x": self.plot_x(1, border_margin),
            "coloraxis_colorbar_y": self.plot_y(1, 0),
            "coloraxis_colorbar_xanchor": "left",
            "coloraxis_colorbar_yanchor": "top",
        }

        kwargs = defaults.copy()
        if "layout" in patches:
            kwargs.update(patches["layout"])

        self.figure.update_layout(**kwargs)

    def _update_axes(self, patches, kwargs):
        if "x" in kwargs and "y" in kwargs:
            if kwargs["x"] is not None:
                # add xaxis tick labels and titles back to overhanging plots
                # in facet column figures
                xaxis_title_text = kwargs["labels"][kwargs.get("x")]

                def update(axis):
                    axis.update(showticklabels=True, title_text=xaxis_title_text)

                for col in range(
                    self.facet_ncols % self.figure_ncols, self.figure_ncols
                ):
                    self.figure.for_each_xaxis(update, col=col + 1, row=2)

            # patch all axes
            defaults = {}

            kwargs = defaults.copy()
            if "xaxis" in patches:
                kwargs.update(patches["xaxis"])

            self.figure.update_xaxes(**kwargs)

            kwargs = defaults.copy()
            if "yaxis" in patches:
                kwargs.update(patches["yaxis"])

            self.figure.update_yaxes(**kwargs)

    def _update_markers(self, patches):
        defaults = {}

        def update(trace):
            kwargs = defaults.copy()
            if "marker" in patches:
                kwargs.update(patches["marker"])

            if isinstance(trace.marker.color, str):
                r, g, b = color_to_rgb(trace.marker.color)
                a = self._get_config("marker_color_alpha")

                kwargs["marker_color"] = f"rgba({r}, {g}, {b}, {a})"
                kwargs["marker_line_color"] = trace.marker.color
            else:
                # what to do for color tuple?
                pass

            trace.update(**kwargs)

        self.figure.for_each_trace(update, selector={"mode": "markers"})

    def _update_annotations(self, patches):
        defaults = {}

        def update(annotation):
            kwargs = defaults.copy()
            if "annotation" in patches:
                kwargs.update(patches["annotation"])

            kwargs["text"] = self._title_case(
                self._clean_text(annotation.text.split("=")[-1])
            )

            annotation.update(**kwargs)

        self.figure.for_each_annotation(update)

    def _add_logo(self, patches):
        if self._get_config("show_logo") is False:
            return

        ###
        """
        import io
        from urllib.request import urlopen

        from PIL import Image

        from PIL import ImageFile

        def getsizes(uri):
            # get file size *and* image size (None if not known)
            file = urlopen(uri)
            size = file.headers.get("content-length")
            if size:
                size = int(size)
            p = ImageFile.Parser()
            while True:
                data = file.read(1024)
                if not data:
                    break
                p.feed(data)
                if p.image:
                    return size, p.image.size
                    break
            file.close()
            return(size, None)

        #logo = urlopen(self.logo_source).read()

        #file = io.StringIO(self.logo_source)

        #print(file)

        #im = Image.open(file)

        im = Image.open(urlopen(self.logo_source).read())
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")

        width, height = 1,2 #getsizes(self.logo_source)

        print(width, height)
        """

        width, height = 0.15, 0.058
        max_height = 0.075

        sizex, sizey = width * max_height / height, max_height
        ###

        defaults = {
            "name": "logo",
            "source": self.logo_source,
            "opacity": 0.75,
            "xref": "paper",
            "yref": "paper",
            "sizing": "contain",
            "x": 1,
            "y": self.plot_y(1, self._get_config("border_margin")),
            "sizex": sizex,  # * self.figure_xscale,
            "sizey": sizey,  # * self.figure_yscale,
            "xanchor": "right",
            "yanchor": "bottom",
        }

        kwargs = defaults.copy()
        if "logo" in patches:
            kwargs.update(patches["logo"])

        if kwargs["source"] is not None:
            self.figure.add_layout_image(**kwargs)

    def _add_watermark(self, patches):
        if self._get_config("show_watermark") is False:
            return

        textangle = (self.figure_height - 600 * 0.5) * -9 / 70

        if abs(textangle) > 45:
            font_size = int(75)  # / self.figure_yscale)
        else:
            font_size = int(75)  # / self.figure_xscale)

        defaults = {
            "name": "watermark",
            "text": "INTERNAL",
            "textangle": textangle,
            "opacity": 0.05,
            "font_color": "black",
            "font_size": font_size,
            "xref": "paper",
            "yref": "paper",
            "x": 0.5,
            "y": 0.5,
            "showarrow": False,
        }

        kwargs = defaults.copy()
        if "watermark" in patches:
            kwargs.update(patches["watermark"])

        self.figure.add_annotation(**kwargs)

    def _add_note(self, text, patches):
        if text is None:
            return

        axis_margin = self._get_config("axis_margin")
        border_margin = 10

        defaults = {
            "name": "note",
            "text": text,
            "opacity": 0.85,
            "font_size": self.font_size * 2 / 3,
            "x": self.plot_x(0, border_margin - axis_margin),
            "y": self.plot_y(0, -axis_margin),
            "xref": "paper",
            "yref": "paper",
            "xanchor": "left",
            "yanchor": "top",
            "showarrow": False,
        }

        kwargs = defaults.copy()
        if "note" in patches:
            kwargs.update(patches["note"])

        self.figure.add_annotation(**kwargs)


def load(app):
    """
    Extension loader function.
    """
    app.handler.register(PlotlyPlotHandler)
