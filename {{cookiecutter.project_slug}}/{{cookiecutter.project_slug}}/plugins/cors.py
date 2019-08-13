import logging

from aiohttp import web
import aiohttp_cors

LOG = logging.getLogger(__name__)


async def enable(app: web.Application) -> None:
    """Configures a default CORS resource for every origin and route"""

    cors_config = app.config.get('cors')

    if not cors_config:
        LOG.warning('No CORS config found, skipping CORS setup')
        return

    default_option = aiohttp_cors.ResourceOptions(
        expose_headers='*', allow_headers='*', allow_credentials=True
    )

    defaults = {}
    for origin in cors_config.get('origins', []):
        LOG.debug(f'CORS: allowing all requests from origin: {origin}')
        defaults[origin] = default_option

    cors = aiohttp_cors.setup(app, defaults=defaults)

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        LOG.debug('add CORS for route %s', route)
        cors.add(route)

    app['cors_config'] = cors
    yield
