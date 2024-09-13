# for
# En los lenguajes de programacion se consideran a los bucles definidos e indefinidos.
# Los bucles definidos son los que preestablecen las conficiones de iteracion por adelantado
# Los bucles indefinifos establecen la condicion en la que la iteracion terminara, en este existe el riesgo de que el bucle se vuelva infinito cuando nunca se cumple la condicion dada

# a partir del keyword for se implementa en python los bucles definidos
# a partir de while se implementan los bucles indefinidos en python

# Los bucles for iteran dentro de una coleccion de objetos y se crea una variable propia en el for que le podemos dar cualquier nombre, esta representara todos los elementos dentro del objeto dado, Ejemplo:
phrase = 'Por la tarde mientras el sol se escondia...'

# Ciclo definido for
for char in phrase:
    print(char)

for letter in phrase:
    print(letter)

for etc in phrase:
    print(etc)

# Los 3 retornar los mismos resultados, pues su unica variacion es la denominacion que le damos a la variable interna de for, 
# sin embargo esta variable interna no cambia ningun resultado, 
# lo que si es recomendable es ponerle como nombre algo que describa lo que es de una forma acertada por su contexto.
# Esto con la finalidad de darle mayor legibilidad a nuestro codigo

# For en listas en python
fruits = ['Pera', 'Manzana', 'Platano', 'Uva', 'Naranja']

for fruit in fruits:
    print(fruit)

# Este ciclo for nos imprimira en la consola cada fruta que hay en la lista: 
# Pera
# Manzana
# Platano
# Uva
# Naranja
