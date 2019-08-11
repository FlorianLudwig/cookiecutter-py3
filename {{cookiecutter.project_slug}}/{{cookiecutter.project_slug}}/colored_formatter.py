"""wrapper around coloredlogs to make it usable with logging.config

It also changes the default styles:

 * no use of black as a font color as it is the most common terminal bg color

See https://github.com/xolox/python-coloredlogs/issues/75
"""
import coloredlogs


DEFAULT_FIELD_STYLES = dict(
    asctime=dict(color="green"),
    hostname=dict(color="magenta"),
    levelname=dict(color="green", faint=True),
    programname=dict(color="cyan"),
    name=dict(color="blue"),
)
"""Mapping of log format names to default font styles."""


class ColoredFormatter(coloredlogs.ColoredFormatter):
    def __init__(self, fmt=None, datefmt=None, field_styles=None):
        super(ColoredFormatter, self).__init__(
            fmt, datefmt, style=field_styles, field_styles=DEFAULT_FIELD_STYLES
        )
