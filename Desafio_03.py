# Crear un programa que le permita al usuario elegir entre los 3 distintos tipos de algoritmos para encontrar la raiz cuadrada de un numero.
def program():
    def enumeration():
            answer = 0
            print('enumeracion')
            while answer**2 < objective:
                answer += 1
            
            if answer**2 == objective:
                return answer
            else:
                print(f'No existe una raiz cuadrada exacta')

    def aproximation():
                answer = 0
                epsilon = 0.001
                step = epsilon**2


                while abs(answer**2 - objective) >= epsilon and answer <= objective:
                    answer += step
                

                if abs(answer**2 - objective) >= epsilon:
                    return None
                return answer
    
    def binary():
        epsilon = 0.001
        lower = 0
        higher = max(1, objective) # Obtiene el maximo entre 1 y el objetivo y se asigna a higher
        answer = (lower + higher) / 2

        while abs(answer**2 - objective) >= epsilon:
            if answer**2 < objective:
                lower = answer
            else:
                higher = answer
            
            answer = (lower + higher) / 2
        return answer


    while True:
        select_algorithm = int(input('Por que metodo deseas realizar el calculo? \n1. Enumeracion Exhaustiva\n2.Aproximacion de soluciones\n3.Busqueda Binaria\n => '))
        objective = int(input('Escribe el numero de la raiz a encontrar => '))
        algorithms = [enumeration, aproximation, binary] #aproximacion, binaria
        result = algorithms[select_algorithm - 1]()
        if result:
            print(f'La raiz cuadrada de {objective} es {result}')
        else:
             print('No se hallo un resultado que satisfaga los requerimientos')
        
        seguir_programa = input('Deseas seguir realizando calculos? Y / N =>').lower()
        if seguir_programa != 'Y':
            return
program()