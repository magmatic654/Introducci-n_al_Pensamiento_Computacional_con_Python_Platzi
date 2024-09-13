# Cadena de texto simple:
string_1 = '123'
print(string_1) # => '123'

# Cadena de texto multiplicada
string_2 = '123' * 3
print(string_2) # => '123123123'

# Cadena de texto con suma
string_3 = '123' + '456'
print(string_3) # => '123456'

# Cadena de texto con multiplicacion y sumas
string_4 = ('Hip' * 3) + ' ' + 'hurra'
print(string_4) # => HipHipHip hurra

# Cadena de texto con formato (se pueden utilizar operaciones dentro de las llaves)
string_5 = f'{"Hip" * 3} hurra'
print(string_5) # => HipHipHip hurra

string_6 = "Hello World!"

# len(): Devuelve la longitud del string (cuantos caracteres contiene)
size = len(string_6)
print(size) # => 12

# indexing: La indexacion en python devuelve el elemento en la posicion deseada, esto se logra poniendo lo que queremos indexar junto a corchetes y el numero de la posicion que buscamos
index1 = string_6[0]
index2 = string_6[1]
index3 = string_6[2]
print(index1) # => H
print(index2) # => e
print(index3) # => l

# slicing: Se pueden cortar pedazos de los elementos de la variable, en este caso las letras del string en distintas partes
slice1 = string_6[0: 3]
slice2 = string_6[3: 8]
slice3 = string_6[8: 12]
print(slice1) # => Hel
print(slice2) # => lo Wo
print(slice3) # => rld!

# Desde la posicion 4 hasta el final
slice4 = string_6[4:]
print(slice4) # => o World!

# Desde la primer posicion hasta la posicion 4
slice5 = string_6[:4]
print(slice5) # => Hell

# Desde la primer posicion hasta 2 posiciones antes de terminar
slice6 = string_6[: -2]
print(slice6) # => Hello Worl

# Desde el inicio saltando de 2 en 2
slice7 = string_6[::2]
print(slice7) # => HloWrd


# Propiedades de las cadenas de texto.
# - Los objetos de tipo str se representan con "" o ''
# - El operador + en cadenas de texto significa concatenacion
# - El operador * multiplica la misma cadena un numero de veces
# - Las cadenas son inmutables, es decir, una vez creadas, estas no pueden mofificarse, la concatenacion no modifica a la cadena incial, sino que se genera un nuevo espacio en memoria con el nuevo valor y se apunta hacia el.

