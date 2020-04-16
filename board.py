def create_board():

    board = [[]] * 8
    pawn = ['W♙'] * 8
    for element in range(8):
        if element == 0: board[element] = ['B♖','B♘','B♗','B♕','B♔','B♗','B♘','B♖']
        elif element == 7 : board[element] = ['W♖','W♘','W♗','W♕','W♔','W♗','W♘','W♖']
        elif element == 1: board[element] = pawn
        elif element == 6 : board[element] = pawn
        else: board[element] = ["  "] * 8

    return board


def show_board(board):

    for row in board:
        for column in row:
            print("   |   ", column, end="  ")
        print("   | \n")


show_board(create_board())