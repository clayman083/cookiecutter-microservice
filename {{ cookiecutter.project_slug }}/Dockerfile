FROM python:alpine

ARG app_version

# Install required packages
RUN apk add --update --no-cache make libc-dev python3-dev linux-headers gcc postgresql-client

# Copy application distribution package
COPY dist/{{ cookiecutter.project_slug }}-${app_version}.tar.gz /root/

# Install application package
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir /root/{{ cookiecutter.project_slug }}-${app_version}.tar.gz && \
    rm /root/{{ cookiecutter.project_slug }}-${app_version}.tar.gz

RUN mkdir -p /usr/share/{{ cookiecutter.project_slug }} && cp /usr/local/lib/python3.6/site-packages/{{ cookiecutter.project_slug }}/repositories/sql/* /usr/share/{{ cookiecutter.project_slug }}


EXPOSE 5000

CMD ["{{ cookiecutter.project_slug }}", "--config=/root/config.yml", "server", "run", "--host=0.0.0.0", "--consul"]
