###
# atividade 9
# aluno: ernandes
# data: 08/04/2024
###
sal = float(input("Digite o salario:"))
prest = float(input("Digite o valor da prestacao do emprestimo: "))

def vere(sal,prest):
    limp = sal * 0.20  
    if prest > limp:
        return "Emprestimo negado"
    else:
        return "Emprestimo aprovado"


result = vere(sal, prest)
print(result)


  

