.PHONY: clean clean-test clean-pyc clean-build

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr tests/coverage
	rm -f tests/coverage.xml

lint:
	flake8 {{ cookiecutter.project_slug }} tests

test:
	py.test

test-all:
	tox

coverage:
	coverage erase
	coverage run -m py.test \
        --pg-image=postgres:alpine \
        --pg-reuse \
        --pg-name=db-cf2b8d1e-24d4-41a0-9e1e-88d2e4789a02 \
        -v tests
	coverage report -m
	coverage xml
	coverage html

dist: clean-build
	python setup.py sdist

install: clean
	pip install -e .

build-image: dist
	docker build --build-arg app_version=`python setup.py --version` -t {{ cookiecutter.project_slug }} .
	docker tag {{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }}:`python setup.py --version`
	docker images -qf dangling=true | xargs docker rmi
