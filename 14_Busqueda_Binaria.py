# Busqueda Binaria
# Nuestro conjunto de busqueda debe estar ordenado
# Es altamente eficiente pues acorta en dos por cada iteracion
# Solo funciona la busqueda binaria si esta ordenado !!

objective = int(input('Escoge un numero => '))
epsilon = 0.001
min = 0.0
max = max(1.0, objective)
answer = (max + min) / 2
temp_answer = None
while abs(answer**2 - objective) >= epsilon:
    if answer**2 < objective:
        min = answer
    # Este elif sirve para resolver las limitaciones en python de calculos grandes, cuando la respuesta se vuelve igual 2 veces, significa que ya no puede sumarse y dividirse en 2 mas veces, por lo cual retornamos la respuesta mas acercada
    elif temp_answer == answer:
        break
    else:
        max = answer
    print(f'Maximo: {max} Minimo: {min}')
    temp_answer = answer
    answer = (max + min) / 2

print(f'la raiz cuadrada de {objective} es {answer}')