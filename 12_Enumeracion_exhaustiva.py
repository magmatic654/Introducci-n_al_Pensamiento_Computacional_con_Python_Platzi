# Enumeracion Exhaustiva
# Cuando se trata de un algoritmo completamente nuevo o que desconocemos, el primer tipo de solucion debe ser pensando en la enumeracion Exhaustiva.
# Tambien llamado "Adivina y Verifica"

objective = int(input('Escoge un numero entero => '))
answer = 0

# Mientras answer elevado al cuadrado saa menor que el numero a encontrar su raiz cuadrada (objective), el programa sumara de uno en uno hasta encontrar un valor que multiplicado por si mismo de igual al resultado, si no lo encuentara, simplemente se quedara en asnwer un resultado que multiplicado por si mismo no es igual al objective  
while answer**2 < objective:
    print(answer ** 2)

    answer += 1

# Si la respuesta al cuadrado es igual al objetivo, entonces el numero encontrado (answer) es la raiz cuadrada exacta del numero inicial (objective), de lo contrario, la raiz cuadrada no tiene raiz cuadrada exacta
if answer**2 == objective:
    print(f'La raiz cuadrada de {objective} es {answer}')
else:
    print(f'{objective} no tiene una raiz cuadrada exacta')