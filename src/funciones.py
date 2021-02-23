
import numpy as np
import random
from const_variables import *


#La función "disparar" efectua la actualizacion de los tableros de usuario u ordenador, pintando una "X" o un "-" en la posición resultante de las coordenadas
#en el tablero de impactos que se indique al llamar a la función en el main. La función devuelve dicho tablero actualizado.

def disparar (x, y, tab_b,tab_i):

    if 'O' in tab_b[(x, y)]:

        tab_i[(x, y)] = "X"

    else:

        tab_i[(x, y)] = "-"

    return tab_i

#La función "pintar barcos" coloca los barcos en los tableros de usuario y ordenador de forma aleatoria. La función devuelve los tableros con los barcos
#ya colocados.
def pintar_barcos(tab_b, esloras, jugador):

        for barco in esloras:

            while True:

                if jugador == "usuario":

                    orient = random.choice(['N', 'S', 'E', 'O'])

                    current_pos = np.random.randint(10, size=2)

                    fila = current_pos[0]

                    col = current_pos[1]

                elif jugador == "ordenador":

                    orient = random.choice(['N', 'S', 'E', 'O'])

                    current_pos = np.random.randint(10, size=2)

                    fila = current_pos[0]

                    col = current_pos[1]

                coors_posiN = tab_b[fila:fila - barco:-1, col]

                coors_posiE = tab_b[fila, col: col + barco]

                coors_posiS = tab_b[fila:fila + barco, col]

                coors_posiO = tab_b[fila, col:col - barco:-1]

                if (orient == 'N') and (len(coors_posiN) == barco) and ('O' not in coors_posiN):
                    tab_b[fila:fila - barco:-1, col] = 'O'
                    break

                elif (orient == 'E') and (len(coors_posiE) == barco) and ('O' not in coors_posiE):
                    tab_b[fila, col: col + barco] = 'O'
                    break

                elif (orient == 'S') and (len(coors_posiS) == barco) and ('O' not in coors_posiS):
                    tab_b[fila:fila + barco, col] = 'O'
                    break

                elif (orient == 'O') and (len(coors_posiO) == barco) and ('O' not in coors_posiO):
                    tab_b[fila, col:col - barco:-1] = 'O'
                    break

        return tab_b






