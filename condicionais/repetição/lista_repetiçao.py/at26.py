
def primeiro_multiplo(numero_dado):
    num = numero_dado + 1
    while True:
        if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
            return num
        num += 1

numero_dado = int(input("Digite um número: "))
primeiro = primeiro_multiplo(numero_dado)
print("O primeiro múltiplo de 11, 13 ou 17 após", numero_dado, "é:", primeiro)
