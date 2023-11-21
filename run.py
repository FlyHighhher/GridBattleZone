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


# Ship placement function on the board
def place_ships(board, num):
    for _ in range(num):
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        while board[row][col] == "X":
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
        board[row][col] = "X"


# Ship placement variables
place_ships(board_player, 5)
place_ships(board_computer, 5)