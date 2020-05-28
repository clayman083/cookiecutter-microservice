.PHONY: build clean clean-test clean-pyc clean-build proto

NAME	:= {{ cookiecutter.dockerhub_username }}/{{ cookiecutter.project_name.lower().replace('-', '_') }}
VERSION ?= latest


clean: clean-build clean-image clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-image:
	docker images -qf dangling=true | xargs docker rmi

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

install: clean
	poetry install

lint:
	poetry run flake8 src/{{ cookiecutter.project_name.lower().replace('-', '_') }} tests
	poetry run mypy src/{{ cookiecutter.project_name.lower().replace('-', '_') }} tests

run:
	poetry run python3 -m {{ cookiecutter.project_name.lower().replace('-', '_') }} --debug server run -t develop

test:
	tox

dist: clean-build
	poetry build

build:
	docker build -t ${NAME} .
	docker tag ${NAME} ${NAME}:$(VERSION)

publish:
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)
	docker push ${NAME}:$(VERSION)
