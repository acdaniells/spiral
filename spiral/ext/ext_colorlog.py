"""
Spiral colorlog extension module.
"""

import logging
import os
import sys

from spiral.ext.ext_logging import LoggingLogHandler

from cement.utils.misc import is_true
from colorlog import ColoredFormatter


class ColorLogHandler(LoggingLogHandler):

    """
    Colorlog handler class.

    This class implements the Log Handler interface. It is a sub-class of
    :class:`spiral.ext.ext_logging.LoggingLogHandler` which is based on the
    standard :py:class:`logging` library, and adds colorized console output
    using the `ColorLog <https://pypi.python.org/pypi/colorlog>`_ library.

    **Note** This extension has an external dependency on ``colorlog``. You
    must include ``colorlog`` in your applications dependencies as Spiral
    explicitly does **not** include external dependencies for optional
    extensions.

    """

    class Meta:

        """
        Handler meta-data.
        """

        #: The string identifier of the handler.
        label = "colorlog"

        #: Color mapping for each log level
        colors = {
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "blue",
            "ERROR": "red",
            "CRITICAL": "fg_bold_white,bg_red",
        }

        #: Secondary colors
        secondary_colors = {}

        #: Default configuration settings. Will be overridden by the same
        #: settings in any application configuration file under a
        #: ``[log.colorlog]`` block.
        config_defaults = {
            "file": None,
            "level": "INFO",
            "to_console": True,
            "rotate": False,
            "max_bytes": 512_000,
            "max_files": 4,
            "colorize_file_log": False,
            "colorize_console_log": True,
        }

        #: Formatter class to use for non-colorized logging (non-tty, file,
        #: etc)
        formatter_class_without_color = logging.Formatter

        #: Formatter class to use for colorized logging
        formatter_class = ColoredFormatter

    def _get_console_format(self):
        console_format = super()._get_console_format()
        colorize = self.app.config.get("log.colorlog", "colorize_console_log")
        if sys.stdout.isatty() or "CEMENT_TEST" in os.environ:
            if is_true(colorize):
                for key in self._meta.secondary_colors.keys():
                    console_format = console_format.replace(
                        f"{{{key}}}",
                        f"{{reset}}{{{key}_log_color}}{{{key}}}{{reset}}{{log_color}}",
                    )
                console_format = "{log_color}" + console_format
        return console_format

    def _get_file_format(self):
        file_format = super()._get_file_format()
        colorize = self.app.config.get("log.colorlog", "colorize_file_log")
        if is_true(colorize):
            for key in self._meta.secondary_colors.keys():
                file_format = file_format.replace(
                    f"{{{key}}}",
                    f"{{reset}}{{{key}_log_color}}{{{key}}}{{reset}}{{log_color}}",
                )
            file_format = "{log_color}" + file_format
        return file_format

    def _get_console_formatter(self, console_format):
        colorize = self.app.config.get("log.colorlog", "colorize_console_log")

        if sys.stdout.isatty() or "CEMENT_TEST" in os.environ:
            if is_true(colorize):
                formatter = self._meta.formatter_class(
                    console_format,
                    datefmt=self._meta.date_format,
                    style=self._meta.format_style,
                    log_colors=self._meta.colors,
                    secondary_log_colors=self._meta.secondary_colors,
                )
            else:
                formatter = self._meta.formatter_class_without_color(
                    console_format,
                    datefmt=self._meta.date_format,
                    style=self._meta.format_style,
                )
        else:
            klass = self._meta.formatter_class_without_color  # pragma: nocover
            formatter = klass(
                console_format,
                datefmt=self._meta.date_format,
                style=self._meta.format_style,
            )  # pragma: nocover

        return formatter

    def _get_file_formatter(self, file_format):
        colorize = self.app.config.get("log.colorlog", "colorize_file_log")

        if is_true(colorize):
            formatter = self._meta.formatter_class(
                file_format,
                datefmt=self._meta.date_format,
                style=self._meta.format_style,
                log_colors=self._meta.colors,
                secondary_log_colors=self._meta.secondary_colors,
            )
        else:
            formatter = self._meta.formatter_class_without_color(
                file_format,
                datefmt=self._meta.date_format,
                style=self._meta.format_style,
            )

        return formatter


def load(app):
    """
    Extension loader function.
    """
    app.handler.register(ColorLogHandler)
