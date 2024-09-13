# Utilizar if para comprobar si una expresion es verdadera y ejecutar el bloque de codigo dentro de el
if 3 > 2:
    print('3 es mayor que 2') 

# Utilizar else despues de if es para ejecutar un bloque de codigo si es que la primer conficion if no fue cumplida
if 2 > 2:
    pass
else:
    print('2 no es mayor que 2')

# Utilizar elif es para verificar otra condicion aparte del if, pueden haber muchos elif dentro de la estructura decisional
if 4  > 5:
    pass
elif 4 < 5:
    print('4 Es menor que 5')
else:
    pass