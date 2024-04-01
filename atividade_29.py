###
# atividade 29
# aluno: ernandes
# data: 31/03/2024
###
diat = float(input("digite o numero de dias trabalhados"))

vd = 30.00
sb = vd * diat
desp = 0.11 * sb
desir = 0.08 * sb
sl = sb - desp - desir

print("o salario limpo para o encanador sera de ",(sl))
