

N = int(input("Digite um número inteiro N: "))

contador = 0
impar = 1

print("Os", N, "primeiros números naturais ímpares são:")
while contador < N:
    print(impar)
    impar += 2
    contador += 1
