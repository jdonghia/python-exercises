saque = int(input('Digite um valor para sacar: '))

ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1

quant_ced50 = quant_ced20 = quant_ced10 = quant_ced1 = 0

while True:
    if saque >= ced50:
        saque -= ced50
        quant_ced50 += 1
    elif saque >= ced20:
        saque -= ced20
        quant_ced20 += 1
    elif saque >= ced10:
        saque -= ced10
        quant_ced10 += 1
    elif saque >= ced1:
        saque -= ced1
        quant_ced1 += 1
    if saque == 0:
        break

print(f'Notas de 50: {quant_ced50}\n'
      f'Notas de 20: {quant_ced20}\n'
      f'Notas de 10: {quant_ced10}\n'
      f'Notas de 1: {quant_ced1}')