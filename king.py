# from board import Board

def king_movements(board, column, row, next_column, next_row):
    if (column + row) - (next_column + next_row) in [0, 1, -1 , 2, -2]:
        board[next_row][next_column] = board[row][column]
        board[row][column] = "  "    
        return True
    else: return False

# chess_board = Board().create_board()
# bishop_movements(chess_board, 3, 0, 2, 2)
# for i in chess_board:
#     print(i)