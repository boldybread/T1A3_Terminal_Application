#!/bin/bash

# check if python installed
[[ "$(python3 -V)" =~ "Python 3" ]] && echo "Python 3 is already installed"

# Create and activate venv
source venv_create.sh

# Download all required Python packages. packages.sh contains individual file paths if needed for reinstalling modules
./packages.sh