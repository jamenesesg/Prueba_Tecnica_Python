import collections
from itertools import zip_longest

class Polinomio():
    """ Clase (Plantilla) que permite simular un objeto algebraico """
    
    def __init__(self, *args):
        """ Puede crear un Polinomio de una de las tres formas, enviando como argumento:

                p = Polinomio(polinomio)      # objeto Polinomio
                p = Polinomio([1,2,3 ...])    # secuencia
                p = Polinomio(1, 2, 3 ...)    # escalar """        
        try:
            if len(args)==1:            
                if isinstance(args[0], Polinomio):                 # Se envió como argumento un polinomio
                    self.coeficientes = args[0].coeficientes                
                elif isinstance(args[0], collections.Iterable):    # Se envió como argumento una coleccion de elementos
                    self.coeficientes = list(args[0])
                else:                                              # Se envió como argumento un escalar
                    self.coeficientes = [args[0]+0]
            elif len(args)==0:                                     # Se envió como argumento un campo vacio, se asume valor cero
                self.coeficientes = [0]
            else:                                                  # Se envian como argumento multiples escalares
                   self.coeficientes = [i+0 for i in args]
        except Exception as e:
            print("Ocurrio el siguiente error:", type(e).__name__)

    def __evaluar__(self, x):
        """ Permite evaluar un Polinomio:

                Se hace un llamado al método (Polinomio.__evaluar__())
                y se envia como argumento el polinomio a evaluar y la variable:

                Polinomio.__evaluar__(Polinomio(5,3,0,1,3),5)      
                Polinomio.__evaluar__(p,3)                         # (p) objeto polinomio """
        res = 0
        for i in reversed(self.coeficientes):
            res *= x
            res += i
            
        eq = []
        for po,co in enumerate(self.coeficientes):
            if co:
                if po==0:
                    po = ''
                elif po==1:
                    po = '('+ str(x) +')'
                else:
                    po = '('+ str(x) +')^'+str(po)
                eq.append(str(co)+po)
        if eq:
            eq.reverse()
            return ' + '.join(eq) + ' = ' + str(res)
        else:
            return "0"

    def __add__(self, val):
        """ Permite sumar dos Polinomios, de la forma:

                p1.__add__(p2) """
        
        if isinstance(val, Polinomio):
            res = [ a+b for a,b in zip_longest(self.coeficientes, val.coeficientes, fillvalue=0)]   
            #zip_longest funciona igual que zip, pero permite asignar un valor por defecto a un campo no definido y poder iterar dos polinomios de igual longitud.
        else:
            res = self.coeficientes[:]
            res[0] += val
        return res 
    
    def __sub__(self, val):
        """ Permite restar dos Polinomios, de la forma:

                p1.__sub__(p2) """
        
        if isinstance(val, Polinomio):
            res = [ a-b for a,b in zip_longest(self.coeficientes, val.coeficientes, fillvalue=0)]
        else:
            res = self.coeficientes[:]
            res[0] -= val
        return res 
    
    def __mul__(self, val):
        """ Permite Multiplicar dos Polinomios o Multiplicar un Polinomio por un escalar, de la forma:

                p1.__mul__(p2)
                p1.__mul__(5) """
        
        if isinstance(val, Polinomio):
            res= [0]*(len(self.coeficientes)+len(val.coeficientes)-1)
            
            for sgrado, scoef in enumerate(self.coeficientes):
                for ogrado, ocoef in enumerate(val.coeficientes):
                    res[sgrado+ogrado]+= scoef*ocoef
            return res
        else:
            res = [i*val for i in self.coeficientes]
        return res

    def __str__(self):
        """ Retorna el termino algebraico asociado al Polinomio enviado como argumento 

                Polinomio(5,3,0,1,3)  ->   3X^4 + 1X^3 + 3X + 5   """
        eq = []
        for po,co in enumerate(self.coeficientes):
            if co:
                if po==0:
                    po = ''
                elif po==1:
                    po = 'X'
                else:
                    po = 'X^'+str(po)
                eq.append(str(co)+po)
        if eq:
            eq.reverse()
            return ' + '.join(eq)
        else:
            return "0"        
            

# from numpy.polynomial import polynomial as p

# c1 = (1,2,3)
# c2 = 3

# p.polyadd(c1,c2)        # Suma entre polinomios
# p.polysub(c1,c2)        # Resta entre polinomios
# p.polymul(c1,c2)        # Resta entre polinomios

# c1*2
# c2*3

# p.polyval(2, c1) # 4 + 4(2) + 4(2**2)
# p.polyval(2, c2) # 4 + 4(2) + 4(2**2)
    
    


