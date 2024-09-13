# Entradas(Inputs)

# Invocacion
# La funcion input recibe un parametro el cual es el texto que podra ver el usuario: input('Parametro')

# Propiedades
# La funcion input siempre regresa una cadena como resultado, por lo cual si requerimos algun otro tipo de dato, tendremos que hacer type casting

name = input('Escribe tu nombre => ')

# La funcion print puede recibir varios parametros
print('Tu nombre es', name)

# Se puede imprimir una cadena formateada incluyendo la variable
print(f'Tu nombre es {name}')

number = input('Escribe un numero => ')
print(number)

# La funcion type retorna el tipo de variable que es el argumento dado, en este caso es un <class 'str'>, ya que los input siempre devuelven strings como resultado
print(type(number))

# Podemos cambiar el tipo de dato que va a devolver el input como un numero entero.
number = int(input('Escribe un numero => '))

# En esta ocasion nos devuelve <class 'int'> como su tipo de dato
print(type(number))
