import random

# Set up the board
def create_board():
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

# Randomly place the battleship
def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

# Initialize the game
board = create_board()
ship_row = random_row(board)
ship_col = random_col(board)

print("Let's play Battleship!")
print_board(board)

# Allow the player to guess
for turn in range(4):
    print(f"\nTurn {turn + 1}")

    try:
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))

        # Check if guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            # Check for invalid guesses
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)

        # If the player runs out of turns
        if turn == 3:
            print(f"Game Over! The battleship was at Row {ship_row}, Col {ship_col}.")
    except ValueError:
        print("Please enter a valid integer.")