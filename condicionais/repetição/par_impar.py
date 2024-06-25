#solicite para o ususario informar o numero que ele quer exibir (par ou impar)
#exiba todos os numeros do intervalo informado mostrando quais pares ou impares conforme a escolha

num = int(input("insira um numero"))
ip = int(input("pares ou impares? (p - I)"))


               
for n in range(num + 1):
    if ip == 1:
        if ip.upper() == "p":
             print(f"o numero {n} e par!")
    else:
        if ip.upper() == "p":
            print(f"o numero {n} e impar! ")
    

    