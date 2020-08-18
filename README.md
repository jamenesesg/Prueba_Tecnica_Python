# full_project


Subdirectorios:

- Paquete "package": contiene un archivo ejecutable "ejecutable.py" y el subpaquete "codigo"				   
- SubPaquete "codigo": contiene los archivos "ajedrez.py" y "polinomio.py"


- Archivo "polinomio.py": (Clase implementada "Polinomio")

	help(Polinomio)
	
	<class Polinomio()>
		""" Clase (Plantilla) que permite simular un objeto algebraico """
			
		__init__(self, *args)		
	        Permite crear un Polinomio de una de las tres formas, enviando como argumento:
	        
		        p = Polinomio(polinomio)      # objeto Polinomio
		        p = Polinomio([1,2,3 ...])    # secuencia
		        p = Polinomio(1, 2, 3 ...)    # escalar

		__add__(self, val)
		    Permite sumar dos Polinomios, de la forma:
		    
		    	p1.__add__(p2)
		
		__evaluar__(self, x)
		    Permite evaluar un Polinomio:
		    
		    Se hace un llamado al método (Polinomio.__evaluar__())
		    y se envia como argumento el polinomio a evaluar y la variable:
		    
			    Polinomio.__evaluar__(Polinomio(5,3,0,1,3),5)      
			    Polinomio.__evaluar__(p,3)                         # (p) objeto polinomio
		
		__mul__(self, val)
		    Permite Multiplicar dos Polinomios o Multiplicar un Polinomio por un escalar, de la forma:
		    
			    p1.__mul__(p2)
			    p1.__mul__(5)
		
		__str__(self)
		    Imprime el termino algebraico asociado al Polinomio enviado como argumento

		    	Polinomio(5,3,0,1,3)  ->   3X^4 + 1X^3 + 3X + 5
		
		__sub__(self, val)
		    Permite restar dos Polinomios, de la forma:
		    
		    	p1.__sub__(p2)


- Archivo "ajedrez.py": (Clases implementadas:
 								Clase Ficha, Subclases Torre, Alfil, Reina, Rey, Peon, Caballo
 								Clase Tablero)


	help(Polinomio)
	
	<class Ficha>
		""" Clase (Plantilla) que permite simular un objeto algebraico """
			
		__init__(self, *args)		
	        