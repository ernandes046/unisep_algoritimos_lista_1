###
# atividade 3 
# aluno: ernandes
# data: 08/04/2024
###

import math

num = float(input("insira um numero real: "))

if num>0:
     raiz = math.sqrt(num)
     print(f"a raiz de {num} e {raiz}")
else:
    qua = num * num
    print(f"o quadrado de {num} e {qua}")
