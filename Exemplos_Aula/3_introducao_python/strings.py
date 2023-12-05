# Funções Built-in para Strings em Python

# Exemplo 1: Concatenação de strings
nome = "Rafaella"
sobrenome = str(input('Digite o seu sobrenome: '))
nome_completo = nome + " " + sobrenome
print(nome_completo)

# Exemplo 2: Comprimento de uma string
texto = "Hello World!"
tamanho = len(texto)
print("O tamanho da string é:", tamanho)

# Exemplo 3: Maiúsculas e minúsculas
frase = "Economia é o melhor curso do Mundo"
maiusculas = frase.upper()
minusculas = frase.lower()
print(maiusculas)
print(minusculas)

# Exemplo 4: Substituição de caracteres
nova_frase = frase.replace("Economia", "")
print(nova_frase)

# Exemplo 5: Divisão de strings
frase = "Python é uma linguagem de programação."
palavras = frase.split(" ")
print(palavras)

# Exemplo 6: Verificação de prefixo e sufixo
texto = "Bem-vindo ao mundo do Python"
tem_prefixo = texto.startswith("Bem")
tem_sufixo = texto.endswith("Python")
print(tem_prefixo)  # Saída: True
print(tem_sufixo)   # Saída: True
