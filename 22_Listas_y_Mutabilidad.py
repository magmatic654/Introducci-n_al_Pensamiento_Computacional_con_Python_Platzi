# Listas y mutabiidad

# Propiedades
# - Son secuecias de objetos, pero a diferencia de las tuplas, si son mutables
# - Cuando modificas una lista, pueden existir efectos secundarios (side effects)
# - Es posible iterar con ellas

# Modificacion de una lista (ejemplos)
# - Asignar via indice (my_list[0] = 5)
# - Utilizar los metodos de la lista (append, pop, remove, insert, etc.)

my_list = [1, 2, 3]

my_list[0] # => 1

# Slicing
my_list[1:] # => [2, 3]

my_list.append(4)
print(my_list) # => [1, 2, 3, 4]

my_list[0] = 'a'
print(my_list) # => ['a', 2, 3, 4]

my_list.pop() # => 4
print(my_list) # => ['a', 2, 3]

for element in my_list:
    print(element)

a = [1, 2, 3]
b = a # Dos nombres apuntan al mismo espacio en memoria

print(id(a) == id(b)) # True

c = [a, b]
print(c) # => [[1, 2, 3], [1, 2, 3]]

a.append(5)
# Se modifico a y b cuando solo intentaste cambiar a porque a y b apuntan al mismo apartado en memoria
print(a) # => [1, 2, 3, 5]
print(b) # => [1, 2, 3, 5]
print(c) # => [[1, 2, 3, 5], [1, 2, 3, 5]]
