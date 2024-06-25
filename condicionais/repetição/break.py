#break.py
for n in range(500):
    print(f"N:{n}")
    if n == 50:
        break
        # o break quebra o laço e bota um fim em tudo!
    



for n in range(10):
    if n % 3 == 0:
        continue
        #pula a rodada da vez no loop e vai para a proxima
    print(f"N: {n}")
    
while True:
    opçao = input("digite x para sair:")
    print(opçao)
    if opçao.upper() == "x":
        break