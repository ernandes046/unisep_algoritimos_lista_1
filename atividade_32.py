### atividade 32
# aluno: ernandes
# data: 31/03/2024
###
def calcular_desconto(valor_total):
    desconto = 0.10 * valor_total
    return valor_total - desconto

def calcular_parcelas(valor_total):
    return valor_total / 3

def calcular_comissao_a_vista(valor_total):
    valor_com_desconto = calcular_desconto(valor_total)
    return 0.05 * valor_com_desconto

def calcular_comissao_parcelada(valor_total):
    return 0.05 * valor_total

def main():
    
    valor_total = float(input("Digite o valor total da compra: R$"))

    valor_com_desconto = calcular_desconto(valor_total)
    print("a. O total a pagar com desconto de 10% é: R$", valor_com_desconto)

    valor_parcela = calcular_parcelas(valor_total)
    print("b. O valor de cada parcela (3x sem juros) é: R$", valor_parcela)

    comissao_a_vista = calcular_comissao_a_vista(valor_total)
    print("c. A comissão do vendedor (à vista) é: R$", comissao_a_vista)

    comissao_parcelada = calcular_comissao_parcelada(valor_total)
    print("d. A comissão do vendedor (parcelada) é: R$", comissao_parcelada)

if __name__ == "__main__":
    main()
