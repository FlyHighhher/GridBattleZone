# Provide functions related to random number generation.
import random

# Function for board creation
def board_creation(size):
    """
    Game board creation of given size.
    """
    return [["0" for _ in range(size)] for _ in range(size)]


# Function for game board creation
def print_board(board, header=""):
    """
    Printing out the game board.
    """
    print(header)
    for row in board:
        print(" ".join(row))


# Function for random values generation for row and column
def random_coordinates(board):
    """
    Random row and column coordinates generation within the game board.
    """
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board[0]) - 1)
    return row, col


# Ship placement function on the board
def place_ships(board, num):
    """
    Ship placement on the board.
    """
    for _ in range(num):
        row, col = random_coordinates(board)
        while board[row][col] == "X":
            row, col = random_coordinates(board)
        board[row][col] = "X"


# Function for user input asking row and column
def get_user_guess(size):
    """
    Get the valid input from user for grid coordinates.
    """
    while True:
        try:
            row = int(input(f"Enter row (0-{size-1}): "))
            col = int(input(f"Enter column (0-{size-1}): "))
            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                print(f"Row and column must be between 0 and {size-1}.")
        except ValueError:
            print("Invalid data. Please input a number.")


# Function for user turn handling
def user_turn(board, guess):
    """
    Handle the user's move.
    """
    row, col = guess
    if board[row][col] == "X":
        print("Ship hit!")
        board[row][col] = "H"
    else:
        print("Missed a shot!")

# Game setup
size = int(input("Enter the size of the grid: "))
# Variables for board creation
board_player = board_creation(size)
board_computer = board_creation(size)
# A constant for a number of ships
NUM_SHIPS = 5
# Ship placement variables
place_ships(board_player, NUM_SHIPS)
place_ships(board_computer, NUM_SHIPS)

# Game loop
while True:
    print_board(board_player, "Player's board:")

    print_board(board_computer, "Computer's board:")

    print("Player's turn:")
    user_guess = get_user_guess(size)
    user_turn(board_computer, user_guess)

    if all("X" not in row for row in board_computer):
        print("Congratulations! Enemy ships are sunk! You won the day!")
        break
