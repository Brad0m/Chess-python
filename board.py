class Board:

    def __init__(self):
        self.board = [[]] * 8 

    def create_board(self):

        for element in range(8):
            if element == 0: self.board[element] = ['B♖','B♘','B♗','B♕','B♔','B♗','B♘','B♖']
            elif element == 7 : self.board[element] = ['W♖','W♘','W♗','W♕','W♔','W♗','W♘','W♖']
            elif element == 1: self.board[element] = ['B♙','B♙','B♙','B♙','B♙','B♙','B♙','B♙']
            elif element == 6 : self.board[element] = ['W♙','W♙','W♙','W♙','W♙','W♙','W♙','W♙']
            else: self.board[element] = ["  "] * 8

        return self.board

