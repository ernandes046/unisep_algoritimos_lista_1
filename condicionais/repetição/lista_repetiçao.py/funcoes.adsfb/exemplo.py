def soma():
    num1 = int(input("digite um numero:"))
    num2 = int(input("digite um numero:"))
    print(f"a soma e:{soma}")

def voltasoma():
    num1 = int(input("digite um numero:"))
    num2 = int(input("digite um numero:"))
    soma = num1 + num2
    print(f"a soma e:{soma}")
    return soma
def outrasoma(n1, n2):
    soma = n1 + n2
    return soma

soma()
resultado = voltasoma()
print(resultado)

resultado2 = outrasoma(3, 3)
print(resultado2)

