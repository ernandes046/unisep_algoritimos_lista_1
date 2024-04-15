###
# atividade 6
# aluno: ernandes
# data: 08/04/2024
###

num1 = float(input("insira um numero inteiro: "))
num2 = float(input("insira o segundo numero inteiro"))

if num1>num2:
    print(f"o numero {num1} e maior que o numero {num2}")
    dif = num1 - num2
    print(f"a diferença de ambos e {dif}")
else:
    print(f"o numero {num2} e maior que o numero {num1}")
    dif = num1 - num2
    print(f"a diferença de ambos e {dif}")
