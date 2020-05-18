from playerVsBoot import PlayerVsBoot
from playerVsPlayer import PlayerVsPlayer

def welcome_message():
    print()
    print("MINI PROJECTO: AJEDREZ")
    print('DESARROLLADO POR: BRAYAN DOMINGUEZ')
    print("___________________________________\n")

def instructions():
    print()
    print("PARA JUGAR SE LEPEDIRA FICHA Y MOVIMIENTO", "\n", "PARA SELECCIONAR UNA FICHA INGRESE COLUMNA Y FILA EJ: B6 Y PRECIONE ENTER",\
        "\n", "LO MISMO PARA HACER UN MOVIMIENTO.")
    print()
    print("SELECCIONE MODALIDAD DE JUEGO", "\n", "1- JUGADOR VS MAQUINA | 2- JUGADOR VS JUGADOR")

    opcion = input("INGRESE OPCION [1/2]: ")
    while opcion not in ["1", "2"]:
        opcion
    if opcion == "1": PlayerVsBoot().player()
    elif opcion == "2": PlayerVsPlayer().player1()