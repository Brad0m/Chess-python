from board import board
from show_board import show
from menu import Menu
from search_movements import searchMovements
import os
import time

class PlayerVsBoot:

    def __init__(self):
        self.user1 = input("JUGADOR1: ")
        self.user2 = "BO0T"
        self.board = board()
        self.piece = None
        self.movement = None
        self.container_player = []
        self.container_boot = []
        self.menu = Menu()

    def player(self):

        print("\n")
        show(self.board)
        print("\n")
        print(f"TURNO: {self.user1}", "\n", f"TROFEOS: {self.container_player}", "\n")
        self.piece = self.menu.select("PIEZA: ")
        print(self.piece)
        self.movement = self.menu.select("MOVIMIENT0: ")
        print(self.movement)
        self.check_move()

    def check_move(self):
        ''' Verificar si la pieza seleccionada no es de su mismo equipo
            y que en la casilla a moverse no halla una ficha de su mismo equipo. '''

        movements = searchMovements(self.board) 

        # Verificar si los datos ingresados por el usuario son validos.
        if self.menu.check_select(self.board, self.piece, self.movement, movements, "1") == True:
            self.move(self.container_player)
        else: self.player()


    def move(self, container):
        ''' Mover las piezas en el tablero '''

        # Verificar si el jugador se va a comer alguna pieza para guardarla
        if self.board[self.movement[0]][self.movement[1]] != "   ":
            container.append(self.board[self.movement[0]][self.movement[1]])

        # Mover piezas en el tablero
        self.board[self.movement[0]][self.movement[1]] = self.board[self.piece[0]][self.piece[1]]
        self.board[self.piece[0]][self.piece[1]] = "   "
        
        print("\n")
        show(self.board)
        print("\n")

        # Verificar si user2 el boot para llamar al boot, esto lo hago para cuando herede en PlayerVsPlayer no me llame al boot
        if self.user2 == "BO0T":
            if '♔ 2' in self.container_player:
                self.winner(self.user1, self.movement[0][1])
            else: self.boot()        


    def boot(self):
        
        os.system("cls")
        print("EL BOOT ESTA PENSANDO......")
        time.sleep(2)
        os.system("cls")

        movements = searchMovements(self.board) 
        movements1 = [] # Movimientos de ataques
        movements2 = [] # Movimientos libres
        
        # Buscar todas las piezas numero 2 y los movimientos donde pueden
        # comer almacenarlos en movements1 y los movimientos libres almacenarlos en movements2.
        for piece in movements:
            if self.board[piece[0]][piece[1]][-1] == "2":
                if len(movements[piece][0]) > 0:
                    movements1.append([piece, movements[piece][0][0]])
                if len(movements[piece][1]) > 0:
                    movements2.append([piece, movements[piece][1][0]])
        
        # Verificar si el boot se va a comer alguna pieza para almacenarla en self.container_boot
        if len(movements2) > 0:
            if self.board[movements2[0][1][0]][movements2[0][1][1]] != "   ":
                self.container_boot.append(self.board[movements2[0][1][0]][movements2[0][1][1]])

            # Mover las piezas en el tablero
            self.board[movements2[0][1][0]][movements2[0][1][1]] = self.board[movements2[0][0][0]][movements2[0][0][1]]
            self.board[movements2[0][0][0]][movements2[0][0][1]] = "   "
            print("\n")
            print(F"EL BOOT A JUGADO: {movements2[0][0]} -> {movements2[0][1]}", "\n", f"TROFEOS BOOT: {self.container_boot}")

            # Verificar si el boot se a comido al rey para terminar el juego llamando al metodo winner
            if '♔ 1' in self.container_boot:
                self.winner(self.user2, movements2[0][1])
            else: self.player()
        
        # Si en movements2 de ataque disponibles buscamos en movements1 y hacemos todo lo anterior
        elif len(movements1) > 0:
            if self.board[movements1[0][1][0]][movements1[0][1][1]] != "   ":
                self.container_boot.append(self.board[movements1[0][1][0]][movements1[0][1][1]])

            self.board[movements1[0][1][0]][movements1[0][1][1]] = self.board[movements1[0][0][0]][movements1[0][0][1]]
            self.board[movements1[0][0][0]][movements1[0][0][1]] = "   "
            print("\n")
            print(F"EL BOOT A JUGADO: {movements1[0][0]} -> {movements1[0][1]}", "\n", f"TROFEOS BOOT: {self.container_boot}")

            if '♔ 1' in self.container_boot:
                self.winner(self.user2, movements1[0][1])
            else: self.player()


    def winner(self, winner, movement):

        show(self.boars)
        print("\n")
        print((F"{winner} A GANADO, MOVIMIENTO GANADOR: {movement}"))


# PlayerVsBoot().player()
# PlayerVsBoot().boot()