#!/bin/bash

# check if python installed



python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 main.py