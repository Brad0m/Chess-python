def show_board(board):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"] # letters to represent the columns
    num_row = 8 # Numbers to represent rows
    for row in board:
        print(num_row, end=" ") # print numbers after 30 spaces
        for column in row:
            print("  |  ", column, end="  ") # put space and | -divisor after printing a part

        print("  |", "\n")  # put a | -line at the end of each row
        num_row -= 1
        
    ''' put 20 spaces under the board and put a letter 10 spaces after each one, this represents the columns. '''

    for letter in letters:
        print(" " * 8, letter, end="")

    print("\n")


# from board import Board
# board = Board().create_board()
# show_board(board)