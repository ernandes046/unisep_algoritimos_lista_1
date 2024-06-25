
carros = {
    "AAA-0001": ("JJJJJ", 1599.00),
}

placa = input("digite a placa:")
modelo = input("modelo:")
valor = float(input("valor:"))


def menu():
    print('''/nCARROS
    1 - adicionar
    2 - remover
    3 - listar
    4 -  verificar se esta na lista
    0 - sair
    ''')
    opt = input("selecione uma das opcoes:")
    
def add():
    carros [placa] = (modelo, valor)
def caminho(opt):
    match opt:
        case "1":
            add()
        case "2":
            remover()
        case "3":
            listar()
        case "4":
            buscar()
        case "0":
            return False
    return True
def main():
    while true:
        opt = menu()
        if not caminho(opt):
            break

if __name__=='__main__':
    main()



