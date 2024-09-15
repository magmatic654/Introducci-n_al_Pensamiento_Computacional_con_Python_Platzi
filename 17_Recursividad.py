# Recursividad

# Algoritmica: Una forma de crear soluciones utilizando el principio de "Divide y vencerás"

# Programática: Una tecnica programática mediante la cual una funcion se llama a sí misma

# Ejemplo con factoriales.
def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n!
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('Escribe un numero entero: '))
print(factorial(n))


# Limite de recursividad en libreria sys

# >>> import sys
# >>> print(sys.getrecursionlimit()) # => 1000

# Para modificar ese límite
# sys.setrecursionlimit(n) # n es el nuevo límite a establecer