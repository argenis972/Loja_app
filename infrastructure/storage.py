import os

class Storage:
    def __init__(self, arquivo="data/recibos.txt"):
        self.arquivo = arquivo
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)

    def salvar(self, recibo):
        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write(str(recibo) + "\n")