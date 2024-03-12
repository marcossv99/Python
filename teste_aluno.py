from notas_alunos import*

import unittest

class Testes_das_notas(unittest.TestCase):
    def teste_medias(self):
        self.assertAlmostEquals(verifica_notas(5.5, 6) 5.5)
        self.assertAlmostEquals(verifica_notas(5.5, 6) 5.5)
        self.assertAlmostEquals(verifica_notas(5.5, 6) 5.5)
        
    def teste_intervalo(self):
        self.assertRaises(ValueError, verifica_notas, 11, 4)
        self.assertRaises(ValueError, verifica_notas, 11, 4)
        self.assertRaises(ValueError, verifica_notas, 11, 4)
        
    def teste_aprovado_recuperacao(self):
        
        self.assertRaises(ValueError, verifica_notas, 0, 0)
        self.assertRaises(ValueError, verifica_notas, 0, 0)
        self.assertRaises(ValueError, verifica_notas, 0, 0)    