import unittest
import os
from infrastructure.storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "tests/test_recibos.txt"
        self.storage = Storage(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_salvar_cria_arquivo_e_escreve_conteudo(self):
        conteudo = "Recibo de Teste"
        self.storage.salvar(conteudo)
        
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            self.assertIn(conteudo, f.read())