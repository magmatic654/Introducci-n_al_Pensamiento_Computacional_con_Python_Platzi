# Pruebas de caja negra

# Se basan en la especificacion de la funcion o el programa
# Prueba inputs y valida outputs
# Unit testing o integration testing

import unittest

class CajaNegraTest(unittest.TestCase):
    # Antes de escribir la funcion, escribimos las pruebas para la funcion
    # Sirven para mantener el codigo con calidad y que jamas se cambien los resultados esperados
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_sum_dos_negativos(self):
        num_1 = - 10
        num_2 = - 7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

def suma(num_1, num_2):
    return num_1 + num_2

if __name__ == '__main__':
    unittest.main()
