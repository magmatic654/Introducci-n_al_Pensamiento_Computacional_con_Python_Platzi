# Manejo de excepciones

# Las excepciones se manejan con los keywords:
# try, except, finally

# Se puede utilizar para ramificar programas

# No deben manejarse de maneras silenciosas (por ejemplo, con print statements)

# Para aventar tu propia excepcion utiliza el keyword raise

def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as error:
        print(error)
        return lista
    
lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))