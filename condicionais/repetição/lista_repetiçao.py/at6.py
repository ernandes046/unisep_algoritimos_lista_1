
soma = 0
contador = 0

for i in range(10):
    valor = int(input("Digite o {}º valor positivo: ".format(i + 1)))
    if valor > 0:
        soma += valor
        contador += 1

if contador > 0:
    media = soma / contador
    print("A média dos valores positivos é:", media)
else:
    print("Nenhum valor positivo foi inserido.")
