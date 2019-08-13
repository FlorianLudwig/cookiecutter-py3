import asyncio
import pytest

from {{ cookiecutter.project_slug }}.app import create_app

@pytest.yield_fixture(scope='function')
def loop():
    """
    Create an instance of the default event loop for each test case.
    Prevents leaking of tasks through shared event loops
    Prevents RuntimeError: web.Application instance initialized with different loop
    """

    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop

    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

@pytest.yield_fixture(scope='function')
def client(aiohttp_client, app):
    c = aiohttp_client(app)
    yield c
    c.close()

@pytest.fixture(scope='function')
def app(loop):
    return create_app(loop=loop)
