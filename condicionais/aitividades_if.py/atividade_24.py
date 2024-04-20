###
# atividade 24
# aluno: ernandes
# data: 15/04/2024
###
import math

def calculartarifa(chegada, partida):
    horaschegada, mincheg = chegada
    horaspartida, minpart = partida

    tempototalmin = (horaspartida - horaschegada) * 60 + (minpart - mincheg)
    tempototalhor = math.ceil(tempototalmin / 60)  

    if tempototalhor <= 2:
        tarifa = tempototalhor * 1.00
    elif tempototalhor<= 4:
        tarifa = 2 * 1.00 + (tempototalhor - 2) * 1.40
    else:
        tarifa = 2 * 1.00 + 2 * 1.40 + (tempototalhor - 4) * 2.00

    return tarifa

chegahor = int(input("Hora de chegada (em horas): "))
chegmin = int(input("Minutos de chegada: "))

parthor = int(input("Hora de partida (em horas): "))
partmin = int(input("Minutos de partida: "))

tarifatotal = calculartarifa((chegahor, chegmin), (parthor, partmin))
print("O preço a pagar pelo estacionamento é R$", tarifatotal)
