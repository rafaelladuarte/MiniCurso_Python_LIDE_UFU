# Exemplos de Funções Built-in para Dicionários em Economia

# Suponha que você está trabalhando com informações de empresas em um dicionário.

empresa1 = {
    'nome': 'Empresa A',
    'receita': 500000.0,
    'despesas': 350000.0,
    'lucro': 150000.0
}

empresa2 = {
    'nome': 'Empresa B',
    'receita': 800000.0,
    'despesas': 600000.0,
    'lucro': 200000.0
}

# Exemplo 1: Acessando Valores por Chave
nome_empresa1 = empresa1['nome']  # Acessa o valor da chave 'nome' no dicionário empresa1
print(f"Nome da Empresa 1: {nome_empresa1}")

# Exemplo 2: Verificando se uma Chave Existe
chave_existe = 'funcionarios' in empresa2  # Verifica se a chave 'funcionarios' existe no dicionário empresa2
print(f"A chave 'funcionarios' existe? {chave_existe}")

# Exemplo 3: Obtendo uma Lista de Chaves
chaves_empresa1 = empresa1.keys()  # Obtém uma lista de todas as chaves no dicionário empresa1
print(f"Chaves do dicionário empresa1: {list(chaves_empresa1)}")

# Exemplo 4: Obtendo uma Lista de Valores
valores_empresa2 = empresa2.values()  # Obtém uma lista de todos os valores no dicionário empresa2
print(f"Valores do dicionário empresa2: {list(valores_empresa2)}")

# Exemplo 5: Obtendo Pares Chave-Valor como Tuplas
pares_empresa1 = empresa1.items()  # Obtém uma lista de pares chave-valor como tuplas no dicionário empresa1
print(f"Pares chave-valor do dicionário empresa1: {list(pares_empresa1)}")

# Exemplo 6: Removendo um Par Chave-Valor
empresa2.pop('despesas')  # Remove o par chave-valor com a chave 'despesas' do dicionário empresa2
print("Dicionário empresa2 após a remoção:", empresa2)
