from contextlib import contextmanager
from typing import Dict

import ujson
from aiohttp import web


async def get_payload(request: web.Request) -> Dict:
    if 'application/json' in request.content_type:
        payload = await request.json()
    else:
        payload = await request.post()
    return dict(payload)


def json_response(data, status: int=200, **kwargs) -> web.Response:
    return web.json_response(data, dumps=ujson.dumps, status=status, **kwargs)


@contextmanager
def register_handler(app: web.Application, url_prefix: str=None,
                     name_prefix: str=None):
    def register(method: str, url: str, handler, name: str=None):
        if url_prefix:
            if not url:
                url = url_prefix
            else:
                url = '/'.join((url_prefix.rstrip('/'), url.lstrip('/')))

        if name_prefix:
            name = '.'.join((name_prefix, name))

        app.router.add_route(method, url, handler, name=name)
    yield register


async def index(request):
    return json_response({
        'project': request.app.distribution.project_name,
        'version': request.app.distribution.version
    })
