# Iterators o Iteradores
# los iteradores en python son objetos que regresan de forma sucesiva los valores asociados con el iterable

fruits = ['Pera', 'Manzana', 'Platano', 'Uva', 'Naranja']
iterator = iter(fruits)
print(next(iterator)) # => 'Pera'
print(next(iterator)) # => 'Manzana'
# Esta forma de iterar un objeto, permite hacerlo de una manera manual uno a uno
# Si ya no hay mas elementos siguientes y ponemos un next() a nuestro iterable, nos retornara un error de tipo StopIteration

# Python - Bucles definidos
# En python el ciclo for funciona internamente dando la funcion iter a el elemento a evaluar para obtener in iterator, este repetidamente llama a la funcion next() con el iterador y se detiene hasta que aparece el error StopIteration

# Bucles for con diccionarios

# Iterando un diccionario directamente con un bucle for nos retornara cada una de las llaves del diccionario

# Iterar utilizando .keys() nos retornara cada una de las llaves del diccionario

# Iterar utilizando .values() nos retornara cada uno de los valores asignados a cada llave del diccionario

# Iterar utilizando .items() nos retornara tuplas que contienen clave - valor de todo el diccionario

students = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for country in students:
    print(country)

for country in students.keys():
    print(country)

for country in students.values():
    print(country)

for country in students.items():
    print(country)

# Podemos modificar el comportamiento de nuestros bucles for utilizando
# break y continue

# break - termina el bucle en ese instante y seguira con el flujo del programa

# continue - evita todo el codigo que siga en la misma identacion abajo de el

 