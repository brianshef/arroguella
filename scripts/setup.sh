#!/bin/bash

set -eu
echo "Installing dependencies and setting up virtual python environment ... "
pip install -U pipenv
export PIPENV_VENV_IN_PROJECT=1
pipenv sync
pipenv shell
echo -e "Done.\n"
