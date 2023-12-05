# Exemplos de Operadores Aritméticos em Python

# Exemplo 1: Cálculo de Lucro
receita = 10000  # Receita de uma empresa em dólares
custo = 7000     # Custo operacional em dólares
lucro = receita - custo
print(f"O lucro da empresa é de ${lucro}.")

# Exemplo 2: Cálculo de Imposto de Renda
renda_anual = 80000  # Renda anual de uma pessoa em dólares
taxa_imposto = 0.25  # Taxa de imposto de renda
imposto_de_renda = renda_anual * taxa_imposto
print(f"O imposto de renda anual é de ${imposto_de_renda}.")

# Exemplo 3: Cálculo de Inflação
indice_inflacao = 0.03  # Índice de inflação (3%)
preco_inicial = 100     # Preço inicial de um produto em dólares
preco_final = preco_inicial * (1 + indice_inflacao)
print(f"O preço final do produto após a inflação é de ${preco_final}.")

# Exemplo 4: Cálculo de Juros Simples
capital = 1000   # Capital inicial em dólares
taxa_juros = 0.05  # Taxa de juros (5%) por ano
tempo = 3        # Tempo em anos
juros_simples = capital * taxa_juros * tempo
print(f"Os juros simples após {tempo} anos são de ${juros_simples}.")

# Exemplo 5: Cálculo de Crescimento Percentual
populacao_anterior = 5000   # População de uma cidade no ano anterior
populacao_atual = 5500      # População atual da cidade
crescimento_percentual = (
    (populacao_atual - populacao_anterior) / populacao_anterior
) * 100
print(f"O crescimento populacional foi de {crescimento_percentual}%.")

# Exemplo 6: Cálculo de Valor Futuro
valor_presente = 1000   # Valor presente de um investimento em dólares
taxa_juros = 0.08       # Taxa de juros (8%) por ano
tempo = 5               # Tempo em anos
valor_futuro = valor_presente * (1 + taxa_juros) ** tempo
print(f"O valor futuro do investimento após {tempo} anos é de ${valor_futuro:.2f}.")
