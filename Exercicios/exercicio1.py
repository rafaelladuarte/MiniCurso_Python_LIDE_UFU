'''
--------------------------------------------------------------------------------
Exercício 1 : Calculadora de Juros Compostos
--------------------------------------------------------------------------------
Escreva um programa Python que permite ao usuário calcular o montante final após
um período de investimento com juros compostos. O programa deve realizar o
seguinte:

1. Solicitar ao usuário que insira o principal (o valor inicial do investimento).
2. Solicitar ao usuário que insira a taxa de juros anual (em porcentagem).
3. Solicitar ao usuário que insira o número de anos que deseja investir.
4. Use operadores aritméticos para calcular o montante final com juros
compostos usando a fórmula:

    M = C * (1 + i) ^ n

5. Exiba o montante final calculado para o usuário.

* Lembre-se de usar operadores aritméticos para calcular a diferença entre datas e
horas. Você pode usar o módulo datetime para facilitar a manipulação de datas e
horas em Python.
'''

# Solicitar ao usuário informações de investimento
print("Calculadora de Juros Compostos")
print("-------------------------------")

principal = float(input("Digite o principal (valor inicial do investimento): "))
taxa_juros = float(input("Digite a taxa de juros anual (em porcentagem): "))
anos = int(input("Digite o número de anos de investimento: "))

# Calcular o montante final com juros compostos
taxa_decimal = taxa_juros / 100
montante_final = principal * (1 + taxa_decimal) ** anos

# Exibir o montante final
print(f"O montante final após {anos} anos será: R$ {montante_final:.2f}")
