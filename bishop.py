from board import Board

def bishop_movements(board, column, row, next_column, next_row):

            if (column + next_row) == (row + next_column):
                board[next_row][next_column] = board[row][column]
                board[row][column] = "  "
                return True
            else: return False
                

# chess_board = Board().create_board()
# bishop_movements(chess_board, 2, 0, 1, 2)
# for i in chess_board:
#     print(i)

# xpos = 3
# ypos = 5
# x = 4
# y = 6


# print ((xpos + y) == (ypos + x) ) 
