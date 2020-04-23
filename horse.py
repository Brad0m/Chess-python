# from board import Board
def horse_movements(board, column, row, next_column, next_row):

    if next_row == row + 2 and next_column == column + 1 or next_column == column - 1:
        board[next_row][next_column] = board[row][column]
        board[row][column] = "  "
        return True


    elif next_row == row - 2 and next_column == column + 1 or next_column == column - 1:
        board[next_row][next_column] = board[row][column]
        board[row][column] = "  "
        return True

    elif next_column == column + 2 and next_row == row + 1 or next_row == row - 1:
        board[next_row][next_column] = board[row][column]
        board[row][column] = "  "       
        return True

    else: return False


# chess_board = Board().create_board()
# horse_movements(chess_board, 1, 0, 1, 2 )
# for i in chess_board:
#     print(i)