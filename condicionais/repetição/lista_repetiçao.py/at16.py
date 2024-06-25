

while True:
    N = int(input("Digite um número inteiro positivo par N: "))
    if N > 0 and N % 2 == 0:
        break
    else:
        print("Por favor, digite um número inteiro positivo par.")

print("Números ímpares de", N, "até 1 em ordem decrescente:")
for i in range(N - 1, 0, -2):
    print(i)
