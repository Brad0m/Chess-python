def pawn_movements(board, column, row, next_column, next_row):

    opcion = True
    while opcion == True:
        if board[row][column][-1] == '♙':        
            if row == 1:
                if next_row != row:           
                    if next_row > 1 and next_row <= 4:
                        if next_column == column:
                            board[next_row][next_column] = board[row][column]
                            board[row][column] = "  "
                            opcion = False
                        else:
                            print("El peon no se mueve en diagonal, vuelva a intentarlo")
                            print("################################################################")
                            next_column = int(input(" Columna siguiente: "))
                            next_row = int(input(" Fila siguiente: "))
                            print("################################################################")
                    else:
                        print("La fila no es valida, vuelva a intentarlo")
                        print("################################################################")
                        next_column = int(input(" Columna siguiente: "))
                        next_row = int(input(" Fila siguiente: "))
                        print("################################################################") 
 
                else: 
                    print("Usted introdujo la misma fila, vuelva a intentarlo")
                    print("################################################################")
                    next_column = int(input(" Columna siguiente: "))
                    next_row = int(input(" Fila siguiente: "))
                    print("################################################################") 
