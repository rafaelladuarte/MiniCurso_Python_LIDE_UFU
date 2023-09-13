'''
--------------------------------------------------------------------------------
Exercício 2 : Calculadora de Empréstimos
--------------------------------------------------------------------------------
Você está desenvolvendo uma calculadora de empréstimos para ajudar as pessoas
a entenderem os pagamentos mensais de um empréstimo. O programa deve
solicitar as informações do empréstimo e calcular o pagamento mensal.
Aqui estão as etapas do exercício:

1. Solicite ao usuário o valor do empréstimo (em reais), a taxa de juros anual
(em porcentagem) e o número de meses para o pagamento.
2. Converta a taxa de juros anual em uma taxa de juros mensal, dividindo-a por
12 e por 100.
3. Use a fórmula de pagamento mensal de empréstimo para calcular o
pagamento mensal:

pagamento_mensal = (valor_emprestimo * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_meses)

4. Exiba o pagamento mensal calculado.
5. Verifique se o pagamento mensal é maior do que o valor mínimo viável para o
solicitante do empréstimo. Se for, exiba uma mensagem informando que o
pagamento é aceitável. Caso contrário, informe que o pagamento é muito alto
e pode não ser adequado para o solicitante.
'''

valor_emprestimo = float(input("Digite o valor do empréstimo em reais: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual em porcentagem: "))
num_meses = int(input("Digite o número de meses para o pagamento:"))

# Converte a taxa de juros anual em uma taxa mensal
taxa_juros_mensal = (taxa_juros_anual / 12) / 100

# Calcula o pagamento mensal usando a fórmula
pagamento_mensal = (valor_emprestimo * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_meses)
print(f"O pagamento mensal é de R$ {pagamento_mensal:.2f}")

# Verifica se o pagamento mensal é viável para o solicitante
pagamento_minimo = 1000 # Define um valor mínimo viável
if pagamento_mensal <= pagamento_minimo:
    print("O pagamento é aceitável.")
else:
    print("O pagamento é muito alto e pode não ser adequado para o solicitante.")