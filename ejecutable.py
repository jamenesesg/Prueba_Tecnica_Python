from package.codigo.ajedrez import * 
from package.codigo.polinomio import *

while(True):
    try:
        op = float(input("""
            **********************************
            Ejercicio a Evaluar : 

                1. Tablero de Ajedrez
                2. Clase Polinomio

            Escoja una opción: """))        
        if (op != 1 and op != 2):
            print("""
            \nOpción incorrecta!!\n""")
        elif (op == 2):
            op2 = float(input("""
                1. Crear Polinomio
                2. Evaluar un Polinomio
                3. Sumar dos Polinomios
                4. Restar dos Polinomios
                5. Multiplicar dos Polinomios o Multiplicar un Polinomio por un escalar
                6. Imprimir Polinomio
                7. Salir

                Eliga una opción : """))

            if(op2 == 1)


            break
    except Exception:         #Controla una excepcion no definida
        print("""
            \nOpción incorrecta!!\n""")

input()



# ficha_1 = Torre("Torre")
# print(ficha_1.get_position())

# tablero_ajedrez1 = Tablero()
# tablero_ajedrez1.ubicar_ficha(ficha_1)

# print(ficha_1)
# print(tablero_ajedrez1)
# #-----------------
# ficha_2 = Alfil("Alfil")
# print(ficha_2.get_position())

# tablero_ajedrez2 = Tablero()
# tablero_ajedrez2.ubicar_ficha(ficha_2)

# print(ficha_2)
# print(tablero_ajedrez2)
# #-----------------
# ficha_3 = Reina("Reina",2,4)
# print(ficha_3.get_position())

# tablero_ajedrez3 = Tablero()
# tablero_ajedrez3.ubicar_ficha(ficha_3)

# print(ficha_3)
# print(tablero_ajedrez3)
# #-----------------
# ficha_4 = Rey("Rey",4,4)
# print(ficha_4.get_position())

# tablero_ajedrez4 = Tablero()
# tablero_ajedrez4.ubicar_ficha(ficha_4)

# print(ficha_4)
# print(tablero_ajedrez4)
# #-----------------
# ficha_5 = Peon("Peon")
# print(ficha_5.get_position())

# tablero_ajedrez5 = Tablero()
# tablero_ajedrez5.ubicar_ficha(ficha_5)

# print(ficha_5)
# print(tablero_ajedrez5)
# #-----------------
# ficha_6 = Caballo("Caballo")
# print(ficha_6.get_position())

# tablero_ajedrez6 = Tablero()
# tablero_ajedrez6.ubicar_ficha(ficha_6)

# print(ficha_6)
# print(tablero_ajedrez6)
# #-----------------
# ficha_6 = Caballo("Caballo",0,8)
# print(ficha_6.get_position())

# tablero_ajedrez6 = Tablero()
# tablero_ajedrez6.ubicar_ficha(ficha_6)

# print(ficha_6)
# print(tablero_ajedrez6)




            """)

            """
            1. Puede crear un Polinomio de una de las tres formas, enviando como argumento:

                p = Polinomio(polinomio)      # objeto Polinomio
                p = Polinomio([1,2,3 ...])    # secuencia
                p = Polinomio(1, 2, 3 ...)    # escalar

            1. Evaluar un Polinomio:

                se hace el llamado al método (Polinomio.__evaluar__())
                y se envia como argumento el polinomio a evaluar y la variable:

                    Polinomio.__evaluar__(Polinomio(5,3,0,1,3),5)      
                    Polinomio.__evaluar__(p,3)                         # (p) objeto Polinomio

            2. Sumar dos Polinomios:

                    p1.__add__(p2)

            3. Restar dos Polinomios:

                    p1.__sub__(p2)

            4. Multiplicar dos Polinomios o Multiplicar un Polinomio por un escalar:

                    p1.__mul__(p2)
                    p1.__mul__(5)


           """)