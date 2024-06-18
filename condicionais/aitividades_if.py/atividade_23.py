###
# atividade 23
# aluno: ernandes
# data: 15/04/2024
###

def classificarcat(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    else:
        return "Sênior"
    
idade = int(input("Digite a idade do atleta: "))

categoria = classificarcat(idade)
print("O atleta pertence à categoria:", categoria)
