import pkg_resources
import pytest  # type: ignore


@pytest.mark.integration
async def test_index(aiohttp_client, app):
    client = await aiohttp_client(app)
    resp = await client.get('/')

    assert resp.status == 200
    assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'

    data = await resp.json()
    assert data == {
        'project': pkg_resources.get_distribution('{{ cookiecutter.project_slug }}').project_name,
        'version': pkg_resources.get_distribution('{{ cookiecutter.project_slug }}').version
    }
