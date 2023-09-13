# Exemplos de Operadores Lógicos em Economia

# Exemplo 1: E (and)
idade = 30
renda_anual = 50000
idade_minima = 18
renda_minima = 40000

elegivel_para_investir = idade >= idade_minima and renda_anual >= renda_minima
print(f"Elegível para investir: {elegivel_para_investir}")

# Exemplo 2: Ou (or)
prazo = 3  # Prazo do investimento em anos
taxa_retorno = 0.07  # Taxa de retorno (7%) do investimento

investir_curto_prazo = prazo < 5 or taxa_retorno > 0.1
print(f"Investir a curto prazo: {investir_curto_prazo}")

# Exemplo 3: Não (not)
tem_inflacao_alta = True
poupanca_ruim = not tem_inflacao_alta
print(f"Poupança é uma opção ruim: {poupanca_ruim}")

# Exemplo 4: Combinação de Operadores Lógicos
renda_liquida_mensal = 5000  # Renda líquida mensal em dólares
gastos_mensais = 3500  # Gastos mensais em dólares

renda_suficiente = (
    renda_liquida_mensal >= gastos_mensais
    ) and not (
    tem_inflacao_alta or idade < 25
)
print(f"Renda é suficiente para investir: {renda_suficiente}")
