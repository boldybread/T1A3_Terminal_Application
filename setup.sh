#!/bin/bash

# # Check venv and create if needed
python3 -m venv .venv && echo "virtual environment is created"

# activate venv
source .venv/bin/activate && echo "virtual environment is activated"

# check if python installed
[[ "$(python3 -V)" =~ "Python 3" ]] && echo "Python 3 is already installed"


# Install required packages
# python3 -m pip install colored
# python3 -m pip install fontstyle
# python3 -m pip install computational-stopwatch
# python3 -m pip install names
# python3 -m pip install pygame

python3 -m pip install -r requirements.txt