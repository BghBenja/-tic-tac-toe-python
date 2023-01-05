import string
import random

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('.')
        board.append(row)
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    coordinate = input("Please give a coordinate: ").upper()
    while True:

        if (coordinate[0].isalpha()
        and coordinate[1:].isnumeric()
        and ord(coordinate[0]) - 65 >= 0
        and ord(coordinate[0]) - 65 < 3
        and int(coordinate[1:]) > 0
        and int(coordinate[1:]) < 4):

            row = ord(coordinate[0]) - 65
            col = int(coordinate[1:]) - 1
            if board[row][col] == ".":
                break
            else:
                print("The coordinate is already taken.")
                coordinate = input("Please give a coordinate: ").upper()

        else:
        
            print("Incorect coordinate.")
            coordinate = input("Please give a coordinate: ").upper()

    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    while(True):
        row, col = random.randrange(0,3), random.randrange(0,3)
        if board[row][col] == ".":
                break 
    print(row,col)
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


def has_won(board, player):
    """Returns True if player has won the game."""
    win = None

    n = len(board)

    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n-1-i] != player:
            win = False
            break
    if win:
        return win
    return False


def is_full(board):
    """Returns True if board is full."""
    for i in board:
        if i.count(".") > 0:
            return True
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    n = len(board)
    alphabet = string.ascii_uppercase

    line_breake = f'\n  {"+".join(["---"]*n)}\n'
    result = []
    for row in range(n):
        result.append(f'{alphabet[row]}  {" | ".join(board[row])}')
    print("   1   2   3")
    print(line_breake.join(result))
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("Tie!")
    else:
        print(f'Winner is {winner} player!')


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    player = "X"
    winner = 0
    game_modes = mode.split("-")
    game_mode = game_modes[0]

    print_board(board)

    while(is_full(board)):
        if game_mode == "HUMAN":
            row, col = get_move(board, player)
        else:
            row, col = get_ai_move(board, player)
        mark(board, player, row, col)
        print_board(board)

        if has_won(board, player):
            winner = player
            break

        if player == "X":
            player = "O"
            game_mode = game_modes[1]
        else:
            player = "X"
            game_mode = game_modes[0]
    

    print_result(winner)

def print_menu():
    print("TicTacToa\n\nGame modes:\n\n1: Human vs Human\n2: Human vs Ai")

def main_menu():
    print_menu()
    game_mode = 0
    while(True):
        game_mode = input("\nChoos game mode: ")
        if game_mode.isnumeric() and int(game_mode) > 0 and int(game_mode) < 3:
            break
        else:
            print_menu()
    
    if game_mode == 1:
        tictactoe_game('HUMAN-HUMAN')
    else:
        tictactoe_game('HUMAN-AI')


if __name__ == '__main__':
    main_menu()