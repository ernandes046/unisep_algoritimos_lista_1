import datetime
despesas = []

id_despesa = 1

def gerar_id():
    global id_despesa
    id_atual = id_despesa
    id_despesa += 1
    return id_atual

def validar_data(data):
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def inserir_despesa():
    global despesas
    data = input("Digite a data da despesa (DD/MM/AAAA): ")
    if not validar_data(data):
        print("Data inválida. Tente novamente.")
        return
    categoria = input("Digite a categoria da despesa: ")
    descricao = input("Digite a descrição da despesa: ")
    try:
        valor = float(input("Digite o valor da despesa: "))
        if valor <= 0:
            raise ValueError
    except ValueError:
        print("Valor inválido. Deve ser um número positivo.")
        return
    despesa = {
        "ID": gerar_id(),
        "Data": data,
        "Categoria": categoria,
        "Descrição": descricao,
        "Valor": valor
    }
    despesas.append(despesa)
    print("Despesa inserida com sucesso!")

def editar_despesa():
    global despesas
    id_editar = int(input("Digite o ID da despesa que deseja editar: "))
    for despesa in despesas:
        if despesa["ID"] == id_editar:
            data = input("Digite a nova data da despesa (DD/MM/AAAA): ")
            if validar_data(data):
                despesa["Data"] = data
            else:
                print("Data inválida. Mantendo a data anterior.")
            despesa["Categoria"] = input("Digite a nova categoria da despesa: ")
            despesa["Descrição"] = input("Digite a nova descrição da despesa: ")
            try:
                valor = float(input("Digite o novo valor da despesa: "))
                if valor > 0:
                    despesa["Valor"] = valor
                else:
                    print("Valor inválido. Mantendo o valor anterior.")
            except ValueError:
                print("Valor inválido. Mantendo o valor anterior.")
            print("Despesa editada com sucesso!")
            return
    print("Despesa não encontrada.")

def buscar_despesa():
    global despesas
    criterio = input("Buscar por (1) Data, (2) Categoria, (3) Descrição: ")
    termo = input("Digite o termo de busca: ")
    resultados = []
    if criterio == "1":
        resultados = [d for d in despesas if d["Data"] == termo]
    elif criterio == "2":
        resultados = [d for d in despesas if d["Categoria"].lower() == termo.lower()]
    elif criterio == "3":
        resultados = [d for d in despesas if termo.lower() in d["Descrição"].lower()]
    else:
        print("Critério de busca inválido.")
        return
    if resultados:
        for despesa in resultados:
            print(despesa)
    else:
        print("Nenhuma despesa encontrada.")

def listar_despesas():
    global despesas
    despesas_ordenadas = sorted(despesas, key=lambda d: datetime.datetime.strptime(d["Data"], '%d/%m/%Y'))
    for despesa in despesas_ordenadas:
        print(despesa)

def remover_despesa():
    global despesas
    id_remover = int(input("Digite o ID da despesa que deseja remover: "))
    for despesa in despesas:
        if despesa["ID"] == id_remover:
            despesas.remove(despesa)
            print("Despesa removida com sucesso!")
            return
    print("Despesa não encontrada.")

def relatorio_despesas():
    global despesas
    total_por_categoria = {}
    total_geral = 0
    for despesa in despesas:
        categoria = despesa["Categoria"]
        valor = despesa["Valor"]
        total_geral += valor
        if categoria in total_por_categoria:
            total_por_categoria[categoria] += valor
        else:
            total_por_categoria[categoria] = valor
    print("Relatório de Despesas:")
    for categoria, total in total_por_categoria.items():
        print(f"{categoria}: R$ {total:.2f}")
    print(f"Total Geral: R$ {total_geral:.2f}")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Inserir despesa")
        print("2 - Editar despesa")
        print("3 - Buscar despesa")
        print("4 - Listar todas as despesas")
        print("5 - Remover despesa")
        print("6 - Relatório de despesas")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_despesa()
        elif opcao == "2":
            editar_despesa()
        elif opcao == "3":
            buscar_despesa()
        elif opcao == "4":
            listar_despesas()
        elif opcao == "5":
            remover_despesa()
        elif opcao == "6":
            relatorio_despesas()
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
