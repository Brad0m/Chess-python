import pawn
def identify_piece(board,column, row, next_column, next_row):

    if board[row][column][-1] == '♙':
        pawn.pawn_movements(board,column, row, next_column, next_row) # call pawn 

    elif board[row][column][-1] == '♖':
        # call tower
        pass
    elif board[row][column][-1] == '♖':
        # llamar horse
        pass
    elif board[row][column][-1] == '♖':
        # call bichop
        pass
    elif board[row][column][-1] == '♖':
        # call lady
        pass
    elif board[row][column][-1] == '♖':
        # call king
        pass

    