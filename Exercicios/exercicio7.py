'''
--------------------------------------------------------------------------------
Exercício 7: Monitoramento de Preços de Ações na Bolsa de Valores
--------------------------------------------------------------------------------
Você está desenvolvendo um programa de monitoramento de preços de ações na
bolsa de valores. O programa deve permitir que os usuários escolham uma ação
específica e um preço-alvo. O programa continuará rodando indefinidamente,
verificando se o preço da ação atingiu ou ultrapassou o preço-alvo.
Aqui estão as etapas do exercício:

1. Crie um loop while True que continuará rodando indefinidamente.
2. Solicite ao usuário que insira o nome de uma ação (por exemplo, "AAPL"
para a Apple) e o preço-alvo desejado.
3. Dentro do loop, simule a obtenção do preço atual da ação a partir de uma
fonte fictícia (você pode gerar um preço aleatório para simular isso).
4. Verifique se o preço da ação atingiu ou ultrapassou o preço-alvo. Se isso
acontecer, exiba uma mensagem informando que o preço-alvo foi alcançado
e encerre o programa.
5. Se o preço-alvo não foi alcançado, continue o loop e repita a verificação em
intervalos regulares (por exemplo, a cada 10 segundos).
'''

import random
import time

print("Monitoramento de Preços de Ações na Bolsa de Valores")
while True:
    acao = input("Digite o nome da ação (ex: AAPL): ")
    preco_alvo = float(input("Digite o preço-alvo: "))
    while True:
        # Simule a obtenção do preço atual da ação (valor aleatório entre 100 e 200)
        preco_atual = random.uniform(100, 200)
        print(f"Preço atual da ação {acao}: R$ {preco_atual:.2f}")
        if preco_atual >= preco_alvo:
            print(f"O preço da ação {acao} atingiu ou ultrapassou o preço-alvo de R$ {preco_alvo:.2f}!")
            break
    # Espere 10 segundos antes de verificar novamente#
    time.sleep(10)
