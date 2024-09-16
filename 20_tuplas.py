# Tuplas
# Son secuencias inmutables de objetos
# Pueden contener cualquier tipo de objeto
# Pueden utilizarse para devolver varios valores en una funcion

my_tuple = (1, 'dos', True)
type(my_tuple) # => <class 'tuple'>

my_tuple[0] # => 1
my_tuple[1] # => 'dos'

# Las tuplas no pueden modificarse, pueden reasignarse, pero no se pueden cambiar los elementos.

my_tuple = (1) # Esto no es una tupla, es un int porque una tupla se inicializa agregando mas elementos, una coma o inicializando el objeto directamente 
my_tuple # => <class 'int'>

my_tuple = (1,)
type(my_tuple) # => <class 'tuple'>

my_tuple = tuple([1])
type(my_tuple) # => <class 'tuple'>


# Las tuplas se pueden sumar
my_other_tuple = (2, 3, 4)
# Esto es una reasignacion, no una mutacion
my_tuple += my_other_tuple
print(my_tuple)

# Asignar varias variables desempaquetando los valores de la tupla
x, y, z = my_other_tuple
print(x) # => 2 
print(y) # => 3 
print(z) # => 4

def coordenates():
    return (5, 4)

coordenates = coordenates()
print(coordenates) # => (5, 4)

x, y = coordenates
print(x, y) # => 5 4