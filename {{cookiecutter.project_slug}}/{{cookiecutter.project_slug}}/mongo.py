import copy
import logging

import motor.motor_asyncio


LOG = logging.getLogger(__name__)


def get_app_key(type: str, key: str) -> str:
    if key == 'default':
        template = '{type}'
    else:
        template = '{type}_{name}'
    return template.format(type=type, name=key)


async def enable(app):
    if 'mongodb' not in app.config:
        raise AttributeError('mongodb config is missing')

    for key, client_attr in app.config['mongodb'].items():
        client_attr = copy.copy(client_attr)
        db = client_attr.pop('db')
        client = motor.motor_asyncio.AsyncIOMotorClient(**client_attr)

        app_key = get_app_key('mongo', key)
        LOG.debug(app_key)
        app[app_key] = client

        app_key = get_app_key('db', key)
        LOG.debug(app_key)
        app[app_key] = client[db]

    yield

    for key, client_attr in app.config['mongodb'].items():
        key = get_app_key('mongo', key)
        app[key].close()

    LOG.debug('mongo disconnected')
