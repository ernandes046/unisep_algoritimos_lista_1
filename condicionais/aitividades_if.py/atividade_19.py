###
# atividade 19
# aluno: ernandes
# data: 15/04/2024
###

a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
b = float(input("Digite o comprimento do segundo lado do triângulo: "))
c = float(input("Digite o comprimento do terceiro lado do triângulo: "))

def tipo_triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "Não é um triângulo"
    elif a == b == c:
        return "Triângulo Equilátero"
    elif a == b or a == c or b == c:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"

print(tipo_triangulo(a, b, c))
