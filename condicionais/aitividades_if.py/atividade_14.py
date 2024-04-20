###
# atividade 14
# aluno: ernandes
# data: 15/04/2024
###
def obterdiadasemana(numero):
    diasdasemana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    
    return diasdasemana.get(numero, "Número inválido")

def main():
    numero = int(input("Digite um número entre 1 e 7: "))
    
    diadasemana = obterdiadasemana(numero)
    print("Dia da semana correspondente:", diadasemana)

if __name__ == "__main__":
    main()
