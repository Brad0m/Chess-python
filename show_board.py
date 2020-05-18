def show(board):
    
    letters_columns = ["A","B","C","D","E","F","G","H"]
    for index in reversed(range(8)):
        print(index, " |", end="")
        for column in board :
            print(board[column][index], "|", end="  ")

        print()
        print(end="   ")
        print("-" *55)

    for letter in letters_columns:
        print("    ", letter, end=" ")

# from board import board            
# show(board())
