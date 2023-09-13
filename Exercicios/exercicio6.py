'''
------------------------------------------------------------------------------
Exercício 6: Simulação de Investimento
------------------------------------------------------------------------------
Suponha que você queira simular o crescimento de um investimento ao longo do
tempo, levando em consideração taxas de juros variáveis. Você deseja saber
quantos anos serão necessários para que o investimento atinja um determinado
11valor alvo ou supere um valor mínimo de retorno. Este é um cenário comum no
mercado financeiro.

1. O programa deve fazer o seguinte:
2. Solicitar ao usuário que insira o valor inicial do investimento.
3. Solicitar ao usuário que insira uma taxa de juros anual (em porcentagem).
4. Solicitar ao usuário que insira um valor alvo (o valor que o investimento deve
alcançar) ou um valor mínimo de retorno.
5. Use um loop while para calcular o crescimento anual do investimento com
base na taxa de juros.
6. Verifique a cada ano se o investimento atingiu ou superou o valor alvo ou o
valor mínimo de retorno. Se isso acontecer, exiba uma mensagem
informando o ano em que isso ocorreu e saia do loop usando break.
7. Continue iterando até que o investimento atinja os critérios desejados.
'''

# Solicitar informações ao usuário
print("Simulação de Investimento")
print("-------------------------")
valor_inicial = float(
    input("Digite o valor inicial do investimento: ")
)
taxa_juros_anual = float(
    input("Digite a taxa de juros anual (em porcentagem): ")
)
valor_alvo = float(
    input("Digite o valor alvo ou mínimo de retorno desejado: ")
)

# Inicializar variáveis
ano = 0
valor_atual = valor_inicial

# Executar o loop while
while valor_atual < valor_alvo:
    ano += 1
    valor_atual *= (1 + taxa_juros_anual / 100)
    # Verificar se o investimento atingiu ou superou o valor alvo
    if valor_atual >= valor_alvo:
        print(f"Em {ano} anos, o investimento atingiu o valor alvo de R$ {valor_atual:.2f}")
        break

# Exibir resultado final
if valor_atual >= valor_alvo:
    print("Investimento bem-sucedido!")
else:
    print("Investimento não atingiu o valor alvo desejado.")
