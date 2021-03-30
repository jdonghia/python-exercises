lista = []

loop = True
30
while loop:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('CARACTERE INVÁLIDO! Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        loop = False

lista.sort()
print(f'Os valores numéricos digitados em ordem crescente {lista}')

