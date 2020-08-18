# full_project


Subdirectorios:

- Paquete "package": contiene un archivo ejecutable "ejecutable.py" y el subpaquete "codigo"				   
- SubPaquete "codigo": contiene los archivos "ajedrez.py" y "polinomio.py"


- Archivo "polinomio.py": (Clase implementada "Polinomio")

	
	<class Polinomio()>
		""" Clase (Plantilla) que permite simular un objeto algebraico """

		Metodos:
			
		__init__(self, *args)		
	        Constructor - Permite crear un Polinomio de una de las tres formas, enviando como argumento:
	        
		        p = Polinomio(polinomio)      # objeto Polinomio
		        p = Polinomio([1,2,3 ...])    # secuencia
		        p = Polinomio(1, 2, 3 ...)    # escalar

		__add__(self, val)
		    Permite sumar dos Polinomios, de la forma:
		    
		    	p1.__add__(p2)
		
		__evaluar__(self, x)
		    Permite evaluar un Polinomio:
		    
		    Se hace un llamado al método (Polinomio.__evaluar__(Polinomio, valor))
		    y se envia como argumento el polinomio a evaluar y el valor:
		    
			    Polinomio.__evaluar__(Polinomio(5,3,0,1,3),5)      
			    Polinomio.__evaluar__(p,3)                         # (p) objeto polinomio
		
		__mul__(self, val)
		    Permite Multiplicar dos Polinomios o Multiplicar un Polinomio por un escalar, de la forma:
		    
			    p1.__mul__(p2)                         			   # (p2) objeto polinomio
			    p1.__mul__(5)

		__sub__(self, val)
		    Permite restar dos Polinomios, de la forma:
		    
		    	p1.__sub__(p2)                         			   # (p2) objeto polinomio
		
		__str__(self)
		    Imprime el termino algebraico asociado al Polinomio enviado como argumento

		    	Polinomio(5,3,0,1,3)  ->   3X^4 + 1X^3 + 3X + 5
	

Ejemplo ejecución:

		c1 = Polinomio(1,2,3)    
		c2 = Polinomio(3,2,1)

		print(c1)
		print(c2)

		print(c1.__add__(c2))
		print(c1.__sub__(c2)) 
		print(c1.__mul__(c2))     # Multiplicación de 2 polinomios
		print(c1.__mul__(3))     # Multiplicación de un polinomio por un escalar

		print(Polinomio.__evaluar__(c1,5))



- Archivo "ajedrez.py": (Clases implementadas:
								Clase Tablero
 								Clase Ficha -> Subclases Torre, Alfil, Reina, Rey, Peon, Caballo)

 	<class Tablero>
		""" Clase (Plantilla) que representa un tablero [8x8] de ajedrez. """

		Metodos:
			
		__init__(self)
		    Constructor Clase "Tablero", inicializa con ceros cada posición en el tablero 
		    
		    	tablero_ajedrez = Tablero()
		
		ubicar_ficha(self, ficha)
		    Método que asigna todas las posibles ubicaciones de una ficha en el tablero, anteriormente se debe crear la ficha que se va a ubicar

		    	tablero_ajedrez.ubicar_ficha(ficha)

		__str__(self)
		    Retorna el tablero, para visualización
	
	<class Ficha>
		""" Clase (Plantilla) que representa cualquier ficha de ajedrez """

		Metodos:
			
		get_position(self)
		    Pérmite obtener la posición de un "objeto" Ficha en el tablero de ajedrez
		
		set_position(self, x, y)
		    Método que pérmite setear la posición de un "objeto" Ficha en el tablero de ajedrez	
	        
	<class Torre, Alfil, Reina, Rey, Peon, Caballo>
		""" Subclases que heredan de la clase "Ficha" """

		__init__(self, nombre, x=1, y=7)
		    Puede crear una ficha "Alfil" de las formas:
		    
		    ficha_alfil = Alfil("Alfil")          # posicion aleatoria de la ficha en el tablero
		    ficha_alfil = Alfil("Alfil", 2, 4)    # posicion de la ficha en la celda (2,4) en el tablero


Ejemplo ejecución:

		tablero_ajedrez = Tablero()

		ficha_1 = Torre("Torre")
		print("Ubicación ficha_1 : ", ficha_1.get_position())
		tablero_ajedrez.ubicar_ficha(ficha_1)

		print(ficha_1)
		print(tablero_ajedrez)
		#-----------------
		ficha_2 = Alfil("Alfil")
		print("Ubicación ficha_2 : ", ficha_2.get_position())
		tablero_ajedrez.ubicar_ficha(ficha_2)

		print(ficha_2)
		print(tablero_ajedrez)