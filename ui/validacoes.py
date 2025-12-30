def validacao_de_dados(mensagem, tipo: type, minimo=0.01):
    """
    Valida entrada do usuário convertendo para 'tipo' e garantindo >= minimo.
    Repetirá até uma entrada válida ser informada.
    """
    while True:
        try:
            entrada = input(mensagem)
            # permitir vírgula como separador decimal
            if tipo is float:
                entrada = entrada.replace(",", ".")
            valor = tipo(entrada)
            if minimo is not None and valor < minimo:
                print(f"Valor inválido. Por favor, digite um valor maior ou igual a {minimo}")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")


def pedir_input_numerico(msg, tipo=int, minimo=None, maximo=None):
    """
    Pede um número inteiro (ou outro tipo) com limites opcionais.
    """
    while True:
        try:
            raw = input(msg)
            valor = tipo(raw)
            if minimo is not None and valor < minimo:
                print(f"[ERRO]: O valor mínimo é {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"[ERRO]: O valor máximo é {maximo}.")
                continue
            return valor
        except ValueError:
            print("[ERRO]: Entrada inválida. Por favor, digite um número.")