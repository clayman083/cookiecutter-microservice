import config  # type: ignore
from aiohttp import web
from aiohttp_metrics import setup as setup_metrics  # type: ignore
from aiohttp_micro import (  # type: ignore
    AppConfig,
    setup as setup_micro,
)


async def init(app_name: str, config: AppConfig) -> web.Application:
    app = web.Application()

    setup_micro(app, app_name, config)
    setup_metrics(app)

    app["logger"].info("Initialize application")

    return app
