# Iteraciones
# Las iteraciones permiten realizar la misma tarea en varias ocaciones
# Se pueden escribir iteraciones dento de otras
# Se puede utilizar break para salir de una iteracion deliberadamente
# Se debe tener cuidado con las iteraciones infinitas

# While 
# Es un tipo de iteracion donde se evalua una condicion y mientras sea verdadera se seguira repitiendo el codigo una y otra vez
contador = 0
# El programa termina cuando contador supera a 10 como numero 
while contador < 10:
    contador += 1
    # print(contador)


contador_externo = 0
contador_interno = 0
# Loop adentro de otro Loop
while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo,  contador_interno)
        contador_interno += 1
        
        if contador_interno >= 3:
            break
    contador_externo += 1
    contador_interno = 0