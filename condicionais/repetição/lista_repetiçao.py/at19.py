

while True:
    numero = int(input("Digite um número inteiro entre 100 e 999: "))
    if 100 <= numero <= 999:
        break
    else:
        print("Por favor, digite um número inteiro entre 100 e 999.")


centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

print("Centenas:", centenas)
print("Dezenas:", dezenas)
print("Unidades:", unidades)
