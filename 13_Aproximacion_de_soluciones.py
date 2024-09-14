# Aproximacion de soluciones
# Similar a la enumeracion exhaustiva, pero no necesita una respuesta exacta
# Podemos aproximar soluciones con un margen de error que llamaremos epsilon
# En computacion para ser precisos, necesitamos mas tiempo, no se puede rapidez junto con precision entre mas preciso queremos que sea

objective = int(input('Digita un numero => '))
epsilon = 0.01
step = epsilon**2
answer = 0.0

# La funcion abs() retorna el valor absoluto

# mienstras el valor absoluto de respuesta al cuadrado menos el objetivo al que queremos llegar sea mayor o igual a epsilon y la respuesta sea menor o igual al objetivo, entonces se sumara a la respuesta un paso que esta dado por epsilon**2
while abs(answer**2 - objective) >= epsilon and answer <= objective:
    answer += step

if abs(answer**2 - objective) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objective}')
else:
    print(f'La raiz cuadrada de {objective} es {answer}')