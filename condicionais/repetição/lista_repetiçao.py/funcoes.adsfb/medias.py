#medias.py
alunos = {}

def menu():
    print('''\nNOTAS
    1 - adicionar aluno
    2 - listar aluno
    3 - remover aluno
    4 - procurar aluno
    5 - aprovados
    6 - reprovados
    7 - procurar pelo nome do aluno
    8 - media da turma b1
    9 - media da turma b2
    10 - media geral
    11 - diario da turma
    0 - sair''')
    try:
        
        opt = int(input("\nSelecione uma das opçoes: "))
        return opt
    #except KeyboardInterrupt:
        #print("deu pau no teclado!")
    #except ValueError:
    #    print("numero digitado errado!")
    except Exception as e:
        print(f"digite um numero: {e}")
        return 9
    #finally:
     #   print("mostra isso!")

def add_aluno():
    try:
        ra = input("digite o RA do aluno:")
        nome = input("digite o nome do aluno:")
        nota_b1 = float(input("digite a nota b1 do aluno"))
        nota_b2 = float(input("digite a  nota b2 do aluno"))
        dados = {"nome":nome,"b1": nota_b1,"b2": nota_b2}
        alunos[ra] = dados
    except Exception as e:
        print(f"valor invalido inserido{e}")

def listar_aluno():
    for ra, dados, in alunos.itens():
       print(f"ra: {ra} - nome: {dados["nome"]} - b1: {dados["b1"]} - b2: {dados["b2"]}")
    input("presione qualquer tecla para continuar")

def remover_aluno():
    ra = input("digite o ra do aluno:")
    if ra in alunos:
       aluno = alunos.pop(ra)
       print(f"o aluno:{aluno ["nome"]} foi removido")
    else:
        print("este aluno nao esta listado:")
    input("presione qualquer tecla para continuar:")

def procurar_aluno():
    ra = input("insira o ra do aluno que deseja procurar:")
    if ra in alunos:
        dados = alunos[ra]
        print(f"ra: {ra} - nome: {dados["nome"]} - b1: {dados["b1"]} - b2: {dados["b2"]}")
    else:
        print("este aluno nao esta listado:")
    input("presione qualquer tecla para continuar")

def aprovados():
    for ra, dados in alunos.items():
        if ((dados["b1"] + dados["b2"]) // 2) >= 7.0:
            alunos = f"ra: {ra} - "
            alunos += f"nome: {dados["nome"]} - "
            alunos += f"b1: {dados["b1"]} - "
            alunos += f"b2: {dados["b2"]} - "
            print(alunos)
    input("presione qualquer tecla para continuar:")

def reprovados():
    for ra, dados in alunos.items():
        if ((dados["b1"] + dados["b2"]) // 2) < 7.0:
            alunos = f"ra: {ra} - "
            alunos += f"nome: {dados["nome"]} - "
            alunos += f"b1: {dados["b1"]} - "
            alunos += f"b2: {dados["b2"]} - "
            print(alunos)
    input("presione qualquer tecla para continuar:")


def buscar_aluno_nome():
    nome = input("digite o nome do aluno: ")
    nome = nome.upper
    for ra, dados in alunos.items():
        if (dados["nome"].upper == nome):
            alunos = f"aluno encontrado - ra: {ra} - "
            alunos += f"nome: {dados["nome"]} - "
            alunos =+ f"b1: {dados["b1"]} - "
            alunos += f"b2: {dados["b2"]}"
            print(alunos)
            break
    input("presione qualquer tecla para continuar:")   


def media_turma_b1():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados['b1'] 
        qtd += 1
    media = soma / qtd
    alunos["ra"] += media_turma_b1
    print(f"a media de b1 é: {media:.2f}")  
    input("presione qualquer tecla para continuar")  


def media_turma_b2():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados["b2"]
        qtd += 1
    media = soma / qtd
    alunos["ra"] += media_turma_b2
    print(f"a media b2 e: {media:.2f}")   
    input("dpresione qualquer tecla para continuar") 


def media_geral():
    soma = 0
    qtd = 0 
    for dados in alunos.values():
        soma += dados["b1"] + dados["b2"]  
        qtd += 1
    media = soma / qtd
    alunos["ra"] += media_geral
    print(f"a media de b2 é: {media:.2f}")
    input("presione qualquer tecla para continuar")
            

def diario_da_turma():
    print("----------------------------------------------------------------")
    print("                     DIARIO DA TURMA                            ")
    print("----------------------------------------------------------------") 
    print("ra         nome                             b1      b2     media") 
    print("----------------------------------------------------------------")
    print(f"{"ra"} alunos   {dados["nome"]}                            {dados["b1"]}        {dados["b2"]}   {dados["media"]}")
    print("----------------------------------------------------------------")
    print("                      MEDIA DA TURMA                            ")
    print("----------------------------------------------------------------")

if __name__ == "__main__":
    while True:
        match menu():
            case 0:
                break
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
                buscar_aluno_nome()

            case 8:
                media_turma_b1()

            case 9:
                media_turma_b2()

            case 10:
                media_geral()

            case 11:
                diario_da_turma()    

            case 0:
                break
