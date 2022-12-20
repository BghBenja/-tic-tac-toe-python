import string

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
    row, col = 0, 0
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
            return False
    return True


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
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    print(row,col)
    mark(board, 1, row, col)
    print(board)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()