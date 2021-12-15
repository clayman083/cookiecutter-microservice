#! /bin/sh

set -ex

pyenv local 3.10.0
poetry env use $PYENV_ROOT/versions/3.10.0/bin/python3
poetry install 

# git init
# git add -A
# git commit -m "Initial project structure"
