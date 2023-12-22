# Readme

## 'Malice in Chains' game - T1A3 Terminal Application

### Overview of game

Malice in Chains (MiC) is a text based choose your own adventure game set in a cyberpunk style world. Players will make story choices based on their text input that will either lead them to victory or their untimely demise. You play as Malice and you are tracking down the villainous Killjoy for reasons unknown.

### Referenced Sources

- [PyPi Colored - Used to download Colored library and learn its functionality](https://pypi.org/project/colored/)
- [PyPi Computational-Stopwatch - Used to download Computational-Stopwatch library and learn its functionality](https://pypi.org/project/computational-stopwatch/)
- [PyPi Fontstyle - Used to download Fontstyle library and learn its functionality](https://pypi.org/project/fontstyle/)
- [PyPi name - Used to download name library and learn its functionality](https://pypi.org/project/names/)
- [W3 Schools - Used for various explanations such as understanding global vs local variables](https://www.w3schools.com/python/python_scope.asp)

### Source Control Repository

- [Terminal Application on Github](https://github.com/boldybread/T1A3_Terminal_Application)

### Code Styling Guide

- [PEP8](https://peps.python.org/pep-0008/)

### APP Features

Feature 1 - Story Function (Text input by user & print output of story)

- The bulk of the game will have an input text feature to make choices which continues the story in the form of print output. Depending on choices made by the user determines which path the story follows. I have done this by utilising different functions for different arcs of the story. Certain choices call upon different functions, some loop back into each other, other functions completely diverge off to a separate conclusion. Most of these functions utilised while loops with if user_input this, elif user_input that, to drive the story, and else to catch the errors if text other than what was expected was entered by the user.

Feature 2 - Random Encounter (Random NPC & number minigame)

- I added a compulsory encounter (random_encounter() within encounter.py) near the start of the game that creates a random Non Playable Character (NPC) with random attributes who plays a simple minigame of guess the number based on a randomly generated number. This adds to the replayability of the game by ensuring every playthrough is different. For this minigame I used a try block to test for value errors which could be caught with an exception if any non integers inputed. I was able to implement this in a way that the game would still continue in the event of a value error without disruption.

Feature 3 - Condition Variables (Player Condition & Obtainable Items)

- I added various 'condition' variables such as wounded and ammo which represent the player's condition or obtainable items which had the potential to be picked up by the player depending on certain choices. These are all bool values which would potentially force the story in a certain direction dependent on whether they were True or False at a particular time. Some of these were simple flavour text not providing too extreme a diversion, where some would be the difference between winning or losing the game in certain story arcs. This made the choices in the game more significant for the player.

Feature 4 - Rock, Paper, Scissors (Optional Minigame)

- I created an optional minigame of rock, paper, scissors that can be played with Nikki if she is alive at that point in the story. It can also be skipped by the player if they choose to. The feature randomises Nikki's choice and accepts players choice in the form of input. It then works out who won or a tie based on an if/elif/else statement. It will track the wins for Nikki and player, and when the player quits playing there is different dialogue depending on who was the overall winner or if there was a tie. The game will allow the player to play as many games in a row as they want or finish after any game.

### Implementation Plan

I used Trello to create my project management document.
I kept my implementation plan simple with 4 lists:

- 'Project Resources' list that contained an overview of the project plan and description of my labels that I would use.
- 'To do' list for tasks to be started
- 'Pending' list for tasks in progress
- 'Done' for completed tasks

![Project Management Overview](images\Project_Management.png)

I used the labels to help illustrate at a glance where I was up to and what was a priority or if I was stuck on a task because of a bug.

![Labels](images\labels.png)

I created a task to map out the story and the different arcs, this was vital as I needed to know the direction I was going, and I only had two weeks so I didn't want to be bogged down creating a really elaborate convoluted story. This task mapped out what chapters I wanted to have in the story and what they would contain as well as where I was going to place the two minigames.

![Create and organise the Story and various arcs](images\Create_story.jpg)

I created a task to create the intro feature which described in detail the function system I was going to use to make my game playable by calling a new function (based on player choices and input) to direct the story down a certain path. Once this was created most of the rest of the story involved similar setup for their various chapters.

![Intro Feature](images\Intro_Feature.png)

The random encounter was created as a compulsory minigame introducing a bunch of random elements designed to increase replayability. Player meets an NPC with randomly generated stats and plays a game of guess the number with the NPC.

![Creating Random Encounter story arc](images\Create_Random_Encounter.jpg)

Rock, Paper, Scissors was my second minigame I created that was optional again offering a break from the standard game process allowing the player to do something a bt different.

![Creating Rock, Peper, Scissors minigame](images\Create_RPS.jpg)

I created multiple bash scripts designed to setup the venv, check for python 3, install all required packages and then run the game. This is explained in more detail below in the Help Documentation.

![Creating bash scripts to setup and run game](images\Create_bash_scripts.jpg)

I made a task to create various bool variables that would reflect player conditions or obtainable items. These were key to the narrative as they would drive certain conclusions or offer additional options based on whether the player made certain choices earlier in the story to receive these afflictions or bonuses.

![Creating Player Conditions & Obtainable Items](images\Add_player_conditions.jpg)

### Help Documentation

Malice in Chains (MiC) needs to be run on Python 3 and requires multiple external Python Packages to function properly. Included in the app are 4 bash scripts, run.sh, packages.sh, venv_create.sh & setup.sh as well as a requirements.txt which can be viewed to see system requirements.

#### Running MiC

- First time playing you must first run setup.sh from command line with ```./setup.sh```

- Then execute run.sh from the command line to start game using ```./run.sh```

- For any subsequent playthroughs you can just use run.sh, setup only needs to be run once.

#### setup.sh

setup.sh must be run first. Run this script using the command ```./setup.sh```. This will first check for Python 3 on user's device. It will then run venv_create to create a virtual enviroment if it doesnt exist and then activate it. It will then run packages.sh which installs all required packages required to run MiC based off the requirements.txt file within the activated virtual environment. After this, setup is complete and run.sh can be run to launch the game.

#### venv_create.sh

venv_create.sh creates a virtual enviroment if it doesnt exist and then activates it. This script is automatically run from setup.sh and does not require to be run by the user. The venv will deactivate after the game closes, but be reopened again when run.sh is executed. The venv can be manually run from the command line with ```source .venv/activate/bin``` which can help in case of troubleshooting. The venv can then be deactivated with typing deactivate.

#### packages.sh

packages.sh installs all required packages required to run MiC based off the requirements.txt file within the activated virtual environment. This script is automatically run from setup.sh and does not require to be run by the user. If any of the packages cannot be found try uninstalling them from command line with ```pip uninstall package_name``` then install them with ```pip install package_name```. Their individual install paths can be found within packages.sh

#### run.sh

using the command ```./run.sh``` will run the main.py file which will start MiC. This can be run as long as setup.sh has been run once already to setup and install packages.

#### Troubleshooting

- Within the game the player will be required to enter text to make a story choice. The text that can be chosen as an action will usually be displayed in red. All the story text will be outputed to the screen, when the game is waiting on a choice from the player it will display at least one of the available options to the player for them to type. If a player enters any text other than a valid choice the game will prompt you to enter a valid choice and will not allow you to continue until the player does so.

- If you need to quit the game at anytime you can do so with CTRL Z to exit the APP. To start the game again utilise ```./run.sh```

- In the event of game over either via player death or game completion there will be an option to exit or start over by typing the relevant response.

- If package modules cannot be found when attempting to run the app try uninstalling them using ```pip uninstall package```, then reinstall the package using ```pip install package```. Package names can be found in requirements.txt or in packages.sh you will find the whole command for installing each package.

- If the virtual environment does not activate through the bash script you can manually activate by typing: ```source .venv/bin/activate``` in the command line.

- If the game does not run from the bash script it can be started with ```python main.py``` in the command line.

- If problems still persist try deleting the venv and running setup.sh again, and manually activate the new venv with ```source .venv/bin/activate```
