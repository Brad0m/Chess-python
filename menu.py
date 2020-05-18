# from display import show_board
# from board import board

class Menu:
    '''Esta clase pedira por consola al usuario la ubicacion del la pieza que desea seleccionar
       y la ubicacion del movimiento deceado, una vez echo esto esos datos pasaran al metodo
       check_select el cual verificara si la ficha seleccionada es del mismo equipo y que adonde
       se vaya a mover esa ficha este libre o no haya una ficha de su mismo equipo, de no cumplirse
       estas condiciones se volvera a llamar al metodo select y pedir los datos nuevamente hasta que
       cumplan estas condiciones.'''

    def select(self, message):

        while True:
            columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
            rows = str([i for i in range(8)])
            opcion = input(message).upper()

            if len(opcion) > 1 and len(opcion) < 3:
                if opcion[0].upper() in columns and opcion[1] in rows:
                    break
        return (opcion[0], int(opcion[1]))
    
    def check_select(self, board, piece, movement, movements, number):
        ''' Verificar si la pieza seleccionada no es de su mismo equipo
            y que en la casilla a moverse no halla una ficha de su mismo equipo. '''
            
        if piece in movements:
            if board[piece[0]][piece[1]][-1] == number:
                if movement in movements[piece][0] or movement in movements[piece][1]:
                    if board[movement[0]][movement[1]][-1] != number:
                        return True

# board = board()
# m = Menu(board,1)
# print(m.select())
