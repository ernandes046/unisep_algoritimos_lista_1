# / imc.py

nome = str(input("digite o nome do funcionario"))
altura = float(input("digite a altula em centimetros"))
peso = float(input("digite o peso em kg"))


imc = peso / ((altura / 100)*(altura / 100))

if imc <= 18.5:
    print(f"{nome} abaixo do pesso (pegue o suplementos do cariani)")
elif imc >= 18.6 and imc <= 24.9:
    print(f"{nome} peso ideal(parabens)")
elif imc >= 25.0 and imc <= 29.9:
    print(f"{nome} sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
    print(f"{nome} obesidade grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print(f"{nome} obesidade grau 2")
else:
    print(f"{nome} obesidade grau 3 (Dr. Nowzaradan te espera)")
