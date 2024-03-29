from importlib.metadata import Distribution, distribution

import punq
import pytest
from aiohttp import web
from structlog.types import WrappedLogger

from {{ cookiecutter.project_name.lower().replace('-', '_') }}.app import create_container, init
from {{ cookiecutter.project_name.lower().replace('-', '_') }}.logging import configure_logging


@pytest.fixture(scope="session")
def dist() -> Distribution:
    """Patch application distribution."""
    return distribution("{{ cookiecutter.project_name.lower().replace('-', '_') }}")


@pytest.fixture()
def logger(dist: Distribution) -> WrappedLogger:
    """Configure logging for tests."""
    return configure_logging(dist=dist, debug=False)


@pytest.fixture()
def container(logger: WrappedLogger) -> punq.Container:
    """Create IoC container."""
    return create_container(logger=logger)


@pytest.fixture()
def app(dist: Distribution, container: punq.Container) -> web.Application:
    """Prepare test application."""
    return init(dist=dist, container=container, debug=False)
