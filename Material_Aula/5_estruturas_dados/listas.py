# Exemplos de Funções Built-in para Listas

# Suponha que você está trabalhando com uma lista de preços de produtos.

precos_produtos = [25.99, 12.49, 9.99, 49.95, 35.0]

# Exemplo 1: Calculando o Total de Preços
total = sum(precos_produtos)  # Soma todos os preços para obter o total
print(f"Total de preços: ${total:.2f}")

# Exemplo 2: Encontrando o Menor e o Maior Preço
preco_minimo = min(precos_produtos)  # Encontra o menor preço
preco_maximo = max(precos_produtos)  # Encontra o maior preço
print(f"Preço mínimo: ${preco_minimo:.2f}")
print(f"Preço máximo: ${preco_maximo:.2f}")

# Exemplo 3: Ordenando a Lista de Preços
precos_produtos.sort()  # Ordena a lista de preços em ordem crescente
print("Preços ordenados:", precos_produtos)

# Exemplo 4: Contando a Ocorrência de um Valor
quantidade_de_produtos = precos_produtos.count(9.99)  # Conta quantas vezes o valor 9.99 aparece
print(f"Quantidade de produtos com preço $9.99: {quantidade_de_produtos}")

# Exemplo 5: Removendo um Valor da Lista
precos_produtos.remove(12.49)  # Remove o preço 12.49 da lista
print("Preços após a remoção:", precos_produtos)
