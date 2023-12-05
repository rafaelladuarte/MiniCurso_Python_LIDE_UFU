'''
--------------------------------------------------------------------------------
Exercício 5 : Cálculo do Valor Presente Líquido (VPL)
--------------------------------------------------------------------------------
Suponha que você deseje calcular o Valor Presente Líquido (VPL) de um projeto de
investimento e determinar se o projeto é viável ou não com base no VPL calculado.
O programa deve realizar o seguinte:

1. Solicitar ao usuário que insira a taxa de desconto anual (em porcentagem).
2. Solicitar ao usuário que insira o número de períodos de investimento.
3. Solicitar ao usuário que insira os fluxos de caixa futuros para cada período de
investimento (recebimentos ou desembolsos).
4. Use um loop for para calcular o VPL do projeto com base na fórmula:

    VPL = Somatoria( (F * Ct)/(1 + i)^t )

5. Implemente uma estrutura condicional para verificar se o projeto é viável ou
não. Se o VPL for positivo, exiba uma mensagem de projeto viável. Caso
contrário, exiba uma mensagem de projeto não viável.
'''

# Solicitar ao usuário informações do projeto de investimento
print("-------------------------------------")
print("Calculo do Valor Presente Líquido (VPL)")
print("-------------------------------------")

taxa_desconto = float(
    input("Digite a taxa de desconto anual (em porcentagem): ")
)
periodos = int(
    input("Digite o número de períodos de investimento: ")
)
fluxos_de_caixa = []

# Solicitar ao usuário os fluxos de caixa para cada período
for periodo in range(1, periodos + 1):
    fluxo = float(
        input(f"Digite o fluxo de caixa para o período {periodo}: ")
    )
    fluxos_de_caixa.append(fluxo)

# Calcular o VPL do projeto usando um loop for
vpl = 0
for periodo, fluxo in enumerate(fluxos_de_caixa, start=1):
    vpl += fluxo / ((1 + taxa_desconto / 100) ** periodo)

    # Verificar se o projeto é viável com base no VPL calculado
    if vpl > 0:
        print("O projeto é viável!")
        print(f"O Valor Presente Líquido (VPL) do projeto é: R$ {vpl:.2f}")
    else:
        print("O projeto não é viável.")
        print(f"O Valor Presente Líquido (VPL) do projeto é: R$ {vpl:.2f}")
