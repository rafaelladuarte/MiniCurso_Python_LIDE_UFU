'''
----------------------------------------------------------------------------------
Exercício 12 : Cálculo de Valor Futuro de Investimento
---------------------------------------------------------------------------------
Você está desenvolvendo uma calculadora de investimentos que permitirá aos
usuários calcular o valor futuro de um investimento com base em informações
fornecidas. O programa deve importar o módulo math para realizar cálculos
financeiros.
Aqui estão as etapas do exercício:

1. Importe o módulo math para usar a função pow() que calcula potências.
2. Solicite ao usuário que insira o capital inicial (o valor que está sendo
investido), a taxa de juros anual (em porcentagem) e o número de anos para
o investimento.
3. Converta a taxa de juros anual em uma taxa de juros decimal, dividindo-a por
100.
4. Use a fórmula do valor futuro do investimento para calcular o valor futuro:

    valor_futuro = capital_inicial * (1 + taxa_juros) ** num_anos

5. Exiba o valor futuro calculado.
'''

import math

# Solicita informações do usuário
capital_inicial = float(input("Digite o valor do capital inicial em reais: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual em porcentagem: "))
num_anos = int(input("Digite o número de anos para o investimento: "))

# Converte a taxa de juros anual em taxa de juros decimal
taxa_juros = taxa_juros_anual / 100

# Calcula o valor futuro do investimento
valor_futuro = capital_inicial * math.pow(1 + taxa_juros, num_anos)

# Exibe o valor futuro
print(f"O valor futuro do investimento será de R$ {valor_futuro:.2f}")
