import calculos

# Usando as funções do módulo calculos
valor_inicial = 1000
taxa = 5
tempo = 3

juros_simples = calculos.calcular_juros_simples(valor_inicial, taxa, tempo)
juros_compostos = calculos.calcular_juros_compostos(valor_inicial, taxa, tempo)

print(f"Juros Simples: {juros_simples:.2f}")
print(f"Juros Compostos: {juros_compostos:.2f}")
