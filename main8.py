from conjunto import Conjunto

if __name__=='__main__':
    conjunto_a = Conjunto([1, 2, 3, 4])
    conjunto_b = Conjunto([3, 6, 9])
    
       
    print(f'-----MENU-----')
    print('1- Unión de conjuntos')
    print('2- Diferencia de dos conjuntos')
    print('3- Verificar si dos conjuntos son iguales')
    print('0- Salir')
    opcion = input('Seleccione una opción: ')
    
    while opcion != 0:     
        if opcion == 1:
            union= conjunto_a.__add__(conjunto_b)
            
        elif opcion == 2:
            diferencia = conjunto_a.__sub__(conjunto_b)
            
        elif opcion == 3:
             ig= conjunto_a.__eq__(conjunto_b)
             
        opcion= int(input('Seleccione una opción: '))