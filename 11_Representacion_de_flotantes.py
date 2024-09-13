# Representacion de flotantes

# El tipo flotante es una buena aproaximacion del numero que queremos calcular, sin embargo, a veces se comporta de maneras no esperadas

x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')

#En binario, intenten sumar varios decimales para llegar a 0.1 verán no es posible. Necesitarían una infinita cantidad de números decimales para ello y ++la memoria de una computadora finita++.

# Si es que te parece muy extraño no poder representar un número decimal y difícil de entender, piensa que **este problema ya lo has tenido antes toda tu vida **en el sistema decimal con 1/3. Para ese número necesitamos infinitos dígitos decimales para representarlo.

# Para solucionar este tema, podemos utilzar aproximaciones en vez de comprobar una igualdad, por ejemplo:

x = 0.0
for i in range(10):
    x += 0.1

if x < 1.0 and x > 0.9999:
    print(f'x = {x}')
else:
    print(f'x != {x}')
