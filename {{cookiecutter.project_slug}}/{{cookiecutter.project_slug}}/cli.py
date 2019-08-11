"""Console script for {{cookiecutter.project_slug}}."""
import os
import sys
import click
import logging


LOG = logging.getLogger(__name__)


def setup_logging() -> None:
    default_format = os.environ.get(
        "LOG_FORMAT", "{asctime} {levelname:3.3} {name}: {message}"
    )
    log_config = os.environ.get("LOG_CONFIG", None)

    if log_config:
        config = yaml.safe_load(config)
    else:
        config = {}

    config.setdefault("version", 1)
    config.setdefault("disable_existing_loggers", False)

    # always need a standard formatter
    config.setdefault("formatters", {})
    # XXX import needed to ensure the module (python_boilerplate.colored_formatter) is loaded
    import python_boilerplate.colored_formatter

    config["formatters"].setdefault(
        "default",
        {
            "format": default_format,
            "class": "python_boilerplate.colored_formatter.ColoredFormatter",
            "style": "{",
        },
    )

    # if there is no handler at all, log to console
    config.setdefault(
        "handlers",
        {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "default",
            }
        },
    )

    # set loggers
    config.setdefault(
        "loggers", {"": {"level": "DEBUG", "handlers": list(config["handlers"].keys())}}
    )

    logging.config.dictConfig(config)


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    setup_logging()
    click.echo("Replace this message in the cli.py")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
