# List Comprehension
# - Es una forma concisa de aplicar operaciones a los valores de una secuencia
# - Tambien se pueden aplicar condiciones para filtrar

my_list = list(range(100))
print(my_list)

double = [n * 2 for n in my_list]
print(double)

even = [n for n in my_list if n % 2 == 0]
print(even)