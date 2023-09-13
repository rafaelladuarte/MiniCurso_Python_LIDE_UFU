'''
--------------------------------------------------------------------------------
Exercício 4: Atualização de Saldo em Conta Bancária
--------------------------------------------------------------------------------
Imagine que você está desenvolvendo um sistema bancário simples em Python.
Você precisa escrever um programa que permita ao usuário realizar operações de
depósito e saque em sua conta bancária, atualizando o saldo disponível. Use os
operadores de atribuição para realizar as operações.
O programa deve fazer o seguinte:

1. Inicialize uma variável chamada saldo com um valor inicial, por exemplo, R$
1000.
2. Solicite ao usuário que escolha a operação desejada (depósito ou saque).
3. Solicite ao usuário que insira o valor da operação.
4. Use operadores de atribuição para atualizar o saldo com base na escolha do
usuário (adicionar o valor ao saldo para depósito ou subtrair o valor para
saque).
5. Exiba o saldo atualizado.
'''

# Inicializar o saldo
# Valor inicial
saldo = 1000

# Exibir o saldo atual
print("Sistema Bancário Simples")
print("-------------------------")
print("Seu saldo atual é: R$", saldo)

# Solicitar ao usuário a operação desejada
print("\nEscolha a operação desejada:")
print("1. Depósito")
print("2. Saque")

opcao = int(input("Opção: "))

# Realizar a operação escolhida
if opcao == 1:
    # Depósito
    valor_deposito = float(input("Digite o valor do depósito: "))
    saldo += valor_deposito
    print("\nDepósito realizado com sucesso!")
elif opcao == 2:
    # Saque
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque <= saldo:
        saldo -= valor_saque
        print("\nSaque realizado com sucesso!")
    else:
        print("\nSaldo insuficiente para o saque.")
else:
    print("\nOpção inválida.")

# Exibir o saldo atualizado
print("\nSeu saldo atual é: R$", saldo)
