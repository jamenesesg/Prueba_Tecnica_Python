from package.codigo.ajedrez import * 
from package.codigo.polinomio import Polinomio as p


# tablero de ajedrez

tablero_ajedrez = Tablero()

ficha_1 = Torre()
print("Ubicación ficha_1 : ", ficha_1.get_position())
tablero_ajedrez.ubicar_ficha(ficha_1)
#-----------------
ficha_2 = Alfil(4, 2)
print("Ubicación ficha_2 : ", ficha_2.get_position())
tablero_ajedrez.ubicar_ficha(ficha_2)
#-----------------
tablero_ajedrez2 = Tablero()

ficha_3 = Reina()
print("Ubicación ficha_3 : ", ficha_3.get_position())
tablero_ajedrez2.ubicar_ficha(ficha_3)
#-----------------
tablero_ajedrez3 = Tablero()

ficha_4 = Caballo()
print("Ubicación ficha_4 : ", ficha_4.get_position())
tablero_ajedrez3.ubicar_ficha(ficha_4)
#-----------------
tablero_ajedrez4 = Tablero()

ficha_5 = Caballo(8,2)
print("Ubicación ficha_5 : ", ficha_5.get_position())
tablero_ajedrez4.ubicar_ficha(ficha_5)
print()


#Polinomios

p1 = p(5,2,0,6,7)    
p2 = p(3,2,1)

print("p1 = ", p1)
print("p2 = ", p2)

print(p1.__add__(p2))
print(p1.__sub__(p2)) 
print(p1.__mul__(p2))     # Multiplicación de 2 polinomios
print(p1.__mul__(5))      # Multiplicación de un polinomio por un escalar

print(p.__evaluar__(p2, 5))

input()













