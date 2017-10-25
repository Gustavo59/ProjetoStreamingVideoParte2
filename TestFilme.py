import unittest
from LOGICA import filme

class Teste(unittest.TestCase):

    def setUp(self):
        filme.filmes = []
        filme.iniciar_filmes()
        
    def test_add_usuario(self):
        filme.adicionar_filme('Um Dia', 'Romance', 2011)
        self.assertEqual(5,len(filme.filmes))

    def test_add_dois_filmes(self):
        filme.adicionar_filme('Um Dia', 'Romance', 2011)
        filme.adicionar_filme('Vizinhos', 'Comédia', 2014)
        self.assertEqual(6,len(filme.filmes))

    def test_remover_filme(self):
        filme.remover_filme('Carros')
        self.assertEqual(3,len(filme.filmes))

    def test_buscar_filme(self):   
        self.assertEqual(['Carros', 'Aventura', 2006], filme.buscar_filmes('Carros'))

    def test_buscar_filme_genero(self):
        self.assertEqual(['It - A Coisa'], filme.buscar_filmes_por_genero('Terror'))

    def test_buscar_filmes_com_mesmo_genero(self):
        filme.adicionar_filme('O Chamado', 'Terror', 2002)
        self.assertEqual(['It - A Coisa', 'O Chamado'], filme.buscar_filmes_por_genero('Terror'))

    


if __name__ == '__main__':
    unittest.main(exit=False)
        
