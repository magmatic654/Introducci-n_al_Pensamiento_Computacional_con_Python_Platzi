# Un docstring es una manera de docuementar que es lo que hace nuesto codigo especificamente.

# Primero se da una descripción clara y concisa de la función y su funcionamiento

# En medio se agrega la descripción de los diferentes parámetros, su tipo, su nombre y que es lo que se espera de esos parámetros

# Por ultimo se agrega que es lo que devuelve nuestra función

def sum(a, b):
    """
    Suma dos valores a y b

    param int a cualquier entero
    param int b cualquier entero
    returns la sumatoria de a y b
    """    
    return a + b

def a(any_param):
    """"
    La descripcion de lo que hace nuestra funcion
    any_param int cualquier entero
    returns any_param + 5
    """
    return any_param + 5

help(a) # devuelve que es lo que hace nuestra funcion