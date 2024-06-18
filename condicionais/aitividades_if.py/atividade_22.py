###
# atividade 22
# aluno: ernandes
# data: 15/04/2024
###
valor = float(input("Digite o valor do produto: "))
estado = input("Digite a sigla do estado destino do produto (MG, SP, RJ ou MS): ")

def calcularprecofinal(valor, estado):
    if estado.upper() == "MG":
        taxaimposto = 0.07
    elif estado.upper() == "SP":
        taxaimposto = 0.12
    elif estado.upper() == "RJ":
        taxaimposto = 0.15
    elif estado.upper() == "MS":
        taxaimposto = 0.08
    else:
        return "Erro: Estado inválido."

    precofinal = valor * (1 + taxaimposto)
    return precofinal

preco_final = calcularprecofinal(valor, estado)
print("O preço final do produto é R$", preco_final) if isinstance(preco_final, float) else print(preco_final)
