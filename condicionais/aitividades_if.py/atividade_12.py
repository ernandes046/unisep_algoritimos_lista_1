###
# atividade 12
# aluno: ernandes
# data: 15/04/2024
###
def calcular_media(nota1, nota2):

    media = (nota1 * 1 + nota2 * 2) / 3
    return media

def verificar_aprovacao(media):

    if media >= 70:
        return "Aprovado"
    else:
        return "Reprovado"


def main():
    
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    
    
    media = calcular_media(nota1, nota2)
    
    situacao = verificar_aprovacao(media)
    
    print(f"A média do aluno é: {media:.2f}")
    print("Situação do aluno:", situacao)

if __name__ == "__main__":
    main()
