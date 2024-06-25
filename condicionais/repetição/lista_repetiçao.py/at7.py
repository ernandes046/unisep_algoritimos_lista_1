
numeros = []
for i in range(10):
    numero = float(input("Digite o {}º número: ".format(i + 1)))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)

print("O menor valor lido é:", menor)
print("O maior valor lido é:", maior)
