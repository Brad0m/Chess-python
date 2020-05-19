from search_movements import searchMovements
from playerVsBoot import PlayerVsBoot
from show_board import show
import os

class PlayerVsPlayer(PlayerVsBoot):
    
    def __init__(self):
        super().__init__()
        self.user2 = input("📍 JUGADOR2: ")
        self.container_player1 = []
        self.container_player2 = []

    def player1(self, number ="1"):
        
        print("\n")
        show(self.board)
        print("\n")

        if number == "1": print(f"📍 TURNO: {self.user1}"); print(f"⭐️ TROFEOS: {self.container_player1}", "\n")
        elif number == "2": print(f"📍 TURNO: {self.user2}"); print(f"⭐️ TROFEOS: {self.container_player2}", "\n")

        self.piece = self.menu.select("📍 PIEZA: ")
        self.movement = self.menu.select("📍 MOVIMIENTO: ")
        self.check_select(number)

    def player2(self):
        self.player1("2")
    
    def check_select(self, number):

        container = None
        if number == "1": container = self.container_player1
        elif number == "2": container = self.container_player2

        if self.menu.check_select(self.board, self.piece, self.movement, searchMovements(self.board), number) == True:
            self.move(container, number)
        else: 
            if number == "1": self.player1()
            elif number == "2": self.player2()
                
 
    def move(self, container, number):
        ''' Mover las piezas en el tablero '''

        os.system("cls")
        # Verificar si un peon a llegado el otro extremo y convertirlo en dama
        if self.movement[1] == 0 or self. movement[1] == 7:
            if self.board[self.piece[0]][self.piece[1]] == f'♙ {number}':
                self.board[self.piece[0]][self.piece[1]] = f'♕ {number}'
            
        super().move(container)

        # Verificar si jugador1 o jugador2 se a comido al rey y llamar a la funcion winner, si no es asi llamar al siguiente jugador
        if '♔ 1' in self.container_player2:
            self.winner(self.user2, self.movement)
        elif '♔ 2' in self.container_player1:
            self.winner(self.user1, self.movement)
        else:
            if number == "1": self.player2()
            elif number == "2": self.player1()

# game = PlayerVsPlayer()
# game.player1()
   