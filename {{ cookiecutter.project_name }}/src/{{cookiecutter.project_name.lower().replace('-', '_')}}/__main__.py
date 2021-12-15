import asyncio

import click
import uvloop  # type: ignore
from aiohttp_micro.cli.server import server  # type: ignore
from config import EnvValueProvider, load

from {{ cookiecutter.project_name.lower().replace('-', '_') }}.app import AppConfig, init


@click.group()
@click.option("--debug", default=False, is_flag=True)
@click.option("--conf-dir", default=None)
@click.pass_context
def cli(ctx, conf_dir: str = None, debug: bool = False):
    uvloop.install()
    loop = asyncio.get_event_loop()

    config = AppConfig(defaults={"debug": debug})
    load(config, providers=[EnvValueProvider()])

    app = loop.run_until_complete(init("{{ cookiecutter.project_name.lower().replace('-', '_') }}", config))

    ctx.obj["app"] = app
    ctx.obj["config"] = config
    ctx.obj["loop"] = loop


cli.add_command(server, name="server")


if __name__ == "__main__":
    cli(obj={})
