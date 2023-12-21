#!/bin/bash

# # Check venv and create if needed
python3 -m venv .venv && echo "virtual environment is created"

# activate venv
source .venv/bin/activate && echo "virtual environment is activated"