# salario . py

"""
quero verificar em qual faixa de contribuçao do inss 
o salario informado se enquadra.
de   0,00 ate 1.412,00 - 7,5%
de 1.412,00 ate 2.666,68 - 9,0%
de 2.666,00 ate 4.000,03 - 12,0%
de 4.000,04 ate 7.786,02 - 14,0%
acima de 7.786,03      - R$ 908,85
"""

salario = 2000.00

if salario <= 1412.00:
    aliquota = 7.5
else:
    if salario >= 1412.01 and salario <= 2666.68:
        aliquota = 9.0
    else:
        if salario >= 2666.00 and salario <= 4000.03:
            aliquota = 12.0
        else:
            if salario >= 4000.03 and salario <= 7786.02:
                aliquota = 14.0
            else:
                valor = 908.85

print("o salario e:")


nome = str(input("digite o nome do fincionario:"))
salario = float(input("digite o salario bruto: "))

if salario <= 1421.00:
    aliquota = 7.5
elif salario >= 1421.00 and salario <= 2666.68:
    aliquota = 9.0
elif salario >= 2666.60 and salario <= 4000.03:
    aliquota = 12.0
elif salario >= 4000.04 and salario <= 7786.02:
    aliquota = 14.0
else:
    valor = 908.85

print("o salario e:")

if aliquota != 0:
    valor = (salario * aliquota) / 100

texto = f"""
o salario do funcionario {nome} e: {salario:.2f}
ele esta na aliquota de {aliquota:.2f}%
deve pagar de inss o valor de R$ {valor:.2f}
recebera o valor de R$ {(salario - valor):.2f}
"""
print(texto)




