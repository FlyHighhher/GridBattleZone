# GridBattleZone

## Overview

The game is simplified version of the classic Battleship game, typically played between two players. In this case it is a one player game, where user plays against the computer.

### Game Setup

* The player is prompted to choose the size of the game grid (3*3, 5*5, 7*7).
* The number of ships is determined based on the chosen grid size (1 for 3 by 3, 4 for 5 by 5 and 8 for 7 by 7).
* The maximum number of rounds is calculated based on the grid size ( 8 rounds for grid size 3*3, 18 rounds for grid size 5*5 and 38 rounds for grid size 7*7.)
* Two game boards are created for the player and the computer along with corresponding guess boards.

### Ship Placement

Ships are randomly placed on both the player's and the computer's boards.

### Game Loop

The game consist of a loop where each iteration represents a round. In each round: 

* The player takes a turn by inputting a row and a column coordinates to guess the computers ship position.
* The computer takes a turn by randomly choosing coordinates to guess the player's ship positions.
* The game boards are updated to reflect hits ( marked as 'H' ) and misses ( markes as 'M' ).
* The player's and the computer's boards are displayed to show the progress.

### Winning and Losing Conditions

The game continues until one of the following conditions is met:

* The player sinks all of the computer's ships ('H' in all cells of the computer's board)
* The computer sinks all of the player's ships ('H' in all cells of the player's board)
* The maximum number of rounds is reached, resulting in a draw.

### Game Outcome Display

The game concludes with a message indicating whether the player won, lost, or the game ended in a draw.

### Game Flow Chart

![Flow Chart](/images/flowchart.png)

## Features

The key features for GridBattleZone are:

### Grid Selection

The player's are able to choose the size of the game grid at the beginning of the game. The options are 3 by 3, 5 by 5 and 7 by 7.

### Dynamic Ship Placement

The number of the ships is determined by the chosen grid size, providing a scalable and varied gameplay experience. Ships are randomly placed on the board.

### Turn-Based Gameplay

The game follows a turn-based structure, where the player and the computer take alternating turns to make guesses.

### User Input Validation

The game validates user input for row and column coordinates to ensure they are within the valid range and not have been chosen before.

### Hit and Miss Feedback

After each move, the game provides feedback to the player, indicating whether their guess was a hit or a miss.

### Game Board Display

The game displays the player's and the computer's boards after each move, showing the progress and the locations of hits and misses.

### Winning/Losing Conditions

The game has clear winning and losing coditions. Player wins if all computers ships are sunk. Computer wins if all players ships are sunk. And a draw is declared when the maximum number of rounds is reached.

### Round Limit

There is a maximum limit on the number of rounds, preventing the game from continuing indefinetly. This adds a strategic element to the gameplay.

### Scalable Difficulty

The difficulty scales with the grid size and number of ships, providing different levels of challenge.

### Modular Functions

The game code is organized into modular functions, making it readable and allowing for easy maintenance and expansion.

### Game Outcome Messages

The game provides clear and informative messages to indicate the outcome, such as whether the player won, lost, or if it's a draw.

### Random Number Generation

The game utilizes a random number generation function to determine ship placement and computer guesses, adding an element of unpredictability.

## Validator PEP-8

Python validator was used in order to validate to check if any errors were found. No errors were found.

## Acknowledgements

* Mentor David Bowers was of great help in giving good feedback and ideas for creation of this game.
* Code Institute's walkthrough project Love-Sandwiches was very helpful in creating this project.
* Pythondex battleship game creation with source code was of great inspiration to this game.

## Improvements

* In future versions of the game a improvement of adjustable difficulty levels is considerable.
* Customizable settings in terms of changing the amount of ships and rounds could be also a good future improvement goal.
* Different ship types - as 1, 2, 3 and 4 grid size ships could be a good addition in future versions.



