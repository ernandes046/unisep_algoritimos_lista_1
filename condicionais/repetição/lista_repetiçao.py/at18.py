

quantidade = int(input("Quantos números você deseja inserir? "))

maior_numero = None
contagem_maior = 0

for i in range(quantidade):
    numero = float(input("Digite o {}º número: ".format(i + 1)))
    

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero
        contagem_maior = 1
    elif numero == maior_numero:
        contagem_maior += 1

print("O maior número é:", maior_numero)
print("Ele foi lido", contagem_maior, "vezes.")
