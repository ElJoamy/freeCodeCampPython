import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):

    def test_calculate(self):
        # Prueba con lista válida
        input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected_output = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(calculate(input_list), expected_output)
        print("Prueba con lista válida pasada con éxito.")

        # Prueba con lista inválida
        input_list = [0, 1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            calculate(input_list)
        print("Prueba con lista inválida pasada con éxito.")

if __name__ == '__main__':
    unittest.main()
