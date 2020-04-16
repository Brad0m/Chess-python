def create_board():

    board = [[]] * 8

    for element in range(8):
         if element == 0 or element == 7 : board[element] = ['♖','♘','♗','♕','♔','♗','♘','♖']
         elif element == 1 or element == 6 : board[element] = [i for i in '♙' *8]
         else: board[element] = [i for i in ' ' *8]

    board[3][0] = board[0][1]

    for i in board:
        print(i)

create_board()