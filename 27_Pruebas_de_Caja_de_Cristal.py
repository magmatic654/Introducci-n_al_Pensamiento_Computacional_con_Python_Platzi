# Pruebas de caja de cristal

# Sirve para determinar donde esta el bug

# Propiedades
# - Se basan en el flujo del programa
# - Prueba todos los caminos posibles de una funcion. Ramificaciones, bucles, for y while, recursion
# Regression testing o mocks

import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    return False


class PruebaDeCrustalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, True)
    
    def test_es_menor_de_edad(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()