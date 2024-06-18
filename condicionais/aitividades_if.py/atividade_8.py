###
# atividade 8
# aluno: ernandes
# data: 08/04/2024
###
not1 = float(input("digite a primeira nota"))
not2 = float(input("digite a segunda nota"))

def calcm(not1,not2):
    return (not1 + not2) / 2
def vern(nota):
    return 0.0 <= nota <= 10.0
if vern(not1) and vern(not2):
    med = calcm(not1,not2)
    print("a media das notas e:",med)
else:
    print("as notas nao sao validas verifique se elas estao ente o.o e 10.0")
