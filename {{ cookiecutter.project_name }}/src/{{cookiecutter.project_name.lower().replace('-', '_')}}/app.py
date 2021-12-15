import os

from aiohttp import web
from aiohttp_micro import AppConfig as BaseConfig  # type: ignore
from aiohttp_micro import setup as setup_micro
from aiohttp_micro import setup_logging, setup_metrics


class AppConfig(BaseConfig):
    """Application config."""


async def init(app_name: str, config: AppConfig) -> web.Application:
    app = web.Application()

    app["app_root"] = os.path.dirname(__file__)

    setup_micro(app, app_name=app_name, config=config)
    setup_metrics(app)
    setup_logging(app)

    app["logger"].info("Initialize application")

    return app
