# Provide functions related to random number generation.
import random

# Game board creation grid size for user prompt grid size.
size = int(input("Enter the size of the grid: "))


# Function for board creation
def board_creation(size):
    return [["0" for _ in range(size)] for _ in range(size)]


# Function for game board creation
def print_board(board):
    for row in board:
        print(" ".join(row))

# Variables for board creation
board_player = board_creation(size)
board_computer = board_creation(size)


# Print out variables for boards
print("Player's board:")
print_board(board_player)

print("\nComputer's board:")
print_board(board_computer)