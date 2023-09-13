'''
------------------------------------------------------------------------------------
Exercício 11: Analise de Impostos e Receitas de uma Empresa
------------------------------------------------------------------------------------
Você foi contratado como analista financeiro por uma empresa e precisa
desenvolver um programa para analisar sua situação fiscal. O programa deve
calcular o valor total de impostos pagos pela empresa e determinar se ela teve um
lucro ou prejuízo com base nas receitas e despesas.
Aqui estão as etapas do exercício:

1. Crie três listas vazias: receitas, despesas, e impostos.
2. Solicite ao usuário que insira informações sobre receitas, despesas e
impostos repetidamente até que eles escolham parar. Cada item deve ser um
valor numérico.
3. Use uma estrutura de repetição para calcular o total de receitas, o total de
despesas e o total de impostos. As listas devem ter o mesmo tamanho, e
cada índice corresponde ao mesmo mês.
4. Use uma estrutura condicional para determinar se a empresa teve lucro
(receitas maiores que despesas) ou prejuízo (receitas menores que
despesas).
5. Se a empresa teve lucro, calcule o valor do imposto sobre o lucro como 15%
do lucro (receitas - despesas).
6. Se a empresa teve prejuízo, não calcule o imposto.
7. Exiba o total de receitas, o total de despesas, o total de impostos e se a
empresa teve lucro ou prejuízo.
'''

# Listas vazias para receitas, despesas e impostos
receitas = []
despesas = []
impostos = []

while True:
    mes = input("Digite o mês (ou 'parar' para encerrar): ")
    if mes.lower() == 'parar':
        break

    try:
        receita = float(input(f"Digite as receitas para {mes}: R$ "))
        despesa = float(input(f"Digite as despesas para {mes}: R$ "))
        # Calcula o imposto sobre o lucro
        imposto = 0.15 * max(receita - despesa, 0)
    except ValueError:
        print("Valores inválidos. Tente novamente.")
        continue

    receitas.append(receita)
    despesas.append(despesa)
    impostos.append(imposto)

total_receitas = sum(receitas)
total_despesas = sum(despesas)
total_impostos = sum(impostos)

if total_receitas > total_despesas:
    lucro = total_receitas - total_despesas
    print(f"A empresa teve um lucro de R$ {lucro:.2f}.")
    print(f"O total de impostos sobre o lucro é de R$ {total_impostos:.2f}.")
else:
    print("A empresa teve prejuízo.")
    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
