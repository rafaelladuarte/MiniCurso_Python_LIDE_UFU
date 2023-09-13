'''
----------------------------------------------------------------------------------
Exercício 14 : Analise de Investimentos para Aposentadoria
----------------------------------------------------------------------------------
Você está desenvolvendo uma calculadora de investimentos para ajudar as pessoas
a planejar sua aposentadoria. O programa deve permitir que os usuários insiram
informações sobre suas contribuições de aposentadoria, taxa de retorno anual e
número de anos de investimento, e calcular o valor futuro de seus investimentos.
Aqui estão as etapas do exercício:

1. Crie uma classe chamada PlanoAposentadoria que representará o plano de
aposentadoria de um indivíduo. Essa classe deve conter os seguintes
métodos:
    ● __init__: Inicializa o plano com informações como idade atual, idade de
aposentadoria desejada, contribuição anual e taxa de retorno anual
esperada.
    ● calcular_valor_futuro: Calcula o valor futuro do investimento para a
aposentadoria usando a fórmula de juros compostos: FV = PV * (1 + r)^n,
onde FV é o valor futuro, PV é a contribuição anual, r é a taxa de retorno
anual e n é o número de anos de investimento.
2. Implemente um programa principal que permite ao usuário criar um plano de
aposentadoria, inserir informações como idade atual, idade de aposentadoria
desejada, contribuição anual e taxa de retorno anual. O programa deve então
calcular e exibir o valor futuro estimado para a aposentadoria.
'''


class PlanoAposentadoria:
    def __init__(
        self, 
        idade_atual, 
        idade_aposentadoria,
        contribuicao_anual,
        taxa_retorno_anual
    ):
        self.idade_atual = idade_atual
        self.idade_aposentadoria = idade_aposentadoria
        self.contribuicao_anual = contribuicao_anual
        # Converta a taxa de porcentagem para decimal
        self.taxa_retorno_anual = taxa_retorno_anual / 100
    
    def calcular_valor_futuro(self, anos):
        valor_futuro = self.contribuicao_anual * (1 + self.taxa_retorno_anual) ** anos
        return valor_futuro


# Programa principal
print("Calculadora de Aposentadoria")
print("-"*10)

idade_atual = int(input("Idade atual: "))
idade_aposentadoria = int(input("Idade desejada para aposentadoria: "))
contribuicao_anual = float(input("Contribuição anual: R$ "))
taxa_retorno_anual = float(input("Taxa de retorno anual (em %): "))

plano = PlanoAposentadoria(
    idade_atual=idade_atual,
    idade_aposentadoria=idade_aposentadoria,
    contribuicao_anual=contribuicao_anual,
    taxa_retorno_anual=taxa_retorno_anual
)

anos_de_investimento = idade_aposentadoria - idade_atual
valor_futuro = plano.calcular_valor_futuro(anos_de_investimento)

print(f"O valor estimado para a aposentadoria será de R$ {valor_futuro:.2f}")