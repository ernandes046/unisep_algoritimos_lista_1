carros = {}


def menu():
    try:
        print(''' ESTACIONAMENTO!

        1 - Estacionar veículo

        2 - Retirar veículo

        3 - Veículos estacionados

        4 - Está estacionado?

        0 - Sair

        ''')

        opt = int(input('Escolha uma das opcoes: '))
        return opt
    except Exception as e:

        print(f'Opcao invalida: {e}')
        return 9


def estacionar():
    try:

        placa = input('Digite a placa do veiculo: ')
        marca = input('Digite a marca do veiculo: ')
        modelo = input('Digite o modelo do veiculo: ')
        cor = input('Digite a cor do veiculo: ')
        pro = input('Digite o proprietário do veículo: ')
        chave = {'marca': marca, 'modelo': modelo,
                 'cor': cor, 'proprietario': pro}

        carros[placa] = chave
    except Exception as e:
        print(f'Valor invalido inserido {e}')


def retirar():

    rem = input('Insira a placa do carro que deseja retirar: ')

    if rem in carros:
        carros. pop(rem)
    else:
        print("Esse carro nao esta estacionado")

    input('Pressione qualquer tecla para continuar')


def listar():

    for placa, chave in carros. itens():
        print(f"RA: {placa} - Marca: {chave['marca']} - Modelo: {
              chave['modelo']} - Cor: {chave['cor']} - Proprietario: {chave['proprietario']}")
    input('Pressione qualquer tecla para continuar')


def procurar():
    placa = input('Insira a placa do carro que deseja procurar: ')

    if placa in carros:
        chave = carros[placa]
        print(f"Placa: {placa} - Marca: {chave['marca']} - Modelo: {
              chave['modelo']} - Cor: {chave['cor']} - Proprietario: {chave['proprietario']}")
    else:
        print("Esse carro nao esta estacionado")

    input('Pressione qualquer tecla para continuar')


if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                estacionar()
            case 2:
                retirar()
            case 3:
                listar()
            case 4:
                procurar()
            case 0:
                break
