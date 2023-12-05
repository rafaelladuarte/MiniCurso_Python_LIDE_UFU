from b3 import BolsaDeValores
from b3 import visualizar_acoes_acima_valor


# Função para calcular o valor total de todas as ações na bolsa
def calcular_valor_total(bolsa):
    total = sum(bolsa.acoes.values())
    return total

# Exemplo de uso da classe BolsaDeValores e das funções
bolsa = BolsaDeValores()
bolsa.adicionar_acao("Apple", 150.0)
bolsa.adicionar_acao("Microsoft", 300.0)
bolsa.adicionar_acao("Google", 2500.0)
bolsa.adicionar_acao("Amazon", 3500.0)

bolsa.listar_acoes()

total_valor = calcular_valor_total(bolsa)
print(f"Valor total das ações na bolsa: ${total_valor:.2f}")

visualizar_acoes_acima_valor(bolsa, 1000.0)
