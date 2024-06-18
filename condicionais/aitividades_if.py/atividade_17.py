###
# atividade 17
# aluno: ernandes
# data: 15/04/2024
###

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não pode dividir por zero."
    else:
        return a / b

def menu():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    menu()
    opcao = int(input("Digite o número da operação desejada: "))

    if opcao == 5:
        print("Saindo do programa.")
        break
    elif opcao < 1 or opcao > 4:
        print("Opção inválida. Escolha uma opção de 1 a 4.")
        continue

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if opcao == 1:
        print("Resultado da soma:", soma(valor1, valor2))
    elif opcao == 2:
        print("Resultado da subtração:", subtracao(valor1, valor2))
    elif opcao == 3:
        print("Resultado da multiplicação:", multiplicacao(valor1, valor2))
    elif opcao == 4:
        print("Resultado da divisão:", divisao(valor1, valor2))
