# Cre una funcion que reprecenta cada pieza, segun las reglas de ajedrez cada funcion
# tiene un algoritmo que busca en las posiciones segun se pueda mover esa pieza

def pawn1(board, column, row, movements):

	columns = ["A","B","C","D","E","F","G","H"]
	index_column = columns.index(column)

	if row +1 <= 7:
		if board[column][row +1] == "   ":
			movements[0].append((column, row +1))
			if row == 1:
				if board[column][row +2] == "   ":
					movements[0].append((column, row +2))			

		if index_column +1 <= 7:
			if board[columns[index_column +1]][row +1][-1] == "2":
				movements[1].append((columns[index_column +1], row +1))

		if index_column -1 >= 0:
			if board[columns[index_column -1]][row +1][-1] == "2":
				movements[1].append((columns[index_column -1], row +1))	
	# print(movements)


def pawn2(board, column, row, movements):

	columns = ["A","B","C","D","E","F","G","H"]
	index_column = columns.index(column)

	if row -1 >= 0:
		if board[column][row -1] == "   ":
			movements[0].append((column, row-1))
			if row == 6:
				if board[column][row -2] == "   ":
					movements[0].append((column, row -2))				


		if index_column +1 <= 7:
			if board[columns[index_column +1]][row -1][-1] == "1":
				movements[1].append((columns[index_column +1], row-1))

		if index_column -1 >= 0:
			if board[columns[index_column -1]][row -1][-1] == "1":
				movements[1].append((columns[index_column -1], row-1))			

	# print(movements)


def diagonales(board, column, row, enemy, movements):

		columns = ["A","B","C","D","E","F","G","H"]
		box = columns.index(column)
		row1 = row
		box1 = box

		while row1 < 7 and box1 < 7:
			row1 +=1
			box1 +=1

			if board[columns[box1]][row1] == "   ":
				movements[0].append((columns[box1], row1))

			else:
				if board[columns[box1]][row1][-1] == enemy:
					movements[1].append((columns[box1], row1))
					break

		row2 = row
		box2 = box

		while row2 > 0 and box2 > 0:
			row2 -=1
			box2 -=1

			if board[columns[box2]][row2] == "   ":
				movements[0].append((columns[box2], row2))
			else:
				if board[columns[box2]][row2][-1] == enemy:
					movements[1].append((columns[box2], row2))
					break
				else: break
		
		row3 = row
		box3 = box    

		while row3 < 7 and box3 > 0:
			row3 +=1
			box3 -=1

			if board[columns[box3]][row3] == "   ":
				movements[0].append((columns[box3], row3))
			else:
				if board[columns[box3]][row3][-1] == enemy:
					movements[1].append((columns[box3], row3))
					break
				else: break			

		row4 = row
		box4 = box    

		while row4 > 0 and box4 < 7:
			row4 -=1
			box4 +=1

			if board[columns[box4]][row4] == "   ":
				movements[0].append((columns[box4], row4))
			else:
				if board[columns[box4]][row4][-1] == enemy:
					movements[1].append((columns[box4], row4))
					break
				else: break	


def tower(board, column, row, enemy, movements):

	columns_letters = ["A","B","C","D","E","F","G","H"]
	rows_numbers = [i for i in range(8)]
	index_column = columns_letters.index(column)

	def horizontal():
		if board[column2][row] == "   ":
			movements[0].append((column2, row))
		else:
			if board[column2][row][-1] == enemy:
				movements[1].append((column2, row))
				return False
			else: return False	

	for column2 in columns_letters[index_column:]:
		if column2 > column:
			if horizontal() == False: break

	for column2 in reversed(columns_letters[:index_column]):
		if horizontal() == False: break

	def vertical():	
		if board[column][position] == "   ":
			movements[0].append((column,position))
		else:
			if board[column][position][-1] == enemy:
				movements[1].append((column,position))
				return False
			else: return False		

	for position in rows_numbers:
		if position > row:
			if vertical() == False: break

	for position in reversed(rows_numbers[:row]):
		if position < row:
			if vertical() == False: break

	# print(movements)


def horse(board, column, row, enemy, movements):
	
    columns = ["A","B","C","D","E","F","G","H"]
    index_column = columns.index(column)

    def search_row(operation, operation2):
        if board[columns[index_column +operation2]][row +operation] == "   ":
            movements[0].append((columns[index_column +operation2], row +operation))
        elif board[columns[index_column +operation2]][row +operation][-1] == enemy: 
            movements[1].append((columns[index_column +operation2], row +operation))  

    if index_column +2 <= 7:
        if row +1 <= 7:
            search_row(+1, +2)
        if row -1 >= 0:
            search_row(-1, +2)

    if index_column -2 >= 0:
        if row +1 <= 7:
            search_row(+1, -2)
        if row -1 >= 0:
            search_row(-1, -2)  

    if row +2 <= 7:
        if index_column +1 <= 7:
            search_row(+2, +1)
        if index_column -1 >= 0:
            search_row(+2, -1)  

    if row -2 >= 0:
        if index_column +1 <= 7:
            search_row(-2, +1)
        if index_column -1 >= 0:
            search_row(-2, -1)                                        


def king(board, column, row, enemy, movements):

    columns = ["A","B","C","D","E","F","G","H"]
    index_column = columns.index(column)

    def movements_king(operation, operation2):
        if board[columns[index_column +operation]][row +operation2] == "   ":
            movements[0].append((columns[index_column +operation], row +operation2))
        elif board[columns[index_column +operation]][row +operation2][0] == enemy:
            movements[1].append((columns[index_column +operation], row +operation2)) 

    for i in [+1, -1]:
        if index_column +i >= 0 and index_column +i <= 7:
            movements_king(i, 0)
        if row +i >= 0 and row +i <= 7:
            movements_king(0, i)            

    