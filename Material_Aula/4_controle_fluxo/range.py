# Exemplos de uso da função range() com start, stop e step

# Usando apenas 'stop'
print("Usando apenas 'stop':")
for i in range(5):
    print(i)
# Saída: 0, 1, 2, 3, 4

# Usando 'start' e 'stop'
print("\nUsando 'start' e 'stop':")
for i in range(2, 8):
    print(i)
# Saída: 2, 3, 4, 5, 6, 7

# Usando 'start', 'stop' e 'step'
print("\nUsando 'start', 'stop' e 'step':")
for i in range(1, 10, 2):
    print(i)
# Saída: 1, 3, 5, 7, 9

# Usando 'start', 'stop' e 'step' em ordem decrescente
print("\nUsando 'start', 'stop' e 'step' em ordem decrescente:")
for i in range(10, 0, -1):
    print(i)
# Saída: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
