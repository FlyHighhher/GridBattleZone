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


# Ship placement function on the board
def place_ships(board, num):
    """
    Ship placement on the board.
    """
    for _ in range(num):
        row, col = random_coordinates(board, set())
        while board[row][col] == "X":
            row, col = random_coordinates(board, set())
        board[row][col] = "X"


# Function for user input asking row and column
def get_user_guess(size, chosen_coordinates):
    """
    Get the valid input from user for grid coordinates.
    While also avoiding already chosen coordinates.
    """
    while True:
        try:
            row = int(input(f"Enter row (0-{size-1}): "))
            col = int(input(f"Enter column (0-{size-1}): "))
            if 0 <= row < size and 0 <= col < size and (row, col) \
                    not in chosen_coordinates:
                chosen_coordinates.add((row, col))
                return row, col
            else:
                print(f"Invalid or already chosen coordinates. \
                     Please try again.")
        except ValueError:
            print("Invalid data. Please input a number.")


# Function for user turn handling
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


# Function for computer's turn handling
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
board_computer_ships = board_creation(size)
guess_board_player = board_creation(size)
NUM_SHIPS = 5
# Ship placement variables
place_ships(board_player, NUM_SHIPS)
place_ships(board_computer_ships, NUM_SHIPS)

# Keeping track of chosen coordinates
player_chosen_coordinates = set()
computer_chosen_coordinates = set()

# Game loop
while True:
    print_board(board_player, "Player's board:")

    print("Player's turn:")
    user_guess = get_user_guess(size, player_chosen_coordinates)
    user_turn(board_computer_ships, user_guess, guess_board_player)
    print_board(guess_board_player, "Player's guess board:")

    if all(all(cell != "X" for cell in row) for row in board_computer_ships):
        print("Congratulations! Enemy ships are sunk! You won the day!")
        break
    
    print("Computer's turn:")
    computer_turn(board_player, board_computer_ships, computer_chosen_coordinates)

    if all(all(cell != "X" for cell in row) for row in board_player):
        print("Game over! Enemy sank your ships! You lost!")
        break
