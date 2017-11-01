import unittest
from LOGICA import historico

class TestHistorico(unittest.TestCase):

    def setUp(self):
        historico.historico = []
        
    def test_add_filme_historico(self):
        historico.registrar_filme_assistido("A volta dos que não foram", 999888)
        self.assertEqual(1,len(historico.historico))

    def test_add_dois_filmes_historico_mesma_conta(self):
        historico.registrar_filme_assistido("A volta dos que não foram", 91234)
        historico.registrar_filme_assistido("Conan", 91234)        
        self.assertEqual(2,len(historico.historico[0]))

    def test_add_dois_filmes_historico_contas_diferentes(self):
        historico.registrar_filme_assistido("A volta dos que não foram", 91234)
        historico.registrar_filme_assistido("Conan", 999888)        
        self.assertEqual(2,len(historico.historico[0]))
        self.assertEqual(2,len(historico.historico[1]))

    def test_listar_filmes_historico_vazio(self):
        self.assertEqual(False, historico.listar_filmes_assistidos(91234))

    def test_listar_filmes_historico_um_usuario(self):
        historico.registrar_filme_assistido("A volta dos que não foram", 91234)
        self.assertEqual(historico.historico[0][0], historico.listar_filmes_assistidos(91234))


if __name__ == '__main__':
    unittest.main(exit=False)
        
