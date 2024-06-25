

numero = int(input("Digite um número positivo: "))

if numero <= 0:
    print("Por favor, digite um número positivo.")
else:

    print("Os divisores de", numero, "são:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
