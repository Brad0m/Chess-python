def board():

    filas = {key:[] for key in range(8)}
    dic = ["A","B","C","D","E","F","G","H"]
    columnas = {key:[] for key in dic}

    for fila in filas:
        if fila == 0: filas[0] = ['♖ 1','♘ 1','♗ 1','♕ 1','♔ 1','♗ 1','♘ 1','♖ 1']
        elif fila == 7: filas[7] = ['♖ 2','♘ 2','♗ 2','♕ 2','♔ 2','♗ 2','♘ 2','♖ 2']  
        elif fila == 1: filas[1] = ['♙ 1'] *8 
        elif fila == 6: filas[6] = ['♙ 2'] *8   
        else: filas[fila] = ["   "] *8 

    for casilla,lista in enumerate(columnas.values()):

        for fila in filas:
            lista.append(filas[fila][casilla])
        # print(lista)

    return columnas
