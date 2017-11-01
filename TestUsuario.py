import unittest
from LOGICA import usuario

class Teste(unittest.TestCase):

    def setUp(self):
        usuario.usuarios = []
        usuario.iniciar_usuarios()
        
    def test_add_usuario(self):
        usuario.adicionar_usuario(55555555555, 'Luana', 'luana@gmail.com', 'luana228')
        self.assertEqual(5,len(usuario.usuarios))

    def test_add_dois_usuarios(self):
        usuario.adicionar_usuario(55555555555, 'Luana', 'luana@gmail.com', 'luana228')
        usuario.adicionar_usuario(66666666666, 'Guilherme', 'guilherme@gmail.com', 'guilherme441')
        self.assertEqual(6,len(usuario.usuarios))

    def test_remove_usuario(self):
        usuario.remover_usuario(1)
        self.assertEqual(3,len(usuario.usuarios))

    def test_buscar_usuario(self):
        self.assertEqual([3, "André", "andré@gmail.com", "andre224"], usuario.buscar_usuario(3))

    def test_listar_usuario(self):
        self.assertEqual(len(usuario.usuarios),4)


if __name__ == '__main__':
    unittest.main(exit=False)
        
