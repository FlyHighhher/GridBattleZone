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


# Function for user input asking row and column
def get_user_guess():
    while True:
        try:
            row = int(input(f"Enter row (0-{size-1}): "))
            col = int(input(f"Enter column (0-{size-1}): "))
            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                print(f"Invalid data. Row and column must be between 0 and {size-1}.")
        except ValueError:
            print("Invalid data. Please input a number.")


# Function for user turn handling
def user_turn(board, guess):
    row, col = guess
    if board[row][col] == "X":
        print("Ship hit!")
        board[row][col] = "H"
    else:
        print("Missed a shot!")

# Print out variables for boards
while True:
    print("Player's board:")
    print_board(board_player)

    print("\nComputer's board:")
    print_board(board_computer)

    print("Player's turn:")
    user_guess = get_user_guess()
    user_turn(board_computer, user_guess)

    if all("X" not in row for row in board_computer):
        print("Congratulations! You destroyed all enemy ships! You won the day!")
        break