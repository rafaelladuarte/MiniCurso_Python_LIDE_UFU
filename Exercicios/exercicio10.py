'''
----------------------------------------------------------------------------
Exercício 9: Análise de Taxas de Câmbio
-----------------------------------------------------------------------------
Suponha que você está desenvolvendo um programa para analisar as taxas de
câmbio de diferentes moedas em relação a uma moeda de referência. Você precisa
armazenar essas taxas de câmbio em uma tupla e em um conjunto para realizar
análises.
Aqui estão as etapas do exercício:

1. Crie uma tupla chamada taxas_cambio que contenha as taxas de câmbio de
diferentes moedas em relação a uma moeda de referência (por exemplo,
dólar dos EUA). Você pode definir as taxas como valores de ponto flutuante.
2. Crie um conjunto chamado moedas que contenha as siglas das moedas para
as quais você tem taxas de câmbio. As siglas das moedas podem ser strings.
3. Exiba a lista de moedas disponíveis para análise.
4. Permita que o usuário insira o nome de uma moeda para consultar sua taxa
de câmbio. Use uma estrutura condicional para verificar se a moeda está na
lista de moedas e, se estiver, exiba a taxa de câmbio correspondente da
tupla.
5. Calcule e exiba a média das taxas de câmbio contidas na tupla.
6. Use um conjunto para identificar moedas com taxas de câmbio duplicadas na
tupla e exiba essas moedas.
7. Permita que o usuário insira uma nova taxa de câmbio para uma moeda
específica e adicione essa taxa à tupla e à lista de moedas no conjunto.
8. Exiba a lista atualizada de moedas disponíveis para análise e a tupla de
taxas de câmbio atualizada.
'''

# Tupla de taxas de câmbio
taxas_cambio = (5.25, 0.82, 110.75, 0.71, 0.62)

# Conjunto de moedas disponíveis
moedas = {'USD', 'EUR', 'JPY', 'GBP', 'AUD'}
print("Moedas disponíveis para análise:")
for moeda in moedas:
    print(moeda)

consulta_moeda = input("Digite a sigla da moeda para consultar a taxa de câmbio: ")
if consulta_moeda in moedas:
    indice = moedas.index(consulta_moeda)
    taxa = taxas_cambio[indice]
    print(f"A taxa de câmbio para {consulta_moeda} é {taxa:.2f}")
else:
    print("Moeda não encontrada.")

media_taxas = sum(taxas_cambio) / len(taxas_cambio)
print(f"A média das taxas de câmbio é {media_taxas:.2f}")

moedas_duplicadas = {
    moeda for moeda in moedas
    if taxas_cambio.count(taxas_cambio[moedas.index(moeda)]) > 1
}

print("Moedas com taxas de câmbio duplicadas:", moedas_duplicadas)
nova_moeda = input("Digite a sigla de uma nova moeda: ")
nova_taxa = float(input("Digite a taxa de câmbio para a nova moeda: "))

taxas_cambio = taxas_cambio + (nova_taxa,)
moedas.add(nova_moeda)

print("Moedas disponíveis para análise (atualizado):")
for moeda in moedas:
    print(moeda)

print("Taxas de câmbio (atualizado):", taxas_cambio)