from aiohttp import web

from {{ cookiecutter.project_slug }}.handlers import json_response
from {{ cookiecutter.project_slug }}.validation import ValidationError


class ResourceNotFound(Exception):
    pass


@web.middleware
async def catch_exceptions_middleware(request: web.Request, handler):
    try:
        return await handler(request)
    except ResourceNotFound:
        raise web.HTTPNotFound
    except ValidationError as exc:
        return json_response(exc.errors, status=400)
    except Exception as exc:
        if isinstance(exc, (web.HTTPClientError, )):
            raise

        # send error to sentry
        if request.app.raven:
            request.app.raven.captureException()
        else:
            raise
        raise web.HTTPInternalServerError
