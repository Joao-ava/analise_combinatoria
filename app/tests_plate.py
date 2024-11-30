import unittest
from app.plate import Plate 

# Saida esperada: Ran 7 tests in 0.002s

class TestPlate(unittest.TestCase):
    def test_find_state_ceara(self):
        self.assertEqual(Plate.find_state('HTX1234'), 'Ceará')
        self.assertEqual(Plate.find_state('HZA9999'), 'Ceará')
        self.assertEqual(Plate.find_state('HTY0000'), 'Ceará')

    def test_find_state_maranhao(self):
        self.assertEqual(Plate.find_state('HOL1234'), 'Maranhão')
        self.assertEqual(Plate.find_state('HQE9999'), 'Maranhão')
        self.assertEqual(Plate.find_state('NHT0000'), 'Maranhão')

    def test_find_state_piaui(self):
        self.assertEqual(Plate.find_state('LVF1234'), 'Piauí')
        self.assertEqual(Plate.find_state('LWQ9999'), 'Piauí')
        self.assertEqual(Plate.find_state('PIZ0000'), 'Piauí')

    def test_find_state_invalid(self):
        self.assertEqual(Plate.find_state('XYZ1234'), 'De nenhum dos estados')
        self.assertEqual(Plate.find_state(''), 'Formato de placa inválido')

    def test_count_plates_ceara(self):
        self.assertGreater(int(Plate.count_ce()), 0) 

    def test_count_plates_maranhao(self):
        self.assertGreater(int(Plate.count_ma()), 0)  

    def test_count_plates_piaui(self):
        self.assertGreater(int(Plate.count_pi()), 0)  

def run_tests():
    unittest.main()
