import logging

import pytest  # type: ignore
from aiohttp import web

from {{ cookiecutter.project_slug }}.app import configure, init


@pytest.fixture(scope='session')
def config():
    return configure(defaults={
        'app_name': '{{ cookiecutter.project_slug }}',
        'app_host': 'localhost',
        'app_port': '5000'
    })


@pytest.yield_fixture(scope='function')
def app(loop, config):
    logger = logging.getLogger('app')

    app = loop.run_until_complete(init(config, logger))

    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())

    yield app

    loop.run_until_complete(runner.cleanup())
