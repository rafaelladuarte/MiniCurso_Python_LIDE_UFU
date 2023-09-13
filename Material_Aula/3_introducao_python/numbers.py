# Funções Built-in para Números em Python

# Exemplo 1: Valor absoluto
numero = -5
valor_absoluto = abs(numero)
print(f"Valor absoluto: {valor_absoluto}")

# Exemplo 2: Conversão para int e float
texto = "123"
numero_inteiro = int(texto)
numero_ponto_flutuante = float(texto)
print(f"Número Inteiro: {numero_inteiro}")
print(f"Número de Ponto Flutuante: {numero_ponto_flutuante}")

# Exemplo 3: Máximo e Mínimo
numeros = [10, 5, 8, 15, 3]
maximo = max(numeros)
minimo = min(numeros)
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# Exemplo 4: Potência
base = 2
expoente = 3
resultado = pow(base, expoente)
print(f"Potência: {resultado}")

# Exemplo 5: Arredondamento
numero = 3.14159
arredondado_inteiro = round(numero)
arredondado_decimal = round(numero, 2)
print(f"Arredondado para Inteiro: {arredondado_inteiro}")
print(f"Arredondado para 2 casas decimais: {arredondado_decimal}")

# Exemplo 6: Soma de números
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print(f"Soma dos Números: {soma}")
