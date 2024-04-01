## atividade 37
# aluno: ernandes
# data: 31/03/2024
###
seg = int(input("digite o numero em segundos"))

hor = seg // 3600
segr = seg % 3600
min = segr // 60
segf = segr % 60

print("em hora minutos e sgundos")
print("horas",hor)
print("minutos",min)
print("segundos",segf)
