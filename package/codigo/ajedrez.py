import numpy as np

class Ficha():     #Por defecto se define la posicion aleatoria, pero la puede establecer el usuario
   
    def __init__(self, nombre):
        self.nombre = nombre
 
    def __str__(self):
        return f"{self.nombre}"
    
    def get_position(self):
        return (self.x,self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y

class Torre(Ficha):
    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Alfil(Ficha):
    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        super().__init__(nombre)
        self.x = x
        self.y = y

class Reina(Ficha):
    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Rey(Ficha):
    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Peon(Ficha):
    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Caballo(Ficha):
    def __init__(self, nombre, x = np.random.randint(0,8) , y = np.random.randint(0,8)):
        super().__init__(nombre)
        self.x = x
        self.y = y
        
class Tablero():
    __filas = 8
    __columnas = 8
    
    def __init__(self):
        self.tab = np.zeros((self.__filas,self.__columnas),dtype=int) 
        
    def __str__(self):
        return f"{self.tab}\n"
    
    def __mov_cruz__(self, ficha):
        self.tab[ficha.x,:] = 1
        self.tab[:,ficha.y] = 1
        
    def __mov_diagonal__(self, ficha):
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
                self.tab[0 if(ficha.x-1 < 0) else (ficha.x-1) : ficha.x+2 : 2 , 0 if(ficha.y-2 < 0) else (ficha.y-2) : ficha.y+3 : 4] = 1
                self.tab[0 if(ficha.x-2 < 0) else (ficha.x-2) : ficha.x+3 : 4 , 0 if(ficha.y-1 < 0) else (ficha.y-1) : ficha.y+2 : 2] = 1
        
            self.tab[ficha.x, ficha.y] = 8
        except IndexError as indexerror:
            print("Error: (", indexerror, "), El tablero es [8x8], esta ingresando un indice incorrecto.")
        except ValueError:
            print("Esta ingresando un valor incorrecto.")
        except Exception as e:                              #Controlar una excepcion no definida
            print("Ocurrio el siguiente error:", type(e).__name__)