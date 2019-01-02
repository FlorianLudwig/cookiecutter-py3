import logging

from aiohttp import web
import prometheus_async.aio


LOG = logging.getLogger(__name__)

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.Response(status=200, body='Hello World')


def register(app):
    routes.get('/metrics')(prometheus_async.aio.web.server_stats)
    app.add_routes(routes)
