# Clonacion de listas
# - Casi siempre es mejor clonar una lista en vez de mutarla
# - Para clonar una lista podemos utilizar slices o a la funcion list

a = [1, 2, 3]
b = a
# a y b contienen el mismo id
print(id(a), id(b)) # => 2033458133824 2033458133824
c = list(a) # c es una lista distinta que a en memoria, porque es una copia de a, no es a
print(c) # => [1, 2, 3]
print(id(a), id(b), id(c)) # => 2827501943616 2827501943616 2827505102720
d = a[::]
print(d) # => [1, 2, 3]

# a, c y d tienen distintas direcciones en memoria
print(id(a), id(c), id(d)) # => 2513390385984 2513393086336 2513390381824
