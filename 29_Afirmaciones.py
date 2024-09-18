# Afirmaciones

# Propiedades
# Programacion defensiva
# Pueden utilizarse para verificar que los tipos sean correctos en una funcion
# Tambien sirven para debuguear

# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

# Nos aseguramos que no se cometan errores fatales para poder concluir con el computo.
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras