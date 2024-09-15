# La secuencia de Fibonnaci es una funcion matematica que se define recursivamente. 
# En 1202 Fibonacci encontró una formula para cuantificar el crecimiento que ciertas poblaciones experimentan.

# Imaginando una situacion, en donde existen 2 conejos iniciales, una hembra y un macho, con un periodo de reproduccion que comienza 1 mes despues de edad, un periodo de gestacion de 1 mes y contemplando que los conejos nunca mueren y la hembra es capaz de producir una nueva pareja. Cuantos conejos existirian al final de seis meses?

# Mes - 0 Hembras - 1
# Mes - 1 Hembras - 1
# Mes - 2 Hembras - 2
# Mes - 3 Hembras - 3
# Mes - 4 Hembras - 5
# Mes - 5 Hembras - 8
# Mes - 6 Hembras - 13

# Para el mes n > 1, hembras(n) = hembras(n - 1) + hembras(n - 2)
# Por lo tanto, tenemos 2 casos base (0 y 1) y 2 llamadas recursivas (hembras(n - 1) + hembras(n - 2))

def fibonnaci(n):
    """Calcula la secuencia fibonnaci

    n > 0 int
    returns fibonnaci(n - 1) + fibonnaci(n - 2) 
    """
    if n == 0 or n == 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)

n = int(input("Elige un numero entero "))

help(fibonnaci)