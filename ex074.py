from random import randint

sorted1 = randint(0, 20)
sorted2 = randint(0, 20)
sorted3 = randint(0, 20)
sorted4 = randint(0, 20)
sorted5 = randint(0, 20)
maior = menor = sorted1
tupla = (sorted1, sorted2, sorted3, sorted4, sorted5)

for v in tupla:
    if v > maior:
        maior = v
    elif v < menor:
        menor = v

#EM TUPLA PODE SER UTILIZADO O MÉTODO MAX(TUPLA) PARA IDENTIFICAR O MAIOR NÚMERO DA TUPLA
#PODE SER UTILIZADO, TAMBÉM, O METODO MIN(TUPLA) PARA IDENTIFICAR O MENOR NÚMERO DA TUPLA

print(f'Os números sorteados foram: {tupla}')
print(f'O maior número do sorteio foi {maior}')
print(f'O menor número do sorteio foi {menor}')