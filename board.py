import os
class Board:

    def __init__(self):

        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.board = [[]] * 8
        self.create_board()


    def create_board(self):

        for element in range(8):
            if element == 0: self.board[element] = ['B♖','B♘','B♗','B♕','B♔','B♗','B♘','B♖']
            elif element == 7 : self.board[element] = ['W♖','W♘','W♗','W♕','W♔','W♗','W♘','W♖']
            elif element == 1: self.board[element] = ['B♙','B♙','B♙','B♙','B♙','B♙','B♙','B♙']
            elif element == 6 : self.board[element] = ['W♙','W♙','W♙','W♙','W♙','W♙','W♙','W♙']
            else: self.board[element] = ["  "] * 8


    def show_board(self, board):

        num_row = 8
        for row in board:
            print(" " * 30 ,end= "{}".format(num_row))
            for column in row:
                print("   |   ", column, end="  ")

            print("   | \n")
            num_row -= 1
            
        print(end=" " * 29)
        for letter in self.letters:
            print(" " * 10, letter, end="")

# tablero = Board()
# tablero.show_board(tablero.create_board())
# tablero.create_board()                                                                                                                

def entrada_datos():
    letras =["A", "B", "C", "D", "E", "F", "G", "H"]
    tablero = Board()
    mesa = tablero.board
    tablero.show_board(mesa)
    print("\n")
    columna = int(input(" Columna actual: "))
    fila = int(input(" Fila actual: "))    
    sigC = int(input(" Columna siguiente: "))
    sigf = int(input(" Fila siguiente: "))
    # os.system ("cls")
    mover(columna, fila, sigC, sigf)


def mover(columna, fila, sigC, sigf):

    tablero = Board()
    mesa = tablero.board.copy()

    opcion = True
    while opcion == True:
        if mesa[fila-1][columna-1][-1] == '♙':        
            if fila == 2:
                if sigf != fila:           
                    if sigf > 1 and sigf <= 4:
                        if sigC == columna:
                            mesa[sigf-1][sigC-1] = mesa[fila-1][columna-1]
                            mesa[fila-1][columna-1] = "  "
                            os.system ("cls")
                            tablero.show_board(mesa)
                            opcion = False
                        else:
                            print("El peon no se mueve en diagonal, vuelva a intentarlo")
                            print("################################################################")
                            sigC = int(input(" Columna siguiente: "))
                            sigf = int(input(" Fila siguiente: "))
                            print("################################################################")
                    else:
                        print("La fila no es valida, vuelva a intentarlo")
                        print("################################################################")
                        sigC = int(input(" Columna siguiente: "))
                        sigf = int(input(" Fila siguiente: "))
                        print("################################################################") 
 
                else: 
                    print("Usted introdujo la misma fila, vuelva a intentarlo")
                    print("################################################################")
                    sigC = int(input(" Columna siguiente: "))
                    sigf = int(input(" Fila siguiente: "))
                    print("################################################################") 


entrada_datos()