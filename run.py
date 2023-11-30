# Provide functions related to random number generation.
import random


def board_creation(size):
    """
    Creates a square game board with given size.
    """
    return [["0" for _ in range(size)] for _ in range(size)]


def print_board(board, header=""):
    """
    Prints the board with indices for row and column
    and a header text on top.
    """
    print(header)
    col_indices = [str(i) for i in range(len(board))]
    print("  " + " ".join(col_indices))
    for i, row in enumerate(board):
        print(f"{i}|{' '.join(row)}")


def random_coordinates(
    board,
    chosen_coordinates,
    avoid_player_coordinates=False,
    player_chosen_coordinates=None
):
    """
    Random row and column coordinates generation within the game board.
    Avoiding coordinates that have been already chosen.
    """
    while True:
        row, col = random.randint(0, len(board) - 1), \
            random.randint(0, len(board[0]) - 1)
        if (row, col) not in chosen_coordinates and \
                (
                    not avoid_player_coordinates
                    or (row, col) not in player_chosen_coordinates):
            return row, col


def place_ships(board, num, chosen_coordinates):
    """
    The function randomly selects coordinates
    on the board and places ships marked as ('X')
    at those positions. By also ensuring that there is no
    overlap with already chosen coordinates.
    """
    for _ in range(num):
        row, col = random_coordinates(board, chosen_coordinates)
        while board[row][col] == "X":
            row, col = random_coordinates(board, chosen_coordinates)
        board[row][col] = "X"
        chosen_coordinates.add((row, col))


def get_user_guess(size, guess_board):
    """
    Function asks the user to input row and column coordinates within
    the range. While also ensuring that the coordinates are valid and
    have not been chosen on the guess board.
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
    Updating the game board based on user's move. In case of a hit
    it is marked on the board. In case of a miss it is also marked.
    """
    row, col = guess
    if board[row][col] == "X":
        print("You hit computer's ship!")
        board[row][col] = "H"
        guess_board[row][col] = "H"
    else:
        print("Missed a shot!")
        guess_board[row][col] = "M"


def computer_turn(
    player_board,
    guess_board,
    chosen_coordinates
):
    """
    Handle's the computer's move on the board.
    Function generates random coordinates and checks for hits and misses.
    """
    row, col = random_coordinates(
        player_board,
        chosen_coordinates,
        avoid_player_coordinates=False,
        player_chosen_coordinates=player_chosen_coordinates
    )
    if player_board[row][col] == "X":
        print("Computer hit your ship!")
        player_board[row][col] = "H"
        guess_board[row][col] = "H"
    else:
        print("Computer missed a shot!")
        player_board[row][col] = "M"
        guess_board[row][col] = "M"
    chosen_coordinates.add((row, col))


def get_grid_size():
    """
    Function asks the user to input the size of the game grid
    by also ensuring that is valid number.
    """
    while True:
        try:
            size = int(
                input("Enter the size of the grid (choose from 5, 7, 10): "))
            if size in [5, 7, 10]:
                return size
            else:
                print("Invalid grid size input. Please choose from 5, 7, 10.")
        except ValueError:
            print("Invalid data. Please input a number.")


def calculate_ship_amount(size):
    """
    Function for setting the amount ships depending on the grid size.
    """
    if size == 5:
        return 8
    if size == 7:
        return 15
    if size == 10:
        return 30
    else:
        raise ValueError("Invalid grid size")


def calculate_max_rounds(size):
    """
    Function for calculating maximum rounds based on grid size.
    """
    if size == 5:
        return 17
    elif size == 7:
        return 35
    elif size == 10:
        return 70
    else:
        raise ValueError("Invalid grid size")


def check_draw(round_count, max_rounds):
    """
    Function for checking if the game has reached draw.
    """
    if round_count >= max_rounds:
        print(f"Game Over! You both ran out of ammunition. It's a draw.")
        return True
    return False


# Game setup
valid_grid_sizes = [5, 7, 10]
size = get_grid_size()

NUM_SHIPS = calculate_ship_amount(size)
MAX_ROUNDS = calculate_max_rounds(size)

print(f"Welcome to GridBattleZone!\n"
      f"You must sink {NUM_SHIPS} ships in order to win.\n"
      f"You have limited number of rounds to defeat the computer.\n"
      f"Make every shot count! You will have {MAX_ROUNDS} rounds in total.\n")

# Variables for board creation
board_player = board_creation(size)
board_computer = board_creation(size)
guess_board_player = board_creation(size)
guess_board_computer = board_creation(size)

# Keeping track of chosen coordinates
player_chosen_coordinates = set()
computer_chosen_coordinates = set()
# Ship placement variables
place_ships(board_player, NUM_SHIPS, player_chosen_coordinates)
place_ships(board_computer, NUM_SHIPS, computer_chosen_coordinates)
# Round count
round_count = 0


# Game loop
while True:
    round_count += 1
    print(f"\n--- Round {round_count} ---")

    print("Player's turn:")
    user_guess = get_user_guess(size, guess_board_player)
    user_turn(board_computer, user_guess, guess_board_player)

    print_board(guess_board_player, "Player's guess board:")

    if all(all(cell == "H" for cell in row) for row in board_computer):
        print("Congratulations! Enemy ships are sunk! You won the day!")
        break

    print("Computer's turn:")
    computer_turn(
        board_player,
        guess_board_computer,
        computer_chosen_coordinates,
    )

    print_board(board_player, "Player's board:")

    if all(all(cell == "H" for cell in row) for row in board_player):
        print("Game over! Enemy sank your ships! You lost!")
        break

    max_rounds = calculate_max_rounds(size)
    if check_draw(round_count, max_rounds):
        break
