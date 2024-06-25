

N = int(input("Digite um número inteiro positivo N: "))

print("Números naturais de", N, "até 0 em ordem decrescente:")
for i in range(N, -1, -1):
    print(i)
