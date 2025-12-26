import os
from datetime import datetime
from domain import Recibo

def salvar_recibo_em_arquivo_texto(recibo: Recibo):

    caminho = os.path.join("data", "recibo_de_pagamento.txt")
    # Salvar o recibo em um arquivo de texto
    diretorio = "data"
    nome_arquivo = "recibo_de_pagamento.txt"
    
    # Cria o caminho relativo a partir de onde o script é executado
    caminho_completo = os.path.join(diretorio, nome_arquivo)

    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Escreve os detalhes do recibo no arquivo de texto
    try:
        with open(caminho_completo, "a", encoding="utf-8") as f:
            f.write("\n" + "=="*24 + " RECIBO DE PAGAMENTO " + "=="*24 + "\n")
            f.write(f"Data e hora: {data_hora_atual}\n")
            f.write(f"Total a pagar: R$ {recibo.total:.2f}\n")
            f.write(f"Método de pagamento: {recibo.metodo}\n")

            # Detalhes das parcelas, se houver
            if recibo.parcela > 1:
                f.write(f"Número de parcelas: {recibo.parcela}\n")
                f.write(f"Valor de cada parcela: R$ {recibo.valor_da_parcela:.2f}\n")
            
            if recibo.informacoes_adicionais:
                f.write(f"Informações adicionais: {recibo.informacoes_adicionais}\n")
            
            f.write("\n")
        print(f"Recibo salvo em '{caminho_completo}'")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")
   