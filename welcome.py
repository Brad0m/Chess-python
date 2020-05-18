from playerVsBoot import PlayerVsBoot
from playerVsPlayer import PlayerVsPlayer
import os
import time

data1 = '''Computadora contra humano: El primer programa creado para jugar al ajedrez lo realizó Alan Turing en 1951. 
Sin embargo, ninguna computadora estaba preparada para usarlo, así que él mismo hacía los cálculos y jugaba de acuerdo a ellos '''
data2 = ''' La reina: En un comienzo la reina no era tan poderosa, solo podía mover un espacio en diagonal, hasta que más tarde adquirió poder. 
Fue pensada en un principio como una consejera o primer ministra, pero en 1400 se cambió para que fuera la más fuerte '''

def welcome_message():
    print()
    print("MINI PROJECTO: AJEDREZ")
    print('DESARROLLADO POR: BRAYAN DOMINGUEZ')
    print("___________________________________\n")

def instructions():
    print()
    print("PARA JUGAR SE LE PEDIRA FICHA Y MOVIMIENTO", "\n", "PARA SELECCIONAR UNA FICHA INGRESE COLUMNA Y FILA EJ: B6 Y PRECIONE ENTER",\
        "\n", "LO MISMO PARA HACER UN MOVIMIENTO.")
    print()
    print("SELECCIONE MODALIDAD DE JUEGO", "\n", "1- JUGADOR VS MAQUINA | 2- JUGADOR VS JUGADOR")

    opcion = input("INGRESE OPCION [1/2]: ")
    while opcion not in ["1", "2"]:
        opcion = input("INGRESE OPCION [1/2]: ")
        
    os.system("cls")
    print("\n")
    print("ARMANDO LA MESA.......")
    print("_"*20, "\n")
    print("PD: PONTE COMODO CRACK 😎 ESTO SERA UNA GRAN BATALLA ")
    print("_"*20, "\n")
    print("MIENTRAS ESPERAS, AQUI TE VA UN DATO.", "\n")

    if opcion == "1": print(data1, "\n")
    elif opcion == "2": print(data2, "\n")

    time.sleep(30)
    os.system("cls")

    if opcion == "1": PlayerVsBoot().player()
    elif opcion == "2": PlayerVsPlayer().player1()

