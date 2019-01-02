import logging
import os
from typing import Dict, Optional

import pkg_resources
from aiohttp import web
from prometheus_client import CollectorRegistry, Counter, Gauge, Histogram  # type: ignore
from raven import Client as Raven  # type: ignore
from raven_aiohttp import AioHttpTransport  # type: ignore

from {{ cookiecutter.project_slug }}.adapters.web import core
from {{ cookiecutter.project_slug }}.config import Config


async def init(config: Config, logger: logging.Logger) -> web.Application:
    app = web.Application(logger=logger, middlewares=[
        core.catch_exceptions_middleware, core.prometheus_middleware
    ])

    app['config'] = config

    if config.get('sentry_dsn', None):
        app['raven'] = Raven(config['sentry_dsn'], transport=AioHttpTransport)

    app['distribution'] = pkg_resources.get_distribution('{{ cookiecutter.project_slug }}')

    app['metrics_registry'] = CollectorRegistry()
    app['metrics'] = {
        'REQUEST_COUNT': Counter(
            'requests_total', 'Total request count',
            ['app_name', 'method', 'endpoint', 'http_status'],
            registry=app['metrics_registry']
        ),
        'REQUEST_LATENCY': Histogram(
            'requests_latency_seconds', 'Request latency',
            ['app_name', 'endpoint'], registry=app['metrics_registry']
        ),
        'REQUEST_IN_PROGRESS': Gauge(
            'requests_in_progress_total', 'Requests in progress',
            ['app_name', 'endpoint', 'method'], registry=app['metrics_registry']
        )
    }

    app.router.add_routes([
        web.get('/', core.index, name='index'),
        web.get('/-/health', core.health, name='health'),
        web.get('/-/metrics', core.metrics, name='metrics')
    ])

    return app


config_schema = {
    'app_name': {'type': 'string', 'required': True},
    'app_root': {'type': 'string', 'required': True},
    'app_hostname': {'type': 'string'},
    'app_host': {'type': 'string'},
    'app_port': {'type': 'string'},

    'access_log': {'type': 'string', 'required': True},

    'consul_host': {'type': 'string', 'required': True},
    'consul_port': {'type': 'integer', 'required': True, 'coerce': int},

    'sentry_dsn': {'type': 'string'},

    'logging': {'type': 'dict', 'required': True}
}


def configure(config_file: Optional[str] = None, defaults: Optional[Dict] = None) -> Config:
    config = Config(config_schema, defaults)
    config['app_root'] = os.path.realpath(os.path.dirname(
        os.path.abspath(__file__)))

    if config_file:
        config.update_from_yaml(config_file, True)

    for key in iter(config_schema.keys()):
        config.update_from_env_var(key)

    config.validate()

    return config
