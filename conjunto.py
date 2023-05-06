class Conjunto:
    __numeros=''
   
    def __init__(self, __numeros):
        self.__numeros = set(__numeros)     # función set() para eliminar duplicados y crear conjunto

    def __add__(self, otro_conjunto):
            union = self.__numeros.union(otro_conjunto.__numeros)   # el método union() para unir los elementos de 2 conjuntos y crea una nueva instancia de la clase Conjunto con la unión resultante
            print(f'La unión de los conjuntos es: {union}' ) 
       
    def __sub__(self, otro_conjunto):
            diferencia = self.__numeros.difference(otro_conjunto.__numeros)
            print(f'La diferencia de los conjuntos es:{diferencia} ')
       
    def __eq__(self, otro_conjunto):
           if self.__numeros == otro_conjunto.__numeros:
               print(f'Los conjuntos son iguales.')
           else:
               print(f'Los conjuntos no son iguales.')   
     
