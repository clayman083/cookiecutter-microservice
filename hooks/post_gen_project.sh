#! /bin/sh

python3 -m venv venv
venv/bin/pip3 install -U pip
venv/bin/pip3 install -e '.[develop]'
