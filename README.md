Proyecto Juego hundir la FLOTA
Proyecto realizado por:
-	Julia María Martínez Tapia
-	Marta Miñana Lorente
Recursos
El proyecto se ha desarrollado con Python usando el IDE Pycharm.
Se han importado las siguientes librerías: Numpy, Time.
Además, se han utilizado los siguientes notebooks: 
Flujos_A, Ejercicio modulos – BiciMAD, 1_Numpy, 2_Numpy, Funciones_A
Metodología del juego
Hay dos jugadores, el ordenador y el usuario. 
Cada jugador dispone de dos tableros de juego, un tablero con los barcos posicionados (en adelante, “tablero barcos”) y otro (en adelante, “tablero impactos”) que recoge los disparos que le lanza al contrincante.
En cada “tablero barcos” se posicionan de forma aleatoria los siguientes barcos:
•	4 barcos de 1 posición de eslora
•	3 barcos de 2 posiciones de eslora
•	2 barcos de 3 posiciones de eslora
•	1 barco de 4 posiciones de eslora
La operativa del juego es la siguiente:
Comienza jugando el usuario. Se le pregunta que coordenadas quiere disparar. En caso de que impacte en agua (“-”), será el turno del ordenador. Si, por el contrario, impacta en un barco (“0”) vuelve a jugar el usuario, que indicará nuevamente las coordenadas a las que quiera disparar. 
El funcionamiento es el mismo cuando juega el ordenador en vez del usuario.
De esta manera se va disparando a los barcos y con cada disparo acertado, se van restando las esloras existentes para cada jugador. 
El jugador que impacte a todos los barcos del contrincante (es decir, que reduzca sus esloras a cero) ganará la partida. 
¿Dudas, sugerencias?
Para cualquier duda, sugerencia o mejora, siéntete libre de abrir una issue en el repositorio.


