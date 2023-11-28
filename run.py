# Provide functions related to random number generation.
import random


def board_creation(size):
    """
    Game board creation of given size.
    """
    return [["0" for _ in range(size)] for _ in range(size)]


def print_board(board, header=""):
    """
    Printing out the game board.
    """
    print(header)
    for row in board:
        print(" ".join(row))


def random_coordinates(board, chosen_coordinates):
    """
    Random row and column coordinates generation within the game board.
    Avoiding coordinates that have been already chosen.
    """
    while True:
        row, col = random.randint(0, len(board) - 1), \
            random.randint(0, len(board[0]) - 1)
        if (row, col) not in chosen_coordinates:
            return row, col


def place_ships(board, num, chosen_coordinates):
    """
    Ship placement on the board.
    """
    for _ in range(num):
        row, col = random_coordinates(board, chosen_coordinates)
        while board[row][col] == "X":
            row, col = random_coordinates(board, chosen_coordinates)
        board[row][col] = "X"
        chosen_coordinates.add((row, col))


def get_user_guess(size, guess_board):
    """
    Get the valid input from user for grid coordinates.
    While also avoiding already chosen coordinates.
    """
    while True:
        try:
            row = int(input(f"Enter row (0-{size-1}): "))
            col = int(input(f"Enter column (0-{size-1}): "))
            if 0 <= row < size and 0 <= col < size and guess_board[row][col] \
                    == "0":
                return row, col
            else:
                print(f"Invalid or already chosen coordinates. \
                     Please try again.")
        except ValueError:
            print("Invalid data. Please input a number.")


def user_turn(board, guess, guess_board):
    """
    Handle the user's move.
    """
    row, col = guess
    if board[row][col] == "X":
        print("You hit computer's ship!")
        board[row][col] = "H"
        guess_board[row][col] = "H"
    else:
        print("Missed a shot!")
        guess_board[row][col] = "M"


def computer_turn(player_board, guess_board, chosen_coordinates):
    """
    Handle the computer's move.
    """
    row, col = random_coordinates(player_board, chosen_coordinates)
    if player_board[row][col] == "X":
        print("Computer hit your ship!")
        player_board[row][col] = "H"
        guess_board[row][col] = "H"
    else:
        print("Computer missed a shot!")
        player_board[row][col] = "M"
        guess_board[row][col] = "M"
    chosen_coordinates.add((row, col))


# Game setup
size = int(input("Enter the size of the grid: "))
# Variables for board creation
board_player = board_creation(size)
board_computer = board_creation(size)
guess_board_player = board_creation(size)
guess_board_computer = board_creation(size)
NUM_SHIPS = 5

# Keeping track of chosen coordinates
player_chosen_coordinates = set()
computer_chosen_coordinates = set()
# Ship placement variables
place_ships(board_player, NUM_SHIPS, player_chosen_coordinates)
place_ships(board_computer, NUM_SHIPS, computer_chosen_coordinates)


# Game loop
while True:

    print("Player's turn:")
    user_guess = get_user_guess(size, guess_board_player)
    user_turn(board_computer, user_guess, guess_board_player)

    print_board(guess_board_player, "Player's guess board:")

    if all(all(cell != "X" for cell in row) for row in board_computer):
        print("Congratulations! Enemy ships are sunk! You won the day!")
        break

    print("Computer's turn:")
    computer_turn(board_player, guess_board_computer, computer_chosen_coordinates)

    print_board(board_player, "Player's board:")

    if all(cell == "H" for row in board_player for cell in row):
        print("Game over! Enemy sank your ships! You lost!")
        break
