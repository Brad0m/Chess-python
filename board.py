class Board:

    def __init__(self):
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.board = [[]] * 8
        self.create_board()


    def create_board(self):

        pawn = ['W♙'] * 8
        for element in range(8):
            if element == 0: self.board[element] = ['B♖','B♘','B♗','B♕','B♔','B♗','B♘','B♖']
            elif element == 7 : self.board[element] = ['W♖','W♘','W♗','W♕','W♔','W♗','W♘','W♖']
            elif element == 1: self.board[element] = pawn
            elif element == 6 : self.board[element] = pawn
            else: self.board[element] = ["  "] * 8

        

    def return_board(self):
        return self.board


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


tablero = Board()
# tablero.show_board(tablero.create_board())
# tablero.create_board()
print(tablero.board)