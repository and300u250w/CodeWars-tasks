# from IPython.display import clear_output


def display_board(board):
    # clear_output()
    print(" {} | {} | {}".format(board[1], board[2], board[3]))
    print(" {} | {} | {}".format(board[4], board[5], board[6]))
    print(" {} | {} | {}".format(board[7], board[8], board[9]))


test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
# display_board(test_board)


def player_input():
    marker = ""
    while marker not in ["X", "O"]:
        marker = input("Player 1 please pick a marker 'X' or 'O'").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


# player1_marker, player2_marker = player_input()


def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, "$", 8)
display_board(test_board)


def win_check(board, mark):

    return (
        board[7] == board[8] == board[9] == mark
        or board[1] == board[2] == board[3] == mark
        or board[4] == board[5] == board[6] == mark
        or board[1] == board[5] == board[9] == mark
        or board[3] == board[5] == board[7] == mark
        or board[1] == board[4] == board[7] == mark
        or board[2] == board[5] == board[8] == mark
        or board[3] == board[6] == board[9] == mark
    )


win_check(test_board, "X")

import random


def choose_first():
    result = random.randint(1, 2)
    if result == 1:
        return "Player 1 start the Game"
    else:
        return "Player 2 start the Game"


choose_first()


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):

    for i in range(1, 9):
        if space_check(board, i):
            return False

    return True


def player_choice(board):

    position = int(input("Please enter your number: "))
    if space_check(board, position):
        position = int(input("This position is taken. Please enter your number: "))
    else:
        return position


player_choice(["#", "X", "O", "", "O", "X", "", "X", "", "X"])
