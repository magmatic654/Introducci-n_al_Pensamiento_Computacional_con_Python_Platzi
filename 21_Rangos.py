# Rangos

# Propiedades
# - Representan una secuencia de enteros
# - range(comienzo, fin, pasos)
# - Son inmutables
# - Muy eficientes en uso de memoria y normalmente utilizados en for loops

start = 1
end = 11
steps = 1 
# El rango es de 1 a 11 en cuenta de 1 en 1 no inclusivo, es decir, no se cuenta el ultimo numero 11
my_range = range(start, end, steps)
type(my_range) # => <class 'range'>

# Utilizando un range en un for loop
for i in my_range:
    print(i)


my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

# Ambos rangos generan la misma secuencia de valores, por lo cual, se consideran como iguales
print(my_range == my_other_range)

for i in my_range:
    print(i)

for i in my_other_range:
    print(i)

print(id(my_range))
print(id(my_other_range))

# No son el mismo objeto
# is verifica si ambos son el mismo objeto
# object equality
print(my_range is my_other_range) 

# Secuencia de numeros pares del 0 al 100
for i in range(0, 101, 2):
    print(i)

# Secuencia de numeros impares del 0 al 100
for i in range(1, 100, 2):
    print(i)