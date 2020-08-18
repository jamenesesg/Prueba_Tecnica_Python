import numpy as np

class Ficha():
    """ Clase (Plantilla) que representa cualquier ficha de ajedrez """
   
    def __init__(self, nombre):
        """ Constructor clase "Ficha" """
        self.nombre = nombre
 
    def __str__(self):
        """ Imprime nombre de un objeto "Ficha" """
        return f"{self.nombre}"
    
    def get_position(self):
        """ Método que pérmite obtener la posición de un "objeto" Ficha en un tablero de ajedrez"""
        return (self.x,self.y)

    def set_position(self, x, y):
        """ Método que pérmite setear la posición de un "objeto" Ficha en un tablero de ajedrez"""
        self.x = x
        self.y = y


class Torre(Ficha):
    """ SubClase (Plantilla) que representa la ficha Torre. """

    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        """ Puede crear una ficha "Torre" de las formas:

                ficha_torre = Torre("Torre")          # posicion aleatoria de la ficha en el tablero
                ficha_torre = Torre("Torre", 2, 4)    # posicion de la ficha en la celda (2,4) en el tablero """
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Alfil(Ficha):
    """ SubClase (Plantilla) que representa la ficha Alfil. """    

    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        """ Puede crear una ficha "Alfil" de las formas:

                ficha_alfil = Alfil("Alfil")          # posicion aleatoria de la ficha en el tablero
                ficha_alfil = Alfil("Alfil", 2, 4)    # posicion de la ficha en la celda (2,4) en el tablero """        
        super().__init__(nombre)
        self.x = x
        self.y = y

class Reina(Ficha):
    """ SubClase (Plantilla) que representa la ficha Reina. """    

    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        """ Puede crear una ficha "Reina" de las formas:

                ficha_reina = Reina("Reina")          # posicion aleatoria de la ficha en el tablero
                ficha_reina = Reina("Reina", 2, 4)    # posicion de la ficha en la celda (2,4) en el tablero """        
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Rey(Ficha):
    """ SubClase (Plantilla) que representa la ficha Rey. """    

    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        """ Puede crear una ficha "Rey" de las formas:

                ficha_rey = Rey("Rey")          # posicion aleatoria de la ficha en el tablero
                ficha_rey = Rey("Rey", 2, 4)    # posicion de la ficha en la celda (2,4) en el tablero """        
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Peon(Ficha):
    """ SubClase (Plantilla) que representa la ficha Peon. """    

    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        """ Puede crear una ficha "Peon" de las formas:

                ficha_peon = Peon("Peon")          # posicion aleatoria de la ficha en el tablero
                ficha_peon = Peon("Peon", 2, 4)    # posicion de la ficha en la celda (2,4) en el tablero """        
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Caballo(Ficha):
    """ SubClase (Plantilla) que representa la ficha Caballo. """    

    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        """ Puede crear una ficha "Caballo" de las formas:

                ficha_caballo = Caballo("Caballo")          # posicion aleatoria de la ficha en el tablero
                ficha_caballo = Caballo("Caballo", 2, 4)    # posicion de la ficha en la celda (2,4) en el tablero """        
        super().__init__(nombre)
        self.x = x
        self.y = y


        
class Tablero():
    """ Clase (Plantilla) que representa un tablero [8x8] de ajedrez. """
    __filas = 8
    __columnas = 8
    
    def __init__(self):
        """ Constructor Clase "Tablero", inicializa con ceros cada posición en el tablero 

                tablero_ajedrez = Tablero() """
        self.tab = np.zeros((self.__filas,self.__columnas),dtype=int) 
        
    def __str__(self):
        """ Retorna el tablero, para visualización """
        return f"{self.tab}\n"
    
    def __mov_cruz__(self, ficha):
        """ Método que ubica el movimiento en cruz de una ficha en todo el tablero """
        self.tab[ficha.x,:] = 1
        self.tab[:,ficha.y] = 1
        
    def __mov_diagonal__(self, ficha):
        """ Método que ubica el movimiento en diagonal de una ficha en todo el tablero """
        self.tab[:] = np.eye(self.tab.shape[0], self.tab.shape[1], k = (ficha.y-ficha.x), dtype=int)    # diagonal superior
        self.tab[:][ficha.x, ficha.y] = 7
        
        matriz = self.tab[:]
        
        lista = list()
        for k,i in [(i, np.rot90(self.tab).diagonal(1*i-(self.tab.shape[0])+1)) for i in range((self.tab.shape[0]*2)-1)]:
            if(7 in i):
                i = i+1
            lista.append(list(i[::-1]))
        
        flat_list = []
        for sublist in lista:
            for item in sublist:
                flat_list.append(item)
        
        #primera parte diagonal superior
        con = 0
        for i in range(0,matriz.shape[0]):
            j = 0
            while(j<=i):
                matriz[i-j][j] = flat_list[con]
                j+=1
                con+=1

        #segunda parte diagonal inferior
        for i in range(0,matriz.shape[0]):
            j = 0
            while(j < matriz.shape[0]-i-1):
                matriz[matriz.shape[0]-j-1][j+i+1] = flat_list[con]
                j+=1
                con+=1
        
        self.tab = matriz
        
    def ubicar_ficha(self, ficha): 
        """ Método que asigna todas las posibles ubicaciones de una ficha en el tablero """
        try:
            if(type(ficha).__name__ == 'Torre'):
                self.__mov_cruz__(ficha)
                
            elif(type(ficha).__name__ == 'Alfil'):
                self.__mov_diagonal__(ficha)
                
            elif(type(ficha).__name__ == 'Reina'):
                self.__mov_diagonal__(ficha)
                self.__mov_cruz__(ficha)
                
            elif(type(ficha).__name__ == 'Rey'):
                self.tab[ficha.x-1:ficha.x+2,ficha.y-1:ficha.y+2] = 1
                
            elif(type(ficha).__name__ == 'Peon'):
                self.tab[ficha.x-1:ficha.x,ficha.y-1:ficha.y+2] = 1
                
            elif(type(ficha).__name__ == 'Caballo'):
                if(ficha.x == 0):
                    self.tab[ficha.x+1 if(ficha.x < 2) else (ficha.x-1) : ficha.x+2 : 2 , ficha.y+2 if(ficha.y < 2) else (ficha.y-2) : ficha.y+3 : 4] = 1
                else:    
                    self.tab[ficha.x-1 if(ficha.x < 2) else (ficha.x-1) : ficha.x+2 : 2 , ficha.y+2 if(ficha.y < 2) else (ficha.y-2) : ficha.y+3 : 4] = 1
                self.tab[ficha.x+2 if(ficha.x < 2) else (ficha.x-2) : ficha.x+3 : 4 , ficha.y+1 if(ficha.y < 1) else (ficha.y-1) : ficha.y+2 : 2] = 1
        
            self.tab[ficha.x, ficha.y] = 8
        except IndexError as indexerror:
            print("Error: (", indexerror, "), El tablero es [8x8], esta ingresando un indice incorrecto.")
        except ValueError:
            print("Esta ingresando un valor incorrecto.")
        except Exception as e:                              #Controlar una excepcion no definida
            print("Ocurrio el siguiente error:", type(e).__name__)