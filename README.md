# GridBattleZone

## Overview

The game is simplified version of the classic Battleship game, typically played between two players. In this case it is a one player game, where user plays against the computer.

### Game Setup

* The player is prompted to choose the size of the game grid (5*5, 7*7, 10*10).
* The number of ships is determined based on the chosen grid size (8 for 5 by 5, 15 for 7 by 7 and 30 for 10 by 10).
* The maximum number of rounds is calculated based on the grid size ( 17 rounds for grid size 5, 35 rounds for grid size 7 and 70 rounds for grid size 10.)
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


