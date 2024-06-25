
total_numeros = 0
pares = 0

while True:
    numero = int(input("Digite um número inteiro (digite 1000 para sair): "))
    
    if numero == 1000:
        break
    
    total_numeros += 1
    
    
    if numero % 2 == 0:
        pares += 1

print("Número de dados lidos:", total_numeros)
print("Número de valores pares:", pares)
