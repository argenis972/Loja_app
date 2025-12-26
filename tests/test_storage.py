import os
from unittest.mock import patch, mock_open
from infrastructure.storage import salvar_recibo_em_arquivo_texto
from domain import Recibo

def test_salvar_recibo_no_diretorio_correto():
    recibo = Recibo(
        total = 100.0,
        metodo = "Dinheiro"
    )
    # Testa se o recibo gerado é salvo corretamente em um arquivo de texto. 
    
    caminho_esperado = os.path.join("data", "recibo_de_pagamento.txt")
    
    with patch("builtins.open", mock_open()) as mocked_file:
        salvar_recibo_em_arquivo_texto(recibo)  
        
        chamada_real = mocked_file.call_args[0][0]
        assert chamada_real == caminho_esperado