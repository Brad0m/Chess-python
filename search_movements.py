# from board import board
from movements_pieces import *
# from show_board import show

def searchMovements(board):
    ''' Crear un diccionario movements y recorrer el tablero pasado cada vez que una posicion no este vacia 
        almcanea esa pocicion el el diccionario movements como una clave y verifica que pieza es para llamar
        a la funcion que busca los movimientos de respectiva pieza una vez buscados esos mivimietos de esa pieza
        se almacena como valor en el diccionario bajo la clave que le corresponda, una vez acaba de recorrer todo el 
        tablero esta funcion retornara dicho diccionario de movimientos. '''

    movements = {}
    for column_index, column in enumerate(board):
        for row_index, row in enumerate(board[column]):
            if row != "   ":
                movements[column, row_index] = [[],[]]

            if board[column][row_index] == '♙ 1':
                pawn1(board, column, row_index, movements[column, row_index])

            if board[column][row_index] == '♙ 2':
                pawn2(board, column, row_index, movements[column, row_index])

            if board[column][row_index] == '♗ 1' or board[column][row_index] == '♕ 1':
                diagonales(board, column, row_index, "2" ,movements[column, row_index])            


            if board[column][row_index] == '♗ 2' or board[column][row_index] == '♕ 2':
                diagonales(board, column, row_index, "1" ,movements[column, row_index])

            if board[column][row_index] == '♖ 1' or board[column][row_index] == '♕ 1':
                tower(board, column, row_index, "2" , movements[column, row_index])

            if board[column][row_index] == '♖ 2' or board[column][row_index] == '♕ 2':
                tower(board, column, row_index, "1" , movements[column, row_index])    

            if board[column][row_index] == '♘ 1':
                horse(board, column, row_index, "2", movements[column, row_index])

            if board[column][row_index] == '♘ 2':
                horse(board, column, row_index, "1", movements[column, row_index])   

            if board[column][row_index] == '♔ 1':
                king(board, column, row_index, "2", movements[column, row_index])   
                
            if board[column][row_index] == '♔ 2':
                king(board, column, row_index, "1", movements[column, row_index])                                  

    
    # print(movements)
    return movements

# board = board() 
# show(board)
# searchMovements(board)