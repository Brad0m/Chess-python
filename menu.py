import os
from display import show_board
class Menu:

    def __init__(self, board, list, instruction, message):
        self.instruction = instruction
        self.message = message
        self.column_row_index = None
        self.board = board
        self.index = 0
        self.column_row = list
        # self.selec_column_row()

    def menu(self):

        show_board(self.board)
        print(" " * 70, self.message)
        print(" " * 78,self.column_row[self.index])
        print(" " * 51,end="") 
        print(self.instruction)
        print(" " * 77,end="")
        opcion = input(": ") 
        return opcion.upper()

    def  selec_column_row(self):

        while True:
            opcion = self.menu()
            if opcion == "A":
                if self.index == 0:
                    self.index = 0
                else: self.index -= 1
                    
            if opcion == "X":
                os.system("cls")
                return self.index

            if opcion == "D":
                if self.index == len(self.column_row)-1:
                    self.index = len(self.column_row)-1
                else: self.index += 1

            os.system ("cls")
            # show_board(self.board)
                