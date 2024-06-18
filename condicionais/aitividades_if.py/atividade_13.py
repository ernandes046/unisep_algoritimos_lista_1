###
# atividade 13
# aluno: ernandes
# data: 15/04/2024
###
def calcular_nota_final(notalab, notasemestral, notaexame):
    
    media = (notalab * 2 + notasemestral * 3 + notaexame * 5) / 10
    return media

def verificar_situacao(media):
    if media < 3.0:
        return "Reprovado"
    elif media < 5.0:
        return "Recuperação"
    else:
        return "Aprovado"

def main():
    
    notalab = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
    notasemestral = float(input("Digite a nota da prova semestral (0 a 10): "))
    notaexame = float(input("Digite a nota final (0 a 10): "))
    
    
    media = calcular_nota_final(notalab, notasemestral, notaexame)
    
    situacao = verificar_situacao(media)
    
    print(f"A nota final do aluno é: {media:.2f}")
    print("Situação do aluno:", situacao)

if __name__ == "__main__":
    main()
