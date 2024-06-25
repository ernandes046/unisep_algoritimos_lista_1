
soma = 0

for i in range(10):
    valor = int(input("Digite o {}º inteiro: ".format(i + 1)))
    soma += valor

media = soma / 10

print("A média dos 10 inteiros é:", media)
