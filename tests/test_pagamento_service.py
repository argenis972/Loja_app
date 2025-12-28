# tests/test_pagamento_service.py
import unittest
from unittest.mock import MagicMock
from services.pagamento_service import PagamentoService
from domain.recibo import Recibo

class TestPagamentoService(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.service = PagamentoService(repositorio=self.mock_repo)

    def test_deve_calcular_previa_a_vista_dinheiro(self):
        resultado = self.service.calcular_previa(100.0, 1)

        # Asserção
        self.assertIsInstance(resultado, Recibo)
        self.assertEqual(resultado.total, 90.0) # Supondo 10% desc

    def test_deve_finalizar_venda_e_salvar(self):
        # Cenário
        recibo_fake = Recibo(total=100.0, metodo="Dinheiro")
        
        # Ação
        self.service.finalizar_venda(recibo_fake)

        # Asserção: Verifica se chamou o repositório
        self.mock_repo.salvar.assert_called_once_with(recibo_fake)

    def test_deve_falhar_com_opcao_invalida(self):
        # Ajustado para calcular_previa
        with self.assertRaises(ValueError):
            self.service.calcular_previa(100, 99)