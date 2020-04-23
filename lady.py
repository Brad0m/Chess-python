# from board import Board
from tower import tower_movements
from bishop import bishop_movements

def lady_movements(board, column, row, next_column, next_row):
    if tower_movements(board, column, row, next_column, next_row) and bishop_movements(board, column, row, next_column, next_row) == False :
        return False


# chess_board = Board().create_board()
# bishop_movements(chess_board, 3, 0, 2, 2)
# for i in chess_board:
#     print(i)
