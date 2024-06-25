

multiplos = []
numero = 1

while len(multiplos) < 5:
    if numero % 3 == 0:
        multiplos.append(numero)
    numero += 1

print("Os cinco primeiros múltiplos de 3 são:")
for multiplo in multiplos:
    print(multiplo)
