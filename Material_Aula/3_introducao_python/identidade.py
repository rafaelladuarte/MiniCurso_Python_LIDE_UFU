# Exemplos de Operadores de Identidade em Economia

# Exemplo 1: Comparação de Objetos
transacao1 = ["compra", 1000]
transacao2 = ["compra", 1000]

mesma_transacao = transacao1 is transacao2
print(f"São a mesma transação? {mesma_transacao}")

# Exemplo 2: Verificando se um objeto é None
saldo_conta = None
conta_ativa = saldo_conta is not None
print(f"A conta está ativa? {conta_ativa}")

# Exemplo 3: Comparação de Listas
carteira_atual = ["ações", "títulos", "imóveis"]
outra_carteira = carteira_atual

mesma_carteira = carteira_atual is outra_carteira
print(f"São a mesma carteira? {mesma_carteira}")

# Exemplo 4: Verificando se um objeto não é None
investimento = 5000
investimento_valido = investimento is not None
print(f"O investimento é válido? {investimento_valido}")
