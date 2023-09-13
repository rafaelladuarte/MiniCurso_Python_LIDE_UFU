'''
-----------------------------------------------------------------------------
Exercício 9 : Controle de Despesas Empresariais
-----------------------------------------------------------------------------
Suponha que você está desenvolvendo um programa de controle de despesas para
uma pequena empresa. Você precisa criar um dicionário para armazenar
informações sobre despesas de diferentes categorias. Cada categoria é uma chave
e os valores são listas de despesas.
Aqui estão as etapas do exercício:

1. Crie um dicionário vazio chamado despesas_empresariais.
2. Solicite ao usuário que insira o nome de uma categoria de despesa e o valor
da despesa. Use uma estrutura de repetição para permitir que o usuário
insira várias despesas na mesma categoria. Adicione cada despesa à lista
correspondente no dicionário.
3. Permita que o usuário insira despesas para diferentes categorias, repetindo o
processo de inserção.
4. Após inserir todas as despesas, exiba o total de despesas para cada
categoria.
5. Calcule o total geral de despesas da empresa somando todas as despesas
de todas as categorias.
6. Exiba o total geral de despesas.
7. Permita que o usuário consulte as despesas de uma categoria específica,
digitando o nome da categoria. Mostre as despesas dessa categoria.
8. Permita que o usuário consulte todas as categorias disponíveis e escolha
uma para ver as despesas.
'''

# Dicionário para armazenar despesas empresariais
despesas_empresariais = {}
while True:
    categoria = input("Digite o nome da categoria de despesa (ou'sair' para encerrar): ")
    if categoria.lower() == 'sair':
        break

    if categoria not in despesas_empresariais:
        despesas_empresariais[categoria] = []

    while True:
        try:
            valor = float(input(f"Digite o valor da despesa para '{categoria}': "))
            despesas_empresariais[categoria].append(valor)
        except ValueError:
            print("Valor inválido. Tente novamente.")

        continuar = input("Deseja adicionar outra despesa para esta categoria? (sim/não): ")
        if continuar.lower() != 'sim':
            break

print("\nTotal de despesas por categoria:")
for categoria, despesas in despesas_empresariais.items():
    total_categoria = sum(despesas)
    print(f"{categoria}: R$ {total_categoria:.2f}")

total_geral = sum(sum(despesas) for despesas in despesas_empresariais.values())
print(f"\nTotal geral de despesas da empresa: R$ {total_geral:.2f}")
consulta_categoria = input("Digite o nome de uma categoria para consultar as despesas: ")

if consulta_categoria in despesas_empresariais:
    print(f"Despesas da categoria '{consulta_categoria}':")

    for valor in despesas_empresariais[consulta_categoria]:
        print(f"R$ {valor:.2f}")
else:
    print("Categoria não encontrada.")
    print("\nCategorias disponíveis para consulta:")
    for categoria in despesas_empresariais.keys():
        print(categoria)
