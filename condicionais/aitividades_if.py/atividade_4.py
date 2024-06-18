###
# atividade 4
# aluno: ernandes
# data: 08/04/2024
###
import math

num = float(input("informe um numero: "))

if num>=0:
    qua = num * num 
    raiz = math.sqrt(num)
    print(f"o quadrado de {num} e {qua}")
    print(f"a raiz de {num} e {raiz}")
else:
    print("numero invalido")
