# Exemplo de Estruturas Condicionais em Economia

# Exemplo 1: Verificação de Lucro
lucro_anual = 50000  # Lucro anual da empresa em dólares
meta_lucro = 60000  # Meta de lucro anual em dólares

if lucro_anual >= meta_lucro:
    print("A empresa atingiu a meta de lucro.")
else:
    diferenca = meta_lucro - lucro_anual
    print(f"A empresa não atingiu a meta de lucro. Faltam {diferenca} dólares para atingir a meta.")

# Exemplo 2: Classificação de Rendimento
renda_mensal = 4000  # Renda mensal de um indivíduo em dólares

if renda_mensal >= 5000:
    print("Alto rendimento.")
elif renda_mensal >= 3000:
    print("Rendimento médio.")
else:
    print("Baixo rendimento.")

# Exemplo 3: Tomada de Decisão de Investimento
taxa_retorno = 0.08  # Taxa de retorno (8%) do investimento
prazo = 5  # Prazo do investimento em anos

if taxa_retorno >= 0.1:
    print("Investimento de alto risco.")
elif prazo < 5:
    print("Investimento de curto prazo.")
else:
    print("Investimento recomendado.")
