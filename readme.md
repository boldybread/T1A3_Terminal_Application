# Readme

## 'Malice in Chains' game - T1A3 Terminal Application

### Overview of game

Malice in Chains (MiC) is a text based choose your own adventure game set in a cyberpunk style world. Players will make story choices based on their text input that will either lead them to victory or their untimely demise. You play as Malice and you are tracking down the villainous Killjoy for reasons unknown.

### Referenced Sources

- [PyPi Pygame - Used to download Pygame library and learn its functionality](https://pypi.org/project/pygame/)
- [PyPi Colored - Used to download Colored library and learn its functionality](https://pypi.org/project/colored/)
- [PyPi Computational-Stopwatch - Used to download Computational-Stopwatch library and learn its functionality](https://pypi.org/project/computational-stopwatch/)
- [PyPi Fontstyle - Used to download Fontstyle library and learn its functionality](https://pypi.org/project/fontstyle/)
- [PyPi name - Used to download name library and learn its functionality](https://pypi.org/project/names/)
- [Educative - Used for help to get the audio to work](https://www.educative.io/answers/how-to-play-an-audio-file-in-pygame)
- [W3 Schools - Used for various explanations such as understanding global vs local variables](https://www.w3schools.com/python/python_scope.asp)
- [YtMp3 - Used to download copyright free music off Youtube](https://ytmp3.cc/a172/)

### Source Control Repository

- [Terminal Application on Github](https://github.com/boldybread/T1A3_Terminal_Application)

### Code Styling Guide

- [PEP8](https://peps.python.org/pep-0008/)

### APP Features

- The bulk of the game will have an input text feature to make choices which continues the story in the form of print output. Depending on choices made by the user determines which path the story follows. I have done this by utilising different functions for different arcs of the story. Certain choices call upon different functions, some loop back into each other, other functions completely diverge off to a separate conclusion. Most of these functions utilised while loops with if user_input this, elif user_input that, to drive the story, and else to catch the errors if text other than what was expected was entered by the user.

- I added a compulsory encounter near the start of the game that creates a random Non Playable Character with random attributes who plays a simple mini game of guess the number based on a random number. This adds to the replayability of the game by ensuring every playthrough is different. For this mini game I used a try except block to test for value errors which could catch any non integers inputed.

- I added various variables such as wounded and lighter which represent player condition or obtainable items. These are all bool values which would potentially force the story in a certain direction dependent on whether they were True or False at a particular time. Some of these were simple flavor text, where some would be the difference between winning or losing the game in certain story arcs.

### Implementation Plan

Images from Trello

### Help Documentation

Malice in Chains (MiC) needs to be run on Python 3 and requires multiple external Python Packages to function properly. Included in the app are 4 bash scripts, run.sh, packages.sh, venv_create.sh & setup.sh as well as a requirements.txt which can be viewed to see system requirements.

#### setup.sh

setup.sh should be run first. Run this script using the command ```./setup.sh```. This will first check for Python 3 on user's device. It will then run venv_create to create a virtual enviroment if it doesnt exist and then activate it. It will then run packages.sh which installs all required packages required to run MiC based off the requirements.txt file within the activated virtual enviroment. After this setup is complete and run.sh can be run to launch the game.

#### venv_create.sh

venv_create.sh creates a virtual enviroment if it doesnt exist and then activates it. This script is automatically run from setup.sh and does not require to be run by the user. If the venv does not activate it can be manually run from the command line with ```source .venv/activate/bin```

#### packages.sh

packages.sh installs all required packages required to run MiC based off the requirements.txt file within the activated virtual enviroment. This script is automatically run from setup.sh and does not require to be run by the user. If any of the packages cannot be found try uninstalling them from command line with ```pip uninstall package_name``` then install them with ```pip install package_name```. Their individual install paths can be found within packages.sh

#### run.sh

using the command ```./run.sh``` will run the main.py file which will start MiC. This can be run as long as setup.sh has been run already to setup and install packages.

#### Troubleshooting

- Within the game the player will be required to enter text to make a story choice. The text that can be chosen as an action will be displayed in red. All the story text will be outputed to the screen, when the game is waiting on a choice from the player it will display at least one of the available options to the player for them to type. If a player enters any text other than a valid choice the game will prompt you to enter a valid choice and will not allow you to continue until the player does so.

- If you need to quit the game at anytime you can do so with CTRL Z to exit the APP. To start the game again utilise ```./run.sh or python main.py```

- In the event of gameover either via player death or game completion there will be an option to exit or start over by typing the relevant response.

- If package modules cannot be found when attempting to run app try uninstalling them using ```pip uninstall package```, then reinstall the package using ```pip install package```. Package names can be found in requirements.txt or setup.sh

- If the virtual environment does not activate through the bash script you can manually activate by typing: ```source .venv/bin/activate``` in the command line.

- If the game does not run from the bash script it can be started with ```python main.py``` in the command line.

- If problems still persist try deleting the venv and running setup.sh again, and manually enter activate the new venv with ```source .venv/bin/activate```
