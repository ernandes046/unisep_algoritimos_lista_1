
alunos = {}

def menu():
    try:
        print('''\nNOTAS
        1 - adicionar aluno
        2 - listar aluno
        3 - remover aluno
        4 - procurar aluno
        5 - aprovados
        6 - reprovados
        7 - procurar pelo nome do aluno
        8 - media da turma B1
        9 - media da turma B2
        10 - media da turma GERAL
        11 - Diario da Turma
        0 - sair''')
        opt = int(input("\nSelecione uma das opcoes: "))
        return opt
    # except KeyboardInterrupt:
    #     print('Deu pau no teclado!')
    # except ValueError:
    #     print('Numero digitado errado!')
    except Exception as e:
        print(f'Opcao invalida: {e}')
        return 9
    # finally:
    #     print('mostra isso!')

def add_aluno():
    try:
        ra = input('Digite o RA do Aluno: ')
        nome = input('Digite o nome do Aluno: ')
        nota_b1 = float(input('Digite a nota B1 do Aluno: '))
        nota_b2 = float(input('Digite a nota B2 do Aluno: '))
        dados = {"nome": nome, 'b1': nota_b1, 'b2': nota_b2}
        alunos[ra] = dados
    except Exception as e:
        print(f'Valor invalido inserido {e}')


def listar_aluno():
    for ra, dados in alunos.items():
        print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
    input('Pressione qualquer tecla para continuar')


def remover_aluno():
    rem = input('Insira o RA do Aluno que deseja remover: ')
    if rem in alunos:
        alunos.pop(rem)
    else:
        print("Esse Aluno nao esta listado")
    input('Pressione qualquer tecla para continuar')


def procurar_aluno():
    ra = input('Insira o RA do Aluno que deseja procurar: ')
    if ra in alunos:
        dados = alunos[ra]
        print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
    else:
        print("Esse Aluno nao esta listado")
    input('Pressione qualquer tecla para continuar')


def aprovados():
    for ra, dados in alunos.items():
        if (dados['b1'] + dados['b2']) // 2 >= 7:
            print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
    input('Pressione qualquer tecla para continuar')


def reprovados():
    for ra, dados in alunos.items():
        if (dados['b1'] + dados['b2']) // 2 < 7:
            print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
    input('Pressione qualquer tecla para continuar')


def procurar_nome():
    nome = input('Insira o nome do Aluno que deseja procurar: ')
    nome = nome.upper
    for ra, dados in alunos.items():
        if dados['nome'].upper() == nome:
            print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
        else:
            print("Esse Aluno nao esta listado")
    input('Pressione qualquer tecla para continuar')


def media_b1():
    soma = 0
    qtd = 0
    for ra, dados in alunos.items():
        soma += dados['b1']
        qtd += 1
    media1 = soma / qtd
    print(f'A media de B1 e: {media1:.2f}')
    input('Pressione qualquer tecla para continuar')


def media_b2():
    soma = 0
    qtd = 0
    for ra, dados in alunos.values():
        soma += dados['b2']
        qtd += 1
    media2 = soma / qtd
    print(f'A media de B2 e: {media2:.2f}')
    input('Pressione qualquer tecla para continuar')


def media_geral():
    soma = 0
    qtd = 0
    for ra, dados in alunos.values():
        soma += (dados['b1'] + dados['b2'])
        qtd += 1
    mediag = soma / qtd
    print(f'A media de B2 e: {mediag:.2f}')
    input('Pressione qualquer tecla para continuar')


def diario_da_turma():
    media1 = media_b1(media1)
    media2 = media_b2(media2)
    mediag = media_geral(mediag)
    for ra, dados in alunos.items():
        dados = alunos[ra]
        dados['media'] = (dados['b1'] + dados['b2']) / 2

    print("--------------------------------------------------------")
    print("                    Diario da Turma                     ")
    print("--------------------------------------------------------")
    print("RA      NOME                         B1     B2     MEDIA")
    print("--------------------------------------------------------")
    for ra, dados in alunos.items():
        print(f"{ra}    Aluno  {dados['nome']}                  {dados['b1']}    {dados['b2']}    {dados['media']}" )
    print("--------------------------------------------------------")
    print(f"                   Medias da Turma   {media1}   {media2}    {mediag}                ")
    print("--------------------------------------------------------")
    input('Pressione qualquer tecla para continuar')


if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                add_aluno()


            case 2:
                listar_aluno()


            case 3:
                remover_aluno()


            case 4:
                procurar_aluno()


            case 5:
                aprovados()


            case 6:
                reprovados()


            case 7:
                procurar_nome()


            case 8:
                media_b1()


            case 9:
                media_b2()


            case 10:
                media_geral()


            case 11:
                diario_da_turma()

                
            case 0:
                break
