###
# atividade 6
# aluno: ernandes
# data: 08/04/2024
###
num1 = float(input("digite o primeiro numero; "))
num2 = float(input("digite o segundo numero: "))

def encontar_maior(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Números iguais"

result = encontar_maior(num1,num2)
print("o maior numero e: ",result)




