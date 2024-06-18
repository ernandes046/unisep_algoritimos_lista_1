#media.py
b1 = float(input("digite um numero da nota b1: "))
b2 = float(input("digite um numero da nota b2:" ))

media = (b1 + b2) / 2

if media >= 7:
    print("voçe foi aprovado sua nota e:", media)
else:
    print("voçe nao passou sua nota e:",media)