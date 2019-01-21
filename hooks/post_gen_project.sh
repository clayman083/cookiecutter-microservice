#! /bin/sh

git init

python3 -m venv venv
venv/bin/pip3 install -U pip

flit install -s --python venv/bin/python
