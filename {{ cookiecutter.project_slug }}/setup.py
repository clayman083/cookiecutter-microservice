import os

from setuptools import find_packages, setup


project = '{{ cookiecutter.project_slug }}'


def static_files(path, prefix):
    for root, _, files in os.walk(path):
        paths = []
        for item in files:
            paths.append(os.path.join(root, item))
        yield (root.replace(path, prefix), paths)


setup(
    name=project,
    version='{{ cookiecutter.version }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    license='MIT',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    description="{{ cookiecutter.project_short_description }}",
    keywords="{{ cookiecutter.project_slug }}"

    packages=find_packages(exclude=['tests']),

    zip_safe=True,
    include_package_data=True,

    data_files=[item for item in static_files(
        '%s/repositories/sql' % project, 'usr/share/%s' % project
    )],

    install_requires=[
        'aiohttp',
        'asyncpg',
        'cerberus',
        'click',
        'pyyaml',
        'raven',
        'raven-aiohttp',
        'ujson',
        'uvloop',
    ],

    extras_require={
        'develop': [
            'flake8',
            'flake8-builtins-unleashed',
            'flake8-bugbear',
            'flake8-comprehensions',
            'flake8-import-order',
            'flake8-mypy',
            'flake8-pytest'
        ]
    },

    entry_points='''
        [console_scripts]
        {{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.management.cli:cli
    '''
)
