#!/bin/bash

python3 -m venv .venv
cd .venv
source /bin/activate


# check if python installed
# [[ "$(python3 -V)" =~ "Python 3" ]] && echo "Python 3 is installed"



pip3 install colored
pip3 install fontstyle
pip3 install pygame
# python3 main.py