## atividade 36
# aluno: ernandes
# data: 31/03/2024
###
num = int(input("digite um numero inteiro de 4 digitos (entre 1000 e 9999):"))

if 1000 <= num <= 9999:
    milh = num // 1000
    cent = (num // 100) % 10
    dez = (num // 10) % 10
    uni = num % 10

    print(milh)
    print(cent)
    print(dez)
    print(uni)

else:
    print("o numero inserido e invalido.")


