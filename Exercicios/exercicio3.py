'''
--------------------------------------------------------------------------------
Exercício 3: Avaliação de Investimento
--------------------------------------------------------------------------------
Suponha que você é um consultor financeiro e deseja criar um programa em Python
para ajudar seus clientes a avaliar se um investimento é viável. O programa deve
realizar o seguinte:

1. Solicitar ao usuário que insira o valor do investimento inicial.
2. Solicitar ao usuário que insira o valor do retorno anual esperado (em
porcentagem).
3. Solicitar ao usuário que insira o período de investimento em anos.
4. Solicitar ao usuário que insira o valor mínimo de retorno desejado (em
porcentagem).
5. Use operadores relacionais para verificar se o investimento atinge ou supera
o valor mínimo de retorno desejado durante o período de investimento.
6. Use operadores lógicos and, or e not para combinar as verificações de
retorno anual esperado e período de investimento.
7. Exibir uma mensagem indicando se o investimento é viável de acordo com os
critérios definidos.
'''

# Solicitar ao usuário informações do investimento
print("Avaliação de Investimento")
print("-------------------------")
investimento_inicial = float(
    input("Digite o valor do investimento inicial: ")
)
retorno_anual_esperado = float(
    input("Digite o retorno anual esperado (em porcentagem): ")
)
periodo_investimento = int(
    input("Digite o período de investimento em anos: ")
)
retorno_minimo_desejado = float(
    input("Digite o valor mínimo de retorno desejado (em porcentagem): ")
)

# Verificar se o investimento é viável com base nos critérios usando operadores lógicos
viavel = (
    retorno_anual_esperado >= retorno_minimo_desejado
    ) and (periodo_investimento >= 1)

# Exibir mensagem de viabilidade do investimento
if viavel:
    print(
        "O investimento é viável, pois atinge o retorno desejado de",
        retorno_minimo_desejado,
        "% ou mais durante o período de",
        periodo_investimento, "anos."
    )
else:
    print("O investimento não atinge os critérios de viabilidade estabelecidos.")
