from board import Board

def tower_movements(board, column, row, next_column, next_row):
      
            if next_column == column: 
                board[next_row][column] = board[row][column]
                board[row][column] = "  "
                return True

            elif next_row == row:
                board[row][next_column] = board[row][column]
                board[row][column] = "  "
                return True
                
            else: return False

# chess_board = Board().create_board()
# tower_movements(chess_board, 0, 0, 1, 1)
# for i in chess_board:
#     print(i)