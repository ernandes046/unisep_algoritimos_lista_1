###
# atividade 18
# aluno: ernandes
# data: 15/04/2024
###
def veridiv(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "O número é divisível por 3 e por 5."
    elif numero % 3 == 0:
        return "O número é divisível por 3, mas não por 5."
    elif numero % 5 == 0:
        return "O número é divisível por 5, mas não por 3."
    else:
        return "O número não é divisível por 3 nem por 5."

numero = int(input("Digite um número inteiro: "))
print(veridiv(numero))
