'''
--------------------------------------------------------------------------------
Exercício 8: Gerenciamento de Gastos Mensais
--------------------------------------------------------------------------------
Suponha que você esteja gerenciando seus gastos mensais ao longo de um ano.
Você mantém uma lista de gastos mensais e deseja realizar várias operações com
ela.
Aqui estão as etapas do exercício:

1. Crie uma lista vazia chamada gastos_mensais.
2. Solicite ao usuário que insira os gastos mensais para cada mês do ano
(janeiro a dezembro) usando um loop for e a função append() para adicionar
cada gasto à lista.
3. Calcule o total de gastos ao longo do ano usando a função sum().
4. Solicite ao usuário que insira o número do mês (1 a 12) para acessar os
gastos desse mês específico. Use a entrada do usuário como índice para
acessar o elemento correspondente na lista.
5. Exiba o gasto do mês selecionado.
6. Solicite ao usuário que insira um novo gasto para um mês específico e use a
função insert() para adicionar esse gasto à lista na posição correta (de acordo
com o mês).
7. Exiba a lista atualizada de gastos mensais.
8. Solicite ao usuário que insira um mês para remover o gasto desse mês da 
lista, usando a função pop().
9. Exiba a lista de gastos mensais após a remoção.
'''

# Lista de gastos mensais vazia
gastos_mensais = []
# Solicitar gastos mensais do usuário
for mes in range(1, 13):
    gasto = float(input(f"Digite o gasto de {mes}/2023: "))
    gastos_mensais.append(gasto)

# Calcular o total de gastos
total_gastos = sum(gastos_mensais)

# Solicitar o mês para acessar
mes_acesso = int(input("Digite o número do mês (1 a 12) para acessar os gastos: "))
gasto_mes_acesso = gastos_mensais[mes_acesso - 1]

# Exibir o gasto do mês selecionado
print(f"O gasto do mês {mes_acesso} foi: R$ {gasto_mes_acesso:.2f}")

# Solicitar um novo gasto para um mês específico
novo_gasto = float(input("Digite o novo gasto: "))
mes_novo_gasto = int(
    input("Digite o mês para adicionar o novo gasto (1 a 12): ")
)
gastos_mensais.insert(mes_novo_gasto - 1, novo_gasto)

# Exibir a lista de gastos atualizada
print("Lista de gastos atualizada:")
print(gastos_mensais)

# Solicitar o mês para remover um gasto
mes_remocao = int(input("Digite o mês para remover o gasto: "))
gastos_mensais.pop(mes_remocao - 1)

# Exibir a lista de gastos após a remoção
print("Lista de gastos após a remoção:")
print(gastos_mensais)
