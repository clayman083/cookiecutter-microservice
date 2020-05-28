FROM python:3.8-alpine3.11 as build

RUN apk add --update --no-cache --quiet \
        make libc-dev python3-dev libffi-dev gcc g++ git openssl-dev && \
    python3 -m pip install --no-cache-dir --quiet -U pip && \
    python3 -m pip install --no-cache-dir --quiet poetry

ADD . /app

WORKDIR /app

RUN poetry build


FROM python:3.8-alpine3.11

COPY --from=build /app/dist/*.whl .

RUN apk add --update --no-cache --quiet \
        make libc-dev python3-dev libffi-dev openssl-dev gcc g++ git && \
    python3 -m pip install --no-cache-dir --quiet -U pip && \
    python3 -m pip install --no-cache-dir --quiet *.whl && \
    rm -f *.whl && \
    apk del --quiet make libc-dev python3-dev libffi-dev openssl-dev gcc g++ git

EXPOSE 5000

ENTRYPOINT ["python3", "-m", "{{ cookiecutter.project_name.lower().replace('-', '_') }}"]

CMD [ "server", "run", "--host=0.0.0.0", "--port=5000" ]
