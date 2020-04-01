"""
Plotly template generator.

This is an adapted version of the plotly project `templategen` script.
https://github.com/plotly/plotly.py/tree/master/packages/python/plotly/templategen

"""

import json
import os

from spiral import App, io

from plotly.utils import PlotlyJSONEncoder

from .definitions import builders

META = {
    "log.colorlog": {
        "console_format": "{levelname:^8s}: {title}{message}{value}",
        "attribute_formats": {"title": " === {title} === ", "value": " -> {value}"},
        "secondary_colors": {
            "title": {"INFO": "fg_bold_white,bg_green"},
            "value": {"INFO": "bold_purple"},
        },
    }
}


class BuilderApp(App):
    class Meta:
        label = "plotly_theme_builder"
        meta_defaults = META
        log_handler = "colorlog"
        extensions = ["colorlog"]


def main():
    with BuilderApp() as app:
        app.log.info(title="Start")
        app.log.info(f"{len(builders)} theme(s) identified")

        for theme_name in builders:
            template = builders[theme_name]()

            path = os.path.join("data", "plotly_themes", f"{theme_name}.json")
            filename = io.resource_filename(path)

            with open(filename, "w") as fp:
                json.dump(template, fp, cls=PlotlyJSONEncoder)

            app.log.info(f"Created '{theme_name}' theme", value=filename)

        app.log.info(title="Complete")


if __name__ == "__main__":
    main()
