###
# atividade 21
# aluno: ernandes
# data: 15/04/2024
###

def bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

ano = int(input("Digite um ano para verificar se é bissexto: "))

if bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

