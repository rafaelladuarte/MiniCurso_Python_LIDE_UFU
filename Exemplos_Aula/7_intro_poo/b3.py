class BolsaDeValores:
    def __init__(self):
        self.acoes = {}

    def adicionar_acao(self, nome, preco):
        self.acoes[nome] = preco

    def remover_acao(self, nome):
        if nome in self.acoes:
            del self.acoes[nome]
        else:
            print(f"Ação {nome} não encontrada na bolsa.")

    def obter_acao(self, nome):
        if nome in self.acoes:
            return self.acoes[nome]
        else:
            print(f"Ação {nome} não encontrada na bolsa.")
            return None

    def listar_acoes(self):
        print("Ações na Bolsa de Valores:")
        for nome, preco in self.acoes.items():
            print(f"{nome}: ${preco:.2f}")


# Função para visualizar as ações com preços acima de um valor específico
def visualizar_acoes_acima_valor(bolsa, valor_limite):
    print(f"Ações com preços acima de ${valor_limite:.2f}:")
    for nome, preco in bolsa.acoes.items():
        if preco > valor_limite:
            print(f"{nome}: ${preco:.2f}")
