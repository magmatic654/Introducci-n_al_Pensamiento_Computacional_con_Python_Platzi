# Abstraccion 
# Significa que no necesitas entender algo que opera internamente para poderlo utilizar
# Como ingenieros de software se deben generar estas abstracciones que permiten utilizar una funcion sin que una persona necesariamente sepa como funciona

# Decomposicion
# Dividir el codigo en componentes que colaboran en conjunto para llegar a una solucion
# Podemos generar muchos pedazos de nuestro codigo

# Funciones
def function_name (parameters, p2, p3, etc):
    # Body of function
    return parameters

# Definiendo a la funcion sum para sumar
def sum(a, b):
    return a + b # Retorna la suma entre a y b

result1 = sum(1,2) # Guardamos el valor de nuestra funcion en la variable result1
result2 = sum(6,3) # Guardamos el valor de nuestra funcion en la variable result2

# Podemos llamar a nuestra funcion las veces que queramos o sean necesarias.

def full_name(name, last_name, inverse = False): # Podemos asignar valores iniciales a nuestras variables internas si es que no se utilizan, por ejemplo inverse = False, si no se utiliza inverse se dara por hecho que es False
    if inverse:
        return f'{last_name} {name}'
    else:
        return f'{name} {last_name}'
    
name1 = full_name('Harold', 'Navarro') # Las funciones reciben parametros, los cuales estan en el mismo orden que en la funcion inicial, por ejemplo, en este caso 'Harold' se asigna a la variable de la funcion name y 'Navarro' a la variable last name
name2 = full_name('Harold', 'Navarro', inverse=True)
name3 = full_name(last_name='Navarro', name='Harold') # El orden de los parametros puede ser cambiado si definimos exactamente a que variable le corresponde cada parametro dado

print(name1, name2, name3)
