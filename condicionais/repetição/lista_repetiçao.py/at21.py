

def eh_par(numero):
    return numero % 2 == 0


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


menor = min(numero1, numero2)
maior = max(numero1, numero2)

soma_pares = 0
multiplicacao_impares = 1

for numero in range(menor, maior + 1):
    if eh_par(numero):
        soma_pares += numero
    else:
        multiplicacao_impares *= numero

print("a. A soma dos números pares no intervalo de", menor, "a", maior, "é:", soma_pares)
print("b. A multiplicação dos números ímpares no intervalo de", menor, "a", maior, "é:", multiplicacao_impares)
