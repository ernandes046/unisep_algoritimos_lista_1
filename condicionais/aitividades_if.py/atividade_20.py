###
# atividade 20
# aluno: ernandes
# data: 15/04/2024
###

idade = int(input("Digite a idade do trabalhador: "))
temposerv = int(input("Digite o tempo de serviço do trabalhador (em anos): "))

def verificar_aposentadoria(idade, temposerv):
    if idade >= 65 or temposerv >= 30 or (idade >= 60 and temposerv >= 25):
        return "O trabalhador pode se aposentar."
    else:
        return "O trabalhador ainda não pode se aposentar."

print(verificar_aposentadoria(idade, temposerv))
