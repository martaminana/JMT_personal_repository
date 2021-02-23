
import numpy as np

#creamos los cuatro tableros.

tab_b_us = np.full((10,10), " ")

tab_i_us= np.full((10,10), " ")

tab_b_or = np.full((10,10), " ")

tab_i_or = np.full((10,10), " ")

#creamos una variable que nos almacene el jugador
jugador = "usuario"

#creamos una variable que nos almacene una lista de las esloras que tiene cada uno de los barcos. Esta variable la utilizaremos
#en la función pintar barcos.
esloras = [4,3,3,2,2,2,1,1,1,1]

#creamos dos variables que nos almacenen la suma de las esloras para usuario y ordenador, respectivamente. Con ellas
#controlamos la salida del bucle while en el main.
suma_us = sum(esloras)
suma_or = sum(esloras)

