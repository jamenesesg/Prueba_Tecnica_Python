from package.codigo.ajedrez import * 
from package.codigo.polinomio import *


# tablero de ajedrez

tablero_ajedrez = Tablero()

ficha_1 = Torre("Torre")
print("Ubicación ficha_1 : ", ficha_1.get_position())
tablero_ajedrez.ubicar_ficha(ficha_1)

print(ficha_1)
print(tablero_ajedrez)
#-----------------
ficha_2 = Alfil("Alfil", 4, 2)
print("Ubicación ficha_2 : ", ficha_2.get_position())
tablero_ajedrez.ubicar_ficha(ficha_2)

print(ficha_2)
print(tablero_ajedrez)
#-----------------
tablero_ajedrez2 = Tablero()

ficha_3 = Reina("Reina")
print("Ubicación ficha_3 : ", ficha_3.get_position())
tablero_ajedrez2.ubicar_ficha(ficha_3)

print(ficha_3)
print(tablero_ajedrez2)
#-----------------
tablero_ajedrez3 = Tablero()

ficha_4 = Caballo("Caballo")
print("Ubicación ficha_4 : ", ficha_4.get_position())
tablero_ajedrez3.ubicar_ficha(ficha_4)

print(ficha_4)
print(tablero_ajedrez3)



# Polinomios

p1 = Polinomio(5,2,0,6,7)    
p2 = Polinomio(3,2,1)

print("p1 = ", p1)
print("p2 = ", p2)

print(p1.__add__(p2))
print(p1.__sub__(p2)) 
print(p1.__mul__(p2))     # Multiplicación de 2 polinomios
print(p1.__mul__(5))      # Multiplicación de un polinomio por un escalar

print(Polinomio.__evaluar__(p2, 5))

input()













