#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate


# check if python installed
[[ "$(python3 -V)" =~ "Python 3" ]] && echo "Python 3 is installed"



python3 -m pip install colored
python3 -m pip install fontstyle
python3 -m pip install computational-stopwatch

python3 main.py