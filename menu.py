import os
from display import show_board
class Menu:

    def __init__(self, board, list, message):
        self.message = message
        self.column_row_index = None
        self.board = board
        self.index = 0
        self.column_row = list
        self.selec_column_row()

    def menu(self):

        print("\n")
        print(" " * 78,self.column_row[self.index])
        print(" " * 51,end="")
        print(self.message)
        print(" " * 77,end="")
        opcion = input(": ") 
        return opcion.upper()

    def  selec_column_row(self):

        iterate = True
        while iterate == True:
            opcion = self.menu()
            if opcion == "A" or opcion == "S":
                if self.index == 0:
                    self.index = 0
                else: self.index -= 1
                    
            if opcion == "X":
                self.column_row_index = self.index
                iterate = False

            if opcion == "D" or opcion == "W":
                if self.index == len(self.column_row)-1:
                    self.index = len(self.column_row)-1

                else: self.index += 1

            os.system ("cls")
            show_board(self.board)
                
    def return_column_row(self):
        return self.column_row_index
