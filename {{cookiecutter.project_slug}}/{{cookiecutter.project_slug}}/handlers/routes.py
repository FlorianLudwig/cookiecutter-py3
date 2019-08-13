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

    # aiohttp merges routes with the same name and path into a single resource,
    # if they are added in direct succession.
    # For aiohttp_cors to work correctly all mergeable routes must be merged.
    # Bug: Unmerged routes raise a 403 response on options requests
    # See: https://github.com/aio-libs/aiohttp-cors/issues/226
    app.add_routes(routes)
