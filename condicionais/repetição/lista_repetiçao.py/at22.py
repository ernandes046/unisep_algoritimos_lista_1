
soma_notas = 0
contador_notas = 0


while True:
    nota = float(input("Digite a nota (entre 10 e 20, ou um valor fora do intervalo para terminar): "))
    
    
    if 10 <= nota <= 20:
        soma_notas += nota
        contador_notas += 1
    else:
        
        if contador_notas == 0:
            print("Nenhuma nota válida foi inserida.")
        else:
            media = soma_notas / contador_notas
            print("Média aritmética das notas inseridas:", media)
        break
