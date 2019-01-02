"""Console script for {{ cookiecutter.project_slug }}."""
import sys
import click
import functools

import asyncio
import aiohttp

import {{ cookiecutter.project_slug }}.app


def async_cli(f):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(f(*args, **kwargs))
    return functools.update_wrapper(wrapper, f)


@click.group()
def main():
    """Console script for {{ cookiecutter.project_slug }}"""
    pass


@main.command()
@click.option('--port', default=9000)
def serv(port):
    aiohttp.web.run_app({{ cookiecutter.project_slug }}.app.Application(), port=port)


@main.command()
@async_cli
async def status(url):
    status_url = url + '/api/v1/status'
    timeout = aiohttp.ClientTimeout(total=0, connect=15,
                                    sock_connect=15, sock_read=0)
    async with aiohttp.ClientSession(timeout=timeout) as client:
        async with client.get(url) as resp:
            assert resp.status == 200

            status = await resp.content.read()
            status = status.decode('utf-8')
            print(status.strip('\n'))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
