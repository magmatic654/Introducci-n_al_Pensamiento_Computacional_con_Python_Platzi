# En Python Todo es un Objeto, incluyendo las funciones.

# Propiedades de las funciones en Python
# Tienen tipo
# Se pueden pasar argumentos de otras funciones
# Se pueden utilizar en expresiones
# Se pueden incluir en varias estructuras de datos (como listas, tuplas, diccionarios, etc)

# Argumentos de otras funciones
# Las funciones pueden recibir funciones como parametros

# Ejemplo:
def multiplicar_por_dos(n):
    """multiplicamos por dos el numero n

    n int
    returns n * 2
    """
    
    return n * 2

def sumar_dos(n):
    """Sumamos dos al numero n 

    n int
    returns n + 2
    """
    return n + 2

def aplicar_operacion(f, numeros):
    """Aplica una funcion a cada elemento de una lista de numeros
    
    numeros list
    returns f(n) each numeros
    """
    resultados = []

    for n in numeros:
        resultados.append(f(n))
    return resultados

print(aplicar_operacion(sumar_dos, [1, 2, 3, 4, 5])) # => [3, 4, 5, 6, 7]
print(aplicar_operacion(multiplicar_por_dos, [1, 2, 3, 4, 5])) # => [2, 4, 6, 8, 10]


# Funciones en expresiones
# Podemos definir una funcion en una expresion utilizando el keyword lambda 
# Las funciones lambda las podemos guardar en variables.

# Ejemplo:
sumar = lambda x, y: x + y
sumar(10, 5) # => 15


# Funciones en estructuras de datos
# Las funciones se pueden incluir en estructuras que las permitan almacenar.

# Ejemplo: tenemos una funcion que recibe un numero n y contiene una lista de funciones llamada operaciones.
# Utilizando un for utilizamos cada funcion de la lista de operaciones en el numero n y el resultado lo guardamos en la lista resultado.
# La funcion retorna una lista con el resultado de aplicar todas las funciones a un numero
def aplicar_operaciones(n):
    operaciones = [abs, float]

    resultado = []

    for operacion in operaciones:
        resultado.append(operacion(n))
    
    return resultado

print(aplicar_operaciones(-2)) # => [2, -2.0]


