# Exemplo de Loop while com break e continue

# Suponha que você queira imprimir todos os números de 1 a 10, exceto o número 5.

contador = 1

while contador <= 10:
    if contador == 5:
        contador += 1
        continue  # Ignora a iteração atual e vai para a próxima
    elif contador == 8:
        break  # Sai do loop quando atingir o número 8
    print(contador)
    contador += 1
