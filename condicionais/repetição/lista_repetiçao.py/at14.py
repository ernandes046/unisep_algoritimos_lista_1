

while True:
    N = int(input("Digite um número inteiro positivo par N: "))
    if N > 0 and N % 2 == 0:
        break
    else:
        print("Por favor, digite um número inteiro positivo par.")


print("Números pares de", N, "até 0 em ordem decrescente:")
for i in range(N, -1, -2):
    print(i)

