Word Game Project
This repository contains a Python-based word game that allows users to play a word-guessing game with both GUI and command-line interfaces. The project includes multiple classes and modules designed to handle various aspects of gameplay, including player management, game logic, and word processing.

Project Overview
The Word Game Project is a comprehensive implementation that includes:

Word Game Logic: The core logic that handles the word guessing game, ensuring proper tracking of guesses, word validation, and scoring.
GUI Implementation: A graphical user interface built with Python to provide an interactive experience for players.
AI Player: A class implementation that allows the computer to play the game using algorithmic strategies.
Unit Tests: Test scripts to ensure the reliability and correctness of the game’s functionality.
Key Features
Command-Line and GUI Support: Play the game either in the terminal or using the graphical interface.
AI Player Option: Challenge a computer player with different levels of difficulty.
Word Bank: A comprehensive list of valid words stored in words.txt to ensure varied gameplay.
Modular Code Structure: The project is organized into several Python files, each handling specific aspects of the game like game logic, player management, and testing.
How to Run the Game
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/word-game-project.git
Install Required Dependencies (if any):

Run the Game:
For the command-line version:
bash
Copy code
python wordgame.py
For the GUI version:
bash
Copy code
python wordgamegui.py
Files in the Repository
wordgame.py: Main game logic and command-line interface.
wordgamegui.py: GUI version of the word game.
wordgameplayer.py: Handles player-related logic, including AI strategies.
wordgametest.py: Unit tests to validate game functionalities.
words.txt: The word list used in the game for validation.
