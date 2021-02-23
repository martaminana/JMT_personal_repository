
from funciones import *
from const_variables import *
import numpy as np
import time

print("¡¡¡¡¡¡Bienvenido a Hundir la flota!!!!!!\n EL juego consiste en hundir los barcos de tu adversario, en este caso el ordenador.\
Contamos con los siguientes barcos:\n 4 barcos de 1 posición de eslora \n 3 barcos de 2 posiciones de eslora \n 2 barcos de 3 posiciones de eslora\n\
1 barco de 4 posiciones de eslora \n\
Siempre empezarás disparando, si aciertas en tu tablero saldrá una “X”, si disparas al agua saldrá “-“.\n\
Si aciertas a un barco te tocará jugar otra vez. Sino, será el turno del ordenador.\n\
¡¡¡¡Mucha suerte y que gane el MEJOR!!!!\n")

#Esto es la llamada a la función que usamos para colocar los barcos en los tableros.
pintar_barcos(tab_b_us, esloras, jugador)
pintar_barcos(tab_b_or, esloras, jugador)

print("Empezamos, este es tu tablero:\n", tab_b_us)
print("Y este es el tablero del ordenador:\n", tab_i_or)

#En este bucle implementamos el juego. Con condicionales controlamos los turnos de juego entre el usuario y el ordenador.
while True:

    if jugador == "usuario":
        #Este while true controla la introducción de coordenadas por el usuario.
        while True:
            try:
                x_y = input("Facilita las coordenadas del disparo, separadas por una coma: ")
                time.sleep(2)
                coordenadas = x_y.split(",")
                coor_x = int(coordenadas[0])
                coor_y = int(coordenadas[1])
                if coor_x <= 9 and coor_y <= 9:
                    break
                else:
                    print("Error, debes ingresar valores numéricos dentro de la x y la y, entre 0 y 9")
            except:
                print("Error, debes ingresar valores numéricos dentro de la x y la y, entre 0 y 9")

        #Aauí llamamos a la función disparar.
        tab_i_or = disparar(coor_x, coor_y,tab_b_or,tab_i_or)

        #Con el siguiente condicional dirigimos las consecuencias del disparo efectuado por el usuario y, por tanto, sus efectos
        #sobre el conteo de barcos (en la variable suma_or) y el cambio o no de jugador.
        if tab_i_or[coor_x,coor_y] == "-":
            print("¡Ooops!, me temo que no has acertado:\n",tab_i_or)
            print("Es el turno del ordenador: ...a ver...")
            jugador = "ordenador"
            time.sleep(2)

        elif tab_i_or[coor_x,coor_y] == "X":
            print("¡Felicidades! ¡has impactado en uno de los barcos del ordenador!:\n", tab_i_or)
            suma_or = suma_or - 1
            #Con este condicional controlamos la salida del bucle while, de manera que cuando el valor de la variable que
            #almacena las esloras se iguale a cero, se aplica el break, el programa sale del bucle y se declara el ganador del juego.
            if suma_or == 0:
                print("¡Has ganado el juego!")
                break
            else:
                print("Vuelves a jugar")

    elif jugador == "ordenador":
        #Las coordenadas del disparo del ordenador son aleatorias y se obtienen aplicando un random.
        coor_x = np.random.randint(10)
        coor_y = np.random.randint(10)

        # Aauí llamamos a la función disparar e introducimos un lapso de tiempo para la ejecución y visualización del tablero.
        tab_i_us = disparar(coor_x, coor_y, tab_b_us, tab_i_us)
        time.sleep(2)
        print("el ordenador ha disparado a las coordenadas (" + str(coor_x) + "," + str(coor_y) + ")")
        time.sleep(2)

        # Con el siguiente condicional dirigimos las consecuencias del disparo efectuado por el ordenador y, por tanto, sus efectos
        # sobre el conteo de barcos (en la variable suma_us) y el cambio o no de jugador.
        if tab_i_us[coor_x,coor_y] == "-":
            tab_b_us[coor_x, coor_y] = "-"
            print("y...¡enhorabuena!¡no ha acertado!:\n", tab_b_us)
            print("¡Ahora es tu turno!")
            jugador = "usuario"

        elif tab_i_us[coor_x,coor_y] == "X":
            tab_b_us[coor_x, coor_y] = "X"
            print("¡Vaya!, ¡el ordenador ha impactado en uno de tus barcos!:\n",tab_b_us)
            ##Con este condicional controlamos la salida del bucle while, de manera que cuando el valor de la variable que
            #almacena las esloras se iguale a cero, se aplica el break, el programa sale del bucle y se declara el ganador del juego.
            suma_us = suma_us - 1
            if suma_us == 0:
                print("¡oops! ¡el ordenador te ha ganado la partida!")
                break