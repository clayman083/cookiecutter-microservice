FROM python:3.7-alpine3.8

ARG app_version

# Copy application distribution package
COPY dist/{{ cookiecutter.project_slug }}-${app_version}.tar.gz /root/

# Install required packages
RUN apk add --update --no-cache make libc-dev python3-dev linux-headers gcc g++ postgresql-client && \
    pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir /root/{{ cookiecutter.project_slug }}-${app_version}.tar.gz && \
    rm /root/{{ cookiecutter.project_slug }}-${app_version}.tar.gz && \
    apk del make libc-dev python3-dev linux-headers gcc g++

EXPOSE 5000

CMD ["{{ cookiecutter.project_slug }}", "--config=/root/config.yml", "server", "run", "--host=0.0.0.0", "--consul"]
