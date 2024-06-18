## atividade 35
# aluno: ernandes
# data: 31/03/2024
###
num = int(input("digite tres numeros interios de (entre 100 e 999):"))

if 100 <= num <= 999:
    cent = num // 100
    dez = (num // 10) % 10
    uni = num % 10

    inve = uni * 100 + dez * 10 + cent 

    print("o numero invertido e:",(inve)) 
else:
    print("o numero e invalido")
