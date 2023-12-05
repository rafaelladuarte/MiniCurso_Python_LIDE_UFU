# Exemplos de Funções Built-in para Tuplas em Economia

# Suponha que você está trabalhando com uma tupla de informações financeiras.

informacoes_financeiras = (2023, 'Janeiro', 3500.0, 2800.0, 700.0)

# Exemplo 1: Acessando Elementos da Tupla
ano = informacoes_financeiras[0]  # Acessa o primeiro elemento (ano)
mes = informacoes_financeiras[1]  # Acessa o segundo elemento (mês)
receita = informacoes_financeiras[2]  # Acessa o terceiro elemento (receita)
despesas = informacoes_financeiras[3]  # Acessa o quarto elemento (despesas)
lucro = informacoes_financeiras[4]  # Acessa o quinto elemento (lucro)

print(f"Relatório financeiro de {mes} de {ano}:")
print(f"Receita: ${receita:.2f}")
print(f"Despesas: ${despesas:.2f}")
print(f"Lucro: ${lucro:.2f}")

# Exemplo 2: Verificando a Existência de um Valor na Tupla
mes_ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')
mes_procurado = 'Abril'

if mes_procurado in mes_ano:
    print(f"{mes_procurado} está na lista de meses.")
else:
    print(f"{mes_procurado} não está na lista de meses.")

# Exemplo 3: Contando a Ocorrência de um Valor na Tupla
contagem_janeiro = mes_ano.count('Janeiro')  # Conta quantas vezes 'Janeiro' aparece
print(f"Quantidade de 'Janeiro': {contagem_janeiro}")

# Exemplo 4: Encontrando o Índice de um Valor na Tupla
indice_fevereiro = mes_ano.index('Fevereiro')  # Encontra o índice de 'Fevereiro'
print(f"Índice de 'Fevereiro': {indice_fevereiro}")
