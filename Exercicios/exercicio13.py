'''
----------------------------------------------------------------------------------
Exercício 12 : Simulação de Abertura de Contas Bancárias
----------------------------------------------------------------------------------
Você está desenvolvendo um programa para um banco fictício chamado "Banco
Python". O programa deve permitir que o banco abra contas bancárias para clientes
e realizar algumas operações básicas.
Aqui estão as etapas do exercício:
1. Crie as classes Cliente, ContaBancaria e Banco como definidas nos
exemplos anteriores.
2. Implemente uma função no Banco que permita a abertura de uma conta
bancária para um cliente. Essa função deve receber o cliente, o número da
conta e o saldo inicial como argumentos e criar uma nova conta bancária
para o cliente.
3. Implemente uma função no Banco que liste todos os clientes com suas
informações básicas (nome e sobrenome).
4. Implemente uma função no Banco que permita realizar um depósito em uma
conta bancária. A função deve receber o número da conta e o valor do
depósito como argumentos e atualizar o saldo da conta correspondente.
5. Implemente uma função no Banco que permita realizar um saque em uma
conta bancária. A função deve receber o número da conta e o valor do saque
como argumentos, verificar se há saldo suficiente e atualizar o saldo da conta
correspondente.
'''

class Cliente:
    def __init__(self, nome, sobrenome, endereco, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.telefone = telefone
        self.contas = []

    def calcular_idade(self, ano_nascimento):
        ano_atual = 2023
        idade = ano_atual - ano_nascimento

        return idade


class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.historico_transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico_transacoes.append(f"Depósito de R$ {valor:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico_transacoes.append(f"Saque de R$ {valor:.2f}")
        else:
            print("Saldo insuficiente.")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def criar_conta(self, cliente, numero_conta, saldo_inicial):
        conta = ContaBancaria(numero_conta, saldo_inicial)
        cliente.contas.append(conta)
        print(f"Conta criada para {cliente.nome} {cliente.sobrenome} - Número da conta: {numero_conta}")

    def listar_clientes(self):
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome} {cliente.sobrenome}")

    def depositar(self, numero_conta, valor):
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    conta.depositar(valor)
                    print(f"Depósito de R$ {valor:.2f} na conta {numero_conta} de {cliente.nome} {cliente.sobrenome}")
                    return
        print("Conta não encontrada.")

    def sacar(self, numero_conta, valor):
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    conta.sacar(valor)
                    print(f"Saque de R$ {valor:.2f} da conta {numero_conta} de {cliente.nome} {cliente.sobrenome}")
                    return
        print("Conta não encontrada.")


# Criar clientes
cliente1 = Cliente("João", "Silva", "123 Rua Principal", "123-456-7890")
cliente2 = Cliente("Maria", "Santos", "456 Rua Secundária", "987-654-3210")

# Criar banco
banco = Banco("Banco Python")

# Adicionar clientes ao banco
banco.clientes.append(cliente1)
banco.clientes.append(cliente2)

# Listar clientes antes de abrir contas
print("\nLista de clientes antes de abrir contas:")
banco.listar_clientes()

# Abrir contas bancárias
banco.criar_conta(cliente1, "12345", 1000.0)
banco.criar_conta(cliente2, "67890", 500.0)

# Listar clientes depois de abrir contas
print("\nLista de clientes depois de abrir contas:")
banco.listar_clientes()

# Realizar operações
banco.depositar("12345", 500.0)
banco.sacar("67890", 200.0)