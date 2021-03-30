lista = []
maior = menor = 0

for c in range(5):
    n = int(input(f'Digite um valor: '))
    lista.append(n)
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f'O maior valor é {maior} e ele aparece na posição', end = ' ')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i + 1}', end = '..')
print()
print(f'O menor valor é {menor} e ele aparece na posição', end = ' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i + 1}', end='..')

