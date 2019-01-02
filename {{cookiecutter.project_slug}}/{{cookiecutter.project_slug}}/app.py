import logging

import yacm
import asyncio
from aiohttp import web

from .handlers import routes
from . import mongo


class Application(web.Application):
    def __init__(self, extra_config=None, **kwargs):
        super(Application, self).__init__(**kwargs)
        self.config = yacm.read_configs('{{ cookiecutter.project_slug }}')
        self.load_plugins()
        routes.register(self)

    def load_plugins(self):
        self.cleanup_ctx.append(mongo.enable)


# used for aiohttp-devtools
def create_app(loop=None):
    if loop is None:
        logging.basicConfig(level=logging.DEBUG)
        loop = asyncio.get_event_loop()
    return Application(loop=loop)
