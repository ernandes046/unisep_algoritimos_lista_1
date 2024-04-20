###
# atividade 15
# aluno: ernandes
# data: 15/04/2024
###
def obter_nome_mes(numero):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    return meses.get(numero, "Mês inválido")

def main():
    numero = int(input("Digite um número entre 1 e 12: "))
    
    nome_mes = obter_nome_mes(numero)
    print("Mês correspondente:", nome_mes)

if __name__ == "__main__":
    main()

