

carros = {
    "AAA-0001": ("JJJJJ", 1599.00),
}

print(carros)

def menu():
    print('''\nCARROS
    1 - Adicionar
    2 - Remover                          
    3 - Listar             
    4 - Verificar se está na lista             
    0 - Sair             
    ''')
    opt = input("Selecione uma das opcoes: ")
    caminho(opt)
        

def add():
    placa = input("\nDigite a placa: ")
    modelo = input("Modelo: ")
    valor = float(input("Valor: "))
    carros[placa] = (modelo, valor)
    return menu()


def remover():
    rem = input("\nQual carro voce gostaria de remover da lista (por placa)? ")
    if rem in carros:
        carros.pop(rem)
    else:
        print("\nEsse carro nao esta na lista!")
    return menu()


def listar():
    print(carros)
    return menu()


def buscar():
    ver = input("\nDigite qual carro gostaria de verificar se esta na lista (por placa): ")
    if ver in carros:
        print('\nEste carro esta na lista')
    else:
        print('\nEste carro nao esta na lista')
    return menu()


def caminho(opt):
    match opt:
        case '1':
            add()


        case '2':
            remover()


        case '3':
            listar()


        case '4':
            buscar()


        case '0':
            return False    


def main():
    while True:
        opt = menu()
        if not caminho(opt):
            break


main()