###
# atividade 18
# aluno: ernandes
# data: 30/03/2024
###
g1 = int(input("digite a nota da prova 1:" ))

g2 = int(input("digite a nota da prova 2:"))

media = g1 + (g2*2) / 3
if media >=7.0:
    print(f"voce foi aprovado", {media})

else:
    print(f"voce nao foi aprovado", {media})