###
# atividade 16
# aluno: ernandes
# data: 15/04/2024
###


basemai = float(input("Digite o valor da base maior do trapézio: "))
basemeno = float(input("Digite o valor da base menor do trapézio: "))
alt = float(input("Digite o valor da altura do trapézio: "))

def calcular_area_trapezio(basemai, base_meno, alt):
    if basemai <= 0 or basemeno <= 0:
        return "As bases devem ser números maiores que zero."
    else:
        area = ((basemai + basemeno) * alt) / 2
        return area

area = calcular_area_trapezio(basemai, basemeno, alt)
print("A área do trapézio é:", area)
