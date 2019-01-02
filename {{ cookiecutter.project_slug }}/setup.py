import os

from setuptools import find_packages, setup


setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    license='MIT',
    author="{{ cookiecutter.author_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    description="{{ cookiecutter.description }}",
    keywords="{{ cookiecutter.project_slug }}",

    packages=find_packages(exclude=['tests']),

    zip_safe=True,
    include_package_data=True,

    install_requires=[
        'aiodns==1.1.1',
        'aiohttp==3.5.1',
        'attrs==18.2.0',
        'cchardet==2.1.4',
        'cerberus==1.2',
        'click==7.0',
        'prometheus_client==0.5.0',
        'pyyaml==3.13',
        'raven==6.10.0',
        'raven-aiohttp==0.7.0',
        'ujson==1.35',
        'uvloop==0.11.3',
    ],

    extras_require={
        'develop': [
            'flake8==3.6.0',
            'flake8-bugbear==18.8.0',
            'flake8-builtins-unleashed==1.3.1',
            'flake8-comprehensions==1.4.1',
            'flake8-import-order==0.18',
            'flake8-pytest==1.3',
            'flake8-print==3.1.0',
            'mypy==0.650',

            'faker==1.0.1',
            'pytest==4.0.2',
            'pytest-aiohttp==0.3.0',
            'coverage==4.5.2',
        ]
    },

    entry_points='''
        [console_scripts]
        {{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:cli
    '''
)
