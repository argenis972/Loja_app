# Validação de dados de entrada

def validacao_de_dados(mensagem, tipo : type, minimo = 0.01):
    # Validação de dados de entrada do usuário
    while True:
        try:
            entrada = input(mensagem)
            valor = tipo(entrada)
            if valor < minimo:
                print(f"Valor inválido. Por favor, digite um valor maior ou igual a {minimo}")
                continue
            return valor
            
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
