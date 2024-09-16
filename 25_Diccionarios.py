# Diccionarios

# Propiedades
# Los diccionarios son como listas, que en vez de indices utilizan llaves
# No tienen orden interno
# Son mutables
# Pueden iterarse

# Tambien se conocen como hash maps

my_dict = {
    'Harold': 33,
    'Carlos': 42,
    'Jaime': 50
}

# Para encontrar los valores asociados a las llaves se escribe la siguiente notacion.
print(my_dict['Jaime'])

# Si no sabemos si existe o no una llave, podemos utilizar .get() para evitar un error y a su vez que nos pueda devolver un valor por default
print(my_dict.get('David', 'No existe')) # => 'No existe'
print(my_dict.get('Harold', 'No existe')) # => 33

# Reasignar un valor
my_dict['Jaime'] = 20
print(my_dict)

# Asignar una nueva llave - valor
# Si la llave que encerramos entre corchetes no existe y le asignamos un valor, este conjunto llave-valor se agregara a el diccionario como un nuevo elemento
my_dict['Kenn'] = 74
print(my_dict) # => {'Harold': 33, 'Carlos': 42, 'Jaime': 20, 'Kenn': 74}

# Eliminar un elemento del diccionario
# Podemos utilizar el keyword 'del' para eliminar un elemento de nuestro diccionario
del my_dict['Jaime']
print(my_dict) # => {'Harold': 33, 'Carlos': 42, 'Kenn': 74}

# Iterar en el diccionario a lo largo de las llaves, de los valores o de las llaves y valores.

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

print('Harold' in my_dict) # => True
print('Pedro' in my_dict) # => False
