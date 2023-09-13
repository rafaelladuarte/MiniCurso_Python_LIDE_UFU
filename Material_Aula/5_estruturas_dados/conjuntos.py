# Exemplos de Funções Built-in para Conjuntos (sets) em Economia

# Suponha que você está trabalhando com conjuntos de produtos.

produtos1 = {'arroz', 'feijão', 'macarrão', 'óleo'}
produtos2 = {'feijão', 'açúcar', 'óleo', 'farinha'}

# Exemplo 1: União de Conjuntos
todos_produtos = produtos1.union(produtos2)  # Combina todos os produtos em um único conjunto
print("Todos os produtos disponíveis:", todos_produtos)

# Exemplo 2: Interseção de Conjuntos
produtos_em_comum = produtos1.intersection(produtos2)  # Encontra produtos em comum entre os conjuntos
print("Produtos em comum:", produtos_em_comum)

# Exemplo 3: Diferença de Conjuntos
produtos_exclusivos = produtos1.difference(produtos2)  # Encontra produtos exclusivos do conjunto 1
print("Produtos exclusivos no conjunto 1:", produtos_exclusivos)

# Exemplo 4: Verificando Subconjuntos
e_subconjunto = produtos1.issubset(produtos2)  # Verifica se produtos1 é subconjunto de produtos2
print("produtos1 é subconjunto de produtos2? ", e_subconjunto)

# Exemplo 5: Adicionando Elementos ao Conjunto
produtos1.add('café')  # Adiciona o produto 'café' ao conjunto produtos1
print("produtos1 após a adição de café:", produtos1)

# Exemplo 6: Removendo Elementos do Conjunto
produtos2.remove('açúcar')  # Remove o produto 'açúcar' do conjunto produtos2
print("produtos2 após a remoção de açúcar:", produtos2)
